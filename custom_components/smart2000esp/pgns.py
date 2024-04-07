def process_pgn_128259(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128259."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Speed', '', '128259')
    _LOGGER.debug('SID  : %s', sid)

    # speed_water_referenced | Offset: 8, Length: 16, Resolution: 0.01, Field Type: NUMBER
    speed_water_referenced_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    speed_water_referenced = speed_water_referenced_raw * 0.01
    publish_field(hass, instance_name, 'speed_water_referenced', 'Speed Water Referenced', speed_water_referenced, 'Speed', 'm/s', '128259')
    publish_field(hass, instance_name, 'speed_water_referenced_knots', 'Speed Water Referenced Knots', mps_to_knots(speed_water_referenced), 'Speed', 'Kn', '128259')
    _LOGGER.debug('Speed Water Referenced  : %s', speed_water_referenced)

    # speed_ground_referenced | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    speed_ground_referenced_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    speed_ground_referenced = speed_ground_referenced_raw * 0.01
    publish_field(hass, instance_name, 'speed_ground_referenced', 'Speed Ground Referenced', speed_ground_referenced, 'Speed', 'm/s', '128259')
    publish_field(hass, instance_name, 'speed_ground_referenced_knots', 'Speed Ground Referenced Knots', mps_to_knots(speed_ground_referenced), 'Speed', 'Kn', '128259')
    _LOGGER.debug('Speed Ground Referenced  : %s', speed_ground_referenced)

    # speed_water_referenced_type | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    speed_water_referenced_type_raw = (data_raw >> 40) & 0xFF
    speed_water_referenced_type = speed_water_referenced_type_raw * 1
    publish_field(hass, instance_name, 'speed_water_referenced_type', 'Speed Water Referenced Type', speed_water_referenced_type, 'Speed', '', '128259')
    _LOGGER.debug('Speed Water Referenced Type  : %s', speed_water_referenced_type)

    # speed_direction | Offset: 48, Length: 4, Resolution: 1, Field Type: NUMBER
    speed_direction_raw = decode_number((data_raw >> 48) & 0xF, 4)
    speed_direction = speed_direction_raw * 1
    publish_field(hass, instance_name, 'speed_direction', 'Speed Direction', speed_direction, 'Speed', '', '128259')
    _LOGGER.debug('Speed Direction  : %s', speed_direction)

    # reserved | Offset: 52, Length: 12, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 52) & 0xFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Speed', '', '128259')
    _LOGGER.debug('Reserved  : %s', reserved)

from .utils import *
import logging
_LOGGER = logging.getLogger(__name__)

def process_pgn_128267(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128267."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Water Depth', '', '128267')
    _LOGGER.debug('SID  : %s', sid)

    # depth | Offset: 8, Length: 32, Resolution: 0.01, Field Type: NUMBER
    depth_raw = decode_number((data_raw >> 8) & 0xFFFFFFFF, 32)
    depth = depth_raw * 0.01
    publish_field(hass, instance_name, 'depth', 'Depth', depth, 'Water Depth', 'm', '128267')
    _LOGGER.debug('Depth  : %s', depth)

    # offset | Offset: 40, Length: 16, Resolution: 0.001, Field Type: NUMBER
    offset_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if offset_raw & (1 << (16 - 1)):
        offset_raw -= (1 << 16)
    offset = offset_raw * 0.001
    publish_field(hass, instance_name, 'offset', 'Offset', offset, 'Water Depth', 'm', '128267')
    _LOGGER.debug('Offset  : %s', offset)

    # range | Offset: 56, Length: 8, Resolution: 10, Field Type: NUMBER
    range_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    range = range_raw * 10
    publish_field(hass, instance_name, 'range', 'Range', range, 'Water Depth', 'm', '128267')
    _LOGGER.debug('Range  : %s', range)

def process_pgn_128275(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128275."""
    # date | Offset: 0, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 0) & 0xFFFF
    date = date_raw * 1
    publish_field(hass, instance_name, 'date', 'Date', date, 'Distance Log', 'd', '128275')
    _LOGGER.debug('Date  : %s', date)

    # time | Offset: 16, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 16) & 0xFFFFFFFF
    time = time_raw * 0.0001
    publish_field(hass, instance_name, 'time', 'Time', time, 'Distance Log', 's', '128275')
    _LOGGER.debug('Time  : %s', time)

    # log | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    log_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    log = log_raw * 1
    publish_field(hass, instance_name, 'log', 'Log', log, 'Distance Log', 'm', '128275')
    _LOGGER.debug('Log  : %s', log)

    # trip_log | Offset: 80, Length: 32, Resolution: 1, Field Type: NUMBER
    trip_log_raw = decode_number((data_raw >> 80) & 0xFFFFFFFF, 32)
    trip_log = trip_log_raw * 1
    publish_field(hass, instance_name, 'trip_log', 'Trip Log', trip_log, 'Distance Log', 'm', '128275')
    _LOGGER.debug('Trip Log  : %s', trip_log)

def process_pgn_129025(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129025."""
    # latitude | Offset: 0, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'Position, Rapid Update', 'deg', '129025')
    _LOGGER.debug('Latitude  : %s', latitude)

    # longitude | Offset: 32, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'Position, Rapid Update', 'deg', '129025')
    _LOGGER.debug('Longitude  : %s', longitude)

def process_pgn_130306(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130306."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Wind Data', '', '130306')
    _LOGGER.debug('SID  : %s', sid)

    # wind_speed | Offset: 8, Length: 16, Resolution: 0.01, Field Type: NUMBER
    wind_speed_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    wind_speed = wind_speed_raw * 0.01
    publish_field(hass, instance_name, 'wind_speed', 'Wind Speed', wind_speed, 'Wind Data', 'm/s', '130306')
    publish_field(hass, instance_name, 'wind_speed_knots', 'Wind Speed Knots', mps_to_knots(wind_speed), 'Wind Data', 'Kn', '130306')
    _LOGGER.debug('Wind Speed  : %s', wind_speed)

    # wind_angle | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    wind_angle_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    wind_angle = wind_angle_raw * 0.0001
    publish_field(hass, instance_name, 'wind_angle', 'Wind Angle', wind_angle, 'Wind Data', 'rad', '130306')
    publish_field(hass, instance_name, 'wind_angle_degrees', 'Wind Angle Degrees', radians_to_degrees(wind_angle), 'Wind Data', 'Deg', '130306')
    _LOGGER.debug('Wind Angle  : %s', wind_angle)

    # reference | Offset: 40, Length: 3, Resolution: 1, Field Type: LOOKUP
    reference_raw = (data_raw >> 40) & 0x7
    reference = reference_raw * 1
    publish_field(hass, instance_name, 'reference', 'Reference', reference, 'Wind Data', '', '130306')
    _LOGGER.debug('Reference  : %s', reference)

    # reserved | Offset: 43, Length: 21, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 43) & 0x1FFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Wind Data', '', '130306')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_130310(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130310."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Environmental Parameters (obsolete)', '', '130310')
    _LOGGER.debug('SID  : %s', sid)

    # water_temperature | Offset: 8, Length: 16, Resolution: 0.01, Field Type: NUMBER
    water_temperature_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    water_temperature = water_temperature_raw * 0.01
    publish_field(hass, instance_name, 'water_temperature', 'Water Temperature', water_temperature, 'Environmental Parameters (obsolete)', 'K', '130310')
    publish_field(hass, instance_name, 'water_temperature_celsius', 'Water Temperature Celsius', kelvin_to_celsius(water_temperature), 'Environmental Parameters (obsolete)', 'C', '130310')
    publish_field(hass, instance_name, 'water_temperature_fahrenheit', 'Water Temperature Fahrenheit', kelvin_to_fahrenheit(water_temperature), 'Environmental Parameters (obsolete)', 'F', '130310')
    _LOGGER.debug('Water Temperature  : %s', water_temperature)

    # outside_ambient_air_temperature | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    outside_ambient_air_temperature_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    outside_ambient_air_temperature = outside_ambient_air_temperature_raw * 0.01
    publish_field(hass, instance_name, 'outside_ambient_air_temperature', 'Outside Ambient Air Temperature', outside_ambient_air_temperature, 'Environmental Parameters (obsolete)', 'K', '130310')
    publish_field(hass, instance_name, 'outside_ambient_air_temperature_celsius', 'Outside Ambient Air Temperature Celsius', kelvin_to_celsius(outside_ambient_air_temperature), 'Environmental Parameters (obsolete)', 'C', '130310')
    publish_field(hass, instance_name, 'outside_ambient_air_temperature_fahrenheit', 'Outside Ambient Air Temperature Fahrenheit', kelvin_to_fahrenheit(outside_ambient_air_temperature), 'Environmental Parameters (obsolete)', 'F', '130310')
    _LOGGER.debug('Outside Ambient Air Temperature  : %s', outside_ambient_air_temperature)

    # atmospheric_pressure | Offset: 40, Length: 16, Resolution: 100, Field Type: NUMBER
    atmospheric_pressure_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    atmospheric_pressure = atmospheric_pressure_raw * 100
    publish_field(hass, instance_name, 'atmospheric_pressure', 'Atmospheric Pressure', atmospheric_pressure, 'Environmental Parameters (obsolete)', 'Pa', '130310')
    _LOGGER.debug('Atmospheric Pressure  : %s', atmospheric_pressure)

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Environmental Parameters (obsolete)', '', '130310')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_130311(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130311."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Environmental Parameters', '', '130311')
    _LOGGER.debug('SID  : %s', sid)

    # temperature_source | Offset: 8, Length: 6, Resolution: 1, Field Type: LOOKUP
    temperature_source_raw = (data_raw >> 8) & 0x3F
    temperature_source = temperature_source_raw * 1
    publish_field(hass, instance_name, 'temperature_source', 'Temperature Source', temperature_source, 'Environmental Parameters', '', '130311')
    _LOGGER.debug('Temperature Source  : %s', temperature_source)

    # humidity_source | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    humidity_source_raw = (data_raw >> 14) & 0x3
    humidity_source = humidity_source_raw * 1
    publish_field(hass, instance_name, 'humidity_source', 'Humidity Source', humidity_source, 'Environmental Parameters', '', '130311')
    _LOGGER.debug('Humidity Source  : %s', humidity_source)

    # temperature | Offset: 16, Length: 16, Resolution: 0.01, Field Type: NUMBER
    temperature_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    temperature = temperature_raw * 0.01
    publish_field(hass, instance_name, 'temperature', 'Temperature', temperature, 'Environmental Parameters', 'K', '130311')
    publish_field(hass, instance_name, 'temperature_celsius', 'Temperature Celsius', kelvin_to_celsius(temperature), 'Environmental Parameters', 'C', '130311')
    publish_field(hass, instance_name, 'temperature_fahrenheit', 'Temperature Fahrenheit', kelvin_to_fahrenheit(temperature), 'Environmental Parameters', 'F', '130311')
    _LOGGER.debug('Temperature  : %s', temperature)

    # humidity | Offset: 32, Length: 16, Resolution: 0.004, Field Type: NUMBER
    humidity_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if humidity_raw & (1 << (16 - 1)):
        humidity_raw -= (1 << 16)
    humidity = humidity_raw * 0.004
    publish_field(hass, instance_name, 'humidity', 'Humidity', humidity, 'Environmental Parameters', '%', '130311')
    _LOGGER.debug('Humidity  : %s', humidity)

    # atmospheric_pressure | Offset: 48, Length: 16, Resolution: 100, Field Type: NUMBER
    atmospheric_pressure_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    atmospheric_pressure = atmospheric_pressure_raw * 100
    publish_field(hass, instance_name, 'atmospheric_pressure', 'Atmospheric Pressure', atmospheric_pressure, 'Environmental Parameters', 'Pa', '130311')
    _LOGGER.debug('Atmospheric Pressure  : %s', atmospheric_pressure)

def process_pgn_130577(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130577."""
    # data_mode | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    data_mode_raw = (data_raw >> 0) & 0xF
    data_mode = data_mode_raw * 1
    publish_field(hass, instance_name, 'data_mode', 'Data Mode', data_mode, 'Direction Data', '', '130577')
    _LOGGER.debug('Data Mode  : %s', data_mode)

    # cog_reference | Offset: 4, Length: 2, Resolution: 1, Field Type: LOOKUP
    cog_reference_raw = (data_raw >> 4) & 0x3
    cog_reference = cog_reference_raw * 1
    publish_field(hass, instance_name, 'cog_reference', 'COG Reference', cog_reference, 'Direction Data', '', '130577')
    _LOGGER.debug('COG Reference  : %s', cog_reference)

    # reserved | Offset: 6, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 6) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Direction Data', '', '130577')
    _LOGGER.debug('Reserved  : %s', reserved)

    # sid | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Direction Data', '', '130577')
    _LOGGER.debug('SID  : %s', sid)

    # cog | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'Direction Data', 'rad', '130577')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'Direction Data', 'Deg', '130577')
    _LOGGER.debug('COG  : %s', cog)

    # sog | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    sog_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    sog = sog_raw * 0.01
    publish_field(hass, instance_name, 'sog', 'SOG', sog, 'Direction Data', 'm/s', '130577')
    publish_field(hass, instance_name, 'sog_knots', 'SOG Knots', mps_to_knots(sog), 'Direction Data', 'Kn', '130577')
    _LOGGER.debug('SOG  : %s', sog)

    # heading | Offset: 48, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    heading = heading_raw * 0.0001
    publish_field(hass, instance_name, 'heading', 'Heading', heading, 'Direction Data', 'rad', '130577')
    publish_field(hass, instance_name, 'heading_degrees', 'Heading Degrees', radians_to_degrees(heading), 'Direction Data', 'Deg', '130577')
    _LOGGER.debug('Heading  : %s', heading)

    # speed_through_water | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    speed_through_water_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    speed_through_water = speed_through_water_raw * 0.01
    publish_field(hass, instance_name, 'speed_through_water', 'Speed through Water', speed_through_water, 'Direction Data', 'm/s', '130577')
    publish_field(hass, instance_name, 'speed_through_water_knots', 'Speed through Water Knots', mps_to_knots(speed_through_water), 'Direction Data', 'Kn', '130577')
    _LOGGER.debug('Speed through Water  : %s', speed_through_water)

    # set | Offset: 80, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    set_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    set = set_raw * 0.0001
    publish_field(hass, instance_name, 'set', 'Set', set, 'Direction Data', 'rad', '130577')
    publish_field(hass, instance_name, 'set_degrees', 'Set Degrees', radians_to_degrees(set), 'Direction Data', 'Deg', '130577')
    _LOGGER.debug('Set  : %s', set)

    # drift | Offset: 96, Length: 16, Resolution: 0.01, Field Type: NUMBER
    drift_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    drift = drift_raw * 0.01
    publish_field(hass, instance_name, 'drift', 'Drift', drift, 'Direction Data', 'm/s', '130577')
    publish_field(hass, instance_name, 'drift_knots', 'Drift Knots', mps_to_knots(drift), 'Direction Data', 'Kn', '130577')
    _LOGGER.debug('Drift  : %s', drift)

