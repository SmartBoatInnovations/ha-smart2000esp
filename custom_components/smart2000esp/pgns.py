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

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # command | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'command', command, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('command  : %s', command)

    # unknown_1 | Offset: 40, Length: 24, Resolution: 1, Field Type: BINARY
    unknown_1_raw = (data_raw >> 40) & 0xFFFFFF
    unknown_1 = unknown_1_raw * 1
    publish_field(hass, instance_name, 'unknown_1', 'Unknown 1', unknown_1, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Unknown 1  : %s', unknown_1)

    # pilot_mode | Offset: 64, Length: 8, Resolution: 1, Field Type: LOOKUP
    pilot_mode_raw = (data_raw >> 64) & 0xFF
    pilot_mode = pilot_mode_raw * 1
    publish_field(hass, instance_name, 'pilot_mode', 'Pilot Mode', pilot_mode, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Pilot Mode  : %s', pilot_mode)

    # sub_mode | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    sub_mode_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    sub_mode = sub_mode_raw * 1
    publish_field(hass, instance_name, 'sub_mode', 'Sub Mode', sub_mode, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Sub Mode  : %s', sub_mode)

    # pilot_mode_data | Offset: 80, Length: 8, Resolution: 1, Field Type: BINARY
    pilot_mode_data_raw = (data_raw >> 80) & 0xFF
    pilot_mode_data = pilot_mode_data_raw * 1
    publish_field(hass, instance_name, 'pilot_mode_data', 'Pilot Mode Data', pilot_mode_data, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Pilot Mode Data  : %s', pilot_mode_data)

    # unknown_2 | Offset: 88, Length: 80, Resolution: 1, Field Type: BINARY
    unknown_2_raw = (data_raw >> 88) & 0xFFFFFFFFFFFFFFFFFFFF
    unknown_2 = unknown_2_raw * 1
    publish_field(hass, instance_name, 'unknown_2', 'Unknown 2', unknown_2, 'Seatalk1: Pilot Mode', '', '126720')
    _LOGGER.debug('Unknown 2  : %s', unknown_2)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Media Control', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Media Control', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Media Control', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Media Control', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Media Control', '', '126720')
    _LOGGER.debug('Unknown  : %s', unknown)

    # source_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'Fusion: Media Control', '', '126720')
    _LOGGER.debug('Source ID  : %s', source_id)

    # command | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    command_raw = (data_raw >> 40) & 0xFF
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Fusion: Media Control', '', '126720')
    _LOGGER.debug('Command  : %s', command)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Sirius Control', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Sirius Control', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Sirius Control', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Sirius Control', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Sirius Control', '', '126720')
    _LOGGER.debug('Unknown  : %s', unknown)

    # source_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'Fusion: Sirius Control', '', '126720')
    _LOGGER.debug('Source ID  : %s', source_id)

    # command | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    command_raw = (data_raw >> 40) & 0xFF
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Fusion: Sirius Control', '', '126720')
    _LOGGER.debug('Command  : %s', command)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Request Status', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Request Status', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Request Status', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Request Status', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Request Status', '', '126720')
    _LOGGER.debug('Unknown  : %s', unknown)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Set Source', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Set Source', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Set Source', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Set Source', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Set Source', '', '126720')
    _LOGGER.debug('Unknown  : %s', unknown)

    # source_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'Fusion: Set Source', '', '126720')
    _LOGGER.debug('Source ID  : %s', source_id)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Set Mute', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Set Mute', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Set Mute', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Set Mute', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # command | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    command_raw = (data_raw >> 24) & 0xFF
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Fusion: Set Mute', '', '126720')
    _LOGGER.debug('Command  : %s', command)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Set Zone Volume', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Set Zone Volume', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Set Zone Volume', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Set Zone Volume', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Set Zone Volume', '', '126720')
    _LOGGER.debug('Unknown  : %s', unknown)

    # zone | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    zone = zone_raw * 1
    publish_field(hass, instance_name, 'zone', 'Zone', zone, 'Fusion: Set Zone Volume', '', '126720')
    _LOGGER.debug('Zone  : %s', zone)

    # volume | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    volume_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    volume = volume_raw * 1
    publish_field(hass, instance_name, 'volume', 'Volume', volume, 'Fusion: Set Zone Volume', '', '126720')
    _LOGGER.debug('Volume  : %s', volume)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Unknown  : %s', unknown)

    # zone1 | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    zone1_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    zone1 = zone1_raw * 1
    publish_field(hass, instance_name, 'zone1', 'Zone1', zone1, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Zone1  : %s', zone1)

    # zone2 | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone2_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone2 = zone2_raw * 1
    publish_field(hass, instance_name, 'zone2', 'Zone2', zone2, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Zone2  : %s', zone2)

    # zone3 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    zone3_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    zone3 = zone3_raw * 1
    publish_field(hass, instance_name, 'zone3', 'Zone3', zone3, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Zone3  : %s', zone3)

    # zone4 | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    zone4_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    zone4 = zone4_raw * 1
    publish_field(hass, instance_name, 'zone4', 'Zone4', zone4, 'Fusion: Set All Volumes', '', '126720')
    _LOGGER.debug('Zone4  : %s', zone4)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # command | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'command', command, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('command  : %s', command)

    # device | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    device_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    device = device_raw * 1
    publish_field(hass, instance_name, 'device', 'device', device, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('device  : %s', device)

    # key | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    key_raw = (data_raw >> 48) & 0xFF
    key = key_raw * 1
    publish_field(hass, instance_name, 'key', 'key', key, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('key  : %s', key)

    # keyinverted | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    keyinverted_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    keyinverted = keyinverted_raw * 1
    publish_field(hass, instance_name, 'keyinverted', 'keyInverted', keyinverted, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('keyInverted  : %s', keyinverted)

    # unknown_data | Offset: 64, Length: 112, Resolution: 1, Field Type: BINARY
    unknown_data_raw = (data_raw >> 64) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    unknown_data = unknown_data_raw * 1
    publish_field(hass, instance_name, 'unknown_data', 'Unknown data', unknown_data, 'Seatalk1: Keystroke', '', '126720')
    _LOGGER.debug('Unknown data  : %s', unknown_data)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Device Identification', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Device Identification', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Device Identification', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Device Identification', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # command | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'command', command, 'Seatalk1: Device Identification', '', '126720')
    _LOGGER.debug('command  : %s', command)

    # reserved | Offset: 40, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Device Identification', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # device | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    device_raw = (data_raw >> 48) & 0xFF
    device = device_raw * 1
    publish_field(hass, instance_name, 'device', 'device', device, 'Seatalk1: Device Identification', '', '126720')
    _LOGGER.debug('device  : %s', device)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Display Brightness', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Display Brightness', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Display Brightness', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Display Brightness', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # group | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_raw = (data_raw >> 32) & 0xFF
    group = group_raw * 1
    publish_field(hass, instance_name, 'group', 'Group', group, 'Seatalk1: Display Brightness', '', '126720')
    _LOGGER.debug('Group  : %s', group)

    # unknown_1 | Offset: 40, Length: 8, Resolution: 1, Field Type: BINARY
    unknown_1_raw = (data_raw >> 40) & 0xFF
    unknown_1 = unknown_1_raw * 1
    publish_field(hass, instance_name, 'unknown_1', 'Unknown 1', unknown_1, 'Seatalk1: Display Brightness', '', '126720')
    _LOGGER.debug('Unknown 1  : %s', unknown_1)

    # command | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Seatalk1: Display Brightness', '', '126720')
    _LOGGER.debug('Command  : %s', command)

    # brightness | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    brightness_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    brightness = brightness_raw * 1
    publish_field(hass, instance_name, 'brightness', 'Brightness', brightness, 'Seatalk1: Display Brightness', '%', '126720')
    _LOGGER.debug('Brightness  : %s', brightness)

    # unknown_2 | Offset: 64, Length: 8, Resolution: 1, Field Type: BINARY
    unknown_2_raw = (data_raw >> 64) & 0xFF
    unknown_2 = unknown_2_raw * 1
    publish_field(hass, instance_name, 'unknown_2', 'Unknown 2', unknown_2, 'Seatalk1: Display Brightness', '', '126720')
    _LOGGER.debug('Unknown 2  : %s', unknown_2)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # group | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_raw = (data_raw >> 32) & 0xFF
    group = group_raw * 1
    publish_field(hass, instance_name, 'group', 'Group', group, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Group  : %s', group)

    # unknown_1 | Offset: 40, Length: 8, Resolution: 1, Field Type: BINARY
    unknown_1_raw = (data_raw >> 40) & 0xFF
    unknown_1 = unknown_1_raw * 1
    publish_field(hass, instance_name, 'unknown_1', 'Unknown 1', unknown_1, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Unknown 1  : %s', unknown_1)

    # command | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Command  : %s', command)

    # color | Offset: 56, Length: 8, Resolution: 1, Field Type: LOOKUP
    color_raw = (data_raw >> 56) & 0xFF
    color = color_raw * 1
    publish_field(hass, instance_name, 'color', 'Color', color, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Color  : %s', color)

    # unknown_2 | Offset: 64, Length: 8, Resolution: 1, Field Type: BINARY
    unknown_2_raw = (data_raw >> 64) & 0xFF
    unknown_2 = unknown_2_raw * 1
    publish_field(hass, instance_name, 'unknown_2', 'Unknown 2', unknown_2, 'Seatalk1: Display Color', '', '126720')
    _LOGGER.debug('Unknown 2  : %s', unknown_2)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Attitude Offset', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Attitude Offset', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Attitude Offset', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Attitude Offset', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # azimuth_offset | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    azimuth_offset_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if azimuth_offset_raw & (1 << (16 - 1)):
        azimuth_offset_raw -= (1 << 16)
    azimuth_offset = azimuth_offset_raw * 0.0001
    publish_field(hass, instance_name, 'azimuth_offset', 'Azimuth offset', azimuth_offset, 'Airmar: Attitude Offset', 'rad', '126720')
    publish_field(hass, instance_name, 'azimuth_offset_degrees', 'Azimuth offset Degrees', radians_to_degrees(azimuth_offset), 'Airmar: Attitude Offset', 'Deg', '126720')
    _LOGGER.debug('Azimuth offset  : %s', azimuth_offset)

    # pitch_offset | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    pitch_offset_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if pitch_offset_raw & (1 << (16 - 1)):
        pitch_offset_raw -= (1 << 16)
    pitch_offset = pitch_offset_raw * 0.0001
    publish_field(hass, instance_name, 'pitch_offset', 'Pitch offset', pitch_offset, 'Airmar: Attitude Offset', 'rad', '126720')
    publish_field(hass, instance_name, 'pitch_offset_degrees', 'Pitch offset Degrees', radians_to_degrees(pitch_offset), 'Airmar: Attitude Offset', 'Deg', '126720')
    _LOGGER.debug('Pitch offset  : %s', pitch_offset)

    # roll_offset | Offset: 56, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    roll_offset_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    if roll_offset_raw & (1 << (16 - 1)):
        roll_offset_raw -= (1 << 16)
    roll_offset = roll_offset_raw * 0.0001
    publish_field(hass, instance_name, 'roll_offset', 'Roll offset', roll_offset, 'Airmar: Attitude Offset', 'rad', '126720')
    publish_field(hass, instance_name, 'roll_offset_degrees', 'Roll offset Degrees', radians_to_degrees(roll_offset), 'Airmar: Attitude Offset', 'Deg', '126720')
    _LOGGER.debug('Roll offset  : %s', roll_offset)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # calibrate_function | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    calibrate_function_raw = (data_raw >> 24) & 0xFF
    calibrate_function = calibrate_function_raw * 1
    publish_field(hass, instance_name, 'calibrate_function', 'Calibrate Function', calibrate_function, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Calibrate Function  : %s', calibrate_function)

    # calibration_status | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    calibration_status_raw = (data_raw >> 32) & 0xFF
    calibration_status = calibration_status_raw * 1
    publish_field(hass, instance_name, 'calibration_status', 'Calibration Status', calibration_status, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Calibration Status  : %s', calibration_status)

    # verify_score | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    verify_score_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    verify_score = verify_score_raw * 1
    publish_field(hass, instance_name, 'verify_score', 'Verify Score', verify_score, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Verify Score  : %s', verify_score)

    # x_axis_gain_value | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    x_axis_gain_value_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    if x_axis_gain_value_raw & (1 << (16 - 1)):
        x_axis_gain_value_raw -= (1 << 16)
    x_axis_gain_value = x_axis_gain_value_raw * 0.01
    publish_field(hass, instance_name, 'x_axis_gain_value', 'X-axis gain value', x_axis_gain_value, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('X-axis gain value  : %s', x_axis_gain_value)

    # y_axis_gain_value | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    y_axis_gain_value_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    if y_axis_gain_value_raw & (1 << (16 - 1)):
        y_axis_gain_value_raw -= (1 << 16)
    y_axis_gain_value = y_axis_gain_value_raw * 0.01
    publish_field(hass, instance_name, 'y_axis_gain_value', 'Y-axis gain value', y_axis_gain_value, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Y-axis gain value  : %s', y_axis_gain_value)

    # z_axis_gain_value | Offset: 80, Length: 16, Resolution: 0.01, Field Type: NUMBER
    z_axis_gain_value_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    if z_axis_gain_value_raw & (1 << (16 - 1)):
        z_axis_gain_value_raw -= (1 << 16)
    z_axis_gain_value = z_axis_gain_value_raw * 0.01
    publish_field(hass, instance_name, 'z_axis_gain_value', 'Z-axis gain value', z_axis_gain_value, 'Airmar: Calibrate Compass', '', '126720')
    _LOGGER.debug('Z-axis gain value  : %s', z_axis_gain_value)

    # x_axis_linear_offset | Offset: 96, Length: 16, Resolution: 0.01, Field Type: NUMBER
    x_axis_linear_offset_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    if x_axis_linear_offset_raw & (1 << (16 - 1)):
        x_axis_linear_offset_raw -= (1 << 16)
    x_axis_linear_offset = x_axis_linear_offset_raw * 0.01
    publish_field(hass, instance_name, 'x_axis_linear_offset', 'X-axis linear offset', x_axis_linear_offset, 'Airmar: Calibrate Compass', 'T', '126720')
    _LOGGER.debug('X-axis linear offset  : %s', x_axis_linear_offset)

    # y_axis_linear_offset | Offset: 112, Length: 16, Resolution: 0.01, Field Type: NUMBER
    y_axis_linear_offset_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    if y_axis_linear_offset_raw & (1 << (16 - 1)):
        y_axis_linear_offset_raw -= (1 << 16)
    y_axis_linear_offset = y_axis_linear_offset_raw * 0.01
    publish_field(hass, instance_name, 'y_axis_linear_offset', 'Y-axis linear offset', y_axis_linear_offset, 'Airmar: Calibrate Compass', 'T', '126720')
    _LOGGER.debug('Y-axis linear offset  : %s', y_axis_linear_offset)

    # z_axis_linear_offset | Offset: 128, Length: 16, Resolution: 0.01, Field Type: NUMBER
    z_axis_linear_offset_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    if z_axis_linear_offset_raw & (1 << (16 - 1)):
        z_axis_linear_offset_raw -= (1 << 16)
    z_axis_linear_offset = z_axis_linear_offset_raw * 0.01
    publish_field(hass, instance_name, 'z_axis_linear_offset', 'Z-axis linear offset', z_axis_linear_offset, 'Airmar: Calibrate Compass', 'T', '126720')
    _LOGGER.debug('Z-axis linear offset  : %s', z_axis_linear_offset)

    # x_axis_angular_offset | Offset: 144, Length: 16, Resolution: 0.1, Field Type: NUMBER
    x_axis_angular_offset_raw = decode_number((data_raw >> 144) & 0xFFFF, 16)
    if x_axis_angular_offset_raw & (1 << (16 - 1)):
        x_axis_angular_offset_raw -= (1 << 16)
    x_axis_angular_offset = x_axis_angular_offset_raw * 0.1
    publish_field(hass, instance_name, 'x_axis_angular_offset', 'X-axis angular offset', x_axis_angular_offset, 'Airmar: Calibrate Compass', 'deg', '126720')
    publish_field(hass, instance_name, 'x_axis_angular_offset_degrees', 'X-axis angular offset Degrees', radians_to_degrees(x_axis_angular_offset), 'Airmar: Calibrate Compass', 'Deg', '126720')
    _LOGGER.debug('X-axis angular offset  : %s', x_axis_angular_offset)

    # pitch_and_roll_damping | Offset: 160, Length: 16, Resolution: 0.05, Field Type: TIME
    pitch_and_roll_damping_raw = (data_raw >> 160) & 0xFFFF
    if pitch_and_roll_damping_raw & (1 << (16 - 1)):
        pitch_and_roll_damping_raw -= (1 << 16)
    pitch_and_roll_damping = decode_time(pitch_and_roll_damping_raw * 0.05)
    publish_field(hass, instance_name, 'pitch_and_roll_damping', 'Pitch and Roll damping', pitch_and_roll_damping, 'Airmar: Calibrate Compass', 's', '126720')
    _LOGGER.debug('Pitch and Roll damping  : %s', pitch_and_roll_damping)

    # compass_rate_gyro_damping | Offset: 176, Length: 16, Resolution: 0.05, Field Type: TIME
    compass_rate_gyro_damping_raw = (data_raw >> 176) & 0xFFFF
    if compass_rate_gyro_damping_raw & (1 << (16 - 1)):
        compass_rate_gyro_damping_raw -= (1 << 16)
    compass_rate_gyro_damping = decode_time(compass_rate_gyro_damping_raw * 0.05)
    publish_field(hass, instance_name, 'compass_rate_gyro_damping', 'Compass/Rate gyro damping', compass_rate_gyro_damping, 'Airmar: Calibrate Compass', 's', '126720')
    _LOGGER.debug('Compass/Rate gyro damping  : %s', compass_rate_gyro_damping)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: True Wind Options', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: True Wind Options', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: True Wind Options', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: True Wind Options', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # cog_substitution_for_hdg | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    cog_substitution_for_hdg_raw = (data_raw >> 24) & 0x3
    cog_substitution_for_hdg = cog_substitution_for_hdg_raw * 1
    publish_field(hass, instance_name, 'cog_substitution_for_hdg', 'COG substitution for HDG', cog_substitution_for_hdg, 'Airmar: True Wind Options', '', '126720')
    _LOGGER.debug('COG substitution for HDG  : %s', cog_substitution_for_hdg)

    # reserved | Offset: 26, Length: 22, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3FFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: True Wind Options', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Simulate Mode', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Simulate Mode', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Simulate Mode', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Simulate Mode', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # simulate_mode | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    simulate_mode_raw = (data_raw >> 24) & 0x3
    simulate_mode = simulate_mode_raw * 1
    publish_field(hass, instance_name, 'simulate_mode', 'Simulate Mode', simulate_mode, 'Airmar: Simulate Mode', '', '126720')
    _LOGGER.debug('Simulate Mode  : %s', simulate_mode)

    # reserved | Offset: 26, Length: 22, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3FFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Simulate Mode', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Calibrate Depth', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Depth', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Calibrate Depth', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Calibrate Depth', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # speed_of_sound_mode | Offset: 24, Length: 16, Resolution: 0.1, Field Type: NUMBER
    speed_of_sound_mode_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    speed_of_sound_mode = speed_of_sound_mode_raw * 0.1
    publish_field(hass, instance_name, 'speed_of_sound_mode', 'Speed of Sound Mode', speed_of_sound_mode, 'Airmar: Calibrate Depth', 'm/s', '126720')
    publish_field(hass, instance_name, 'speed_of_sound_mode_knots', 'Speed of Sound Mode Knots', mps_to_knots(speed_of_sound_mode), 'Airmar: Calibrate Depth', 'Kn', '126720')
    _LOGGER.debug('Speed of Sound Mode  : %s', speed_of_sound_mode)

    # reserved | Offset: 40, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Depth', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Calibrate Speed', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Speed', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Calibrate Speed', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Calibrate Speed', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # number_of_pairs_of_data_points | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_pairs_of_data_points_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    number_of_pairs_of_data_points = number_of_pairs_of_data_points_raw * 1
    publish_field(hass, instance_name, 'number_of_pairs_of_data_points', 'Number of pairs of data points', number_of_pairs_of_data_points, 'Airmar: Calibrate Speed', '', '126720')
    _LOGGER.debug('Number of pairs of data points  : %s', number_of_pairs_of_data_points)

    # input_frequency | Offset: 32, Length: 16, Resolution: 0.1, Field Type: NUMBER
    input_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    input_frequency = input_frequency_raw * 0.1
    publish_field(hass, instance_name, 'input_frequency', 'Input frequency', input_frequency, 'Airmar: Calibrate Speed', 'Hz', '126720')
    _LOGGER.debug('Input frequency  : %s', input_frequency)

    # output_speed | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    output_speed_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    output_speed = output_speed_raw * 0.01
    publish_field(hass, instance_name, 'output_speed', 'Output speed', output_speed, 'Airmar: Calibrate Speed', 'm/s', '126720')
    publish_field(hass, instance_name, 'output_speed_knots', 'Output speed Knots', mps_to_knots(output_speed), 'Airmar: Calibrate Speed', 'Kn', '126720')
    _LOGGER.debug('Output speed  : %s', output_speed)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Calibrate Temperature', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Temperature', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Calibrate Temperature', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Calibrate Temperature', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # temperature_instance | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    temperature_instance_raw = (data_raw >> 24) & 0x3
    temperature_instance = temperature_instance_raw * 1
    publish_field(hass, instance_name, 'temperature_instance', 'Temperature instance', temperature_instance, 'Airmar: Calibrate Temperature', '', '126720')
    _LOGGER.debug('Temperature instance  : %s', temperature_instance)

    # reserved | Offset: 26, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Temperature', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # temperature_offset | Offset: 32, Length: 16, Resolution: 0.001, Field Type: NUMBER
    temperature_offset_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if temperature_offset_raw & (1 << (16 - 1)):
        temperature_offset_raw -= (1 << 16)
    temperature_offset = temperature_offset_raw * 0.001
    publish_field(hass, instance_name, 'temperature_offset', 'Temperature offset', temperature_offset, 'Airmar: Calibrate Temperature', 'K', '126720')
    _LOGGER.debug('Temperature offset  : %s', temperature_offset)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Speed Filter None', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Filter None', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Speed Filter None', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Speed Filter None', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # filter_type | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    filter_type_raw = decode_number((data_raw >> 24) & 0xF, 4)
    filter_type = filter_type_raw * 1
    publish_field(hass, instance_name, 'filter_type', 'Filter type', filter_type, 'Airmar: Speed Filter None', '', '126720')
    _LOGGER.debug('Filter type  : %s', filter_type)

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Filter None', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # sample_interval | Offset: 32, Length: 16, Resolution: 0.01, Field Type: TIME
    sample_interval_raw = (data_raw >> 32) & 0xFFFF
    sample_interval = decode_time(sample_interval_raw * 0.01)
    publish_field(hass, instance_name, 'sample_interval', 'Sample interval', sample_interval, 'Airmar: Speed Filter None', 's', '126720')
    _LOGGER.debug('Sample interval  : %s', sample_interval)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Speed Filter IIR', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Filter IIR', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Speed Filter IIR', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Speed Filter IIR', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # filter_type | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    filter_type_raw = decode_number((data_raw >> 24) & 0xF, 4)
    filter_type = filter_type_raw * 1
    publish_field(hass, instance_name, 'filter_type', 'Filter type', filter_type, 'Airmar: Speed Filter IIR', '', '126720')
    _LOGGER.debug('Filter type  : %s', filter_type)

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Filter IIR', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # sample_interval | Offset: 32, Length: 16, Resolution: 0.01, Field Type: TIME
    sample_interval_raw = (data_raw >> 32) & 0xFFFF
    sample_interval = decode_time(sample_interval_raw * 0.01)
    publish_field(hass, instance_name, 'sample_interval', 'Sample interval', sample_interval, 'Airmar: Speed Filter IIR', 's', '126720')
    _LOGGER.debug('Sample interval  : %s', sample_interval)

    # filter_duration | Offset: 48, Length: 16, Resolution: 0.01, Field Type: TIME
    filter_duration_raw = (data_raw >> 48) & 0xFFFF
    filter_duration = decode_time(filter_duration_raw * 0.01)
    publish_field(hass, instance_name, 'filter_duration', 'Filter duration', filter_duration, 'Airmar: Speed Filter IIR', 's', '126720')
    _LOGGER.debug('Filter duration  : %s', filter_duration)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Temperature Filter None', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Temperature Filter None', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Temperature Filter None', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Temperature Filter None', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # filter_type | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    filter_type_raw = decode_number((data_raw >> 24) & 0xF, 4)
    filter_type = filter_type_raw * 1
    publish_field(hass, instance_name, 'filter_type', 'Filter type', filter_type, 'Airmar: Temperature Filter None', '', '126720')
    _LOGGER.debug('Filter type  : %s', filter_type)

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Temperature Filter None', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # sample_interval | Offset: 32, Length: 16, Resolution: 0.01, Field Type: TIME
    sample_interval_raw = (data_raw >> 32) & 0xFFFF
    sample_interval = decode_time(sample_interval_raw * 0.01)
    publish_field(hass, instance_name, 'sample_interval', 'Sample interval', sample_interval, 'Airmar: Temperature Filter None', 's', '126720')
    _LOGGER.debug('Sample interval  : %s', sample_interval)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Temperature Filter IIR', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Temperature Filter IIR', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Temperature Filter IIR', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Temperature Filter IIR', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # filter_type | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    filter_type_raw = decode_number((data_raw >> 24) & 0xF, 4)
    filter_type = filter_type_raw * 1
    publish_field(hass, instance_name, 'filter_type', 'Filter type', filter_type, 'Airmar: Temperature Filter IIR', '', '126720')
    _LOGGER.debug('Filter type  : %s', filter_type)

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Temperature Filter IIR', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # sample_interval | Offset: 32, Length: 16, Resolution: 0.01, Field Type: TIME
    sample_interval_raw = (data_raw >> 32) & 0xFFFF
    sample_interval = decode_time(sample_interval_raw * 0.01)
    publish_field(hass, instance_name, 'sample_interval', 'Sample interval', sample_interval, 'Airmar: Temperature Filter IIR', 's', '126720')
    _LOGGER.debug('Sample interval  : %s', sample_interval)

    # filter_duration | Offset: 48, Length: 16, Resolution: 0.01, Field Type: TIME
    filter_duration_raw = (data_raw >> 48) & 0xFFFF
    filter_duration = decode_time(filter_duration_raw * 0.01)
    publish_field(hass, instance_name, 'filter_duration', 'Filter duration', filter_duration, 'Airmar: Temperature Filter IIR', 's', '126720')
    _LOGGER.debug('Filter duration  : %s', filter_duration)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: NMEA 2000 options', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: NMEA 2000 options', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: NMEA 2000 options', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: NMEA 2000 options', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

    # transmission_interval | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    transmission_interval_raw = (data_raw >> 24) & 0x3
    transmission_interval = transmission_interval_raw * 1
    publish_field(hass, instance_name, 'transmission_interval', 'Transmission Interval', transmission_interval, 'Airmar: NMEA 2000 options', '', '126720')
    _LOGGER.debug('Transmission Interval  : %s', transmission_interval)

    # reserved | Offset: 26, Length: 22, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3FFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: NMEA 2000 options', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Addressable Multi-Frame', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Addressable Multi-Frame', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Addressable Multi-Frame', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Addressable Multi-Frame', '', '126720')
    _LOGGER.debug('Proprietary ID  : %s', proprietary_id)

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Maretron: Slave Response', '', '126720')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Slave Response', '', '126720')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Maretron: Slave Response', '', '126720')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # product_code | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    product_code_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    product_code = product_code_raw * 1
    publish_field(hass, instance_name, 'product_code', 'Product code', product_code, 'Maretron: Slave Response', '', '126720')
    _LOGGER.debug('Product code  : %s', product_code)

    # software_code | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    software_code_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    software_code = software_code_raw * 1
    publish_field(hass, instance_name, 'software_code', 'Software code', software_code, 'Maretron: Slave Response', '', '126720')
    _LOGGER.debug('Software code  : %s', software_code)

    # command | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Maretron: Slave Response', '', '126720')
    _LOGGER.debug('Command  : %s', command)

    # status | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    status_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Maretron: Slave Response', '', '126720')
    _LOGGER.debug('Status  : %s', status)

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
    date = decode_date(date_raw * 1)
    publish_field(hass, instance_name, 'date', 'Date', date, 'System Time', 'd', '126992')
    _LOGGER.debug('Date  : %s', date)

    # time | Offset: 32, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 32) & 0xFFFFFFFF
    time = decode_time(time_raw * 0.0001)
    publish_field(hass, instance_name, 'time', 'Time', time, 'System Time', 's', '126992')
    _LOGGER.debug('Time  : %s', time)

def process_pgn_127237(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127237."""
    # rudder_limit_exceeded | Offset: 0, Length: 2, Resolution: 1, Field Type: LOOKUP
    rudder_limit_exceeded_raw = (data_raw >> 0) & 0x3
    rudder_limit_exceeded = rudder_limit_exceeded_raw * 1
    publish_field(hass, instance_name, 'rudder_limit_exceeded', 'Rudder Limit Exceeded', rudder_limit_exceeded, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Rudder Limit Exceeded  : %s', rudder_limit_exceeded)

    # off_heading_limit_exceeded | Offset: 2, Length: 2, Resolution: 1, Field Type: LOOKUP
    off_heading_limit_exceeded_raw = (data_raw >> 2) & 0x3
    off_heading_limit_exceeded = off_heading_limit_exceeded_raw * 1
    publish_field(hass, instance_name, 'off_heading_limit_exceeded', 'Off-Heading Limit Exceeded', off_heading_limit_exceeded, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Off-Heading Limit Exceeded  : %s', off_heading_limit_exceeded)

    # off_track_limit_exceeded | Offset: 4, Length: 2, Resolution: 1, Field Type: LOOKUP
    off_track_limit_exceeded_raw = (data_raw >> 4) & 0x3
    off_track_limit_exceeded = off_track_limit_exceeded_raw * 1
    publish_field(hass, instance_name, 'off_track_limit_exceeded', 'Off-Track Limit Exceeded', off_track_limit_exceeded, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Off-Track Limit Exceeded  : %s', off_track_limit_exceeded)

    # override | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    override_raw = (data_raw >> 6) & 0x3
    override = override_raw * 1
    publish_field(hass, instance_name, 'override', 'Override', override, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Override  : %s', override)

    # steering_mode | Offset: 8, Length: 3, Resolution: 1, Field Type: LOOKUP
    steering_mode_raw = (data_raw >> 8) & 0x7
    steering_mode = steering_mode_raw * 1
    publish_field(hass, instance_name, 'steering_mode', 'Steering Mode', steering_mode, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Steering Mode  : %s', steering_mode)

    # turn_mode | Offset: 11, Length: 3, Resolution: 1, Field Type: LOOKUP
    turn_mode_raw = (data_raw >> 11) & 0x7
    turn_mode = turn_mode_raw * 1
    publish_field(hass, instance_name, 'turn_mode', 'Turn Mode', turn_mode, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Turn Mode  : %s', turn_mode)

    # heading_reference | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    heading_reference_raw = (data_raw >> 14) & 0x3
    heading_reference = heading_reference_raw * 1
    publish_field(hass, instance_name, 'heading_reference', 'Heading Reference', heading_reference, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Heading Reference  : %s', heading_reference)

    # reserved | Offset: 16, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Reserved  : %s', reserved)

    # commanded_rudder_direction | Offset: 21, Length: 3, Resolution: 1, Field Type: LOOKUP
    commanded_rudder_direction_raw = (data_raw >> 21) & 0x7
    commanded_rudder_direction = commanded_rudder_direction_raw * 1
    publish_field(hass, instance_name, 'commanded_rudder_direction', 'Commanded Rudder Direction', commanded_rudder_direction, 'Heading/Track control', '', '127237')
    _LOGGER.debug('Commanded Rudder Direction  : %s', commanded_rudder_direction)

    # commanded_rudder_angle | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    commanded_rudder_angle_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if commanded_rudder_angle_raw & (1 << (16 - 1)):
        commanded_rudder_angle_raw -= (1 << 16)
    commanded_rudder_angle = commanded_rudder_angle_raw * 0.0001
    publish_field(hass, instance_name, 'commanded_rudder_angle', 'Commanded Rudder Angle', commanded_rudder_angle, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'commanded_rudder_angle_degrees', 'Commanded Rudder Angle Degrees', radians_to_degrees(commanded_rudder_angle), 'Heading/Track control', 'Deg', '127237')
    _LOGGER.debug('Commanded Rudder Angle  : %s', commanded_rudder_angle)

    # heading_to_steer__course_ | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_to_steer__course__raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    heading_to_steer__course_ = heading_to_steer__course__raw * 0.0001
    publish_field(hass, instance_name, 'heading_to_steer__course_', 'Heading-To-Steer (Course)', heading_to_steer__course_, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'heading_to_steer__course__degrees', 'Heading-To-Steer (Course) Degrees', radians_to_degrees(heading_to_steer__course_), 'Heading/Track control', 'Deg', '127237')
    _LOGGER.debug('Heading-To-Steer (Course)  : %s', heading_to_steer__course_)

    # track | Offset: 56, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    track_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    track = track_raw * 0.0001
    publish_field(hass, instance_name, 'track', 'Track', track, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'track_degrees', 'Track Degrees', radians_to_degrees(track), 'Heading/Track control', 'Deg', '127237')
    _LOGGER.debug('Track  : %s', track)

    # rudder_limit | Offset: 72, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    rudder_limit_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    rudder_limit = rudder_limit_raw * 0.0001
    publish_field(hass, instance_name, 'rudder_limit', 'Rudder Limit', rudder_limit, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'rudder_limit_degrees', 'Rudder Limit Degrees', radians_to_degrees(rudder_limit), 'Heading/Track control', 'Deg', '127237')
    _LOGGER.debug('Rudder Limit  : %s', rudder_limit)

    # off_heading_limit | Offset: 88, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    off_heading_limit_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    off_heading_limit = off_heading_limit_raw * 0.0001
    publish_field(hass, instance_name, 'off_heading_limit', 'Off-Heading Limit', off_heading_limit, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'off_heading_limit_degrees', 'Off-Heading Limit Degrees', radians_to_degrees(off_heading_limit), 'Heading/Track control', 'Deg', '127237')
    _LOGGER.debug('Off-Heading Limit  : %s', off_heading_limit)

    # radius_of_turn_order | Offset: 104, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    radius_of_turn_order_raw = decode_number((data_raw >> 104) & 0xFFFF, 16)
    if radius_of_turn_order_raw & (1 << (16 - 1)):
        radius_of_turn_order_raw -= (1 << 16)
    radius_of_turn_order = radius_of_turn_order_raw * 0.0001
    publish_field(hass, instance_name, 'radius_of_turn_order', 'Radius of Turn Order', radius_of_turn_order, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'radius_of_turn_order_degrees', 'Radius of Turn Order Degrees', radians_to_degrees(radius_of_turn_order), 'Heading/Track control', 'Deg', '127237')
    _LOGGER.debug('Radius of Turn Order  : %s', radius_of_turn_order)

    # rate_of_turn_order | Offset: 120, Length: 16, Resolution: 3.125e-05, Field Type: NUMBER
    rate_of_turn_order_raw = decode_number((data_raw >> 120) & 0xFFFF, 16)
    if rate_of_turn_order_raw & (1 << (16 - 1)):
        rate_of_turn_order_raw -= (1 << 16)
    rate_of_turn_order = rate_of_turn_order_raw * 3.125e-05
    publish_field(hass, instance_name, 'rate_of_turn_order', 'Rate of Turn Order', rate_of_turn_order, 'Heading/Track control', 'rad/s', '127237')
    _LOGGER.debug('Rate of Turn Order  : %s', rate_of_turn_order)

    # off_track_limit | Offset: 136, Length: 16, Resolution: 1, Field Type: NUMBER
    off_track_limit_raw = decode_number((data_raw >> 136) & 0xFFFF, 16)
    if off_track_limit_raw & (1 << (16 - 1)):
        off_track_limit_raw -= (1 << 16)
    off_track_limit = off_track_limit_raw * 1
    publish_field(hass, instance_name, 'off_track_limit', 'Off-Track Limit', off_track_limit, 'Heading/Track control', 'm', '127237')
    _LOGGER.debug('Off-Track Limit  : %s', off_track_limit)

    # vessel_heading | Offset: 152, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    vessel_heading_raw = decode_number((data_raw >> 152) & 0xFFFF, 16)
    vessel_heading = vessel_heading_raw * 0.0001
    publish_field(hass, instance_name, 'vessel_heading', 'Vessel Heading', vessel_heading, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'vessel_heading_degrees', 'Vessel Heading Degrees', radians_to_degrees(vessel_heading), 'Heading/Track control', 'Deg', '127237')
    _LOGGER.debug('Vessel Heading  : %s', vessel_heading)

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
    date = decode_date(date_raw * 1)
    publish_field(hass, instance_name, 'date', 'Date', date, 'Distance Log', 'd', '128275')
    _LOGGER.debug('Date  : %s', date)

    # time | Offset: 16, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 16) & 0xFFFFFFFF
    time = decode_time(time_raw * 0.0001)
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
    date = decode_date(date_raw * 1)
    publish_field(hass, instance_name, 'date', 'Date', date, 'GNSS Position Data', 'd', '129029')
    _LOGGER.debug('Date  : %s', date)

    # time | Offset: 24, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 24) & 0xFFFFFFFF
    time = decode_time(time_raw * 0.0001)
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
    age_of_dgnss_corrections = decode_time(age_of_dgnss_corrections_raw * 0.01)
    publish_field(hass, instance_name, 'age_of_dgnss_corrections', 'Age of DGNSS Corrections', age_of_dgnss_corrections, 'GNSS Position Data', 's', '129029')
    _LOGGER.debug('Age of DGNSS Corrections  : %s', age_of_dgnss_corrections)

def process_pgn_129033(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129033."""
    # date | Offset: 0, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 0) & 0xFFFF
    date = decode_date(date_raw * 1)
    publish_field(hass, instance_name, 'date', 'Date', date, 'Time & Date', 'd', '129033')
    _LOGGER.debug('Date  : %s', date)

    # time | Offset: 16, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 16) & 0xFFFFFFFF
    time = decode_time(time_raw * 0.0001)
    publish_field(hass, instance_name, 'time', 'Time', time, 'Time & Date', 's', '129033')
    _LOGGER.debug('Time  : %s', time)

    # local_offset | Offset: 48, Length: 16, Resolution: 60, Field Type: TIME
    local_offset_raw = (data_raw >> 48) & 0xFFFF
    if local_offset_raw & (1 << (16 - 1)):
        local_offset_raw -= (1 << 16)
    local_offset = decode_time(local_offset_raw * 60)
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

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Reprogram Status', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Reprogram Status', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Reprogram Status', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Reprogram Status', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # status | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    status_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Simnet: Reprogram Status', '', '130820')
    _LOGGER.debug('Status  : %s', status)

    # reserved | Offset: 32, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Reprogram Status', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Unknown 130820', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Unknown 130820', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Unknown 130820', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Furuno: Unknown 130820', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Furuno: Unknown 130820', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # c | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Furuno: Unknown 130820', '', '130820')
    _LOGGER.debug('C  : %s', c)

    # d | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Furuno: Unknown 130820', '', '130820')
    _LOGGER.debug('D  : %s', d)

    # e | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Furuno: Unknown 130820', '', '130820')
    _LOGGER.debug('E  : %s', e)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # source_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('Source ID  : %s', source_id)

    # current_source_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    current_source_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    current_source_id = current_source_id_raw * 1
    publish_field(hass, instance_name, 'current_source_id', 'Current Source ID', current_source_id, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('Current Source ID  : %s', current_source_id)

    # d | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('D  : %s', d)

    # e | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('E  : %s', e)

    # source | Offset: 64, Length: 40, Resolution: 1, Field Type: STRING_LZ
    source_raw = (data_raw >> 64) & 0xFFFFFFFFFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Fusion: Source Name', '', '130820')
    _LOGGER.debug('Source  : %s', source)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # transport | Offset: 40, Length: 4, Resolution: 1, Field Type: LOOKUP
    transport_raw = (data_raw >> 40) & 0xF
    transport = transport_raw * 1
    publish_field(hass, instance_name, 'transport', 'Transport', transport, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('Transport  : %s', transport)

    # x | Offset: 44, Length: 4, Resolution: 1, Field Type: NUMBER
    x_raw = decode_number((data_raw >> 44) & 0xF, 4)
    x = x_raw * 1
    publish_field(hass, instance_name, 'x', 'X', x, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('X  : %s', x)

    # b | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # track__ | Offset: 56, Length: 16, Resolution: 1, Field Type: NUMBER
    track___raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    track__ = track___raw * 1
    publish_field(hass, instance_name, 'track__', 'Track #', track__, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('Track #  : %s', track__)

    # c | Offset: 72, Length: 16, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('C  : %s', c)

    # track_count | Offset: 88, Length: 16, Resolution: 1, Field Type: NUMBER
    track_count_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    track_count = track_count_raw * 1
    publish_field(hass, instance_name, 'track_count', 'Track Count', track_count, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('Track Count  : %s', track_count)

    # e | Offset: 104, Length: 16, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 104) & 0xFFFF, 16)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('E  : %s', e)

    # length | Offset: 120, Length: 24, Resolution: 0.001, Field Type: TIME
    length_raw = (data_raw >> 120) & 0xFFFFFF
    length = decode_time(length_raw * 0.001)
    publish_field(hass, instance_name, 'length', 'Length', length, 'Fusion: Track Info', 's', '130820')
    _LOGGER.debug('Length  : %s', length)

    # position_in_track | Offset: 144, Length: 24, Resolution: 0.001, Field Type: TIME
    position_in_track_raw = (data_raw >> 144) & 0xFFFFFF
    position_in_track = decode_time(position_in_track_raw * 0.001)
    publish_field(hass, instance_name, 'position_in_track', 'Position in track', position_in_track, 'Fusion: Track Info', 's', '130820')
    _LOGGER.debug('Position in track  : %s', position_in_track)

    # h | Offset: 168, Length: 16, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 168) & 0xFFFF, 16)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Fusion: Track Info', '', '130820')
    _LOGGER.debug('H  : %s', h)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Track', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Track', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Track', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Track', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Track', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 40, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFFFFFFFFFF, 40)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Track', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # track | Offset: 72, Length: 80, Resolution: 1, Field Type: STRING_LZ
    track_raw = (data_raw >> 72) & 0xFFFFFFFFFFFFFFFFFFFF
    track = track_raw * 1
    publish_field(hass, instance_name, 'track', 'Track', track, 'Fusion: Track', '', '130820')
    _LOGGER.debug('Track  : %s', track)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Artist', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Artist', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Artist', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Artist', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Artist', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 40, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFFFFFFFFFF, 40)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Artist', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # artist | Offset: 72, Length: 80, Resolution: 1, Field Type: STRING_LZ
    artist_raw = (data_raw >> 72) & 0xFFFFFFFFFFFFFFFFFFFF
    artist = artist_raw * 1
    publish_field(hass, instance_name, 'artist', 'Artist', artist, 'Fusion: Artist', '', '130820')
    _LOGGER.debug('Artist  : %s', artist)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Album', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Album', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Album', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Album', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Album', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 40, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFFFFFFFFFF, 40)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Album', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # album | Offset: 72, Length: 80, Resolution: 1, Field Type: STRING_LZ
    album_raw = (data_raw >> 72) & 0xFFFFFFFFFFFFFFFFFFFF
    album = album_raw * 1
    publish_field(hass, instance_name, 'album', 'Album', album, 'Fusion: Album', '', '130820')
    _LOGGER.debug('Album  : %s', album)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Unit Name', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Unit Name', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Unit Name', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Unit Name', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Unit Name', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # name | Offset: 32, Length: 112, Resolution: 1, Field Type: STRING_LZ
    name_raw = (data_raw >> 32) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    name = name_raw * 1
    publish_field(hass, instance_name, 'name', 'Name', name, 'Fusion: Unit Name', '', '130820')
    _LOGGER.debug('Name  : %s', name)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Zone Name', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Zone Name', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Zone Name', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Zone Name', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Zone Name', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # number | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    number_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    number = number_raw * 1
    publish_field(hass, instance_name, 'number', 'Number', number, 'Fusion: Zone Name', '', '130820')
    _LOGGER.debug('Number  : %s', number)

    # name | Offset: 40, Length: 104, Resolution: 1, Field Type: STRING_LZ
    name_raw = (data_raw >> 40) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFF
    name = name_raw * 1
    publish_field(hass, instance_name, 'name', 'Name', name, 'Fusion: Zone Name', '', '130820')
    _LOGGER.debug('Name  : %s', name)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Play Progress', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Play Progress', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Play Progress', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Play Progress', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Play Progress', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Play Progress', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # progress | Offset: 40, Length: 24, Resolution: 0.001, Field Type: TIME
    progress_raw = (data_raw >> 40) & 0xFFFFFF
    progress = decode_time(progress_raw * 0.001)
    publish_field(hass, instance_name, 'progress', 'Progress', progress, 'Fusion: Play Progress', 's', '130820')
    _LOGGER.debug('Progress  : %s', progress)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # am_fm | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    am_fm_raw = (data_raw >> 32) & 0xFF
    am_fm = am_fm_raw * 1
    publish_field(hass, instance_name, 'am_fm', 'AM/FM', am_fm, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('AM/FM  : %s', am_fm)

    # b | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # frequency | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    frequency_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    frequency = frequency_raw * 1
    publish_field(hass, instance_name, 'frequency', 'Frequency', frequency, 'Fusion: AM/FM Station', 'Hz', '130820')
    _LOGGER.debug('Frequency  : %s', frequency)

    # c | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('C  : %s', c)

    # track | Offset: 88, Length: 80, Resolution: 1, Field Type: STRING_LZ
    track_raw = (data_raw >> 88) & 0xFFFFFFFFFFFFFFFFFFFF
    track = track_raw * 1
    publish_field(hass, instance_name, 'track', 'Track', track, 'Fusion: AM/FM Station', '', '130820')
    _LOGGER.debug('Track  : %s', track)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: VHF', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: VHF', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: VHF', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: VHF', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: VHF', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: VHF', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # channel | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    channel_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    channel = channel_raw * 1
    publish_field(hass, instance_name, 'channel', 'Channel', channel, 'Fusion: VHF', '', '130820')
    _LOGGER.debug('Channel  : %s', channel)

    # d | Offset: 48, Length: 24, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 48) & 0xFFFFFF, 24)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Fusion: VHF', '', '130820')
    _LOGGER.debug('D  : %s', d)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Squelch', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Squelch', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Squelch', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Squelch', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Squelch', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Squelch', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # squelch | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    squelch_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    squelch = squelch_raw * 1
    publish_field(hass, instance_name, 'squelch', 'Squelch', squelch, 'Fusion: Squelch', '', '130820')
    _LOGGER.debug('Squelch  : %s', squelch)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Scan', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Scan', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Scan', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Scan', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Scan', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Scan', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # scan | Offset: 40, Length: 2, Resolution: 1, Field Type: LOOKUP
    scan_raw = (data_raw >> 40) & 0x3
    scan = scan_raw * 1
    publish_field(hass, instance_name, 'scan', 'Scan', scan, 'Fusion: Scan', '', '130820')
    _LOGGER.debug('Scan  : %s', scan)

    # c | Offset: 42, Length: 6, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 42) & 0x3F, 6)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Fusion: Scan', '', '130820')
    _LOGGER.debug('C  : %s', c)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # line | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    line_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    line = line_raw * 1
    publish_field(hass, instance_name, 'line', 'Line', line, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('Line  : %s', line)

    # e | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('E  : %s', e)

    # f | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    f_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    f = f_raw * 1
    publish_field(hass, instance_name, 'f', 'F', f, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('F  : %s', f)

    # g | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    g_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    g = g_raw * 1
    publish_field(hass, instance_name, 'g', 'G', g, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('G  : %s', g)

    # h | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('H  : %s', h)

    # i | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    i_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    i = i_raw * 1
    publish_field(hass, instance_name, 'i', 'I', i, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('I  : %s', i)

    # text | Offset: 88, Length: 40, Resolution: 1, Field Type: STRING_LZ
    text_raw = (data_raw >> 88) & 0xFFFFFFFFFF
    text = text_raw * 1
    publish_field(hass, instance_name, 'text', 'Text', text, 'Fusion: Menu Item', '', '130820')
    _LOGGER.debug('Text  : %s', text)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # mode | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    mode_raw = (data_raw >> 32) & 0xFF
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('Mode  : %s', mode)

    # c | Offset: 40, Length: 24, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 40) & 0xFFFFFF, 24)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('C  : %s', c)

    # d | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('D  : %s', d)

    # e | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('E  : %s', e)

    # status | Offset: 80, Length: 8, Resolution: 1, Field Type: LOOKUP
    status_raw = (data_raw >> 80) & 0xFF
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('Status  : %s', status)

    # h | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('H  : %s', h)

    # i | Offset: 96, Length: 8, Resolution: 1, Field Type: NUMBER
    i_raw = decode_number((data_raw >> 96) & 0xFF, 8)
    i = i_raw * 1
    publish_field(hass, instance_name, 'i', 'I', i, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('I  : %s', i)

    # j | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    j_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    j = j_raw * 1
    publish_field(hass, instance_name, 'j', 'J', j, 'Fusion: Replay', '', '130820')
    _LOGGER.debug('J  : %s', j)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Mute', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Mute', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Mute', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Mute', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Mute', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # mute | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    mute_raw = (data_raw >> 32) & 0xFF
    mute = mute_raw * 1
    publish_field(hass, instance_name, 'mute', 'Mute', mute, 'Fusion: Mute', '', '130820')
    _LOGGER.debug('Mute  : %s', mute)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # zone_1 | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_1_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    zone_1 = zone_1_raw * 1
    publish_field(hass, instance_name, 'zone_1', 'Zone 1', zone_1, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('Zone 1  : %s', zone_1)

    # zone_2 | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_2_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone_2 = zone_2_raw * 1
    publish_field(hass, instance_name, 'zone_2', 'Zone 2', zone_2, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('Zone 2  : %s', zone_2)

    # zone_3 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_3_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    zone_3 = zone_3_raw * 1
    publish_field(hass, instance_name, 'zone_3', 'Zone 3', zone_3, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('Zone 3  : %s', zone_3)

    # zone_4 | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_4_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    zone_4 = zone_4_raw * 1
    publish_field(hass, instance_name, 'zone_4', 'Zone 4', zone_4, 'Fusion: Sub Volume', '', '130820')
    _LOGGER.debug('Zone 4  : %s', zone_4)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('B  : %s', b)

    # bass | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    bass_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    if bass_raw & (1 << (8 - 1)):
        bass_raw -= (1 << 8)
    bass = bass_raw * 1
    publish_field(hass, instance_name, 'bass', 'Bass', bass, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('Bass  : %s', bass)

    # mid | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    mid_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    if mid_raw & (1 << (8 - 1)):
        mid_raw -= (1 << 8)
    mid = mid_raw * 1
    publish_field(hass, instance_name, 'mid', 'Mid', mid, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('Mid  : %s', mid)

    # treble | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    treble_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    if treble_raw & (1 << (8 - 1)):
        treble_raw -= (1 << 8)
    treble = treble_raw * 1
    publish_field(hass, instance_name, 'treble', 'Treble', treble, 'Fusion: Tone', '', '130820')
    _LOGGER.debug('Treble  : %s', treble)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # zone_1 | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_1_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    zone_1 = zone_1_raw * 1
    publish_field(hass, instance_name, 'zone_1', 'Zone 1', zone_1, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('Zone 1  : %s', zone_1)

    # zone_2 | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_2_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone_2 = zone_2_raw * 1
    publish_field(hass, instance_name, 'zone_2', 'Zone 2', zone_2, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('Zone 2  : %s', zone_2)

    # zone_3 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_3_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    zone_3 = zone_3_raw * 1
    publish_field(hass, instance_name, 'zone_3', 'Zone 3', zone_3, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('Zone 3  : %s', zone_3)

    # zone_4 | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_4_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    zone_4 = zone_4_raw * 1
    publish_field(hass, instance_name, 'zone_4', 'Zone 4', zone_4, 'Fusion: Volume', '', '130820')
    _LOGGER.debug('Zone 4  : %s', zone_4)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Power State', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Power State', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Power State', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Power State', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Power State', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # state | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    state_raw = (data_raw >> 32) & 0xFF
    state = state_raw * 1
    publish_field(hass, instance_name, 'state', 'State', state, 'Fusion: Power State', '', '130820')
    _LOGGER.debug('State  : %s', state)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: SiriusXM Channel', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: SiriusXM Channel', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: SiriusXM Channel', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: SiriusXM Channel', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: SiriusXM Channel', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # channel | Offset: 56, Length: 96, Resolution: 1, Field Type: STRING_LZ
    channel_raw = (data_raw >> 56) & 0xFFFFFFFFFFFFFFFFFFFFFFFF
    channel = channel_raw * 1
    publish_field(hass, instance_name, 'channel', 'Channel', channel, 'Fusion: SiriusXM Channel', '', '130820')
    _LOGGER.debug('Channel  : %s', channel)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: SiriusXM Title', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: SiriusXM Title', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: SiriusXM Title', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: SiriusXM Title', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: SiriusXM Title', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # title | Offset: 56, Length: 96, Resolution: 1, Field Type: STRING_LZ
    title_raw = (data_raw >> 56) & 0xFFFFFFFFFFFFFFFFFFFFFFFF
    title = title_raw * 1
    publish_field(hass, instance_name, 'title', 'Title', title, 'Fusion: SiriusXM Title', '', '130820')
    _LOGGER.debug('Title  : %s', title)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: SiriusXM Artist', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: SiriusXM Artist', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: SiriusXM Artist', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: SiriusXM Artist', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: SiriusXM Artist', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # artist | Offset: 56, Length: 96, Resolution: 1, Field Type: STRING_LZ
    artist_raw = (data_raw >> 56) & 0xFFFFFFFFFFFFFFFFFFFFFFFF
    artist = artist_raw * 1
    publish_field(hass, instance_name, 'artist', 'Artist', artist, 'Fusion: SiriusXM Artist', '', '130820')
    _LOGGER.debug('Artist  : %s', artist)

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: SiriusXM Genre', '', '130820')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: SiriusXM Genre', '', '130820')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: SiriusXM Genre', '', '130820')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: SiriusXM Genre', '', '130820')
    _LOGGER.debug('Message ID  : %s', message_id)

    # a | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: SiriusXM Genre', '', '130820')
    _LOGGER.debug('A  : %s', a)

    # genre | Offset: 56, Length: 96, Resolution: 1, Field Type: STRING_LZ
    genre_raw = (data_raw >> 56) & 0xFFFFFFFFFFFFFFFFFFFFFFFF
    genre = genre_raw * 1
    publish_field(hass, instance_name, 'genre', 'Genre', genre, 'Fusion: SiriusXM Genre', '', '130820')
    _LOGGER.debug('Genre  : %s', genre)

def process_pgn_130846(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130846."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('Industry Code  : %s', industry_code)

    # address | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    address_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    address = address_raw * 1
    publish_field(hass, instance_name, 'address', 'Address', address, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('Address  : %s', address)

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('B  : %s', b)

    # display_group | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    display_group_raw = (data_raw >> 32) & 0xFF
    display_group = display_group_raw * 1
    publish_field(hass, instance_name, 'display_group', 'Display Group', display_group, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('Display Group  : %s', display_group)

    # d | Offset: 40, Length: 16, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('D  : %s', d)

    # key | Offset: 56, Length: 16, Resolution: 1, Field Type: FIELDTYPE_LOOKUP
    key_raw = (data_raw >> 56) & 0xFFFF
    key = key_raw * 1
    publish_field(hass, instance_name, 'key', 'Key', key, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('Key  : %s', key)

    # spare | Offset: 72, Length: 8, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 72) & 0xFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('Spare  : %s', spare)

    # length | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    length_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    length = length_raw * 1
    publish_field(hass, instance_name, 'length', 'Length', length, 'Simnet: Parameter Set', '', '130846')
    _LOGGER.debug('Length  : %s', length)

def process_pgn_130846(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130846."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Motion Sensor Status Extended', '', '130846')
    _LOGGER.debug('Manufacturer Code  : %s', manufacturer_code)

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Motion Sensor Status Extended', '', '130846')
    _LOGGER.debug('Reserved  : %s', reserved)

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Motion Sensor Status Extended', '', '130846')
    _LOGGER.debug('Industry Code  : %s', industry_code)

