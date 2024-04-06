from .utils import *
import logging
_LOGGER = logging.getLogger(__name__)

def process_pgn_65359(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65359."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Pilot Heading', '', '65359')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Heading', '', '65359')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Pilot Heading', '', '65359')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: BINARY
    sid_raw = (data_raw >> 16) & 0xFF
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Seatalk: Pilot Heading', '', '65359')
    _LOGGER.debug('SID  : %s', sid)

    # heading_true | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_true_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    heading_true = heading_true_raw * 0.0001
    publish_field(hass, instance_name, 'heading_true', 'Heading True', heading_true, 'Seatalk: Pilot Heading', 'rad', '65359')
    publish_field(hass, instance_name, 'heading_true_degrees', 'Heading True Degrees', radians_to_degrees(heading_true), 'Seatalk: Pilot Heading', 'Deg', '65359')
    _LOGGER.debug('Heading True  : %s', heading_true)

    # heading_magnetic | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_magnetic_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    heading_magnetic = heading_magnetic_raw * 0.0001
    publish_field(hass, instance_name, 'heading_magnetic', 'Heading Magnetic', heading_magnetic, 'Seatalk: Pilot Heading', 'rad', '65359')
    publish_field(hass, instance_name, 'heading_magnetic_degrees', 'Heading Magnetic Degrees', radians_to_degrees(heading_magnetic), 'Seatalk: Pilot Heading', 'Deg', '65359')
    _LOGGER.debug('Heading Magnetic  : %s', heading_magnetic)

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Heading', '', '65359')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_65379(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65379."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Pilot Mode', '', '65379')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Mode', '', '65379')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Pilot Mode', '', '65379')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # pilot_mode | Offset: 16, Length: 8, Resolution: 1, Field Type: BINARY
    pilot_mode_raw = (data_raw >> 16) & 0xFF
    pilot_mode = pilot_mode_raw * 1
    publish_field(hass, instance_name, 'pilot_mode', 'Pilot Mode', pilot_mode, 'Seatalk: Pilot Mode', '', '65379')
    _LOGGER.debug('Pilot Mode  : %s', pilot_mode)

    # sub_mode | Offset: 24, Length: 8, Resolution: 1, Field Type: BINARY
    sub_mode_raw = (data_raw >> 24) & 0xFF
    sub_mode = sub_mode_raw * 1
    publish_field(hass, instance_name, 'sub_mode', 'Sub Mode', sub_mode, 'Seatalk: Pilot Mode', '', '65379')
    _LOGGER.debug('Sub Mode  : %s', sub_mode)

    # pilot_mode_data | Offset: 32, Length: 8, Resolution: 1, Field Type: BINARY
    pilot_mode_data_raw = (data_raw >> 32) & 0xFF
    pilot_mode_data = pilot_mode_data_raw * 1
    publish_field(hass, instance_name, 'pilot_mode_data', 'Pilot Mode Data', pilot_mode_data, 'Seatalk: Pilot Mode', '', '65379')
    _LOGGER.debug('Pilot Mode Data  : %s', pilot_mode_data)

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Mode', '', '65379')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_126992(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126992."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'System Time', '', '126992')
    _LOGGER.debug('SID  : %s', sid)

    # source | Offset: 8, Length: 4, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 8) & 0xF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'System Time', '', '126992')
    _LOGGER.debug('Source  : %s', source)

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'System Time', '', '126992')
    _LOGGER.debug('Reserved  : %s', reserved)

    # date | Offset: 16, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 16) & 0xFFFF
    date = date_raw * 1
    publish_field(hass, instance_name, 'date', 'Date', date, 'System Time', 'd', '126992')
    _LOGGER.debug('Date  : %s', date)

    # time | Offset: 32, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 32) & 0xFFFFFFFF
    time = time_raw * 0.0001
    publish_field(hass, instance_name, 'time', 'Time', time, 'System Time', 's', '126992')
    _LOGGER.debug('Time  : %s', time)

def process_pgn_127245(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127245."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Rudder', '', '127245')
    _LOGGER.debug('Instance  : %s', instance)

    # direction_order | Offset: 8, Length: 3, Resolution: 1, Field Type: LOOKUP
    direction_order_raw = (data_raw >> 8) & 0x7
    direction_order = direction_order_raw * 1
    publish_field(hass, instance_name, 'direction_order', 'Direction Order', direction_order, 'Rudder', '', '127245')
    _LOGGER.debug('Direction Order  : %s', direction_order)

    # reserved | Offset: 11, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Rudder', '', '127245')
    _LOGGER.debug('Reserved  : %s', reserved)

    # angle_order | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    angle_order_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    if angle_order_raw & (1 << (16 - 1)):
        angle_order_raw -= (1 << 16)
    angle_order = angle_order_raw * 0.0001
    publish_field(hass, instance_name, 'angle_order', 'Angle Order', angle_order, 'Rudder', 'rad', '127245')
    publish_field(hass, instance_name, 'angle_order_degrees', 'Angle Order Degrees', radians_to_degrees(angle_order), 'Rudder', 'Deg', '127245')
    _LOGGER.debug('Angle Order  : %s', angle_order)

    # position | Offset: 32, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    position_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if position_raw & (1 << (16 - 1)):
        position_raw -= (1 << 16)
    position = position_raw * 0.0001
    publish_field(hass, instance_name, 'position', 'Position', position, 'Rudder', 'rad', '127245')
    publish_field(hass, instance_name, 'position_degrees', 'Position Degrees', radians_to_degrees(position), 'Rudder', 'Deg', '127245')
    _LOGGER.debug('Position  : %s', position)

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Rudder', '', '127245')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_127251(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127251."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Rate of Turn', '', '127251')
    _LOGGER.debug('SID  : %s', sid)

    # rate | Offset: 8, Length: 32, Resolution: 3.125e-08, Field Type: NUMBER
    rate_raw = decode_number((data_raw >> 8) & 0xFFFFFFFF, 32)
    if rate_raw & (1 << (32 - 1)):
        rate_raw -= (1 << 32)
    rate = rate_raw * 3.125e-08
    publish_field(hass, instance_name, 'rate', 'Rate', rate, 'Rate of Turn', 'rad/s', '127251')
    _LOGGER.debug('Rate  : %s', rate)

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Rate of Turn', '', '127251')
    _LOGGER.debug('Reserved  : %s', reserved)

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

def process_pgn_129029(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129029."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('SID  : %s', sid)

    # date | Offset: 8, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 8) & 0xFFFF
    date = date_raw * 1
    publish_field(hass, instance_name, 'date', 'Date', date, 'GNSS Position Data', 'd', '129029')
    _LOGGER.debug('Date  : %s', date)

    # time | Offset: 24, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 24) & 0xFFFFFFFF
    time = time_raw * 0.0001
    publish_field(hass, instance_name, 'time', 'Time', time, 'GNSS Position Data', 's', '129029')
    _LOGGER.debug('Time  : %s', time)

    # latitude | Offset: 56, Length: 64, Resolution: 1e-16, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 56) & 0xFFFFFFFFFFFFFFFF, 64)
    if latitude_raw & (1 << (64 - 1)):
        latitude_raw -= (1 << 64)
    latitude = latitude_raw * 1e-16
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'GNSS Position Data', 'deg', '129029')
    _LOGGER.debug('Latitude  : %s', latitude)

    # longitude | Offset: 120, Length: 64, Resolution: 1e-16, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 120) & 0xFFFFFFFFFFFFFFFF, 64)
    if longitude_raw & (1 << (64 - 1)):
        longitude_raw -= (1 << 64)
    longitude = longitude_raw * 1e-16
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'GNSS Position Data', 'deg', '129029')
    _LOGGER.debug('Longitude  : %s', longitude)

    # altitude | Offset: 184, Length: 64, Resolution: 1e-06, Field Type: NUMBER
    altitude_raw = decode_number((data_raw >> 184) & 0xFFFFFFFFFFFFFFFF, 64)
    if altitude_raw & (1 << (64 - 1)):
        altitude_raw -= (1 << 64)
    altitude = altitude_raw * 1e-06
    publish_field(hass, instance_name, 'altitude', 'Altitude', altitude, 'GNSS Position Data', 'm', '129029')
    _LOGGER.debug('Altitude  : %s', altitude)

    # gnss_type | Offset: 248, Length: 4, Resolution: 1, Field Type: LOOKUP
    gnss_type_raw = (data_raw >> 248) & 0xF
    gnss_type = gnss_type_raw * 1
    publish_field(hass, instance_name, 'gnss_type', 'GNSS type', gnss_type, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('GNSS type  : %s', gnss_type)

    # method | Offset: 252, Length: 4, Resolution: 1, Field Type: LOOKUP
    method_raw = (data_raw >> 252) & 0xF
    method = method_raw * 1
    publish_field(hass, instance_name, 'method', 'Method', method, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('Method  : %s', method)

    # integrity | Offset: 256, Length: 2, Resolution: 1, Field Type: LOOKUP
    integrity_raw = (data_raw >> 256) & 0x3
    integrity = integrity_raw * 1
    publish_field(hass, instance_name, 'integrity', 'Integrity', integrity, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('Integrity  : %s', integrity)

    # reserved | Offset: 258, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 258) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('Reserved  : %s', reserved)

    # number_of_svs | Offset: 264, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_svs_raw = decode_number((data_raw >> 264) & 0xFF, 8)
    number_of_svs = number_of_svs_raw * 1
    publish_field(hass, instance_name, 'number_of_svs', 'Number of SVs', number_of_svs, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('Number of SVs  : %s', number_of_svs)

    # hdop | Offset: 272, Length: 16, Resolution: 0.01, Field Type: NUMBER
    hdop_raw = decode_number((data_raw >> 272) & 0xFFFF, 16)
    if hdop_raw & (1 << (16 - 1)):
        hdop_raw -= (1 << 16)
    hdop = hdop_raw * 0.01
    publish_field(hass, instance_name, 'hdop', 'HDOP', hdop, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('HDOP  : %s', hdop)

    # pdop | Offset: 288, Length: 16, Resolution: 0.01, Field Type: NUMBER
    pdop_raw = decode_number((data_raw >> 288) & 0xFFFF, 16)
    if pdop_raw & (1 << (16 - 1)):
        pdop_raw -= (1 << 16)
    pdop = pdop_raw * 0.01
    publish_field(hass, instance_name, 'pdop', 'PDOP', pdop, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('PDOP  : %s', pdop)

    # geoidal_separation | Offset: 304, Length: 32, Resolution: 0.01, Field Type: NUMBER
    geoidal_separation_raw = decode_number((data_raw >> 304) & 0xFFFFFFFF, 32)
    if geoidal_separation_raw & (1 << (32 - 1)):
        geoidal_separation_raw -= (1 << 32)
    geoidal_separation = geoidal_separation_raw * 0.01
    publish_field(hass, instance_name, 'geoidal_separation', 'Geoidal Separation', geoidal_separation, 'GNSS Position Data', 'm', '129029')
    _LOGGER.debug('Geoidal Separation  : %s', geoidal_separation)

    # reference_stations | Offset: 336, Length: 8, Resolution: 1, Field Type: NUMBER
    reference_stations_raw = decode_number((data_raw >> 336) & 0xFF, 8)
    reference_stations = reference_stations_raw * 1
    publish_field(hass, instance_name, 'reference_stations', 'Reference Stations', reference_stations, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('Reference Stations  : %s', reference_stations)

    # reference_station_type | Offset: 344, Length: 4, Resolution: 1, Field Type: LOOKUP
    reference_station_type_raw = (data_raw >> 344) & 0xF
    reference_station_type = reference_station_type_raw * 1
    publish_field(hass, instance_name, 'reference_station_type', 'Reference Station Type', reference_station_type, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('Reference Station Type  : %s', reference_station_type)

    # reference_station_id | Offset: 348, Length: 12, Resolution: 1, Field Type: NUMBER
    reference_station_id_raw = decode_number((data_raw >> 348) & 0xFFF, 12)
    reference_station_id = reference_station_id_raw * 1
    publish_field(hass, instance_name, 'reference_station_id', 'Reference Station ID', reference_station_id, 'GNSS Position Data', '', '129029')
    _LOGGER.debug('Reference Station ID  : %s', reference_station_id)

    # age_of_dgnss_corrections | Offset: 360, Length: 16, Resolution: 0.01, Field Type: TIME
    age_of_dgnss_corrections_raw = (data_raw >> 360) & 0xFFFF
    age_of_dgnss_corrections = age_of_dgnss_corrections_raw * 0.01
    publish_field(hass, instance_name, 'age_of_dgnss_corrections', 'Age of DGNSS Corrections', age_of_dgnss_corrections, 'GNSS Position Data', 's', '129029')
    _LOGGER.debug('Age of DGNSS Corrections  : %s', age_of_dgnss_corrections)

def process_pgn_129033(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129033."""
    # date | Offset: 0, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 0) & 0xFFFF
    date = date_raw * 1
    publish_field(hass, instance_name, 'date', 'Date', date, 'Time & Date', 'd', '129033')
    _LOGGER.debug('Date  : %s', date)

    # time | Offset: 16, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 16) & 0xFFFFFFFF
    time = time_raw * 0.0001
    publish_field(hass, instance_name, 'time', 'Time', time, 'Time & Date', 's', '129033')
    _LOGGER.debug('Time  : %s', time)

    # local_offset | Offset: 48, Length: 16, Resolution: 60, Field Type: TIME
    local_offset_raw = (data_raw >> 48) & 0xFFFF
    if local_offset_raw & (1 << (16 - 1)):
        local_offset_raw -= (1 << 16)
    local_offset = local_offset_raw * 60
    publish_field(hass, instance_name, 'local_offset', 'Local Offset', local_offset, 'Time & Date', 's', '129033')
    _LOGGER.debug('Local Offset  : %s', local_offset)

def process_pgn_129291(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129291."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Set & Drift, Rapid Update', '', '129291')
    _LOGGER.debug('SID  : %s', sid)

    # set_reference | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    set_reference_raw = (data_raw >> 8) & 0x3
    set_reference = set_reference_raw * 1
    publish_field(hass, instance_name, 'set_reference', 'Set Reference', set_reference, 'Set & Drift, Rapid Update', '', '129291')
    _LOGGER.debug('Set Reference  : %s', set_reference)

    # reserved | Offset: 10, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 10) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Set & Drift, Rapid Update', '', '129291')
    _LOGGER.debug('Reserved  : %s', reserved)

    # set | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    set_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    set = set_raw * 0.0001
    publish_field(hass, instance_name, 'set', 'Set', set, 'Set & Drift, Rapid Update', 'rad', '129291')
    publish_field(hass, instance_name, 'set_degrees', 'Set Degrees', radians_to_degrees(set), 'Set & Drift, Rapid Update', 'Deg', '129291')
    _LOGGER.debug('Set  : %s', set)

    # drift | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    drift_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    drift = drift_raw * 0.01
    publish_field(hass, instance_name, 'drift', 'Drift', drift, 'Set & Drift, Rapid Update', 'm/s', '129291')
    publish_field(hass, instance_name, 'drift_knots', 'Drift Knots', mps_to_knots(drift), 'Set & Drift, Rapid Update', 'Kn', '129291')
    _LOGGER.debug('Drift  : %s', drift)

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Set & Drift, Rapid Update', '', '129291')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_129540(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129540."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS Sats in View', '', '129540')
    _LOGGER.debug('SID  : %s', sid)

    # range_residual_mode | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    range_residual_mode_raw = (data_raw >> 8) & 0x3
    range_residual_mode = range_residual_mode_raw * 1
    publish_field(hass, instance_name, 'range_residual_mode', 'Range Residual Mode', range_residual_mode, 'GNSS Sats in View', '', '129540')
    _LOGGER.debug('Range Residual Mode  : %s', range_residual_mode)

    # reserved | Offset: 10, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 10) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS Sats in View', '', '129540')
    _LOGGER.debug('Reserved  : %s', reserved)

    # sats_in_view | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    sats_in_view_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    sats_in_view = sats_in_view_raw * 1
    publish_field(hass, instance_name, 'sats_in_view', 'Sats in View', sats_in_view, 'GNSS Sats in View', '', '129540')
    _LOGGER.debug('Sats in View  : %s', sats_in_view)

    # prn | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    prn_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    prn = prn_raw * 1
    publish_field(hass, instance_name, 'prn', 'PRN', prn, 'GNSS Sats in View', '', '129540')
    _LOGGER.debug('PRN  : %s', prn)

    # elevation | Offset: 32, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    elevation_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if elevation_raw & (1 << (16 - 1)):
        elevation_raw -= (1 << 16)
    elevation = elevation_raw * 0.0001
    publish_field(hass, instance_name, 'elevation', 'Elevation', elevation, 'GNSS Sats in View', 'rad', '129540')
    publish_field(hass, instance_name, 'elevation_degrees', 'Elevation Degrees', radians_to_degrees(elevation), 'GNSS Sats in View', 'Deg', '129540')
    _LOGGER.debug('Elevation  : %s', elevation)

    # azimuth | Offset: 48, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    azimuth_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    azimuth = azimuth_raw * 0.0001
    publish_field(hass, instance_name, 'azimuth', 'Azimuth', azimuth, 'GNSS Sats in View', 'rad', '129540')
    publish_field(hass, instance_name, 'azimuth_degrees', 'Azimuth Degrees', radians_to_degrees(azimuth), 'GNSS Sats in View', 'Deg', '129540')
    _LOGGER.debug('Azimuth  : %s', azimuth)

    # snr | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    snr_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    snr = snr_raw * 0.01
    publish_field(hass, instance_name, 'snr', 'SNR', snr, 'GNSS Sats in View', 'dB', '129540')
    _LOGGER.debug('SNR  : %s', snr)

    # range_residuals | Offset: 80, Length: 32, Resolution: 1, Field Type: NUMBER
    range_residuals_raw = decode_number((data_raw >> 80) & 0xFFFFFFFF, 32)
    if range_residuals_raw & (1 << (32 - 1)):
        range_residuals_raw -= (1 << 32)
    range_residuals = range_residuals_raw * 1
    publish_field(hass, instance_name, 'range_residuals', 'Range residuals', range_residuals, 'GNSS Sats in View', '', '129540')
    _LOGGER.debug('Range residuals  : %s', range_residuals)

    # status | Offset: 112, Length: 4, Resolution: 1, Field Type: LOOKUP
    status_raw = (data_raw >> 112) & 0xF
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'GNSS Sats in View', '', '129540')
    _LOGGER.debug('Status  : %s', status)

    # reserved | Offset: 116, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 116) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS Sats in View', '', '129540')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_129542(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129542."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS Pseudorange Noise Statistics', '', '129542')
    _LOGGER.debug('SID  : %s', sid)

    # rms_of_position_uncertainty | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    rms_of_position_uncertainty_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    rms_of_position_uncertainty = rms_of_position_uncertainty_raw * 1
    publish_field(hass, instance_name, 'rms_of_position_uncertainty', 'RMS of Position Uncertainty', rms_of_position_uncertainty, 'GNSS Pseudorange Noise Statistics', '', '129542')
    _LOGGER.debug('RMS of Position Uncertainty  : %s', rms_of_position_uncertainty)

    # std_of_major_axis | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_major_axis_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    std_of_major_axis = std_of_major_axis_raw * 1
    publish_field(hass, instance_name, 'std_of_major_axis', 'STD of Major axis', std_of_major_axis, 'GNSS Pseudorange Noise Statistics', '', '129542')
    _LOGGER.debug('STD of Major axis  : %s', std_of_major_axis)

    # std_of_minor_axis | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_minor_axis_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    std_of_minor_axis = std_of_minor_axis_raw * 1
    publish_field(hass, instance_name, 'std_of_minor_axis', 'STD of Minor axis', std_of_minor_axis, 'GNSS Pseudorange Noise Statistics', '', '129542')
    _LOGGER.debug('STD of Minor axis  : %s', std_of_minor_axis)

    # orientation_of_major_axis | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    orientation_of_major_axis_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    orientation_of_major_axis = orientation_of_major_axis_raw * 1
    publish_field(hass, instance_name, 'orientation_of_major_axis', 'Orientation of Major axis', orientation_of_major_axis, 'GNSS Pseudorange Noise Statistics', '', '129542')
    _LOGGER.debug('Orientation of Major axis  : %s', orientation_of_major_axis)

    # std_of_lat_error | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_lat_error_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    std_of_lat_error = std_of_lat_error_raw * 1
    publish_field(hass, instance_name, 'std_of_lat_error', 'STD of Lat Error', std_of_lat_error, 'GNSS Pseudorange Noise Statistics', '', '129542')
    _LOGGER.debug('STD of Lat Error  : %s', std_of_lat_error)

    # std_of_lon_error | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_lon_error_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    std_of_lon_error = std_of_lon_error_raw * 1
    publish_field(hass, instance_name, 'std_of_lon_error', 'STD of Lon Error', std_of_lon_error, 'GNSS Pseudorange Noise Statistics', '', '129542')
    _LOGGER.debug('STD of Lon Error  : %s', std_of_lon_error)

    # std_of_alt_error | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_alt_error_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    std_of_alt_error = std_of_alt_error_raw * 1
    publish_field(hass, instance_name, 'std_of_alt_error', 'STD of Alt Error', std_of_alt_error, 'GNSS Pseudorange Noise Statistics', '', '129542')
    _LOGGER.debug('STD of Alt Error  : %s', std_of_alt_error)

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

