# Standard Library Imports
import asyncio
import json
import logging
import os
from datetime import  datetime, timedelta
import pprint

# Third-Party Library Imports

# Home Assistant Imports
from homeassistant.core import callback
from homeassistant.components.sensor import  SensorStateClass
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_track_state_change

from homeassistant.const import (
    CONF_NAME
)

from .pgns import *

# Setting up logging and configuring constants and default values

_LOGGER = logging.getLogger(__name__)


async def update_sensor_availability(hass,instance_name):
    """Update the availability of all sensors every 5 minutes."""
    
    created_sensors_key = f"{instance_name}_created_sensors"

    while True:
        _LOGGER.debug("Running update_sensor_availability")
        await asyncio.sleep(300)  # wait for 5 minutes

        for sensor in hass.data[created_sensors_key].values():
            sensor.update_availability()


# The main setup function to initialize the sensor platform

async def async_setup_entry(hass, entry, async_add_entities):
    # Retrieve configuration from entry
    name = entry.data[CONF_NAME]

    # Log the retrieved configuration values for debugging purposes
    _LOGGER.info(f"Configuring sensor with name: {name}")
    
    # Initialize unique dictionary keys based on the integration name
    add_entities_key = f"{name}_add_entities"
    created_sensors_key = f"{name}_created_sensors"
    smart2000esp_data_key = f"{name}_smart2000esp_data"
    fast_packet_key = f"{name}_fast_packet_key"
    
    # Initialize dictionary to hold fast packet frames
    hass.data[fast_packet_key] = {}


     # Save a reference to the add_entities callback
    _LOGGER.debug(f"Assigning async_add_entities to hass.data[{add_entities_key}].")
    hass.data[add_entities_key] = async_add_entities


    # Initialize a dictionary to store references to the created sensors
    hass.data[created_sensors_key] = {}
    
    # Load the Smart2000 json data 
    config_dir = hass.config.config_dir
    json_path = os.path.join(config_dir, 'custom_components', 'smart2000esp', 'smart2000pgns.json')
    try:
        with open(json_path, "r") as file:
            smart_data = json.load(file)

        pgn_dict = {}
        for pgn in smart_data["PGNs"]:  
            pgn_id = pgn["PGN"] 
            
            pgn_dict[pgn_id] = {
                "Description": pgn["Description"],
                "Type": pgn["Type"],
                "FieldCount": pgn["FieldCount"],
                "Length": pgn.get("Length", 0)
            }

        hass.data[smart2000esp_data_key] = pgn_dict
        
        _LOGGER.debug(f"smart2000esp_data_key: {smart2000esp_data_key}")


    except Exception as e:
        _LOGGER.error(f"Error loading Smart2000.json: {e}")
        return

    _LOGGER.debug(f"Loaded smart data: {hass.data[smart2000esp_data_key]}")
    
    
    
    # Define a callback to handle when te esp32 sends a new canbus frame
    @callback
    def sensor_state_change(entity_id, old_state, new_state):
        # Log the new value
        if new_state is not None:
            set_pgn_entity(hass, name, entity_id, new_state.state)          
        else:
            _LOGGER.debug('Sensor %s has no new state', entity_id)
            
            

    # Subscribe to changes of the specific sensor
    # async_track_state_change(hass, 'sensor.esphome_web_3e9a60_s_2000_frame', sensor_state_change)
    
    sensor_name = name.replace('-', '_')

    esp32name = f'sensor.{sensor_name}_s_2000_frame'

    async_track_state_change(hass, esp32name, sensor_state_change)

    _LOGGER.info(f"{esp32name} setup completed.")


def call_process_function(pgn, hass, instance_name, entity_id, data_frames):
    function_name = f'process_pgn_{pgn}'
    function_to_call = globals().get(function_name)

    # Check if the function exists
    if function_to_call:
        function_to_call(hass, instance_name, entity_id, data_frames)
    else:
        print(f"No function found for PGN: {pgn}")

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



def process_fast_packet(pgn, hass, instance_name, entity_id, data64, data64_hex):
    
    fast_packet_key = f"{instance_name}_fast_packet_key"
    
    # Check if this PGN already has a storage structure; if not, create one
    if pgn not in hass.data[fast_packet_key]:
        _LOGGER.info("Create Storage for PGN: %d", pgn)
        hass.data[fast_packet_key][pgn] = {'frames': {}, 'payload_length': 0, 'bytes_stored': 0}
        
    pgn_data = hass.data[fast_packet_key][pgn]
               
    # Convert the last two characters to an integer to get the sequence and frame counters
    last_byte = int(data64_hex[-2:], 16)  # Convert the last two hex digits to an integer
    
    # Extract the sequence counter (high 3 bits) and frame counter (low 5 bits) from the last byte
    sequence_counter = (last_byte >> 5) & 0b111  # Extract high 3 bits
    frame_counter = last_byte & 0b11111  # Extract low 5 bits
    
    total_bytes = None
    
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
    
    data_payload_int = int(data_payload_hex, 16)     
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

            call_process_function(pgn, hass, instance_name, entity_id, combined_payload_int)

        # Reset the structure for this PGN
        del hass.data[fast_packet_key][pgn]
        


def set_pgn_entity(hass, instance_name, entity_id, state_value):
    """Reconstructs PGN and data64 from the sensor state, handling various edge cases."""

    smart2000esp_data_key = f"{instance_name}_smart2000esp_data"


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
        source_id = int(source_id_hex, 16)
        data64 = int(data64_hex, 16)

        _LOGGER.debug('---------------------------------------------------')
        _LOGGER.info('Reconstructed PGN  : %d (Hex: %s)', pgn, pgn_hex)
        _LOGGER.debug('Reconstructed source ID  : %d (Hex: %s)', source_id, source_id_hex)
        _LOGGER.info('Reconstructed data64  : %d (Hex: %s)', data64, data64_hex)

    
        pgn_entry = hass.data[smart2000esp_data_key].get(pgn)
        
        _LOGGER.debug(f"smart2000esp_data_key: {smart2000esp_data_key}")
        
            
        if pgn_entry and pgn_entry['Type'] == 'Fast':
            _LOGGER.info(f"PGN {pgn} is of type 'Fast'.")
            process_fast_packet(pgn, hass, instance_name, entity_id, data64, data64_hex)
        else:
            _LOGGER.debug(f"PGN {pgn} is of type 'Single'.")
            call_process_function(pgn, hass, instance_name, entity_id, data64)

            

    except ValueError as e:
        _LOGGER.error('Error processing state value  : %s. Error: %s' , state_value, e)


def publish_field(hass, instance_name, field_name, field_description, field_value, pgn_description, unit, pgn_id):
    _LOGGER.info(f"Publishing field for PGN {pgn_id} and field {field_name} with value {field_value}")

    add_entities_key = f"{instance_name}_add_entities"
    created_sensors_key = f"{instance_name}_created_sensors"
    smart2000esp_data_key = f"{instance_name}_smart2000esp_data"

    # Construct unique sensor name
    sensor_name = f"{instance_name}_{pgn_id}_{field_name}"
    #_LOGGER.debug(f"Constructed sensor name: {sensor_name}")

    # Define sensor characteristics
    group = "Smart2000"
    unit_of_measurement = unit  # Determine based on field_name if applicable
    
    device_name = pgn_description
    #_LOGGER.debug(f"Device name for PGN {pgn_id}: {device_name}")

    # Access keys for created sensors and entity addition
    created_sensors_key = f"{instance_name}_created_sensors"
    add_entities_key = f"{instance_name}_add_entities"

    # Check for sensor existence and create/update accordingly
    if sensor_name not in hass.data[created_sensors_key]:
        #_LOGGER.debug(f"Creating new sensor for {sensor_name}")
        # If sensor does not exist, create and add it
        sensor = SmartSensor(
            sensor_name, 
            field_description, 
            field_value, 
            group, 
            unit_of_measurement, 
            device_name, 
            pgn_id
        )
        
        hass.data[add_entities_key]([sensor])
        hass.data[created_sensors_key][sensor_name] = sensor
        #_LOGGER.debug(f"Sensor {sensor_name} added successfully.")
    else:
        # If sensor exists, update its state
        _LOGGER.debug(f"Updating existing sensor {sensor_name} with new value: {field_value}")
        sensor = hass.data[created_sensors_key][sensor_name]
        sensor.set_state(field_value)
        #_LOGGER.debug(f"Sensor {sensor_name} updated successfully.")

        




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
        sentence_type=None
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
            "identifiers": {("smart0183tcp", self._device_name)},
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
        _LOGGER.debug(f"Setting state for sensor: '{self._name}' to {new_state}")
        self._state = new_state
        if new_state is None or new_state == "":
            self._available = False
            _LOGGER.debug(f"Setting sensor:'{self._name}' with unavailable")
        else:
            self._available = True
        self._last_updated = datetime.now()

        try:
            self.async_schedule_update_ha_state()
        except RuntimeError as re:
            if "Attribute hass is None" in str(re):
                pass  # Ignore this specific error
            else:
                _LOGGER.warning(f"Could not update state for sensor '{self._name}': {re}")
        except Exception as e:  # Catch all other exception types
            _LOGGER.warning(f"Could not update state for sensor '{self._name}': {e}")



