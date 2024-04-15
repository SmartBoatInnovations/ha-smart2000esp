# Standard Library Imports
import asyncio
import json
import logging
import os
from datetime import  datetime, timedelta
import pprint

# Third-Party Library Imports

# Home Assistant Imports
from homeassistant.core import callback, HomeAssistant
from homeassistant.components.sensor import  SensorStateClass
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_track_state_change
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.const import (
    CONF_NAME
)

from .pgns import *

# Setting up logging and configuring constants and default values

_LOGGER = logging.getLogger(__name__)


# The main setup function to initialize the sensor platform

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    
    # Retrieve configuration from entry
    name = entry.data[CONF_NAME]
    pgn_include = parse_and_validate_comma_separated_integers(entry.data.get('pgn_include', ''))
    pgn_exclude = parse_and_validate_comma_separated_integers(entry.data.get('pgn_exclude', ''))
    
    _LOGGER.info(f"Configuring sensor with name: {name}, PGN Include: {pgn_include}, PGN Exclude: {pgn_exclude}")
        
    # Initialize unique dictionary keys based on the integration name
    add_entities_key = f"{name}_add_entities"
    created_sensors_key = f"{name}_created_sensors"
    smart2000esp_data_key = f"{name}_smart2000esp_data"
    fast_packet_key = f"{name}_fast_packet_key"
    whitelist_key = f"{name}_whitelist_key"
    blacklist_key = f"{name}_blacklist_key"
    
    hass.data[whitelist_key] = pgn_include
    hass.data[blacklist_key] = pgn_exclude
    
    smart2000timestamp_key = f"{name}_smart2000timestamp_key"
    hass.data[smart2000timestamp_key] = {
        "last_processed": {},  
        "min_interval": timedelta(seconds=5),  
        }
    
    # Initialize dictionary to hold fast packet frames
    hass.data[fast_packet_key] = {}


     # Save a reference to the add_entities callback
    hass.data[add_entities_key] = async_add_entities


    # Initialize a dictionary to store references to the created sensors
    hass.data[created_sensors_key] = {}
    
    # Load the fast pgn json data 
    config_dir = hass.config.config_dir
    json_path = os.path.join(config_dir, 'custom_components', 'smart2000esp', 'pgn_type.json')
    try:
        with open(json_path, "r") as file:
            smart_data = json.load(file)

        pgn_dict = {}
        # Iterate over each PGN entry in the list
        for pgn_entry in smart_data["PGNs"]:
            pgn_id, pgn_type = pgn_entry  # Unpack the tuple
    
            # Store the PGN and its type in the dictionary
            pgn_dict[pgn_id] = pgn_type
            
            
        hass.data[smart2000esp_data_key] = pgn_dict
        

    except Exception as e:
        _LOGGER.error(f"Error loading Smart2000.json: {e}")
        return
  
    
    
    # Define a callback to handle when the esp32 sends a new canbus frame
    @callback
    def sensor_state_change(entity_id, old_state, new_state):
        # Log the new value
        if new_state is not None:
            set_pgn_entity(hass, name, new_state.state)          
        else:
            _LOGGER.debug('Sensor %s has no new state')
            
            

    
    sensor_name = name.replace('-', '_')

    esp32name = f'sensor.{sensor_name}_smart2000_frame'

    # Subscribe to changes of the main sensor

    unsubscribe = async_track_state_change(hass, esp32name, sensor_state_change)
    
    # Store the unsubscribe callback to use it later for cleanup
    hass.data[f"{name}_unsubscribe"] = unsubscribe
     
    # Start the task that updates the sensor availability every 5 minutes
    hass.loop.create_task(update_sensor_availability(hass,name))

    _LOGGER.info(f"{esp32name} setup completed.")
    
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    
    # Retrieve configuration from entry
    name = entry.data["name"]

    _LOGGER.info(f"Unload integration with name: {name}")

    # Unsubscribe from state changes
    unsubscribe_key = f"{name}_unsubscribe"
    if unsubscribe_key in hass.data:
        _LOGGER.info(f"Unsubscribing from state changes for {name}.")
        hass.data[unsubscribe_key]()
        del hass.data[unsubscribe_key]
    
    # Clean up hass.data entries
    for key_suffix in ['add_entities', 'created_sensors', 'smart2000esp_data', 'fast_packet', 'whitelist', 'blacklist', 'smart2000timestamp']:
        key = f"{name}_{key_suffix}"
        if key in hass.data:
            _LOGGER.info(f"Removing {key} from hass.data.")
            del hass.data[key]

    _LOGGER.info(f"Unload and cleanup for {name} completed successfully.")
    
    return True


async def update_sensor_availability(hass,instance_name):
    """Update the availability of all sensors every 5 minutes."""
    
    created_sensors_key = f"{instance_name}_created_sensors"

    while True:
        _LOGGER.debug("Running update_sensor_availability")
        await asyncio.sleep(300)  # wait for 5 minutes

        for sensor in hass.data[created_sensors_key].values():
            sensor.update_availability()


def parse_and_validate_comma_separated_integers(input_str: str):
    
    # Check if the input string is empty or contains only whitespace
    if not input_str.strip():
        return []

    # Split the string by commas to get potential integer values
    potential_integers = input_str.split(',')

    validated_integers = []
    for value in potential_integers:
        value = value.strip()  # Remove any leading/trailing whitespace
        if value:  # Check if the string is not empty
            try:
                # Attempt to convert the string to an integer
                integer_value = int(value)
                validated_integers.append(integer_value)
            except ValueError:
                # Raise an error indicating the specific value that couldn't be converted
                _LOGGER.error(f"Invalid pgn value found: '{value}' in input '{input_str}'.")
    
    return validated_integers


def call_process_function(pgn, hass, instance_name, data_frames):
    function_name = f'process_pgn_{pgn}'
    function_to_call = globals().get(function_name)

    # Check if the function exists
    if function_to_call:
        function_to_call(hass, instance_name, data_frames)
    else:
        _LOGGER.info(f"No function found for PGN: {pgn}")


def combine_pgn_frames(hass, pgn, instance_name):
    """Combine stored frame data for a PGN into a single hex string, preserving the original byte lengths."""
    
    fast_packet_key = f"{instance_name}_fast_packet_key"
    
    if pgn not in hass.data[fast_packet_key]:
        _LOGGER.info(f"No fast packet data available for PGN {pgn}")
        return None

    pgn_data = hass.data[fast_packet_key][pgn]
    combined_payload_hex = ""  # Start with an empty string

    for frame_counter in sorted(pgn_data['frames']):
        frame_data_hex = pgn_data['frames'][frame_counter]
        combined_payload_hex += frame_data_hex  # Concatenate hex strings directly

    return combined_payload_hex



def process_fast_packet(pgn, hass, instance_name, data64, data64_hex):
    
    fast_packet_key = f"{instance_name}_fast_packet_key"
    
    # Check if this PGN already has a storage structure; if not, create one
    if pgn not in hass.data[fast_packet_key]:
        hass.data[fast_packet_key][pgn] = {'frames': {}, 'payload_length': 0, 'bytes_stored': 0}
        
    pgn_data = hass.data[fast_packet_key][pgn]
               
    # Convert the last two characters to an integer to get the sequence and frame counters
    last_byte = int(data64_hex[-2:], 16)  # Convert the last two hex digits to an integer
    
    # Extract the sequence counter (high 3 bits) and frame counter (low 5 bits) from the last byte
    sequence_counter = (last_byte >> 5) & 0b111  # Extract high 3 bits
    frame_counter = last_byte & 0b11111  # Extract low 5 bits
    
    total_bytes = None
    
    if frame_counter == 0 and not can_process(hass, instance_name, pgn):
        return

    if frame_counter != 0 and pgn_data['payload_length'] == 0:
        _LOGGER.info(f"Ignoring frame {frame_counter} for PGN {pgn} as first frame has not been received.")
        return
       
    # Calculate data payload
    if frame_counter == 0:
        
        # Extract the total number of frames from the second-to-last byte
        total_bytes_hex = data64_hex[-4:-2]  # Get the second-to-last byte in hex
        total_bytes = int(total_bytes_hex, 16)  # Convert hex to int
        
        # Start a new pgn hass structure 
      
        pgn_data['payload_length'] = total_bytes
        pgn_data['sequence_counter'] = sequence_counter
        pgn_data['bytes_stored'] = 0  # Reset bytes stored for a new message
        pgn_data['frames'].clear()  # Clear previous frames
                
        # For the first frame, exclude the last 4 hex characters (2 bytes) from the payload
        data_payload_hex = data64_hex[:-4]
        
    else:       
        if sequence_counter != pgn_data['sequence_counter']:
            _LOGGER.info(f"Ignoring frame {sequence_counter} for PGN {pgn} as it does not match current sequence.")
            return
        elif frame_counter in pgn_data['frames']:
            _LOGGER.info(f"Frame {frame_counter} for PGN {pgn} is already stored.")
            return
        else:
            # For subsequent frames, exclude the last 2 hex characters (1 byte) from the payload
            data_payload_hex = data64_hex[:-2]
    
    byte_length = len(data_payload_hex) // 2

    # Store the frame data
    pgn_data['frames'][frame_counter] = data_payload_hex
    pgn_data['bytes_stored'] += byte_length  # Update the count of bytes stored
     
    # Log the extracted values
    _LOGGER.info(f"Sequence Counter: {sequence_counter}")
    _LOGGER.info(f"Frame Counter: {frame_counter}")
    
    if total_bytes is not None:
        _LOGGER.info(f"Total Payload Bytes: {total_bytes}")

    _LOGGER.info(f"Orig Payload (hex): {data64_hex}")
    _LOGGER.info(f"Data Payload (hex): {data_payload_hex}")
    
    formatted_data = pprint.pformat(hass.data[fast_packet_key])
    _LOGGER.info("HASS PGN Data: %s", formatted_data)
    
    # Check if all expected bytes have been stored
    if pgn_data['bytes_stored'] >= pgn_data['payload_length']:
        
        _LOGGER.info("All Fast packet frames collected for PGN: %d", pgn)

        # All data for this PGN has been received, proceed to publish
        combined_payload_hex = combine_pgn_frames(hass, pgn, instance_name)
        combined_payload_int = int(combined_payload_hex, 16)
        
        if combined_payload_int is not None:
            _LOGGER.info(f"Combined Payload (hex): {combined_payload_hex})")
            _LOGGER.info(f"Combined Payload (hex): (hex: {combined_payload_int:x})")

            call_process_function(pgn, hass, instance_name, combined_payload_int)

        # Reset the structure for this PGN
        del hass.data[fast_packet_key][pgn]

        
def can_process(hass, instance_name, pgn_id):

    smart2000timestamp_key = f"{instance_name}_smart2000timestamp_key"
    
    now = datetime.now()
    last_processed = hass.data[smart2000timestamp_key]["last_processed"]
    min_interval = hass.data[smart2000timestamp_key]["min_interval"]
    
    if pgn_id not in last_processed or now - last_processed[pgn_id] >= min_interval:
        hass.data[smart2000timestamp_key]["last_processed"][pgn_id] = now  
        return True
    else:
        _LOGGER.info(f"Throttling activated for PGN {pgn_id} in instance {instance_name}.")
        return False


def is_pgn_allowed_based_on_lists(pgn, pgn_include_list, pgn_exclude_list):
    """
    Determines whether a given PGN should be processed based on whitelist and blacklist rules.

    :param pgn: The PGN to check.
    :param pgn_include_list: A list of PGNs to include (whitelist).
    :param pgn_exclude_list: A list of PGNs to exclude (blacklist).
    :return: True if the PGN should be processed, False otherwise.
    """
    # If the include list is not empty, process only if PGN is in the include list
    if pgn_include_list:
        return pgn in pgn_include_list

    # If the include list is empty but the exclude list is not, process only if PGN is not in the exclude list
    elif pgn_exclude_list:
        return pgn not in pgn_exclude_list

    # If both lists are empty, process all PGNs
    return True


def set_pgn_entity(hass, instance_name, state_value):
    """Reconstructs PGN and data64 from the sensor state, handling various edge cases."""

    smart2000esp_data_key = f"{instance_name}_smart2000esp_data"
    whitelist_key = f"{instance_name}_whitelist_key"
    blacklist_key = f"{instance_name}_blacklist_key"
    
    pgn_include_list = hass.data[whitelist_key]
    pgn_exclude_list = hass.data[blacklist_key]
    

    # Check if the state_value is None or does not contain a colon, indicating an invalid or unavailable state
    if state_value is None or ':' not in state_value:
        _LOGGER.debug('Invalid or unavailable state  : %s' , state_value)
        return

    try:
        # Split the state string into PGN, frame counter, and data payload hexadecimal strings
        parts = state_value.split(':')
        if len(parts) < 3:
            _LOGGER.debug('Invalid state format  : %s' , state_value)
            return
    
        pgn_hex, source_id_hex, data64_hex = parts[0], parts[1], parts[2]
    
        # Convert the hexadecimal strings back to integer values
        pgn = int(pgn_hex, 16)
        
        if not is_pgn_allowed_based_on_lists(pgn, pgn_include_list, pgn_exclude_list):
            _LOGGER.info(f"PGN {pgn} skipped due to white/black lists.")
            return

        
        source_id = int(source_id_hex, 16)
        data64 = int(data64_hex, 16)

        _LOGGER.debug('---------------------------------------------------')
        _LOGGER.info('Reconstructed PGN  : %d (Hex: %s)', pgn, pgn_hex)
        _LOGGER.debug('Reconstructed source ID  : %d (Hex: %s)', source_id, source_id_hex)
        _LOGGER.info('Reconstructed data64  : %d (Hex: %s)', data64, data64_hex)

    
        pgn_type = hass.data[smart2000esp_data_key].get(pgn)
        
        _LOGGER.debug(f"smart2000esp_data_key: {smart2000esp_data_key}")
        
            
        if pgn_type and pgn_type == 'Fast':
            _LOGGER.info(f"PGN {pgn} is of type 'Fast'.")
            process_fast_packet(pgn, hass, instance_name, data64, data64_hex)
        elif pgn_type and pgn_type == 'Single':
            if not can_process(hass, instance_name, pgn):
                return
            
            _LOGGER.debug(f"PGN {pgn} is of type 'Single'.")
            call_process_function(pgn, hass, instance_name, data64)
        else:
            _LOGGER.info(f"PGN {pgn} is not a known PGN.")
                

    except ValueError as e:
        _LOGGER.error('Error processing state value  : %s. Error: %s' , state_value, e)


def publish_field(hass, instance_name, field_name, field_description, field_value, pgn_description, unit, pgn_id):
    _LOGGER.info(f"Publishing field for PGN {pgn_id} and field {field_name} with value {field_value}")

    add_entities_key = f"{instance_name}_add_entities"
    created_sensors_key = f"{instance_name}_created_sensors"

    # Construct unique sensor name
    sensor_name = f"{instance_name}_{pgn_id}_{field_name}"
    
    # Define sensor characteristics
    group = "Smart2000"
    
    unit_of_measurement = unit  # Determine based on field_name if applicable
    
    device_name = pgn_description

    # Access keys for created sensors and entity addition
    created_sensors_key = f"{instance_name}_created_sensors"
    add_entities_key = f"{instance_name}_add_entities"

    # Check for sensor existence and create/update accordingly
    if sensor_name not in hass.data[created_sensors_key]:
        # If sensor does not exist, create and add it
        sensor = SmartSensor(
            sensor_name, 
            field_description, 
            field_value, 
            group, 
            unit_of_measurement, 
            device_name, 
            pgn_id,
            instance_name
        )
        
        hass.data[add_entities_key]([sensor])
        hass.data[created_sensors_key][sensor_name] = sensor
    else:
        # If sensor exists, update its state
        _LOGGER.debug(f"Updating existing sensor {sensor_name} with new value: {field_value}")
        sensor = hass.data[created_sensors_key][sensor_name]
        sensor.set_state(field_value)

        

# SmartSensor class representing a basic sensor entity with state

class SmartSensor(Entity):
    def __init__(
        self, 
        name, 
        friendly_name, 
        initial_state, 
        group=None, 
        unit_of_measurement=None, 
        device_name=None, 
        sentence_type=None,
        instance_name=None
    ):
        """Initialize the sensor."""
        _LOGGER.info(f"Initializing sensor: {name} with state: {initial_state}")

        self._unique_id = name.lower().replace(" ", "_")
        self.entity_id = f"sensor.{self._unique_id}"
        self._name = friendly_name if friendly_name else self._unique_id
        self._state = initial_state
        self._group = group if group is not None else "Other"
        self._device_name = device_name
        self._sentence_type = sentence_type
        self._instance_name = instance_name
        self._unit_of_measurement = unit_of_measurement
        self._state_class = SensorStateClass.MEASUREMENT
        self._last_updated = datetime.now()
        if initial_state is None or initial_state == "":
            self._available = False
            _LOGGER.debug(f"Setting sensor: '{self._name}' with unavailable")
        else:
            self._available = True

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name
    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._unique_id

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    @property
    def device_info(self):
        """Return device information about this sensor."""
        return {
            "identifiers": {("smart2000esp", f"{self._instance_name}_{self._device_name}")},
            "name": self._device_name,
            "manufacturer": self._group,
            "model": self._sentence_type,
        }

    @property
    def state_class(self):
        """Return the state class of the sensor."""
        return self._state_class

    @property
    def last_updated(self):
        """Return the last updated timestamp of the sensor."""
        return self._last_updated

    @property
    def available(self) -> bool:
        """Return True if the entity is available."""
        return self._available

    @property
    def should_poll(self) -> bool:
        """Return the polling requirement for this sensor."""
        return False

    def update_availability(self):
        """Update the availability status of the sensor."""

        new_availability = (datetime.now() - self._last_updated) < timedelta(minutes=4)

        self._available = new_availability

        try:
            self.async_schedule_update_ha_state()
        except RuntimeError as re:
            if "Attribute hass is None" in str(re):
                pass  # Ignore this specific error
            else:
                _LOGGER.warning(f"Could not update state for sensor '{self._name}': {re}")
        except Exception as e:  # Catch all other exception types
            _LOGGER.warning(f"Could not update state for sensor '{self._name}': {e}")

    def set_state(self, new_state):
        """Set the state of the sensor."""
        
        if new_state is not None and new_state != "":
            # Since the state is valid, update the sensor's state and the last updated timestamp
            self._state = new_state
            self._available = True
            self._last_updated = datetime.now()
            _LOGGER.debug(f"Setting state for sensor: '{self._name}' to {new_state}")
        else:
            # For None or empty string, check the time since last valid update
            if self._last_updated and (datetime.now() - self._last_updated > timedelta(minutes=1)):
                # It's been more than 1 minute since the last valid update
                self._available = False
                _LOGGER.info(f"Setting sensor:'{self._name}' as unavailable due to no valid update for over 1 minute")
            else:
                # It's been less than 1 minute since the last valid update, keep the sensor available
                _LOGGER.info(f"Sensor:'{self._name}' remains available as it's less than 1 minute since last valid state")

        try:
            self.async_schedule_update_ha_state()
        except RuntimeError as re:
            if "Attribute hass is None" in str(re):
                pass  # Ignore this specific error
            else:
                _LOGGER.warning(f"Could not update state for sensor '{self._name}': {re}")
        except Exception as e:  # Catch all other exception types
            _LOGGER.warning(f"Could not update state for sensor '{self._name}': {e}")



