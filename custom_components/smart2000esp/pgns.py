from .utils import *
import logging
_LOGGER = logging.getLogger(__name__)

def process_pgn_59392(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 59392."""
    # control | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 0) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'ISO Acknowledgement', '', '59392')

    # group_function | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    group_function_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    group_function = group_function_raw * 1
    publish_field(hass, instance_name, 'group_function', 'Group Function', group_function, 'ISO Acknowledgement', '', '59392')

    # reserved | Offset: 16, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'ISO Acknowledgement', '', '59392')

    # pgn | Offset: 40, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 40) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'ISO Acknowledgement', '', '59392')

def process_pgn_59904(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 59904."""
    # pgn | Offset: 0, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 0) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'ISO Request', '', '59904')

def process_pgn_60160(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 60160."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'ISO Transport Protocol, Data Transfer', '', '60160')

    # data | Offset: 8, Length: 56, Resolution: 1, Field Type: BINARY
    data_raw = (data_raw >> 8) & 0xFFFFFFFFFFFFFF
    data = data_raw * 1
    publish_field(hass, instance_name, 'data', 'Data', data, 'ISO Transport Protocol, Data Transfer', '', '60160')

def process_pgn_60416(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 60416."""
    # group_function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_function_code_raw = (data_raw >> 0) & 0xFF
    group_function_code = group_function_code_raw * 1
    publish_field(hass, instance_name, 'group_function_code', 'Group Function Code', group_function_code, 'ISO Transport Protocol, Connection Management - Request To Send', '', '60416')

    # message_size | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    message_size_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    message_size = message_size_raw * 1
    publish_field(hass, instance_name, 'message_size', 'Message size', message_size, 'ISO Transport Protocol, Connection Management - Request To Send', '', '60416')

    # packets | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    packets_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    packets = packets_raw * 1
    publish_field(hass, instance_name, 'packets', 'Packets', packets, 'ISO Transport Protocol, Connection Management - Request To Send', '', '60416')

    # packets_reply | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    packets_reply_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    packets_reply = packets_reply_raw * 1
    publish_field(hass, instance_name, 'packets_reply', 'Packets reply', packets_reply, 'ISO Transport Protocol, Connection Management - Request To Send', '', '60416')

    # pgn | Offset: 40, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 40) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'ISO Transport Protocol, Connection Management - Request To Send', '', '60416')

def process_pgn_60416(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 60416."""
    # group_function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_function_code_raw = (data_raw >> 0) & 0xFF
    group_function_code = group_function_code_raw * 1
    publish_field(hass, instance_name, 'group_function_code', 'Group Function Code', group_function_code, 'ISO Transport Protocol, Connection Management - Clear To Send', '', '60416')

    # max_packets | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    max_packets_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    max_packets = max_packets_raw * 1
    publish_field(hass, instance_name, 'max_packets', 'Max packets', max_packets, 'ISO Transport Protocol, Connection Management - Clear To Send', '', '60416')

    # next_sid | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    next_sid_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    next_sid = next_sid_raw * 1
    publish_field(hass, instance_name, 'next_sid', 'Next SID', next_sid, 'ISO Transport Protocol, Connection Management - Clear To Send', '', '60416')

    # reserved | Offset: 24, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 24) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'ISO Transport Protocol, Connection Management - Clear To Send', '', '60416')

    # pgn | Offset: 40, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 40) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'ISO Transport Protocol, Connection Management - Clear To Send', '', '60416')

def process_pgn_60416(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 60416."""
    # group_function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_function_code_raw = (data_raw >> 0) & 0xFF
    group_function_code = group_function_code_raw * 1
    publish_field(hass, instance_name, 'group_function_code', 'Group Function Code', group_function_code, 'ISO Transport Protocol, Connection Management - End Of Message', '', '60416')

    # total_message_size | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    total_message_size_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    total_message_size = total_message_size_raw * 1
    publish_field(hass, instance_name, 'total_message_size', 'Total message size', total_message_size, 'ISO Transport Protocol, Connection Management - End Of Message', '', '60416')

    # total_number_of_frames_received | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    total_number_of_frames_received_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    total_number_of_frames_received = total_number_of_frames_received_raw * 1
    publish_field(hass, instance_name, 'total_number_of_frames_received', 'Total number of frames received', total_number_of_frames_received, 'ISO Transport Protocol, Connection Management - End Of Message', '', '60416')

    # reserved | Offset: 32, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'ISO Transport Protocol, Connection Management - End Of Message', '', '60416')

    # pgn | Offset: 40, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 40) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'ISO Transport Protocol, Connection Management - End Of Message', '', '60416')

def process_pgn_60416(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 60416."""
    # group_function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_function_code_raw = (data_raw >> 0) & 0xFF
    group_function_code = group_function_code_raw * 1
    publish_field(hass, instance_name, 'group_function_code', 'Group Function Code', group_function_code, 'ISO Transport Protocol, Connection Management - Broadcast Announce', '', '60416')

    # message_size | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    message_size_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    message_size = message_size_raw * 1
    publish_field(hass, instance_name, 'message_size', 'Message size', message_size, 'ISO Transport Protocol, Connection Management - Broadcast Announce', '', '60416')

    # packets | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    packets_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    packets = packets_raw * 1
    publish_field(hass, instance_name, 'packets', 'Packets', packets, 'ISO Transport Protocol, Connection Management - Broadcast Announce', '', '60416')

    # reserved | Offset: 32, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'ISO Transport Protocol, Connection Management - Broadcast Announce', '', '60416')

    # pgn | Offset: 40, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 40) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'ISO Transport Protocol, Connection Management - Broadcast Announce', '', '60416')

def process_pgn_60416(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 60416."""
    # group_function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_function_code_raw = (data_raw >> 0) & 0xFF
    group_function_code = group_function_code_raw * 1
    publish_field(hass, instance_name, 'group_function_code', 'Group Function Code', group_function_code, 'ISO Transport Protocol, Connection Management - Abort', '', '60416')

    # reason | Offset: 8, Length: 8, Resolution: 1, Field Type: BINARY
    reason_raw = (data_raw >> 8) & 0xFF
    reason = reason_raw * 1
    publish_field(hass, instance_name, 'reason', 'Reason', reason, 'ISO Transport Protocol, Connection Management - Abort', '', '60416')

    # reserved | Offset: 16, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'ISO Transport Protocol, Connection Management - Abort', '', '60416')

    # pgn | Offset: 40, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 40) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'ISO Transport Protocol, Connection Management - Abort', '', '60416')

def process_pgn_60928(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 60928."""
    # unique_number | Offset: 0, Length: 21, Resolution: 1, Field Type: NUMBER
    unique_number_raw = decode_number((data_raw >> 0) & 0x1FFFFF, 21)
    unique_number = unique_number_raw * 1
    publish_field(hass, instance_name, 'unique_number', 'Unique Number', unique_number, 'ISO Address Claim', '', '60928')

    # manufacturer_code | Offset: 21, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 21) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'ISO Address Claim', '', '60928')

    # device_instance_lower | Offset: 32, Length: 3, Resolution: 1, Field Type: NUMBER
    device_instance_lower_raw = decode_number((data_raw >> 32) & 0x7, 3)
    device_instance_lower = device_instance_lower_raw * 1
    publish_field(hass, instance_name, 'device_instance_lower', 'Device Instance Lower', device_instance_lower, 'ISO Address Claim', '', '60928')

    # device_instance_upper | Offset: 35, Length: 5, Resolution: 1, Field Type: NUMBER
    device_instance_upper_raw = decode_number((data_raw >> 35) & 0x1F, 5)
    device_instance_upper = device_instance_upper_raw * 1
    publish_field(hass, instance_name, 'device_instance_upper', 'Device Instance Upper', device_instance_upper, 'ISO Address Claim', '', '60928')

    # device_function | Offset: 40, Length: 8, Resolution: 1, Field Type: INDIRECT_LOOKUP
    device_function_raw = (data_raw >> 40) & 0xFF
    device_function = device_function_raw * 1
    publish_field(hass, instance_name, 'device_function', 'Device Function', device_function, 'ISO Address Claim', '', '60928')

    # spare | Offset: 48, Length: 1, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 48) & 0x1
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'ISO Address Claim', '', '60928')

    # device_class | Offset: 49, Length: 7, Resolution: 1, Field Type: LOOKUP
    device_class_raw = (data_raw >> 49) & 0x7F
    device_class = device_class_raw * 1
    publish_field(hass, instance_name, 'device_class', 'Device Class', device_class, 'ISO Address Claim', '', '60928')

    # system_instance | Offset: 56, Length: 4, Resolution: 1, Field Type: NUMBER
    system_instance_raw = decode_number((data_raw >> 56) & 0xF, 4)
    system_instance = system_instance_raw * 1
    publish_field(hass, instance_name, 'system_instance', 'System Instance', system_instance, 'ISO Address Claim', '', '60928')

    # industry_group | Offset: 60, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_group_raw = (data_raw >> 60) & 0x7
    industry_group = industry_group_raw * 1
    publish_field(hass, instance_name, 'industry_group', 'Industry Group', industry_group, 'ISO Address Claim', '', '60928')

    # arbitrary_address_capable | Offset: 63, Length: 1, Resolution: 1, Field Type: NUMBER
    arbitrary_address_capable_raw = decode_number((data_raw >> 63) & 0x1, 1)
    arbitrary_address_capable = arbitrary_address_capable_raw * 1
    publish_field(hass, instance_name, 'arbitrary_address_capable', 'Arbitrary address capable', arbitrary_address_capable, 'ISO Address Claim', '', '60928')

def process_pgn_61184(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 61184."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Wireless Keypad Light Control', '', '61184')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Wireless Keypad Light Control', '', '61184')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Wireless Keypad Light Control', '', '61184')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk: Wireless Keypad Light Control', '', '61184')

    # variant | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    variant_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    variant = variant_raw * 1
    publish_field(hass, instance_name, 'variant', 'Variant', variant, 'Seatalk: Wireless Keypad Light Control', '', '61184')

    # wireless_setting | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    wireless_setting_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    wireless_setting = wireless_setting_raw * 1
    publish_field(hass, instance_name, 'wireless_setting', 'Wireless Setting', wireless_setting, 'Seatalk: Wireless Keypad Light Control', '', '61184')

    # wired_setting | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    wired_setting_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    wired_setting = wired_setting_raw * 1
    publish_field(hass, instance_name, 'wired_setting', 'Wired Setting', wired_setting, 'Seatalk: Wireless Keypad Light Control', '', '61184')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Wireless Keypad Light Control', '', '61184')

def process_pgn_61184(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 61184."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Wireless Keypad Control', '', '61184')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Wireless Keypad Control', '', '61184')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Wireless Keypad Control', '', '61184')

    # pid | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    pid_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    pid = pid_raw * 1
    publish_field(hass, instance_name, 'pid', 'PID', pid, 'Seatalk: Wireless Keypad Control', '', '61184')

    # variant | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    variant_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    variant = variant_raw * 1
    publish_field(hass, instance_name, 'variant', 'Variant', variant, 'Seatalk: Wireless Keypad Control', '', '61184')

    # beep_control | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    beep_control_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    beep_control = beep_control_raw * 1
    publish_field(hass, instance_name, 'beep_control', 'Beep Control', beep_control, 'Seatalk: Wireless Keypad Control', '', '61184')

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Wireless Keypad Control', '', '61184')

def process_pgn_61184(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 61184."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Victron Battery Register', '', '61184')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Victron Battery Register', '', '61184')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Victron Battery Register', '', '61184')

    # register_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    register_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    register_id = register_id_raw * 1
    publish_field(hass, instance_name, 'register_id', 'Register Id', register_id, 'Victron Battery Register', '', '61184')

    # payload | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    payload_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    payload = payload_raw * 1
    publish_field(hass, instance_name, 'payload', 'Payload', payload, 'Victron Battery Register', '', '61184')

def process_pgn_65001(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65001."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Bus #1 Phase C Basic AC Quantities', 'V', '65001')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Bus #1 Phase C Basic AC Quantities', 'V', '65001')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Bus #1 Phase C Basic AC Quantities', 'Hz', '65001')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Bus #1 Phase C Basic AC Quantities', '', '65001')

def process_pgn_65002(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65002."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Bus #1 Phase B Basic AC Quantities', 'V', '65002')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Bus #1 Phase B Basic AC Quantities', 'V', '65002')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Bus #1 Phase B Basic AC Quantities', 'Hz', '65002')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Bus #1 Phase B Basic AC Quantities', '', '65002')

def process_pgn_65003(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65003."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Bus #1 Phase A Basic AC Quantities', 'V', '65003')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Bus #1 Phase A Basic AC Quantities', 'V', '65003')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Bus #1 Phase A Basic AC Quantities', 'Hz', '65003')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Bus #1 Phase A Basic AC Quantities', '', '65003')

def process_pgn_65004(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65004."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Bus #1 Average Basic AC Quantities', 'V', '65004')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Bus #1 Average Basic AC Quantities', 'V', '65004')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Bus #1 Average Basic AC Quantities', 'Hz', '65004')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Bus #1 Average Basic AC Quantities', '', '65004')

def process_pgn_65005(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65005."""
    # total_energy_export | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    total_energy_export_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    total_energy_export = total_energy_export_raw * 1
    publish_field(hass, instance_name, 'total_energy_export', 'Total Energy Export', total_energy_export, 'Utility Total AC Energy', 'kWh', '65005')

    # total_energy_import | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    total_energy_import_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    total_energy_import = total_energy_import_raw * 1
    publish_field(hass, instance_name, 'total_energy_import', 'Total Energy Import', total_energy_import, 'Utility Total AC Energy', 'kWh', '65005')

def process_pgn_65006(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65006."""
    # reactive_power | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'Utility Phase C AC Reactive Power', 'VAR', '65006')

    # power_factor | Offset: 16, Length: 16, Resolution: 6.10352e-05, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    power_factor = power_factor_raw * 6.10352e-05
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'Utility Phase C AC Reactive Power', 'Cos Phi', '65006')

    # power_factor_lagging | Offset: 32, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_factor_lagging_raw = (data_raw >> 32) & 0x3
    power_factor_lagging = power_factor_lagging_raw * 1
    publish_field(hass, instance_name, 'power_factor_lagging', 'Power Factor Lagging', power_factor_lagging, 'Utility Phase C AC Reactive Power', '', '65006')

    # reserved | Offset: 34, Length: 30, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 34) & 0x3FFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Utility Phase C AC Reactive Power', '', '65006')

def process_pgn_65007(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65007."""
    # real_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if real_power_raw & (1 << (32 - 1)):
        real_power_raw -= (1 << 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'Utility Phase C AC Power', 'W', '65007')

    # apparent_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    apparent_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if apparent_power_raw & (1 << (32 - 1)):
        apparent_power_raw -= (1 << 32)
    apparent_power = apparent_power_raw * 1
    publish_field(hass, instance_name, 'apparent_power', 'Apparent Power', apparent_power, 'Utility Phase C AC Power', 'VA', '65007')

def process_pgn_65008(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65008."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Utility Phase C Basic AC Quantities', 'V', '65008')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Utility Phase C Basic AC Quantities', 'V', '65008')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Utility Phase C Basic AC Quantities', 'Hz', '65008')

    # ac_rms_current | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'Utility Phase C Basic AC Quantities', 'A', '65008')

def process_pgn_65009(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65009."""
    # reactive_power | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'Utility Phase B AC Reactive Power', 'VAR', '65009')

    # power_factor | Offset: 16, Length: 16, Resolution: 6.10352e-05, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    power_factor = power_factor_raw * 6.10352e-05
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'Utility Phase B AC Reactive Power', 'Cos Phi', '65009')

    # power_factor_lagging | Offset: 32, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_factor_lagging_raw = (data_raw >> 32) & 0x3
    power_factor_lagging = power_factor_lagging_raw * 1
    publish_field(hass, instance_name, 'power_factor_lagging', 'Power Factor Lagging', power_factor_lagging, 'Utility Phase B AC Reactive Power', '', '65009')

    # reserved | Offset: 34, Length: 30, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 34) & 0x3FFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Utility Phase B AC Reactive Power', '', '65009')

def process_pgn_65010(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65010."""
    # real_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if real_power_raw & (1 << (32 - 1)):
        real_power_raw -= (1 << 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'Utility Phase B AC Power', 'W', '65010')

    # apparent_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    apparent_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if apparent_power_raw & (1 << (32 - 1)):
        apparent_power_raw -= (1 << 32)
    apparent_power = apparent_power_raw * 1
    publish_field(hass, instance_name, 'apparent_power', 'Apparent Power', apparent_power, 'Utility Phase B AC Power', 'VA', '65010')

def process_pgn_65011(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65011."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Utility Phase B Basic AC Quantities', 'V', '65011')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Utility Phase B Basic AC Quantities', 'V', '65011')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Utility Phase B Basic AC Quantities', 'Hz', '65011')

    # ac_rms_current | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'Utility Phase B Basic AC Quantities', 'A', '65011')

def process_pgn_65012(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65012."""
    # reactive_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if reactive_power_raw & (1 << (32 - 1)):
        reactive_power_raw -= (1 << 32)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'Utility Phase A AC Reactive Power', 'VAR', '65012')

    # power_factor | Offset: 32, Length: 16, Resolution: 6.10352e-05, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    power_factor = power_factor_raw * 6.10352e-05
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'Utility Phase A AC Reactive Power', 'Cos Phi', '65012')

    # power_factor_lagging | Offset: 48, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_factor_lagging_raw = (data_raw >> 48) & 0x3
    power_factor_lagging = power_factor_lagging_raw * 1
    publish_field(hass, instance_name, 'power_factor_lagging', 'Power Factor Lagging', power_factor_lagging, 'Utility Phase A AC Reactive Power', '', '65012')

    # reserved | Offset: 50, Length: 14, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 50) & 0x3FFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Utility Phase A AC Reactive Power', '', '65012')

def process_pgn_65013(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65013."""
    # real_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if real_power_raw & (1 << (32 - 1)):
        real_power_raw -= (1 << 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'Utility Phase A AC Power', 'W', '65013')

    # apparent_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    apparent_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if apparent_power_raw & (1 << (32 - 1)):
        apparent_power_raw -= (1 << 32)
    apparent_power = apparent_power_raw * 1
    publish_field(hass, instance_name, 'apparent_power', 'Apparent Power', apparent_power, 'Utility Phase A AC Power', 'VA', '65013')

def process_pgn_65014(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65014."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Utility Phase A Basic AC Quantities', 'V', '65014')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Utility Phase A Basic AC Quantities', 'V', '65014')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Utility Phase A Basic AC Quantities', 'Hz', '65014')

    # ac_rms_current | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'Utility Phase A Basic AC Quantities', 'A', '65014')

def process_pgn_65015(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65015."""
    # reactive_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if reactive_power_raw & (1 << (32 - 1)):
        reactive_power_raw -= (1 << 32)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'Utility Total AC Reactive Power', 'VAR', '65015')

    # power_factor | Offset: 32, Length: 16, Resolution: 6.10352e-05, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    power_factor = power_factor_raw * 6.10352e-05
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'Utility Total AC Reactive Power', 'Cos Phi', '65015')

    # power_factor_lagging | Offset: 48, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_factor_lagging_raw = (data_raw >> 48) & 0x3
    power_factor_lagging = power_factor_lagging_raw * 1
    publish_field(hass, instance_name, 'power_factor_lagging', 'Power Factor Lagging', power_factor_lagging, 'Utility Total AC Reactive Power', '', '65015')

    # reserved | Offset: 50, Length: 14, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 50) & 0x3FFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Utility Total AC Reactive Power', '', '65015')

def process_pgn_65016(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65016."""
    # real_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if real_power_raw & (1 << (32 - 1)):
        real_power_raw -= (1 << 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'Utility Total AC Power', 'W', '65016')

    # apparent_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    apparent_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if apparent_power_raw & (1 << (32 - 1)):
        apparent_power_raw -= (1 << 32)
    apparent_power = apparent_power_raw * 1
    publish_field(hass, instance_name, 'apparent_power', 'Apparent Power', apparent_power, 'Utility Total AC Power', 'VA', '65016')

def process_pgn_65017(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65017."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Utility Average Basic AC Quantities', 'V', '65017')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Utility Average Basic AC Quantities', 'V', '65017')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Utility Average Basic AC Quantities', 'Hz', '65017')

    # ac_rms_current | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'Utility Average Basic AC Quantities', 'A', '65017')

def process_pgn_65018(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65018."""
    # total_energy_export | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    total_energy_export_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    total_energy_export = total_energy_export_raw * 1
    publish_field(hass, instance_name, 'total_energy_export', 'Total Energy Export', total_energy_export, 'Generator Total AC Energy', 'kWh', '65018')

    # total_energy_import | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    total_energy_import_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    total_energy_import = total_energy_import_raw * 1
    publish_field(hass, instance_name, 'total_energy_import', 'Total Energy Import', total_energy_import, 'Generator Total AC Energy', 'kWh', '65018')

def process_pgn_65019(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65019."""
    # reactive_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if reactive_power_raw & (1 << (32 - 1)):
        reactive_power_raw -= (1 << 32)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'Generator Phase C AC Reactive Power', 'VAR', '65019')

    # power_factor | Offset: 32, Length: 16, Resolution: 6.10352e-05, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    power_factor = power_factor_raw * 6.10352e-05
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'Generator Phase C AC Reactive Power', 'Cos Phi', '65019')

    # power_factor_lagging | Offset: 48, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_factor_lagging_raw = (data_raw >> 48) & 0x3
    power_factor_lagging = power_factor_lagging_raw * 1
    publish_field(hass, instance_name, 'power_factor_lagging', 'Power Factor Lagging', power_factor_lagging, 'Generator Phase C AC Reactive Power', '', '65019')

    # reserved | Offset: 50, Length: 14, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 50) & 0x3FFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Generator Phase C AC Reactive Power', '', '65019')

def process_pgn_65020(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65020."""
    # real_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if real_power_raw & (1 << (32 - 1)):
        real_power_raw -= (1 << 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'Generator Phase C AC Power', 'W', '65020')

    # apparent_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    apparent_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if apparent_power_raw & (1 << (32 - 1)):
        apparent_power_raw -= (1 << 32)
    apparent_power = apparent_power_raw * 1
    publish_field(hass, instance_name, 'apparent_power', 'Apparent Power', apparent_power, 'Generator Phase C AC Power', 'VAR', '65020')

def process_pgn_65021(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65021."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Generator Phase C Basic AC Quantities', 'V', '65021')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Generator Phase C Basic AC Quantities', 'V', '65021')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Generator Phase C Basic AC Quantities', 'Hz', '65021')

    # ac_rms_current | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'Generator Phase C Basic AC Quantities', 'A', '65021')

def process_pgn_65022(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65022."""
    # reactive_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if reactive_power_raw & (1 << (32 - 1)):
        reactive_power_raw -= (1 << 32)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'Generator Phase B AC Reactive Power', 'VAR', '65022')

    # power_factor | Offset: 32, Length: 16, Resolution: 6.10352e-05, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    power_factor = power_factor_raw * 6.10352e-05
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'Generator Phase B AC Reactive Power', 'Cos Phi', '65022')

    # power_factor_lagging | Offset: 48, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_factor_lagging_raw = (data_raw >> 48) & 0x3
    power_factor_lagging = power_factor_lagging_raw * 1
    publish_field(hass, instance_name, 'power_factor_lagging', 'Power Factor Lagging', power_factor_lagging, 'Generator Phase B AC Reactive Power', '', '65022')

    # reserved | Offset: 50, Length: 14, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 50) & 0x3FFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Generator Phase B AC Reactive Power', '', '65022')

def process_pgn_65023(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65023."""
    # real_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if real_power_raw & (1 << (32 - 1)):
        real_power_raw -= (1 << 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'Generator Phase B AC Power', 'W', '65023')

    # apparent_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    apparent_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if apparent_power_raw & (1 << (32 - 1)):
        apparent_power_raw -= (1 << 32)
    apparent_power = apparent_power_raw * 1
    publish_field(hass, instance_name, 'apparent_power', 'Apparent Power', apparent_power, 'Generator Phase B AC Power', 'VA', '65023')

def process_pgn_65024(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65024."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Generator Phase B Basic AC Quantities', 'V', '65024')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Generator Phase B Basic AC Quantities', 'V', '65024')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Generator Phase B Basic AC Quantities', 'Hz', '65024')

    # ac_rms_current | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'Generator Phase B Basic AC Quantities', 'A', '65024')

def process_pgn_65025(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65025."""
    # reactive_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if reactive_power_raw & (1 << (32 - 1)):
        reactive_power_raw -= (1 << 32)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'Generator Phase A AC Reactive Power', 'VAR', '65025')

    # power_factor | Offset: 32, Length: 16, Resolution: 6.10352e-05, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    power_factor = power_factor_raw * 6.10352e-05
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'Generator Phase A AC Reactive Power', 'Cos Phi', '65025')

    # power_factor_lagging | Offset: 48, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_factor_lagging_raw = (data_raw >> 48) & 0x3
    power_factor_lagging = power_factor_lagging_raw * 1
    publish_field(hass, instance_name, 'power_factor_lagging', 'Power Factor Lagging', power_factor_lagging, 'Generator Phase A AC Reactive Power', '', '65025')

    # reserved | Offset: 50, Length: 14, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 50) & 0x3FFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Generator Phase A AC Reactive Power', '', '65025')

def process_pgn_65026(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65026."""
    # real_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if real_power_raw & (1 << (32 - 1)):
        real_power_raw -= (1 << 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'Generator Phase A AC Power', 'W', '65026')

    # apparent_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    apparent_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if apparent_power_raw & (1 << (32 - 1)):
        apparent_power_raw -= (1 << 32)
    apparent_power = apparent_power_raw * 1
    publish_field(hass, instance_name, 'apparent_power', 'Apparent Power', apparent_power, 'Generator Phase A AC Power', 'VA', '65026')

def process_pgn_65027(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65027."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Generator Phase A Basic AC Quantities', 'V', '65027')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Generator Phase A Basic AC Quantities', 'V', '65027')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Generator Phase A Basic AC Quantities', 'Hz', '65027')

    # ac_rms_current | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'Generator Phase A Basic AC Quantities', 'A', '65027')

def process_pgn_65028(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65028."""
    # reactive_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if reactive_power_raw & (1 << (32 - 1)):
        reactive_power_raw -= (1 << 32)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'Generator Total AC Reactive Power', 'VAR', '65028')

    # power_factor | Offset: 32, Length: 16, Resolution: 6.10352e-05, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    power_factor = power_factor_raw * 6.10352e-05
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'Generator Total AC Reactive Power', 'Cos Phi', '65028')

    # power_factor_lagging | Offset: 48, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_factor_lagging_raw = (data_raw >> 48) & 0x3
    power_factor_lagging = power_factor_lagging_raw * 1
    publish_field(hass, instance_name, 'power_factor_lagging', 'Power Factor Lagging', power_factor_lagging, 'Generator Total AC Reactive Power', '', '65028')

    # reserved | Offset: 50, Length: 14, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 50) & 0x3FFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Generator Total AC Reactive Power', '', '65028')

def process_pgn_65029(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65029."""
    # real_power | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if real_power_raw & (1 << (32 - 1)):
        real_power_raw -= (1 << 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'Generator Total AC Power', 'W', '65029')

    # apparent_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    apparent_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if apparent_power_raw & (1 << (32 - 1)):
        apparent_power_raw -= (1 << 32)
    apparent_power = apparent_power_raw * 1
    publish_field(hass, instance_name, 'apparent_power', 'Apparent Power', apparent_power, 'Generator Total AC Power', 'VA', '65029')

def process_pgn_65030(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65030."""
    # line_line_ac_rms_voltage | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    line_line_ac_rms_voltage_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    line_line_ac_rms_voltage = line_line_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_line_ac_rms_voltage', 'Line-Line AC RMS Voltage', line_line_ac_rms_voltage, 'Generator Average Basic AC Quantities', 'V', '65030')

    # line_neutral_ac_rms_voltage | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    line_neutral_ac_rms_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    line_neutral_ac_rms_voltage = line_neutral_ac_rms_voltage_raw * 1
    publish_field(hass, instance_name, 'line_neutral_ac_rms_voltage', 'Line-Neutral AC RMS Voltage', line_neutral_ac_rms_voltage, 'Generator Average Basic AC Quantities', 'V', '65030')

    # ac_frequency | Offset: 32, Length: 16, Resolution: 0.0078125, Field Type: NUMBER
    ac_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    ac_frequency = ac_frequency_raw * 0.0078125
    publish_field(hass, instance_name, 'ac_frequency', 'AC Frequency', ac_frequency, 'Generator Average Basic AC Quantities', 'Hz', '65030')

    # ac_rms_current | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'Generator Average Basic AC Quantities', 'A', '65030')

def process_pgn_65240(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65240."""
    # unique_number | Offset: 0, Length: 21, Resolution: 1, Field Type: BINARY
    unique_number_raw = (data_raw >> 0) & 0x1FFFFF
    unique_number = unique_number_raw * 1
    publish_field(hass, instance_name, 'unique_number', 'Unique Number', unique_number, 'ISO Commanded Address', '', '65240')

    # manufacturer_code | Offset: 21, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 21) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'ISO Commanded Address', 'Manufacturer Code', '65240')

    # device_instance_lower | Offset: 32, Length: 3, Resolution: 1, Field Type: NUMBER
    device_instance_lower_raw = decode_number((data_raw >> 32) & 0x7, 3)
    device_instance_lower = device_instance_lower_raw * 1
    publish_field(hass, instance_name, 'device_instance_lower', 'Device Instance Lower', device_instance_lower, 'ISO Commanded Address', '', '65240')

    # device_instance_upper | Offset: 35, Length: 5, Resolution: 1, Field Type: NUMBER
    device_instance_upper_raw = decode_number((data_raw >> 35) & 0x1F, 5)
    device_instance_upper = device_instance_upper_raw * 1
    publish_field(hass, instance_name, 'device_instance_upper', 'Device Instance Upper', device_instance_upper, 'ISO Commanded Address', '', '65240')

    # device_function | Offset: 40, Length: 8, Resolution: 1, Field Type: INDIRECT_LOOKUP
    device_function_raw = (data_raw >> 40) & 0xFF
    device_function = device_function_raw * 1
    publish_field(hass, instance_name, 'device_function', 'Device Function', device_function, 'ISO Commanded Address', '', '65240')

    # reserved | Offset: 48, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'ISO Commanded Address', '', '65240')

    # device_class | Offset: 49, Length: 7, Resolution: 1, Field Type: LOOKUP
    device_class_raw = (data_raw >> 49) & 0x7F
    device_class = device_class_raw * 1
    publish_field(hass, instance_name, 'device_class', 'Device Class', device_class, 'ISO Commanded Address', '', '65240')

    # system_instance | Offset: 56, Length: 4, Resolution: 1, Field Type: NUMBER
    system_instance_raw = decode_number((data_raw >> 56) & 0xF, 4)
    system_instance = system_instance_raw * 1
    publish_field(hass, instance_name, 'system_instance', 'System Instance', system_instance, 'ISO Commanded Address', '', '65240')

    # industry_code | Offset: 60, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 60) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'ISO Commanded Address', '', '65240')

    # reserved | Offset: 63, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 63) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'ISO Commanded Address', '', '65240')

    # new_source_address | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    new_source_address_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    new_source_address = new_source_address_raw * 1
    publish_field(hass, instance_name, 'new_source_address', 'New Source Address', new_source_address, 'ISO Commanded Address', '', '65240')

def process_pgn_65280(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65280."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Heave', '', '65280')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Heave', '', '65280')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Heave', '', '65280')

    # heave | Offset: 16, Length: 32, Resolution: 0.001, Field Type: NUMBER
    heave_raw = decode_number((data_raw >> 16) & 0xFFFFFFFF, 32)
    if heave_raw & (1 << (32 - 1)):
        heave_raw -= (1 << 32)
    heave = heave_raw * 0.001
    publish_field(hass, instance_name, 'heave', 'Heave', heave, 'Furuno: Heave', 'm', '65280')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Heave', '', '65280')

def process_pgn_65284(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65284."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Maretron: Proprietary DC Breaker Current', '', '65284')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Proprietary DC Breaker Current', '', '65284')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Maretron: Proprietary DC Breaker Current', '', '65284')

    # bank_instance | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    bank_instance_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    bank_instance = bank_instance_raw * 1
    publish_field(hass, instance_name, 'bank_instance', 'Bank Instance', bank_instance, 'Maretron: Proprietary DC Breaker Current', '', '65284')

    # indicator_number | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    indicator_number_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    indicator_number = indicator_number_raw * 1
    publish_field(hass, instance_name, 'indicator_number', 'Indicator Number', indicator_number, 'Maretron: Proprietary DC Breaker Current', '', '65284')

    # breaker_current | Offset: 32, Length: 16, Resolution: 0.1, Field Type: NUMBER
    breaker_current_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    breaker_current = breaker_current_raw * 0.1
    publish_field(hass, instance_name, 'breaker_current', 'Breaker Current', breaker_current, 'Maretron: Proprietary DC Breaker Current', 'A', '65284')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Proprietary DC Breaker Current', '', '65284')

def process_pgn_65285(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65285."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Boot State Acknowledgment', '', '65285')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Boot State Acknowledgment', '', '65285')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Boot State Acknowledgment', '', '65285')

    # boot_state | Offset: 16, Length: 3, Resolution: 1, Field Type: LOOKUP
    boot_state_raw = (data_raw >> 16) & 0x7
    boot_state = boot_state_raw * 1
    publish_field(hass, instance_name, 'boot_state', 'Boot State', boot_state, 'Airmar: Boot State Acknowledgment', '', '65285')

    # reserved | Offset: 19, Length: 45, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 19) & 0x1FFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Boot State Acknowledgment', '', '65285')

def process_pgn_65285(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65285."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Lowrance: Temperature', '', '65285')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Lowrance: Temperature', '', '65285')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Lowrance: Temperature', '', '65285')

    # temperature_source | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    temperature_source_raw = (data_raw >> 16) & 0xFF
    temperature_source = temperature_source_raw * 1
    publish_field(hass, instance_name, 'temperature_source', 'Temperature Source', temperature_source, 'Lowrance: Temperature', '', '65285')

    # actual_temperature | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    actual_temperature_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    actual_temperature = actual_temperature_raw * 0.01
    publish_field(hass, instance_name, 'actual_temperature', 'Actual Temperature', actual_temperature, 'Lowrance: Temperature', 'K', '65285')
    publish_field(hass, instance_name, 'actual_temperature_celsius', 'Actual Temperature Celsius', kelvin_to_celsius(actual_temperature), 'Lowrance: Temperature', 'C', '65285')
    publish_field(hass, instance_name, 'actual_temperature_fahrenheit', 'Actual Temperature Fahrenheit', kelvin_to_fahrenheit(actual_temperature), 'Lowrance: Temperature', 'F', '65285')

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Lowrance: Temperature', '', '65285')

def process_pgn_65286(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65286."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Chetco: Dimmer', '', '65286')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Chetco: Dimmer', '', '65286')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Chetco: Dimmer', '', '65286')

    # instance | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Chetco: Dimmer', '', '65286')

    # dimmer1 | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    dimmer1_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    dimmer1 = dimmer1_raw * 1
    publish_field(hass, instance_name, 'dimmer1', 'Dimmer1', dimmer1, 'Chetco: Dimmer', '', '65286')

    # dimmer2 | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    dimmer2_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    dimmer2 = dimmer2_raw * 1
    publish_field(hass, instance_name, 'dimmer2', 'Dimmer2', dimmer2, 'Chetco: Dimmer', '', '65286')

    # dimmer3 | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    dimmer3_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    dimmer3 = dimmer3_raw * 1
    publish_field(hass, instance_name, 'dimmer3', 'Dimmer3', dimmer3, 'Chetco: Dimmer', '', '65286')

    # dimmer4 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    dimmer4_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    dimmer4 = dimmer4_raw * 1
    publish_field(hass, instance_name, 'dimmer4', 'Dimmer4', dimmer4, 'Chetco: Dimmer', '', '65286')

    # control | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    control_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'Chetco: Dimmer', '', '65286')

def process_pgn_65286(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65286."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Boot State Request', '', '65286')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Boot State Request', '', '65286')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Boot State Request', '', '65286')

    # reserved | Offset: 16, Length: 48, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Boot State Request', '', '65286')

def process_pgn_65287(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65287."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Access Level', '', '65287')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Access Level', '', '65287')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Access Level', '', '65287')

    # format_code | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    format_code_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    format_code = format_code_raw * 1
    publish_field(hass, instance_name, 'format_code', 'Format Code', format_code, 'Airmar: Access Level', '', '65287')

    # access_level | Offset: 24, Length: 3, Resolution: 1, Field Type: LOOKUP
    access_level_raw = (data_raw >> 24) & 0x7
    access_level = access_level_raw * 1
    publish_field(hass, instance_name, 'access_level', 'Access Level', access_level, 'Airmar: Access Level', '', '65287')

    # reserved | Offset: 27, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 27) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Access Level', '', '65287')

    # access_seed_key | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    access_seed_key_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    access_seed_key = access_seed_key_raw * 1
    publish_field(hass, instance_name, 'access_seed_key', 'Access Seed/Key', access_seed_key, 'Airmar: Access Level', '', '65287')

def process_pgn_65287(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65287."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Configure Temperature Sensor', '', '65287')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Configure Temperature Sensor', '', '65287')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Configure Temperature Sensor', '', '65287')

    # reserved | Offset: 16, Length: 48, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Configure Temperature Sensor', '', '65287')

def process_pgn_65288(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65288."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Alarm', '', '65288')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Alarm', '', '65288')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Alarm', '', '65288')

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: BINARY
    sid_raw = (data_raw >> 16) & 0xFF
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Seatalk: Alarm', '', '65288')

    # alarm_status | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    alarm_status_raw = (data_raw >> 24) & 0xFF
    alarm_status = alarm_status_raw * 1
    publish_field(hass, instance_name, 'alarm_status', 'Alarm Status', alarm_status, 'Seatalk: Alarm', '', '65288')

    # alarm_id | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    alarm_id_raw = (data_raw >> 32) & 0xFF
    alarm_id = alarm_id_raw * 1
    publish_field(hass, instance_name, 'alarm_id', 'Alarm ID', alarm_id, 'Seatalk: Alarm', '', '65288')

    # alarm_group | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    alarm_group_raw = (data_raw >> 40) & 0xFF
    alarm_group = alarm_group_raw * 1
    publish_field(hass, instance_name, 'alarm_group', 'Alarm Group', alarm_group, 'Seatalk: Alarm', '', '65288')

    # alarm_priority | Offset: 48, Length: 16, Resolution: 1, Field Type: BINARY
    alarm_priority_raw = (data_raw >> 48) & 0xFFFF
    alarm_priority = alarm_priority_raw * 1
    publish_field(hass, instance_name, 'alarm_priority', 'Alarm Priority', alarm_priority, 'Seatalk: Alarm', '', '65288')

def process_pgn_65289(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65289."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Trim Tab Sensor Calibration', '', '65289')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Trim Tab Sensor Calibration', '', '65289')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Trim Tab Sensor Calibration', '', '65289')

    # reserved | Offset: 16, Length: 48, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Trim Tab Sensor Calibration', '', '65289')

def process_pgn_65290(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65290."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Paddle Wheel Speed Configuration', '', '65290')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Paddle Wheel Speed Configuration', '', '65290')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Paddle Wheel Speed Configuration', '', '65290')

    # reserved | Offset: 16, Length: 48, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Paddle Wheel Speed Configuration', '', '65290')

def process_pgn_65292(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65292."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Clear Fluid Level Warnings', '', '65292')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Clear Fluid Level Warnings', '', '65292')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Clear Fluid Level Warnings', '', '65292')

    # reserved | Offset: 16, Length: 48, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Clear Fluid Level Warnings', '', '65292')

def process_pgn_65293(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65293."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: LGC-2000 Configuration', '', '65293')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: LGC-2000 Configuration', '', '65293')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: LGC-2000 Configuration', '', '65293')

    # reserved | Offset: 16, Length: 48, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: LGC-2000 Configuration', '', '65293')

def process_pgn_65293(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65293."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Diverse Yacht Services: Load Cell', '', '65293')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Diverse Yacht Services: Load Cell', '', '65293')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Diverse Yacht Services: Load Cell', '', '65293')

    # instance | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Diverse Yacht Services: Load Cell', '', '65293')

    # reserved | Offset: 24, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 24) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Diverse Yacht Services: Load Cell', '', '65293')

    # load_cell | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    load_cell_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    load_cell = load_cell_raw * 1
    publish_field(hass, instance_name, 'load_cell', 'Load Cell', load_cell, 'Diverse Yacht Services: Load Cell', '', '65293')

def process_pgn_65302(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65302."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: AP Unknown 1', '', '65302')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Unknown 1', '', '65302')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: AP Unknown 1', '', '65302')

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Simnet: AP Unknown 1', '', '65302')

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: AP Unknown 1', '', '65302')

    # c | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Simnet: AP Unknown 1', '', '65302')

    # d | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: AP Unknown 1', '', '65302')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Unknown 1', '', '65302')

def process_pgn_65305(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65305."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Device Status', '', '65305')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Device Status', '', '65305')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Device Status', '', '65305')

    # model | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    model_raw = (data_raw >> 16) & 0xFF
    model = model_raw * 1
    publish_field(hass, instance_name, 'model', 'Model', model, 'Simnet: Device Status', '', '65305')

    # report | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    report_raw = (data_raw >> 24) & 0xFF
    report = report_raw * 1
    publish_field(hass, instance_name, 'report', 'Report', report, 'Simnet: Device Status', '', '65305')

    # status | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    status_raw = (data_raw >> 32) & 0xFF
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Simnet: Device Status', '', '65305')

    # spare | Offset: 40, Length: 24, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 40) & 0xFFFFFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: Device Status', '', '65305')

def process_pgn_65305(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65305."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Device Status Request', '', '65305')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Device Status Request', '', '65305')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Device Status Request', '', '65305')

    # model | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    model_raw = (data_raw >> 16) & 0xFF
    model = model_raw * 1
    publish_field(hass, instance_name, 'model', 'Model', model, 'Simnet: Device Status Request', '', '65305')

    # report | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    report_raw = (data_raw >> 24) & 0xFF
    report = report_raw * 1
    publish_field(hass, instance_name, 'report', 'Report', report, 'Simnet: Device Status Request', '', '65305')

    # spare | Offset: 32, Length: 32, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 32) & 0xFFFFFFFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: Device Status Request', '', '65305')

def process_pgn_65305(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65305."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Pilot Mode', '', '65305')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Pilot Mode', '', '65305')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Pilot Mode', '', '65305')

    # model | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    model_raw = (data_raw >> 16) & 0xFF
    model = model_raw * 1
    publish_field(hass, instance_name, 'model', 'Model', model, 'Simnet: Pilot Mode', '', '65305')

    # report | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    report_raw = (data_raw >> 24) & 0xFF
    report = report_raw * 1
    publish_field(hass, instance_name, 'report', 'Report', report, 'Simnet: Pilot Mode', '', '65305')

    # mode | Offset: 32, Length: 16, Resolution: 1, Field Type: BITLOOKUP
    mode_raw = (data_raw >> 32) & 0xFFFF
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Simnet: Pilot Mode', '', '65305')

    # spare | Offset: 48, Length: 16, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 48) & 0xFFFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: Pilot Mode', '', '65305')

def process_pgn_65305(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65305."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Device Mode Request', '', '65305')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Device Mode Request', '', '65305')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Device Mode Request', '', '65305')

    # model | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    model_raw = (data_raw >> 16) & 0xFF
    model = model_raw * 1
    publish_field(hass, instance_name, 'model', 'Model', model, 'Simnet: Device Mode Request', '', '65305')

    # report | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    report_raw = (data_raw >> 24) & 0xFF
    report = report_raw * 1
    publish_field(hass, instance_name, 'report', 'Report', report, 'Simnet: Device Mode Request', '', '65305')

    # spare | Offset: 32, Length: 32, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 32) & 0xFFFFFFFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: Device Mode Request', '', '65305')

def process_pgn_65305(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65305."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Sailing Processor Status', '', '65305')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Sailing Processor Status', '', '65305')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Sailing Processor Status', '', '65305')

    # model | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    model_raw = (data_raw >> 16) & 0xFF
    model = model_raw * 1
    publish_field(hass, instance_name, 'model', 'Model', model, 'Simnet: Sailing Processor Status', '', '65305')

    # report | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    report_raw = (data_raw >> 24) & 0xFF
    report = report_raw * 1
    publish_field(hass, instance_name, 'report', 'Report', report, 'Simnet: Sailing Processor Status', '', '65305')

    # data | Offset: 32, Length: 32, Resolution: 1, Field Type: BINARY
    data_raw = (data_raw >> 32) & 0xFFFFFFFF
    data = data_raw * 1
    publish_field(hass, instance_name, 'data', 'Data', data, 'Simnet: Sailing Processor Status', '', '65305')

def process_pgn_65309(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65309."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Navico: Wireless Battery Status', '', '65309')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navico: Wireless Battery Status', '', '65309')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Navico: Wireless Battery Status', '', '65309')

    # status | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    status_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Navico: Wireless Battery Status', '', '65309')

    # battery_status | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    battery_status_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    battery_status = battery_status_raw * 1
    publish_field(hass, instance_name, 'battery_status', 'Battery Status', battery_status, 'Navico: Wireless Battery Status', '%', '65309')

    # battery_charge_status | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    battery_charge_status_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    battery_charge_status = battery_charge_status_raw * 1
    publish_field(hass, instance_name, 'battery_charge_status', 'Battery Charge Status', battery_charge_status, 'Navico: Wireless Battery Status', '%', '65309')

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navico: Wireless Battery Status', '', '65309')

def process_pgn_65312(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65312."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Navico: Wireless Signal Status', '', '65312')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navico: Wireless Signal Status', '', '65312')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Navico: Wireless Signal Status', '', '65312')

    # unknown | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Navico: Wireless Signal Status', '', '65312')

    # signal_strength | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    signal_strength_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    signal_strength = signal_strength_raw * 1
    publish_field(hass, instance_name, 'signal_strength', 'Signal Strength', signal_strength, 'Navico: Wireless Signal Status', '%', '65312')

    # reserved | Offset: 32, Length: 32, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navico: Wireless Signal Status', '', '65312')

def process_pgn_65340(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65340."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: AP Unknown 2', '', '65340')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Unknown 2', '', '65340')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: AP Unknown 2', '', '65340')

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Simnet: AP Unknown 2', '', '65340')

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: AP Unknown 2', '', '65340')

    # c | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Simnet: AP Unknown 2', '', '65340')

    # d | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: AP Unknown 2', '', '65340')

    # e | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Simnet: AP Unknown 2', '', '65340')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Unknown 2', '', '65340')

def process_pgn_65341(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65341."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Autopilot Angle', '', '65341')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Autopilot Angle', '', '65341')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Autopilot Angle', '', '65341')

    # reserved | Offset: 16, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Autopilot Angle', '', '65341')

    # mode | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    mode_raw = (data_raw >> 32) & 0xFF
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Simnet: Autopilot Angle', '', '65341')

    # reserved | Offset: 40, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Autopilot Angle', '', '65341')

    # angle | Offset: 48, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    angle_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    angle = angle_raw * 0.0001
    publish_field(hass, instance_name, 'angle', 'Angle', angle, 'Simnet: Autopilot Angle', 'rad', '65341')
    publish_field(hass, instance_name, 'angle_degrees', 'Angle Degrees', radians_to_degrees(angle), 'Simnet: Autopilot Angle', 'Deg', '65341')

def process_pgn_65345(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65345."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Pilot Wind Datum', '', '65345')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Wind Datum', '', '65345')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Pilot Wind Datum', '', '65345')

    # wind_datum | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    wind_datum_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    wind_datum = wind_datum_raw * 0.0001
    publish_field(hass, instance_name, 'wind_datum', 'Wind Datum', wind_datum, 'Seatalk: Pilot Wind Datum', 'rad', '65345')
    publish_field(hass, instance_name, 'wind_datum_degrees', 'Wind Datum Degrees', radians_to_degrees(wind_datum), 'Seatalk: Pilot Wind Datum', 'Deg', '65345')

    # rolling_average_wind_angle | Offset: 32, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    rolling_average_wind_angle_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    rolling_average_wind_angle = rolling_average_wind_angle_raw * 0.0001
    publish_field(hass, instance_name, 'rolling_average_wind_angle', 'Rolling Average Wind Angle', rolling_average_wind_angle, 'Seatalk: Pilot Wind Datum', 'rad', '65345')
    publish_field(hass, instance_name, 'rolling_average_wind_angle_degrees', 'Rolling Average Wind Angle Degrees', radians_to_degrees(rolling_average_wind_angle), 'Seatalk: Pilot Wind Datum', 'Deg', '65345')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Wind Datum', '', '65345')

def process_pgn_65350(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65350."""
    # a | Offset: 0, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    if a_raw & (1 << (16 - 1)):
        a_raw -= (1 << 16)
    a = a_raw * 0.0001
    publish_field(hass, instance_name, 'a', 'A', a, 'Simnet: Magnetic Field', 'rad', '65350')
    publish_field(hass, instance_name, 'a_degrees', 'A Degrees', radians_to_degrees(a), 'Simnet: Magnetic Field', 'Deg', '65350')

    # b | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: Magnetic Field', '%', '65350')

    # c | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if c_raw & (1 << (16 - 1)):
        c_raw -= (1 << 16)
    c = c_raw * 0.0001
    publish_field(hass, instance_name, 'c', 'C', c, 'Simnet: Magnetic Field', 'rad', '65350')
    publish_field(hass, instance_name, 'c_degrees', 'C Degrees', radians_to_degrees(c), 'Simnet: Magnetic Field', 'Deg', '65350')

    # d | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if d_raw & (1 << (16 - 1)):
        d_raw -= (1 << 16)
    d = d_raw * 0.0001
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: Magnetic Field', 'rad', '65350')
    publish_field(hass, instance_name, 'd_degrees', 'D Degrees', radians_to_degrees(d), 'Simnet: Magnetic Field', 'Deg', '65350')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Magnetic Field', '', '65350')

def process_pgn_65359(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65359."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Pilot Heading', '', '65359')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Heading', '', '65359')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Pilot Heading', '', '65359')

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: BINARY
    sid_raw = (data_raw >> 16) & 0xFF
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Seatalk: Pilot Heading', '', '65359')

    # heading_true | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_true_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    heading_true = heading_true_raw * 0.0001
    publish_field(hass, instance_name, 'heading_true', 'Heading True', heading_true, 'Seatalk: Pilot Heading', 'rad', '65359')
    publish_field(hass, instance_name, 'heading_true_degrees', 'Heading True Degrees', radians_to_degrees(heading_true), 'Seatalk: Pilot Heading', 'Deg', '65359')

    # heading_magnetic | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_magnetic_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    heading_magnetic = heading_magnetic_raw * 0.0001
    publish_field(hass, instance_name, 'heading_magnetic', 'Heading Magnetic', heading_magnetic, 'Seatalk: Pilot Heading', 'rad', '65359')
    publish_field(hass, instance_name, 'heading_magnetic_degrees', 'Heading Magnetic Degrees', radians_to_degrees(heading_magnetic), 'Seatalk: Pilot Heading', 'Deg', '65359')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Heading', '', '65359')

def process_pgn_65360(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65360."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Pilot Locked Heading', '', '65360')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Locked Heading', '', '65360')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Pilot Locked Heading', '', '65360')

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: BINARY
    sid_raw = (data_raw >> 16) & 0xFF
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Seatalk: Pilot Locked Heading', '', '65360')

    # target_heading_true | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    target_heading_true_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    target_heading_true = target_heading_true_raw * 0.0001
    publish_field(hass, instance_name, 'target_heading_true', 'Target Heading True', target_heading_true, 'Seatalk: Pilot Locked Heading', 'rad', '65360')
    publish_field(hass, instance_name, 'target_heading_true_degrees', 'Target Heading True Degrees', radians_to_degrees(target_heading_true), 'Seatalk: Pilot Locked Heading', 'Deg', '65360')

    # target_heading_magnetic | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    target_heading_magnetic_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    target_heading_magnetic = target_heading_magnetic_raw * 0.0001
    publish_field(hass, instance_name, 'target_heading_magnetic', 'Target Heading Magnetic', target_heading_magnetic, 'Seatalk: Pilot Locked Heading', 'rad', '65360')
    publish_field(hass, instance_name, 'target_heading_magnetic_degrees', 'Target Heading Magnetic Degrees', radians_to_degrees(target_heading_magnetic), 'Seatalk: Pilot Locked Heading', 'Deg', '65360')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Locked Heading', '', '65360')

def process_pgn_65361(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65361."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Silence Alarm', '', '65361')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Silence Alarm', '', '65361')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Silence Alarm', '', '65361')

    # alarm_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    alarm_id_raw = (data_raw >> 16) & 0xFF
    alarm_id = alarm_id_raw * 1
    publish_field(hass, instance_name, 'alarm_id', 'Alarm ID', alarm_id, 'Seatalk: Silence Alarm', '', '65361')

    # alarm_group | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    alarm_group_raw = (data_raw >> 24) & 0xFF
    alarm_group = alarm_group_raw * 1
    publish_field(hass, instance_name, 'alarm_group', 'Alarm Group', alarm_group, 'Seatalk: Silence Alarm', '', '65361')

    # reserved | Offset: 32, Length: 32, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Silence Alarm', '', '65361')

def process_pgn_65371(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65371."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Keypad Message', '', '65371')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Keypad Message', '', '65371')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Keypad Message', '', '65371')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk: Keypad Message', '', '65371')

    # first_key | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    first_key_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    first_key = first_key_raw * 1
    publish_field(hass, instance_name, 'first_key', 'First key', first_key, 'Seatalk: Keypad Message', '', '65371')

    # second_key | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    second_key_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    second_key = second_key_raw * 1
    publish_field(hass, instance_name, 'second_key', 'Second key', second_key, 'Seatalk: Keypad Message', '', '65371')

    # first_key_state | Offset: 40, Length: 2, Resolution: 1, Field Type: NUMBER
    first_key_state_raw = decode_number((data_raw >> 40) & 0x3, 2)
    first_key_state = first_key_state_raw * 1
    publish_field(hass, instance_name, 'first_key_state', 'First key state', first_key_state, 'Seatalk: Keypad Message', '', '65371')

    # second_key_state | Offset: 42, Length: 2, Resolution: 1, Field Type: NUMBER
    second_key_state_raw = decode_number((data_raw >> 42) & 0x3, 2)
    second_key_state = second_key_state_raw * 1
    publish_field(hass, instance_name, 'second_key_state', 'Second key state', second_key_state, 'Seatalk: Keypad Message', '', '65371')

    # reserved | Offset: 44, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 44) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Keypad Message', '', '65371')

    # encoder_position | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    encoder_position_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    encoder_position = encoder_position_raw * 1
    publish_field(hass, instance_name, 'encoder_position', 'Encoder Position', encoder_position, 'Seatalk: Keypad Message', '', '65371')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Keypad Message', '', '65371')

def process_pgn_65374(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65374."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SeaTalk: Keypad Heartbeat', '', '65374')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SeaTalk: Keypad Heartbeat', '', '65374')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SeaTalk: Keypad Heartbeat', '', '65374')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SeaTalk: Keypad Heartbeat', '', '65374')

    # variant | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    variant_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    variant = variant_raw * 1
    publish_field(hass, instance_name, 'variant', 'Variant', variant, 'SeaTalk: Keypad Heartbeat', '', '65374')

    # status | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    status_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'SeaTalk: Keypad Heartbeat', '', '65374')

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SeaTalk: Keypad Heartbeat', '', '65374')

def process_pgn_65379(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65379."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk: Pilot Mode', '', '65379')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Mode', '', '65379')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk: Pilot Mode', '', '65379')

    # pilot_mode | Offset: 16, Length: 8, Resolution: 1, Field Type: BINARY
    pilot_mode_raw = (data_raw >> 16) & 0xFF
    pilot_mode = pilot_mode_raw * 1
    publish_field(hass, instance_name, 'pilot_mode', 'Pilot Mode', pilot_mode, 'Seatalk: Pilot Mode', '', '65379')

    # sub_mode | Offset: 24, Length: 8, Resolution: 1, Field Type: BINARY
    sub_mode_raw = (data_raw >> 24) & 0xFF
    sub_mode = sub_mode_raw * 1
    publish_field(hass, instance_name, 'sub_mode', 'Sub Mode', sub_mode, 'Seatalk: Pilot Mode', '', '65379')

    # pilot_mode_data | Offset: 32, Length: 8, Resolution: 1, Field Type: BINARY
    pilot_mode_data_raw = (data_raw >> 32) & 0xFF
    pilot_mode_data = pilot_mode_data_raw * 1
    publish_field(hass, instance_name, 'pilot_mode_data', 'Pilot Mode Data', pilot_mode_data, 'Seatalk: Pilot Mode', '', '65379')

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk: Pilot Mode', '', '65379')

def process_pgn_65408(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65408."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Depth Quality Factor', '', '65408')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Depth Quality Factor', '', '65408')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Depth Quality Factor', '', '65408')

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Airmar: Depth Quality Factor', '', '65408')

    # depth_quality_factor | Offset: 24, Length: 4, Resolution: 1, Field Type: LOOKUP
    depth_quality_factor_raw = (data_raw >> 24) & 0xF
    depth_quality_factor = depth_quality_factor_raw * 1
    publish_field(hass, instance_name, 'depth_quality_factor', 'Depth Quality Factor', depth_quality_factor, 'Airmar: Depth Quality Factor', '', '65408')

    # reserved | Offset: 28, Length: 36, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Depth Quality Factor', '', '65408')

def process_pgn_65409(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65409."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Speed Pulse Count', '', '65409')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Pulse Count', '', '65409')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Speed Pulse Count', '', '65409')

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Airmar: Speed Pulse Count', '', '65409')

    # duration_of_interval | Offset: 24, Length: 16, Resolution: 0.001, Field Type: TIME
    duration_of_interval_raw = (data_raw >> 24) & 0xFFFF
    duration_of_interval = decode_time(duration_of_interval_raw * 0.001)
    publish_field(hass, instance_name, 'duration_of_interval', 'Duration of interval', duration_of_interval, 'Airmar: Speed Pulse Count', 's', '65409')

    # number_of_pulses_received | Offset: 40, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_pulses_received_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    number_of_pulses_received = number_of_pulses_received_raw * 1
    publish_field(hass, instance_name, 'number_of_pulses_received', 'Number of pulses received', number_of_pulses_received, 'Airmar: Speed Pulse Count', '', '65409')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Pulse Count', '', '65409')

def process_pgn_65410(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65410."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Device Information', '', '65410')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Device Information', '', '65410')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Device Information', '', '65410')

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Airmar: Device Information', '', '65410')

    # internal_device_temperature | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    internal_device_temperature_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    internal_device_temperature = internal_device_temperature_raw * 0.01
    publish_field(hass, instance_name, 'internal_device_temperature', 'Internal Device Temperature', internal_device_temperature, 'Airmar: Device Information', 'K', '65410')
    publish_field(hass, instance_name, 'internal_device_temperature_celsius', 'Internal Device Temperature Celsius', kelvin_to_celsius(internal_device_temperature), 'Airmar: Device Information', 'C', '65410')
    publish_field(hass, instance_name, 'internal_device_temperature_fahrenheit', 'Internal Device Temperature Fahrenheit', kelvin_to_fahrenheit(internal_device_temperature), 'Airmar: Device Information', 'F', '65410')

    # supply_voltage | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    supply_voltage_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    supply_voltage = supply_voltage_raw * 0.01
    publish_field(hass, instance_name, 'supply_voltage', 'Supply Voltage', supply_voltage, 'Airmar: Device Information', 'V', '65410')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Device Information', '', '65410')

def process_pgn_65420(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65420."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: AP Unknown 3', '', '65420')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Unknown 3', '', '65420')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: AP Unknown 3', '', '65420')

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Simnet: AP Unknown 3', '', '65420')

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: AP Unknown 3', '', '65420')

    # c | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Simnet: AP Unknown 3', '', '65420')

    # d | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: AP Unknown 3', '', '65420')

    # e | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Simnet: AP Unknown 3', '', '65420')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Unknown 3', '', '65420')

def process_pgn_65480(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 65480."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Autopilot Mode', '', '65480')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Autopilot Mode', '', '65480')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Autopilot Mode', '', '65480')

    # reserved | Offset: 16, Length: 48, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Autopilot Mode', '', '65480')

def process_pgn_126208(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126208."""
    # function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    function_code_raw = (data_raw >> 0) & 0xFF
    function_code = function_code_raw * 1
    publish_field(hass, instance_name, 'function_code', 'Function Code', function_code, 'NMEA - Request group function', '', '126208')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'NMEA - Request group function', '', '126208')

    # transmission_interval | Offset: 32, Length: 32, Resolution: 0.001, Field Type: TIME
    transmission_interval_raw = (data_raw >> 32) & 0xFFFFFFFF
    transmission_interval = decode_time(transmission_interval_raw * 0.001)
    publish_field(hass, instance_name, 'transmission_interval', 'Transmission interval', transmission_interval, 'NMEA - Request group function', 's', '126208')

    # transmission_interval_offset | Offset: 64, Length: 16, Resolution: 0.01, Field Type: TIME
    transmission_interval_offset_raw = (data_raw >> 64) & 0xFFFF
    transmission_interval_offset = decode_time(transmission_interval_offset_raw * 0.01)
    publish_field(hass, instance_name, 'transmission_interval_offset', 'Transmission interval offset', transmission_interval_offset, 'NMEA - Request group function', 's', '126208')

    # number_of_parameters | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_parameters_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    number_of_parameters = number_of_parameters_raw * 1
    publish_field(hass, instance_name, 'number_of_parameters', 'Number of Parameters', number_of_parameters, 'NMEA - Request group function', '', '126208')

    # parameter | Offset: 88, Length: 8, Resolution: 1, Field Type: FIELD_INDEX
    parameter_raw = (data_raw >> 88) & 0xFF
    parameter = parameter_raw * 1
    publish_field(hass, instance_name, 'parameter', 'Parameter', parameter, 'NMEA - Request group function', '', '126208')

def process_pgn_126208(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126208."""
    # function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    function_code_raw = (data_raw >> 0) & 0xFF
    function_code = function_code_raw * 1
    publish_field(hass, instance_name, 'function_code', 'Function Code', function_code, 'NMEA - Command group function', '', '126208')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'NMEA - Command group function', '', '126208')

    # priority | Offset: 32, Length: 4, Resolution: 1, Field Type: LOOKUP
    priority_raw = (data_raw >> 32) & 0xF
    priority = priority_raw * 1
    publish_field(hass, instance_name, 'priority', 'Priority', priority, 'NMEA - Command group function', '', '126208')

    # reserved | Offset: 36, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 36) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'NMEA - Command group function', '', '126208')

    # number_of_parameters | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_parameters_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    number_of_parameters = number_of_parameters_raw * 1
    publish_field(hass, instance_name, 'number_of_parameters', 'Number of Parameters', number_of_parameters, 'NMEA - Command group function', '', '126208')

    # parameter | Offset: 48, Length: 8, Resolution: 1, Field Type: FIELD_INDEX
    parameter_raw = (data_raw >> 48) & 0xFF
    parameter = parameter_raw * 1
    publish_field(hass, instance_name, 'parameter', 'Parameter', parameter, 'NMEA - Command group function', '', '126208')

def process_pgn_126208(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126208."""
    # function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    function_code_raw = (data_raw >> 0) & 0xFF
    function_code = function_code_raw * 1
    publish_field(hass, instance_name, 'function_code', 'Function Code', function_code, 'NMEA - Acknowledge group function', '', '126208')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'NMEA - Acknowledge group function', '', '126208')

    # pgn_error_code | Offset: 32, Length: 4, Resolution: 1, Field Type: LOOKUP
    pgn_error_code_raw = (data_raw >> 32) & 0xF
    pgn_error_code = pgn_error_code_raw * 1
    publish_field(hass, instance_name, 'pgn_error_code', 'PGN error code', pgn_error_code, 'NMEA - Acknowledge group function', '', '126208')

    # transmission_interval_priority_error_code | Offset: 36, Length: 4, Resolution: 1, Field Type: LOOKUP
    transmission_interval_priority_error_code_raw = (data_raw >> 36) & 0xF
    transmission_interval_priority_error_code = transmission_interval_priority_error_code_raw * 1
    publish_field(hass, instance_name, 'transmission_interval_priority_error_code', 'Transmission interval/Priority error code', transmission_interval_priority_error_code, 'NMEA - Acknowledge group function', '', '126208')

    # number_of_parameters | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_parameters_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    number_of_parameters = number_of_parameters_raw * 1
    publish_field(hass, instance_name, 'number_of_parameters', 'Number of Parameters', number_of_parameters, 'NMEA - Acknowledge group function', '', '126208')

    # parameter | Offset: 48, Length: 4, Resolution: 1, Field Type: LOOKUP
    parameter_raw = (data_raw >> 48) & 0xF
    parameter = parameter_raw * 1
    publish_field(hass, instance_name, 'parameter', 'Parameter', parameter, 'NMEA - Acknowledge group function', '', '126208')

def process_pgn_126208(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126208."""
    # function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    function_code_raw = (data_raw >> 0) & 0xFF
    function_code = function_code_raw * 1
    publish_field(hass, instance_name, 'function_code', 'Function Code', function_code, 'NMEA - Read Fields group function', '', '126208')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'NMEA - Read Fields group function', '', '126208')

    # manufacturer_code | Offset: 32, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 32) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'NMEA - Read Fields group function', '', '126208')

def process_pgn_126208(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126208."""
    # function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    function_code_raw = (data_raw >> 0) & 0xFF
    function_code = function_code_raw * 1
    publish_field(hass, instance_name, 'function_code', 'Function Code', function_code, 'NMEA - Read Fields reply group function', '', '126208')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'NMEA - Read Fields reply group function', '', '126208')

    # manufacturer_code | Offset: 32, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 32) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'NMEA - Read Fields reply group function', '', '126208')

def process_pgn_126208(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126208."""
    # function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    function_code_raw = (data_raw >> 0) & 0xFF
    function_code = function_code_raw * 1
    publish_field(hass, instance_name, 'function_code', 'Function Code', function_code, 'NMEA - Write Fields group function', '', '126208')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'NMEA - Write Fields group function', '', '126208')

    # manufacturer_code | Offset: 32, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 32) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'NMEA - Write Fields group function', '', '126208')

def process_pgn_126208(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126208."""
    # function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    function_code_raw = (data_raw >> 0) & 0xFF
    function_code = function_code_raw * 1
    publish_field(hass, instance_name, 'function_code', 'Function Code', function_code, 'NMEA - Write Fields reply group function', '', '126208')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'NMEA - Write Fields reply group function', '', '126208')

    # manufacturer_code | Offset: 32, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 32) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'NMEA - Write Fields reply group function', '', '126208')

def process_pgn_126464(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126464."""
    # function_code | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    function_code_raw = (data_raw >> 0) & 0xFF
    function_code = function_code_raw * 1
    publish_field(hass, instance_name, 'function_code', 'Function Code', function_code, 'PGN List (Transmit and Receive)', '', '126464')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'PGN List (Transmit and Receive)', '', '126464')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Pilot Mode', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Pilot Mode', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Pilot Mode', '', '126720')

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Pilot Mode', '', '126720')

    # command | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'command', command, 'Seatalk1: Pilot Mode', '', '126720')

    # unknown_1 | Offset: 40, Length: 24, Resolution: 1, Field Type: BINARY
    unknown_1_raw = (data_raw >> 40) & 0xFFFFFF
    unknown_1 = unknown_1_raw * 1
    publish_field(hass, instance_name, 'unknown_1', 'Unknown 1', unknown_1, 'Seatalk1: Pilot Mode', '', '126720')

    # pilot_mode | Offset: 64, Length: 8, Resolution: 1, Field Type: LOOKUP
    pilot_mode_raw = (data_raw >> 64) & 0xFF
    pilot_mode = pilot_mode_raw * 1
    publish_field(hass, instance_name, 'pilot_mode', 'Pilot Mode', pilot_mode, 'Seatalk1: Pilot Mode', '', '126720')

    # sub_mode | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    sub_mode_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    sub_mode = sub_mode_raw * 1
    publish_field(hass, instance_name, 'sub_mode', 'Sub Mode', sub_mode, 'Seatalk1: Pilot Mode', '', '126720')

    # pilot_mode_data | Offset: 80, Length: 8, Resolution: 1, Field Type: BINARY
    pilot_mode_data_raw = (data_raw >> 80) & 0xFF
    pilot_mode_data = pilot_mode_data_raw * 1
    publish_field(hass, instance_name, 'pilot_mode_data', 'Pilot Mode Data', pilot_mode_data, 'Seatalk1: Pilot Mode', '', '126720')

    # unknown_2 | Offset: 88, Length: 80, Resolution: 1, Field Type: BINARY
    unknown_2_raw = (data_raw >> 88) & 0xFFFFFFFFFFFFFFFFFFFF
    unknown_2 = unknown_2_raw * 1
    publish_field(hass, instance_name, 'unknown_2', 'Unknown 2', unknown_2, 'Seatalk1: Pilot Mode', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Media Control', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Media Control', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Media Control', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Media Control', '', '126720')

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Media Control', '', '126720')

    # source_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'Fusion: Media Control', '', '126720')

    # command | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    command_raw = (data_raw >> 40) & 0xFF
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Fusion: Media Control', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Sirius Control', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Sirius Control', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Sirius Control', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Sirius Control', '', '126720')

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Sirius Control', '', '126720')

    # source_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'Fusion: Sirius Control', '', '126720')

    # command | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    command_raw = (data_raw >> 40) & 0xFF
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Fusion: Sirius Control', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Request Status', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Request Status', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Request Status', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Request Status', '', '126720')

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Request Status', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Set Source', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Set Source', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Set Source', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Set Source', '', '126720')

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Set Source', '', '126720')

    # source_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'Fusion: Set Source', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Set Mute', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Set Mute', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Set Mute', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Set Mute', '', '126720')

    # command | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    command_raw = (data_raw >> 24) & 0xFF
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Fusion: Set Mute', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Set Zone Volume', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Set Zone Volume', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Set Zone Volume', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Set Zone Volume', '', '126720')

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Set Zone Volume', '', '126720')

    # zone | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    zone = zone_raw * 1
    publish_field(hass, instance_name, 'zone', 'Zone', zone, 'Fusion: Set Zone Volume', '', '126720')

    # volume | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    volume_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    volume = volume_raw * 1
    publish_field(hass, instance_name, 'volume', 'Volume', volume, 'Fusion: Set Zone Volume', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Set All Volumes', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Set All Volumes', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Set All Volumes', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Fusion: Set All Volumes', '', '126720')

    # unknown | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    unknown_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    unknown = unknown_raw * 1
    publish_field(hass, instance_name, 'unknown', 'Unknown', unknown, 'Fusion: Set All Volumes', '', '126720')

    # zone1 | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    zone1_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    zone1 = zone1_raw * 1
    publish_field(hass, instance_name, 'zone1', 'Zone1', zone1, 'Fusion: Set All Volumes', '', '126720')

    # zone2 | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone2_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone2 = zone2_raw * 1
    publish_field(hass, instance_name, 'zone2', 'Zone2', zone2, 'Fusion: Set All Volumes', '', '126720')

    # zone3 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    zone3_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    zone3 = zone3_raw * 1
    publish_field(hass, instance_name, 'zone3', 'Zone3', zone3, 'Fusion: Set All Volumes', '', '126720')

    # zone4 | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    zone4_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    zone4 = zone4_raw * 1
    publish_field(hass, instance_name, 'zone4', 'Zone4', zone4, 'Fusion: Set All Volumes', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Keystroke', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Keystroke', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Keystroke', '', '126720')

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Keystroke', '', '126720')

    # command | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'command', command, 'Seatalk1: Keystroke', '', '126720')

    # device | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    device_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    device = device_raw * 1
    publish_field(hass, instance_name, 'device', 'device', device, 'Seatalk1: Keystroke', '', '126720')

    # key | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    key_raw = (data_raw >> 48) & 0xFF
    key = key_raw * 1
    publish_field(hass, instance_name, 'key', 'key', key, 'Seatalk1: Keystroke', '', '126720')

    # keyinverted | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    keyinverted_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    keyinverted = keyinverted_raw * 1
    publish_field(hass, instance_name, 'keyinverted', 'keyInverted', keyinverted, 'Seatalk1: Keystroke', '', '126720')

    # unknown_data | Offset: 64, Length: 112, Resolution: 1, Field Type: BINARY
    unknown_data_raw = (data_raw >> 64) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    unknown_data = unknown_data_raw * 1
    publish_field(hass, instance_name, 'unknown_data', 'Unknown data', unknown_data, 'Seatalk1: Keystroke', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Device Identification', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Device Identification', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Device Identification', '', '126720')

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Device Identification', '', '126720')

    # command | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'command', command, 'Seatalk1: Device Identification', '', '126720')

    # reserved | Offset: 40, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Device Identification', '', '126720')

    # device | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    device_raw = (data_raw >> 48) & 0xFF
    device = device_raw * 1
    publish_field(hass, instance_name, 'device', 'device', device, 'Seatalk1: Device Identification', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Display Brightness', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Display Brightness', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Display Brightness', '', '126720')

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Display Brightness', '', '126720')

    # group | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_raw = (data_raw >> 32) & 0xFF
    group = group_raw * 1
    publish_field(hass, instance_name, 'group', 'Group', group, 'Seatalk1: Display Brightness', '', '126720')

    # unknown_1 | Offset: 40, Length: 8, Resolution: 1, Field Type: BINARY
    unknown_1_raw = (data_raw >> 40) & 0xFF
    unknown_1 = unknown_1_raw * 1
    publish_field(hass, instance_name, 'unknown_1', 'Unknown 1', unknown_1, 'Seatalk1: Display Brightness', '', '126720')

    # command | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Seatalk1: Display Brightness', '', '126720')

    # brightness | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    brightness_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    brightness = brightness_raw * 1
    publish_field(hass, instance_name, 'brightness', 'Brightness', brightness, 'Seatalk1: Display Brightness', '%', '126720')

    # unknown_2 | Offset: 64, Length: 8, Resolution: 1, Field Type: BINARY
    unknown_2_raw = (data_raw >> 64) & 0xFF
    unknown_2 = unknown_2_raw * 1
    publish_field(hass, instance_name, 'unknown_2', 'Unknown 2', unknown_2, 'Seatalk1: Display Brightness', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Seatalk1: Display Color', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Seatalk1: Display Color', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Seatalk1: Display Color', '', '126720')

    # proprietary_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Seatalk1: Display Color', '', '126720')

    # group | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_raw = (data_raw >> 32) & 0xFF
    group = group_raw * 1
    publish_field(hass, instance_name, 'group', 'Group', group, 'Seatalk1: Display Color', '', '126720')

    # unknown_1 | Offset: 40, Length: 8, Resolution: 1, Field Type: BINARY
    unknown_1_raw = (data_raw >> 40) & 0xFF
    unknown_1 = unknown_1_raw * 1
    publish_field(hass, instance_name, 'unknown_1', 'Unknown 1', unknown_1, 'Seatalk1: Display Color', '', '126720')

    # command | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Seatalk1: Display Color', '', '126720')

    # color | Offset: 56, Length: 8, Resolution: 1, Field Type: LOOKUP
    color_raw = (data_raw >> 56) & 0xFF
    color = color_raw * 1
    publish_field(hass, instance_name, 'color', 'Color', color, 'Seatalk1: Display Color', '', '126720')

    # unknown_2 | Offset: 64, Length: 8, Resolution: 1, Field Type: BINARY
    unknown_2_raw = (data_raw >> 64) & 0xFF
    unknown_2 = unknown_2_raw * 1
    publish_field(hass, instance_name, 'unknown_2', 'Unknown 2', unknown_2, 'Seatalk1: Display Color', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Attitude Offset', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Attitude Offset', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Attitude Offset', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Attitude Offset', '', '126720')

    # azimuth_offset | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    azimuth_offset_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if azimuth_offset_raw & (1 << (16 - 1)):
        azimuth_offset_raw -= (1 << 16)
    azimuth_offset = azimuth_offset_raw * 0.0001
    publish_field(hass, instance_name, 'azimuth_offset', 'Azimuth offset', azimuth_offset, 'Airmar: Attitude Offset', 'rad', '126720')
    publish_field(hass, instance_name, 'azimuth_offset_degrees', 'Azimuth offset Degrees', radians_to_degrees(azimuth_offset), 'Airmar: Attitude Offset', 'Deg', '126720')

    # pitch_offset | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    pitch_offset_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if pitch_offset_raw & (1 << (16 - 1)):
        pitch_offset_raw -= (1 << 16)
    pitch_offset = pitch_offset_raw * 0.0001
    publish_field(hass, instance_name, 'pitch_offset', 'Pitch offset', pitch_offset, 'Airmar: Attitude Offset', 'rad', '126720')
    publish_field(hass, instance_name, 'pitch_offset_degrees', 'Pitch offset Degrees', radians_to_degrees(pitch_offset), 'Airmar: Attitude Offset', 'Deg', '126720')

    # roll_offset | Offset: 56, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    roll_offset_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    if roll_offset_raw & (1 << (16 - 1)):
        roll_offset_raw -= (1 << 16)
    roll_offset = roll_offset_raw * 0.0001
    publish_field(hass, instance_name, 'roll_offset', 'Roll offset', roll_offset, 'Airmar: Attitude Offset', 'rad', '126720')
    publish_field(hass, instance_name, 'roll_offset_degrees', 'Roll offset Degrees', radians_to_degrees(roll_offset), 'Airmar: Attitude Offset', 'Deg', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Calibrate Compass', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Compass', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Calibrate Compass', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Calibrate Compass', '', '126720')

    # calibrate_function | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    calibrate_function_raw = (data_raw >> 24) & 0xFF
    calibrate_function = calibrate_function_raw * 1
    publish_field(hass, instance_name, 'calibrate_function', 'Calibrate Function', calibrate_function, 'Airmar: Calibrate Compass', '', '126720')

    # calibration_status | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    calibration_status_raw = (data_raw >> 32) & 0xFF
    calibration_status = calibration_status_raw * 1
    publish_field(hass, instance_name, 'calibration_status', 'Calibration Status', calibration_status, 'Airmar: Calibrate Compass', '', '126720')

    # verify_score | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    verify_score_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    verify_score = verify_score_raw * 1
    publish_field(hass, instance_name, 'verify_score', 'Verify Score', verify_score, 'Airmar: Calibrate Compass', '', '126720')

    # x_axis_gain_value | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    x_axis_gain_value_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    if x_axis_gain_value_raw & (1 << (16 - 1)):
        x_axis_gain_value_raw -= (1 << 16)
    x_axis_gain_value = x_axis_gain_value_raw * 0.01
    publish_field(hass, instance_name, 'x_axis_gain_value', 'X-axis gain value', x_axis_gain_value, 'Airmar: Calibrate Compass', '', '126720')

    # y_axis_gain_value | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    y_axis_gain_value_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    if y_axis_gain_value_raw & (1 << (16 - 1)):
        y_axis_gain_value_raw -= (1 << 16)
    y_axis_gain_value = y_axis_gain_value_raw * 0.01
    publish_field(hass, instance_name, 'y_axis_gain_value', 'Y-axis gain value', y_axis_gain_value, 'Airmar: Calibrate Compass', '', '126720')

    # z_axis_gain_value | Offset: 80, Length: 16, Resolution: 0.01, Field Type: NUMBER
    z_axis_gain_value_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    if z_axis_gain_value_raw & (1 << (16 - 1)):
        z_axis_gain_value_raw -= (1 << 16)
    z_axis_gain_value = z_axis_gain_value_raw * 0.01
    publish_field(hass, instance_name, 'z_axis_gain_value', 'Z-axis gain value', z_axis_gain_value, 'Airmar: Calibrate Compass', '', '126720')

    # x_axis_linear_offset | Offset: 96, Length: 16, Resolution: 0.01, Field Type: NUMBER
    x_axis_linear_offset_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    if x_axis_linear_offset_raw & (1 << (16 - 1)):
        x_axis_linear_offset_raw -= (1 << 16)
    x_axis_linear_offset = x_axis_linear_offset_raw * 0.01
    publish_field(hass, instance_name, 'x_axis_linear_offset', 'X-axis linear offset', x_axis_linear_offset, 'Airmar: Calibrate Compass', 'T', '126720')

    # y_axis_linear_offset | Offset: 112, Length: 16, Resolution: 0.01, Field Type: NUMBER
    y_axis_linear_offset_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    if y_axis_linear_offset_raw & (1 << (16 - 1)):
        y_axis_linear_offset_raw -= (1 << 16)
    y_axis_linear_offset = y_axis_linear_offset_raw * 0.01
    publish_field(hass, instance_name, 'y_axis_linear_offset', 'Y-axis linear offset', y_axis_linear_offset, 'Airmar: Calibrate Compass', 'T', '126720')

    # z_axis_linear_offset | Offset: 128, Length: 16, Resolution: 0.01, Field Type: NUMBER
    z_axis_linear_offset_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    if z_axis_linear_offset_raw & (1 << (16 - 1)):
        z_axis_linear_offset_raw -= (1 << 16)
    z_axis_linear_offset = z_axis_linear_offset_raw * 0.01
    publish_field(hass, instance_name, 'z_axis_linear_offset', 'Z-axis linear offset', z_axis_linear_offset, 'Airmar: Calibrate Compass', 'T', '126720')

    # x_axis_angular_offset | Offset: 144, Length: 16, Resolution: 0.1, Field Type: NUMBER
    x_axis_angular_offset_raw = decode_number((data_raw >> 144) & 0xFFFF, 16)
    if x_axis_angular_offset_raw & (1 << (16 - 1)):
        x_axis_angular_offset_raw -= (1 << 16)
    x_axis_angular_offset = x_axis_angular_offset_raw * 0.1
    publish_field(hass, instance_name, 'x_axis_angular_offset', 'X-axis angular offset', x_axis_angular_offset, 'Airmar: Calibrate Compass', 'deg', '126720')
    publish_field(hass, instance_name, 'x_axis_angular_offset_degrees', 'X-axis angular offset Degrees', radians_to_degrees(x_axis_angular_offset), 'Airmar: Calibrate Compass', 'Deg', '126720')

    # pitch_and_roll_damping | Offset: 160, Length: 16, Resolution: 0.05, Field Type: TIME
    pitch_and_roll_damping_raw = (data_raw >> 160) & 0xFFFF
    if pitch_and_roll_damping_raw & (1 << (16 - 1)):
        pitch_and_roll_damping_raw -= (1 << 16)
    pitch_and_roll_damping = decode_time(pitch_and_roll_damping_raw * 0.05)
    publish_field(hass, instance_name, 'pitch_and_roll_damping', 'Pitch and Roll damping', pitch_and_roll_damping, 'Airmar: Calibrate Compass', 's', '126720')

    # compass_rate_gyro_damping | Offset: 176, Length: 16, Resolution: 0.05, Field Type: TIME
    compass_rate_gyro_damping_raw = (data_raw >> 176) & 0xFFFF
    if compass_rate_gyro_damping_raw & (1 << (16 - 1)):
        compass_rate_gyro_damping_raw -= (1 << 16)
    compass_rate_gyro_damping = decode_time(compass_rate_gyro_damping_raw * 0.05)
    publish_field(hass, instance_name, 'compass_rate_gyro_damping', 'Compass/Rate gyro damping', compass_rate_gyro_damping, 'Airmar: Calibrate Compass', 's', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: True Wind Options', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: True Wind Options', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: True Wind Options', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: True Wind Options', '', '126720')

    # cog_substitution_for_hdg | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    cog_substitution_for_hdg_raw = (data_raw >> 24) & 0x3
    cog_substitution_for_hdg = cog_substitution_for_hdg_raw * 1
    publish_field(hass, instance_name, 'cog_substitution_for_hdg', 'COG substitution for HDG', cog_substitution_for_hdg, 'Airmar: True Wind Options', '', '126720')

    # reserved | Offset: 26, Length: 22, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3FFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: True Wind Options', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Simulate Mode', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Simulate Mode', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Simulate Mode', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Simulate Mode', '', '126720')

    # simulate_mode | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    simulate_mode_raw = (data_raw >> 24) & 0x3
    simulate_mode = simulate_mode_raw * 1
    publish_field(hass, instance_name, 'simulate_mode', 'Simulate Mode', simulate_mode, 'Airmar: Simulate Mode', '', '126720')

    # reserved | Offset: 26, Length: 22, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3FFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Simulate Mode', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Calibrate Depth', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Depth', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Calibrate Depth', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Calibrate Depth', '', '126720')

    # speed_of_sound_mode | Offset: 24, Length: 16, Resolution: 0.1, Field Type: NUMBER
    speed_of_sound_mode_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    speed_of_sound_mode = speed_of_sound_mode_raw * 0.1
    publish_field(hass, instance_name, 'speed_of_sound_mode', 'Speed of Sound Mode', speed_of_sound_mode, 'Airmar: Calibrate Depth', 'm/s', '126720')
    publish_field(hass, instance_name, 'speed_of_sound_mode_knots', 'Speed of Sound Mode Knots', mps_to_knots(speed_of_sound_mode), 'Airmar: Calibrate Depth', 'Kn', '126720')

    # reserved | Offset: 40, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Depth', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Calibrate Speed', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Speed', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Calibrate Speed', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Calibrate Speed', '', '126720')

    # number_of_pairs_of_data_points | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_pairs_of_data_points_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    number_of_pairs_of_data_points = number_of_pairs_of_data_points_raw * 1
    publish_field(hass, instance_name, 'number_of_pairs_of_data_points', 'Number of pairs of data points', number_of_pairs_of_data_points, 'Airmar: Calibrate Speed', '', '126720')

    # input_frequency | Offset: 32, Length: 16, Resolution: 0.1, Field Type: NUMBER
    input_frequency_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    input_frequency = input_frequency_raw * 0.1
    publish_field(hass, instance_name, 'input_frequency', 'Input frequency', input_frequency, 'Airmar: Calibrate Speed', 'Hz', '126720')

    # output_speed | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    output_speed_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    output_speed = output_speed_raw * 0.01
    publish_field(hass, instance_name, 'output_speed', 'Output speed', output_speed, 'Airmar: Calibrate Speed', 'm/s', '126720')
    publish_field(hass, instance_name, 'output_speed_knots', 'Output speed Knots', mps_to_knots(output_speed), 'Airmar: Calibrate Speed', 'Kn', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Calibrate Temperature', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Temperature', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Calibrate Temperature', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Calibrate Temperature', '', '126720')

    # temperature_instance | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    temperature_instance_raw = (data_raw >> 24) & 0x3
    temperature_instance = temperature_instance_raw * 1
    publish_field(hass, instance_name, 'temperature_instance', 'Temperature instance', temperature_instance, 'Airmar: Calibrate Temperature', '', '126720')

    # reserved | Offset: 26, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Calibrate Temperature', '', '126720')

    # temperature_offset | Offset: 32, Length: 16, Resolution: 0.001, Field Type: NUMBER
    temperature_offset_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if temperature_offset_raw & (1 << (16 - 1)):
        temperature_offset_raw -= (1 << 16)
    temperature_offset = temperature_offset_raw * 0.001
    publish_field(hass, instance_name, 'temperature_offset', 'Temperature offset', temperature_offset, 'Airmar: Calibrate Temperature', 'K', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Speed Filter None', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Filter None', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Speed Filter None', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Speed Filter None', '', '126720')

    # filter_type | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    filter_type_raw = decode_number((data_raw >> 24) & 0xF, 4)
    filter_type = filter_type_raw * 1
    publish_field(hass, instance_name, 'filter_type', 'Filter type', filter_type, 'Airmar: Speed Filter None', '', '126720')

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Filter None', '', '126720')

    # sample_interval | Offset: 32, Length: 16, Resolution: 0.01, Field Type: TIME
    sample_interval_raw = (data_raw >> 32) & 0xFFFF
    sample_interval = decode_time(sample_interval_raw * 0.01)
    publish_field(hass, instance_name, 'sample_interval', 'Sample interval', sample_interval, 'Airmar: Speed Filter None', 's', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Speed Filter IIR', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Filter IIR', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Speed Filter IIR', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Speed Filter IIR', '', '126720')

    # filter_type | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    filter_type_raw = decode_number((data_raw >> 24) & 0xF, 4)
    filter_type = filter_type_raw * 1
    publish_field(hass, instance_name, 'filter_type', 'Filter type', filter_type, 'Airmar: Speed Filter IIR', '', '126720')

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Speed Filter IIR', '', '126720')

    # sample_interval | Offset: 32, Length: 16, Resolution: 0.01, Field Type: TIME
    sample_interval_raw = (data_raw >> 32) & 0xFFFF
    sample_interval = decode_time(sample_interval_raw * 0.01)
    publish_field(hass, instance_name, 'sample_interval', 'Sample interval', sample_interval, 'Airmar: Speed Filter IIR', 's', '126720')

    # filter_duration | Offset: 48, Length: 16, Resolution: 0.01, Field Type: TIME
    filter_duration_raw = (data_raw >> 48) & 0xFFFF
    filter_duration = decode_time(filter_duration_raw * 0.01)
    publish_field(hass, instance_name, 'filter_duration', 'Filter duration', filter_duration, 'Airmar: Speed Filter IIR', 's', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Temperature Filter None', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Temperature Filter None', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Temperature Filter None', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Temperature Filter None', '', '126720')

    # filter_type | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    filter_type_raw = decode_number((data_raw >> 24) & 0xF, 4)
    filter_type = filter_type_raw * 1
    publish_field(hass, instance_name, 'filter_type', 'Filter type', filter_type, 'Airmar: Temperature Filter None', '', '126720')

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Temperature Filter None', '', '126720')

    # sample_interval | Offset: 32, Length: 16, Resolution: 0.01, Field Type: TIME
    sample_interval_raw = (data_raw >> 32) & 0xFFFF
    sample_interval = decode_time(sample_interval_raw * 0.01)
    publish_field(hass, instance_name, 'sample_interval', 'Sample interval', sample_interval, 'Airmar: Temperature Filter None', 's', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Temperature Filter IIR', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Temperature Filter IIR', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Temperature Filter IIR', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Temperature Filter IIR', '', '126720')

    # filter_type | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    filter_type_raw = decode_number((data_raw >> 24) & 0xF, 4)
    filter_type = filter_type_raw * 1
    publish_field(hass, instance_name, 'filter_type', 'Filter type', filter_type, 'Airmar: Temperature Filter IIR', '', '126720')

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Temperature Filter IIR', '', '126720')

    # sample_interval | Offset: 32, Length: 16, Resolution: 0.01, Field Type: TIME
    sample_interval_raw = (data_raw >> 32) & 0xFFFF
    sample_interval = decode_time(sample_interval_raw * 0.01)
    publish_field(hass, instance_name, 'sample_interval', 'Sample interval', sample_interval, 'Airmar: Temperature Filter IIR', 's', '126720')

    # filter_duration | Offset: 48, Length: 16, Resolution: 0.01, Field Type: TIME
    filter_duration_raw = (data_raw >> 48) & 0xFFFF
    filter_duration = decode_time(filter_duration_raw * 0.01)
    publish_field(hass, instance_name, 'filter_duration', 'Filter duration', filter_duration, 'Airmar: Temperature Filter IIR', 's', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: NMEA 2000 options', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: NMEA 2000 options', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: NMEA 2000 options', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: NMEA 2000 options', '', '126720')

    # transmission_interval | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    transmission_interval_raw = (data_raw >> 24) & 0x3
    transmission_interval = transmission_interval_raw * 1
    publish_field(hass, instance_name, 'transmission_interval', 'Transmission Interval', transmission_interval, 'Airmar: NMEA 2000 options', '', '126720')

    # reserved | Offset: 26, Length: 22, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3FFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: NMEA 2000 options', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Addressable Multi-Frame', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Addressable Multi-Frame', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Addressable Multi-Frame', '', '126720')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    proprietary_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Airmar: Addressable Multi-Frame', '', '126720')

def process_pgn_126720(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126720."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Maretron: Slave Response', '', '126720')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Slave Response', '', '126720')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Maretron: Slave Response', '', '126720')

    # product_code | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    product_code_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    product_code = product_code_raw * 1
    publish_field(hass, instance_name, 'product_code', 'Product code', product_code, 'Maretron: Slave Response', '', '126720')

    # software_code | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    software_code_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    software_code = software_code_raw * 1
    publish_field(hass, instance_name, 'software_code', 'Software code', software_code, 'Maretron: Slave Response', '', '126720')

    # command | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    command_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    command = command_raw * 1
    publish_field(hass, instance_name, 'command', 'Command', command, 'Maretron: Slave Response', '', '126720')

    # status | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    status_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Maretron: Slave Response', '', '126720')

def process_pgn_126983(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126983."""
    # alert_type | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_type_raw = (data_raw >> 0) & 0xF
    alert_type = alert_type_raw * 1
    publish_field(hass, instance_name, 'alert_type', 'Alert Type', alert_type, 'Alert', '', '126983')

    # alert_category | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_category_raw = (data_raw >> 4) & 0xF
    alert_category = alert_category_raw * 1
    publish_field(hass, instance_name, 'alert_category', 'Alert Category', alert_category, 'Alert', '', '126983')

    # alert_system | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_system_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    alert_system = alert_system_raw * 1
    publish_field(hass, instance_name, 'alert_system', 'Alert System', alert_system, 'Alert', '', '126983')

    # alert_sub_system | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_sub_system_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    alert_sub_system = alert_sub_system_raw * 1
    publish_field(hass, instance_name, 'alert_sub_system', 'Alert Sub-System', alert_sub_system, 'Alert', '', '126983')

    # alert_id | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    alert_id_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    alert_id = alert_id_raw * 1
    publish_field(hass, instance_name, 'alert_id', 'Alert ID', alert_id, 'Alert', '', '126983')

    # data_source_network_id_name | Offset: 40, Length: 64, Resolution: 1, Field Type: NUMBER
    data_source_network_id_name_raw = decode_number((data_raw >> 40) & 0xFFFFFFFFFFFFFFFF, 64)
    data_source_network_id_name = data_source_network_id_name_raw * 1
    publish_field(hass, instance_name, 'data_source_network_id_name', 'Data Source Network ID NAME', data_source_network_id_name, 'Alert', '', '126983')

    # data_source_instance | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    data_source_instance = data_source_instance_raw * 1
    publish_field(hass, instance_name, 'data_source_instance', 'Data Source Instance', data_source_instance, 'Alert', '', '126983')

    # data_source_index_source | Offset: 112, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_index_source_raw = decode_number((data_raw >> 112) & 0xFF, 8)
    data_source_index_source = data_source_index_source_raw * 1
    publish_field(hass, instance_name, 'data_source_index_source', 'Data Source Index-Source', data_source_index_source, 'Alert', '', '126983')

    # alert_occurrence_number | Offset: 120, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_occurrence_number_raw = decode_number((data_raw >> 120) & 0xFF, 8)
    alert_occurrence_number = alert_occurrence_number_raw * 1
    publish_field(hass, instance_name, 'alert_occurrence_number', 'Alert Occurrence Number', alert_occurrence_number, 'Alert', '', '126983')

    # temporary_silence_status | Offset: 128, Length: 1, Resolution: 1, Field Type: LOOKUP
    temporary_silence_status_raw = (data_raw >> 128) & 0x1
    temporary_silence_status = temporary_silence_status_raw * 1
    publish_field(hass, instance_name, 'temporary_silence_status', 'Temporary Silence Status', temporary_silence_status, 'Alert', '', '126983')

    # acknowledge_status | Offset: 129, Length: 1, Resolution: 1, Field Type: LOOKUP
    acknowledge_status_raw = (data_raw >> 129) & 0x1
    acknowledge_status = acknowledge_status_raw * 1
    publish_field(hass, instance_name, 'acknowledge_status', 'Acknowledge Status', acknowledge_status, 'Alert', '', '126983')

    # escalation_status | Offset: 130, Length: 1, Resolution: 1, Field Type: LOOKUP
    escalation_status_raw = (data_raw >> 130) & 0x1
    escalation_status = escalation_status_raw * 1
    publish_field(hass, instance_name, 'escalation_status', 'Escalation Status', escalation_status, 'Alert', '', '126983')

    # temporary_silence_support | Offset: 131, Length: 1, Resolution: 1, Field Type: LOOKUP
    temporary_silence_support_raw = (data_raw >> 131) & 0x1
    temporary_silence_support = temporary_silence_support_raw * 1
    publish_field(hass, instance_name, 'temporary_silence_support', 'Temporary Silence Support', temporary_silence_support, 'Alert', '', '126983')

    # acknowledge_support | Offset: 132, Length: 1, Resolution: 1, Field Type: LOOKUP
    acknowledge_support_raw = (data_raw >> 132) & 0x1
    acknowledge_support = acknowledge_support_raw * 1
    publish_field(hass, instance_name, 'acknowledge_support', 'Acknowledge Support', acknowledge_support, 'Alert', '', '126983')

    # escalation_support | Offset: 133, Length: 1, Resolution: 1, Field Type: LOOKUP
    escalation_support_raw = (data_raw >> 133) & 0x1
    escalation_support = escalation_support_raw * 1
    publish_field(hass, instance_name, 'escalation_support', 'Escalation Support', escalation_support, 'Alert', '', '126983')

    # reserved | Offset: 134, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 134) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Alert', '', '126983')

    # acknowledge_source_network_id_name | Offset: 136, Length: 64, Resolution: 1, Field Type: NUMBER
    acknowledge_source_network_id_name_raw = decode_number((data_raw >> 136) & 0xFFFFFFFFFFFFFFFF, 64)
    acknowledge_source_network_id_name = acknowledge_source_network_id_name_raw * 1
    publish_field(hass, instance_name, 'acknowledge_source_network_id_name', 'Acknowledge Source Network ID NAME', acknowledge_source_network_id_name, 'Alert', '', '126983')

    # trigger_condition | Offset: 200, Length: 4, Resolution: 1, Field Type: LOOKUP
    trigger_condition_raw = (data_raw >> 200) & 0xF
    trigger_condition = trigger_condition_raw * 1
    publish_field(hass, instance_name, 'trigger_condition', 'Trigger Condition', trigger_condition, 'Alert', '', '126983')

    # threshold_status | Offset: 204, Length: 4, Resolution: 1, Field Type: LOOKUP
    threshold_status_raw = (data_raw >> 204) & 0xF
    threshold_status = threshold_status_raw * 1
    publish_field(hass, instance_name, 'threshold_status', 'Threshold Status', threshold_status, 'Alert', '', '126983')

    # alert_priority | Offset: 208, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_priority_raw = decode_number((data_raw >> 208) & 0xFF, 8)
    alert_priority = alert_priority_raw * 1
    publish_field(hass, instance_name, 'alert_priority', 'Alert Priority', alert_priority, 'Alert', '', '126983')

    # alert_state | Offset: 216, Length: 8, Resolution: 1, Field Type: LOOKUP
    alert_state_raw = (data_raw >> 216) & 0xFF
    alert_state = alert_state_raw * 1
    publish_field(hass, instance_name, 'alert_state', 'Alert State', alert_state, 'Alert', '', '126983')

def process_pgn_126984(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126984."""
    # alert_type | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_type_raw = (data_raw >> 0) & 0xF
    alert_type = alert_type_raw * 1
    publish_field(hass, instance_name, 'alert_type', 'Alert Type', alert_type, 'Alert Response', '', '126984')

    # alert_category | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_category_raw = (data_raw >> 4) & 0xF
    alert_category = alert_category_raw * 1
    publish_field(hass, instance_name, 'alert_category', 'Alert Category', alert_category, 'Alert Response', '', '126984')

    # alert_system | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_system_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    alert_system = alert_system_raw * 1
    publish_field(hass, instance_name, 'alert_system', 'Alert System', alert_system, 'Alert Response', '', '126984')

    # alert_sub_system | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_sub_system_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    alert_sub_system = alert_sub_system_raw * 1
    publish_field(hass, instance_name, 'alert_sub_system', 'Alert Sub-System', alert_sub_system, 'Alert Response', '', '126984')

    # alert_id | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    alert_id_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    alert_id = alert_id_raw * 1
    publish_field(hass, instance_name, 'alert_id', 'Alert ID', alert_id, 'Alert Response', '', '126984')

    # data_source_network_id_name | Offset: 40, Length: 64, Resolution: 1, Field Type: NUMBER
    data_source_network_id_name_raw = decode_number((data_raw >> 40) & 0xFFFFFFFFFFFFFFFF, 64)
    data_source_network_id_name = data_source_network_id_name_raw * 1
    publish_field(hass, instance_name, 'data_source_network_id_name', 'Data Source Network ID NAME', data_source_network_id_name, 'Alert Response', '', '126984')

    # data_source_instance | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    data_source_instance = data_source_instance_raw * 1
    publish_field(hass, instance_name, 'data_source_instance', 'Data Source Instance', data_source_instance, 'Alert Response', '', '126984')

    # data_source_index_source | Offset: 112, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_index_source_raw = decode_number((data_raw >> 112) & 0xFF, 8)
    data_source_index_source = data_source_index_source_raw * 1
    publish_field(hass, instance_name, 'data_source_index_source', 'Data Source Index-Source', data_source_index_source, 'Alert Response', '', '126984')

    # alert_occurrence_number | Offset: 120, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_occurrence_number_raw = decode_number((data_raw >> 120) & 0xFF, 8)
    alert_occurrence_number = alert_occurrence_number_raw * 1
    publish_field(hass, instance_name, 'alert_occurrence_number', 'Alert Occurrence Number', alert_occurrence_number, 'Alert Response', '', '126984')

    # acknowledge_source_network_id_name | Offset: 128, Length: 64, Resolution: 1, Field Type: NUMBER
    acknowledge_source_network_id_name_raw = decode_number((data_raw >> 128) & 0xFFFFFFFFFFFFFFFF, 64)
    acknowledge_source_network_id_name = acknowledge_source_network_id_name_raw * 1
    publish_field(hass, instance_name, 'acknowledge_source_network_id_name', 'Acknowledge Source Network ID NAME', acknowledge_source_network_id_name, 'Alert Response', '', '126984')

    # response_command | Offset: 192, Length: 2, Resolution: 1, Field Type: LOOKUP
    response_command_raw = (data_raw >> 192) & 0x3
    response_command = response_command_raw * 1
    publish_field(hass, instance_name, 'response_command', 'Response Command', response_command, 'Alert Response', '', '126984')

    # reserved | Offset: 194, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 194) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Alert Response', '', '126984')

def process_pgn_126985(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126985."""
    # alert_type | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_type_raw = (data_raw >> 0) & 0xF
    alert_type = alert_type_raw * 1
    publish_field(hass, instance_name, 'alert_type', 'Alert Type', alert_type, 'Alert Text', '', '126985')

    # alert_category | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_category_raw = (data_raw >> 4) & 0xF
    alert_category = alert_category_raw * 1
    publish_field(hass, instance_name, 'alert_category', 'Alert Category', alert_category, 'Alert Text', '', '126985')

    # alert_system | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_system_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    alert_system = alert_system_raw * 1
    publish_field(hass, instance_name, 'alert_system', 'Alert System', alert_system, 'Alert Text', '', '126985')

    # alert_sub_system | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_sub_system_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    alert_sub_system = alert_sub_system_raw * 1
    publish_field(hass, instance_name, 'alert_sub_system', 'Alert Sub-System', alert_sub_system, 'Alert Text', '', '126985')

    # alert_id | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    alert_id_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    alert_id = alert_id_raw * 1
    publish_field(hass, instance_name, 'alert_id', 'Alert ID', alert_id, 'Alert Text', '', '126985')

    # data_source_network_id_name | Offset: 40, Length: 64, Resolution: 1, Field Type: NUMBER
    data_source_network_id_name_raw = decode_number((data_raw >> 40) & 0xFFFFFFFFFFFFFFFF, 64)
    data_source_network_id_name = data_source_network_id_name_raw * 1
    publish_field(hass, instance_name, 'data_source_network_id_name', 'Data Source Network ID NAME', data_source_network_id_name, 'Alert Text', '', '126985')

    # data_source_instance | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    data_source_instance = data_source_instance_raw * 1
    publish_field(hass, instance_name, 'data_source_instance', 'Data Source Instance', data_source_instance, 'Alert Text', '', '126985')

    # data_source_index_source | Offset: 112, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_index_source_raw = decode_number((data_raw >> 112) & 0xFF, 8)
    data_source_index_source = data_source_index_source_raw * 1
    publish_field(hass, instance_name, 'data_source_index_source', 'Data Source Index-Source', data_source_index_source, 'Alert Text', '', '126985')

    # alert_occurrence_number | Offset: 120, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_occurrence_number_raw = decode_number((data_raw >> 120) & 0xFF, 8)
    alert_occurrence_number = alert_occurrence_number_raw * 1
    publish_field(hass, instance_name, 'alert_occurrence_number', 'Alert Occurrence Number', alert_occurrence_number, 'Alert Text', '', '126985')

    # language_id | Offset: 128, Length: 8, Resolution: 1, Field Type: LOOKUP
    language_id_raw = (data_raw >> 128) & 0xFF
    language_id = language_id_raw * 1
    publish_field(hass, instance_name, 'language_id', 'Language ID', language_id, 'Alert Text', '', '126985')

def process_pgn_126986(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126986."""
    # alert_type | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_type_raw = (data_raw >> 0) & 0xF
    alert_type = alert_type_raw * 1
    publish_field(hass, instance_name, 'alert_type', 'Alert Type', alert_type, 'Alert Configuration', '', '126986')

    # alert_category | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_category_raw = (data_raw >> 4) & 0xF
    alert_category = alert_category_raw * 1
    publish_field(hass, instance_name, 'alert_category', 'Alert Category', alert_category, 'Alert Configuration', '', '126986')

    # alert_system | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_system_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    alert_system = alert_system_raw * 1
    publish_field(hass, instance_name, 'alert_system', 'Alert System', alert_system, 'Alert Configuration', '', '126986')

    # alert_sub_system | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_sub_system_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    alert_sub_system = alert_sub_system_raw * 1
    publish_field(hass, instance_name, 'alert_sub_system', 'Alert Sub-System', alert_sub_system, 'Alert Configuration', '', '126986')

    # alert_id | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    alert_id_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    alert_id = alert_id_raw * 1
    publish_field(hass, instance_name, 'alert_id', 'Alert ID', alert_id, 'Alert Configuration', '', '126986')

    # data_source_network_id_name | Offset: 40, Length: 64, Resolution: 1, Field Type: NUMBER
    data_source_network_id_name_raw = decode_number((data_raw >> 40) & 0xFFFFFFFFFFFFFFFF, 64)
    data_source_network_id_name = data_source_network_id_name_raw * 1
    publish_field(hass, instance_name, 'data_source_network_id_name', 'Data Source Network ID NAME', data_source_network_id_name, 'Alert Configuration', '', '126986')

    # data_source_instance | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    data_source_instance = data_source_instance_raw * 1
    publish_field(hass, instance_name, 'data_source_instance', 'Data Source Instance', data_source_instance, 'Alert Configuration', '', '126986')

    # data_source_index_source | Offset: 112, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_index_source_raw = decode_number((data_raw >> 112) & 0xFF, 8)
    data_source_index_source = data_source_index_source_raw * 1
    publish_field(hass, instance_name, 'data_source_index_source', 'Data Source Index-Source', data_source_index_source, 'Alert Configuration', '', '126986')

    # alert_occurrence_number | Offset: 120, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_occurrence_number_raw = decode_number((data_raw >> 120) & 0xFF, 8)
    alert_occurrence_number = alert_occurrence_number_raw * 1
    publish_field(hass, instance_name, 'alert_occurrence_number', 'Alert Occurrence Number', alert_occurrence_number, 'Alert Configuration', '', '126986')

    # alert_control | Offset: 128, Length: 2, Resolution: 1, Field Type: NUMBER
    alert_control_raw = decode_number((data_raw >> 128) & 0x3, 2)
    alert_control = alert_control_raw * 1
    publish_field(hass, instance_name, 'alert_control', 'Alert Control', alert_control, 'Alert Configuration', '', '126986')

    # user_defined_alert_assignment | Offset: 130, Length: 2, Resolution: 1, Field Type: NUMBER
    user_defined_alert_assignment_raw = decode_number((data_raw >> 130) & 0x3, 2)
    user_defined_alert_assignment = user_defined_alert_assignment_raw * 1
    publish_field(hass, instance_name, 'user_defined_alert_assignment', 'User Defined Alert Assignment', user_defined_alert_assignment, 'Alert Configuration', '', '126986')

    # reserved | Offset: 132, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 132) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Alert Configuration', '', '126986')

    # reactivation_period | Offset: 136, Length: 8, Resolution: 1, Field Type: NUMBER
    reactivation_period_raw = decode_number((data_raw >> 136) & 0xFF, 8)
    reactivation_period = reactivation_period_raw * 1
    publish_field(hass, instance_name, 'reactivation_period', 'Reactivation Period', reactivation_period, 'Alert Configuration', '', '126986')

    # temporary_silence_period | Offset: 144, Length: 8, Resolution: 1, Field Type: NUMBER
    temporary_silence_period_raw = decode_number((data_raw >> 144) & 0xFF, 8)
    temporary_silence_period = temporary_silence_period_raw * 1
    publish_field(hass, instance_name, 'temporary_silence_period', 'Temporary Silence Period', temporary_silence_period, 'Alert Configuration', '', '126986')

    # escalation_period | Offset: 152, Length: 8, Resolution: 1, Field Type: NUMBER
    escalation_period_raw = decode_number((data_raw >> 152) & 0xFF, 8)
    escalation_period = escalation_period_raw * 1
    publish_field(hass, instance_name, 'escalation_period', 'Escalation Period', escalation_period, 'Alert Configuration', '', '126986')

def process_pgn_126987(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126987."""
    # alert_type | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_type_raw = (data_raw >> 0) & 0xF
    alert_type = alert_type_raw * 1
    publish_field(hass, instance_name, 'alert_type', 'Alert Type', alert_type, 'Alert Threshold', '', '126987')

    # alert_category | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_category_raw = (data_raw >> 4) & 0xF
    alert_category = alert_category_raw * 1
    publish_field(hass, instance_name, 'alert_category', 'Alert Category', alert_category, 'Alert Threshold', '', '126987')

    # alert_system | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_system_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    alert_system = alert_system_raw * 1
    publish_field(hass, instance_name, 'alert_system', 'Alert System', alert_system, 'Alert Threshold', '', '126987')

    # alert_sub_system | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_sub_system_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    alert_sub_system = alert_sub_system_raw * 1
    publish_field(hass, instance_name, 'alert_sub_system', 'Alert Sub-System', alert_sub_system, 'Alert Threshold', '', '126987')

    # alert_id | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    alert_id_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    alert_id = alert_id_raw * 1
    publish_field(hass, instance_name, 'alert_id', 'Alert ID', alert_id, 'Alert Threshold', '', '126987')

    # data_source_network_id_name | Offset: 40, Length: 64, Resolution: 1, Field Type: NUMBER
    data_source_network_id_name_raw = decode_number((data_raw >> 40) & 0xFFFFFFFFFFFFFFFF, 64)
    data_source_network_id_name = data_source_network_id_name_raw * 1
    publish_field(hass, instance_name, 'data_source_network_id_name', 'Data Source Network ID NAME', data_source_network_id_name, 'Alert Threshold', '', '126987')

    # data_source_instance | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    data_source_instance = data_source_instance_raw * 1
    publish_field(hass, instance_name, 'data_source_instance', 'Data Source Instance', data_source_instance, 'Alert Threshold', '', '126987')

    # data_source_index_source | Offset: 112, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_index_source_raw = decode_number((data_raw >> 112) & 0xFF, 8)
    data_source_index_source = data_source_index_source_raw * 1
    publish_field(hass, instance_name, 'data_source_index_source', 'Data Source Index-Source', data_source_index_source, 'Alert Threshold', '', '126987')

    # alert_occurrence_number | Offset: 120, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_occurrence_number_raw = decode_number((data_raw >> 120) & 0xFF, 8)
    alert_occurrence_number = alert_occurrence_number_raw * 1
    publish_field(hass, instance_name, 'alert_occurrence_number', 'Alert Occurrence Number', alert_occurrence_number, 'Alert Threshold', '', '126987')

    # number_of_parameters | Offset: 128, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_parameters_raw = decode_number((data_raw >> 128) & 0xFF, 8)
    number_of_parameters = number_of_parameters_raw * 1
    publish_field(hass, instance_name, 'number_of_parameters', 'Number of Parameters', number_of_parameters, 'Alert Threshold', '', '126987')

    # parameter_number | Offset: 136, Length: 8, Resolution: 1, Field Type: NUMBER
    parameter_number_raw = decode_number((data_raw >> 136) & 0xFF, 8)
    parameter_number = parameter_number_raw * 1
    publish_field(hass, instance_name, 'parameter_number', 'Parameter Number', parameter_number, 'Alert Threshold', '', '126987')

    # trigger_method | Offset: 144, Length: 8, Resolution: 1, Field Type: NUMBER
    trigger_method_raw = decode_number((data_raw >> 144) & 0xFF, 8)
    trigger_method = trigger_method_raw * 1
    publish_field(hass, instance_name, 'trigger_method', 'Trigger Method', trigger_method, 'Alert Threshold', '', '126987')

    # threshold_data_format | Offset: 152, Length: 8, Resolution: 1, Field Type: NUMBER
    threshold_data_format_raw = decode_number((data_raw >> 152) & 0xFF, 8)
    threshold_data_format = threshold_data_format_raw * 1
    publish_field(hass, instance_name, 'threshold_data_format', 'Threshold Data Format', threshold_data_format, 'Alert Threshold', '', '126987')

    # threshold_level | Offset: 160, Length: 64, Resolution: 1, Field Type: NUMBER
    threshold_level_raw = decode_number((data_raw >> 160) & 0xFFFFFFFFFFFFFFFF, 64)
    threshold_level = threshold_level_raw * 1
    publish_field(hass, instance_name, 'threshold_level', 'Threshold Level', threshold_level, 'Alert Threshold', '', '126987')

def process_pgn_126988(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126988."""
    # alert_type | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_type_raw = (data_raw >> 0) & 0xF
    alert_type = alert_type_raw * 1
    publish_field(hass, instance_name, 'alert_type', 'Alert Type', alert_type, 'Alert Value', '', '126988')

    # alert_category | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    alert_category_raw = (data_raw >> 4) & 0xF
    alert_category = alert_category_raw * 1
    publish_field(hass, instance_name, 'alert_category', 'Alert Category', alert_category, 'Alert Value', '', '126988')

    # alert_system | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_system_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    alert_system = alert_system_raw * 1
    publish_field(hass, instance_name, 'alert_system', 'Alert System', alert_system, 'Alert Value', '', '126988')

    # alert_sub_system | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_sub_system_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    alert_sub_system = alert_sub_system_raw * 1
    publish_field(hass, instance_name, 'alert_sub_system', 'Alert Sub-System', alert_sub_system, 'Alert Value', '', '126988')

    # alert_id | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    alert_id_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    alert_id = alert_id_raw * 1
    publish_field(hass, instance_name, 'alert_id', 'Alert ID', alert_id, 'Alert Value', '', '126988')

    # data_source_network_id_name | Offset: 40, Length: 64, Resolution: 1, Field Type: NUMBER
    data_source_network_id_name_raw = decode_number((data_raw >> 40) & 0xFFFFFFFFFFFFFFFF, 64)
    data_source_network_id_name = data_source_network_id_name_raw * 1
    publish_field(hass, instance_name, 'data_source_network_id_name', 'Data Source Network ID NAME', data_source_network_id_name, 'Alert Value', '', '126988')

    # data_source_instance | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    data_source_instance = data_source_instance_raw * 1
    publish_field(hass, instance_name, 'data_source_instance', 'Data Source Instance', data_source_instance, 'Alert Value', '', '126988')

    # data_source_index_source | Offset: 112, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_index_source_raw = decode_number((data_raw >> 112) & 0xFF, 8)
    data_source_index_source = data_source_index_source_raw * 1
    publish_field(hass, instance_name, 'data_source_index_source', 'Data Source Index-Source', data_source_index_source, 'Alert Value', '', '126988')

    # alert_occurrence_number | Offset: 120, Length: 8, Resolution: 1, Field Type: NUMBER
    alert_occurrence_number_raw = decode_number((data_raw >> 120) & 0xFF, 8)
    alert_occurrence_number = alert_occurrence_number_raw * 1
    publish_field(hass, instance_name, 'alert_occurrence_number', 'Alert Occurrence Number', alert_occurrence_number, 'Alert Value', '', '126988')

    # number_of_parameters | Offset: 128, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_parameters_raw = decode_number((data_raw >> 128) & 0xFF, 8)
    number_of_parameters = number_of_parameters_raw * 1
    publish_field(hass, instance_name, 'number_of_parameters', 'Number of Parameters', number_of_parameters, 'Alert Value', '', '126988')

    # value_parameter_number | Offset: 136, Length: 8, Resolution: 1, Field Type: NUMBER
    value_parameter_number_raw = decode_number((data_raw >> 136) & 0xFF, 8)
    value_parameter_number = value_parameter_number_raw * 1
    publish_field(hass, instance_name, 'value_parameter_number', 'Value Parameter Number', value_parameter_number, 'Alert Value', '', '126988')

    # value_data_format | Offset: 144, Length: 8, Resolution: 1, Field Type: NUMBER
    value_data_format_raw = decode_number((data_raw >> 144) & 0xFF, 8)
    value_data_format = value_data_format_raw * 1
    publish_field(hass, instance_name, 'value_data_format', 'Value Data Format', value_data_format, 'Alert Value', '', '126988')

    # value_data | Offset: 152, Length: 64, Resolution: 1, Field Type: NUMBER
    value_data_raw = decode_number((data_raw >> 152) & 0xFFFFFFFFFFFFFFFF, 64)
    value_data = value_data_raw * 1
    publish_field(hass, instance_name, 'value_data', 'Value Data', value_data, 'Alert Value', '', '126988')

def process_pgn_126992(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126992."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'System Time', '', '126992')

    # source | Offset: 8, Length: 4, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 8) & 0xF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'System Time', '', '126992')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'System Time', '', '126992')

    # date | Offset: 16, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 16) & 0xFFFF
    date = decode_date(date_raw * 1)
    publish_field(hass, instance_name, 'date', 'Date', date, 'System Time', 'd', '126992')

    # time | Offset: 32, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 32) & 0xFFFFFFFF
    time = decode_time(time_raw * 0.0001)
    publish_field(hass, instance_name, 'time', 'Time', time, 'System Time', 's', '126992')

def process_pgn_126993(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126993."""
    # data_transmit_offset | Offset: 0, Length: 16, Resolution: 0.001, Field Type: TIME
    data_transmit_offset_raw = (data_raw >> 0) & 0xFFFF
    data_transmit_offset = decode_time(data_transmit_offset_raw * 0.001)
    publish_field(hass, instance_name, 'data_transmit_offset', 'Data transmit offset', data_transmit_offset, 'Heartbeat', 's', '126993')

    # sequence_counter | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    sequence_counter_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    sequence_counter = sequence_counter_raw * 1
    publish_field(hass, instance_name, 'sequence_counter', 'Sequence Counter', sequence_counter, 'Heartbeat', '', '126993')

    # controller_1_state | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    controller_1_state_raw = (data_raw >> 24) & 0x3
    controller_1_state = controller_1_state_raw * 1
    publish_field(hass, instance_name, 'controller_1_state', 'Controller 1 State', controller_1_state, 'Heartbeat', '', '126993')

    # controller_2_state | Offset: 26, Length: 2, Resolution: 1, Field Type: LOOKUP
    controller_2_state_raw = (data_raw >> 26) & 0x3
    controller_2_state = controller_2_state_raw * 1
    publish_field(hass, instance_name, 'controller_2_state', 'Controller 2 State', controller_2_state, 'Heartbeat', '', '126993')

    # equipment_status | Offset: 28, Length: 2, Resolution: 1, Field Type: LOOKUP
    equipment_status_raw = (data_raw >> 28) & 0x3
    equipment_status = equipment_status_raw * 1
    publish_field(hass, instance_name, 'equipment_status', 'Equipment Status', equipment_status, 'Heartbeat', '', '126993')

    # reserved | Offset: 30, Length: 34, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 30) & 0x3FFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Heartbeat', '', '126993')

def process_pgn_126996(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126996."""
    # nmea_2000_version | Offset: 0, Length: 16, Resolution: 0.001, Field Type: NUMBER
    nmea_2000_version_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    nmea_2000_version = nmea_2000_version_raw * 0.001
    publish_field(hass, instance_name, 'nmea_2000_version', 'NMEA 2000 Version', nmea_2000_version, 'Product Information', '', '126996')

    # product_code | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    product_code_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    product_code = product_code_raw * 1
    publish_field(hass, instance_name, 'product_code', 'Product Code', product_code, 'Product Information', '', '126996')

    # model_id | Offset: 32, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # software_version_code | Offset: 288, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # model_version | Offset: 544, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # model_serial_code | Offset: 800, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # certification_level | Offset: 1056, Length: 8, Resolution: 1, Field Type: NUMBER
    certification_level_raw = decode_number((data_raw >> 1056) & 0xFF, 8)
    certification_level = certification_level_raw * 1
    publish_field(hass, instance_name, 'certification_level', 'Certification Level', certification_level, 'Product Information', '', '126996')

    # load_equivalency | Offset: 1064, Length: 8, Resolution: 1, Field Type: NUMBER
    load_equivalency_raw = decode_number((data_raw >> 1064) & 0xFF, 8)
    load_equivalency = load_equivalency_raw * 1
    publish_field(hass, instance_name, 'load_equivalency', 'Load Equivalency', load_equivalency, 'Product Information', '', '126996')

def process_pgn_126998(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 126998."""
def process_pgn_127233(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127233."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Man Overboard Notification', '', '127233')

    # mob_emitter_id | Offset: 8, Length: 32, Resolution: 1, Field Type: NUMBER
    mob_emitter_id_raw = decode_number((data_raw >> 8) & 0xFFFFFFFF, 32)
    mob_emitter_id = mob_emitter_id_raw * 1
    publish_field(hass, instance_name, 'mob_emitter_id', 'MOB Emitter ID', mob_emitter_id, 'Man Overboard Notification', '', '127233')

    # man_overboard_status | Offset: 40, Length: 3, Resolution: 1, Field Type: LOOKUP
    man_overboard_status_raw = (data_raw >> 40) & 0x7
    man_overboard_status = man_overboard_status_raw * 1
    publish_field(hass, instance_name, 'man_overboard_status', 'Man Overboard Status', man_overboard_status, 'Man Overboard Notification', '', '127233')

    # reserved | Offset: 43, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 43) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Man Overboard Notification', '', '127233')

    # activation_time | Offset: 48, Length: 32, Resolution: 0.0001, Field Type: TIME
    activation_time_raw = (data_raw >> 48) & 0xFFFFFFFF
    activation_time = decode_time(activation_time_raw * 0.0001)
    publish_field(hass, instance_name, 'activation_time', 'Activation Time', activation_time, 'Man Overboard Notification', 's', '127233')

    # position_source | Offset: 80, Length: 3, Resolution: 1, Field Type: LOOKUP
    position_source_raw = (data_raw >> 80) & 0x7
    position_source = position_source_raw * 1
    publish_field(hass, instance_name, 'position_source', 'Position Source', position_source, 'Man Overboard Notification', '', '127233')

    # reserved | Offset: 83, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 83) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Man Overboard Notification', '', '127233')

    # position_date | Offset: 88, Length: 16, Resolution: 1, Field Type: DATE
    position_date_raw = (data_raw >> 88) & 0xFFFF
    position_date = decode_date(position_date_raw * 1)
    publish_field(hass, instance_name, 'position_date', 'Position Date', position_date, 'Man Overboard Notification', 'd', '127233')

    # position_time | Offset: 104, Length: 32, Resolution: 0.0001, Field Type: TIME
    position_time_raw = (data_raw >> 104) & 0xFFFFFFFF
    position_time = decode_time(position_time_raw * 0.0001)
    publish_field(hass, instance_name, 'position_time', 'Position Time', position_time, 'Man Overboard Notification', 's', '127233')

    # latitude | Offset: 136, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 136) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'Man Overboard Notification', 'deg', '127233')

    # longitude | Offset: 168, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 168) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'Man Overboard Notification', 'deg', '127233')

    # cog_reference | Offset: 200, Length: 2, Resolution: 1, Field Type: LOOKUP
    cog_reference_raw = (data_raw >> 200) & 0x3
    cog_reference = cog_reference_raw * 1
    publish_field(hass, instance_name, 'cog_reference', 'COG Reference', cog_reference, 'Man Overboard Notification', '', '127233')

    # reserved | Offset: 202, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 202) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Man Overboard Notification', '', '127233')

    # cog | Offset: 208, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 208) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'Man Overboard Notification', 'rad', '127233')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'Man Overboard Notification', 'Deg', '127233')

    # sog | Offset: 224, Length: 16, Resolution: 0.01, Field Type: NUMBER
    sog_raw = decode_number((data_raw >> 224) & 0xFFFF, 16)
    sog = sog_raw * 0.01
    publish_field(hass, instance_name, 'sog', 'SOG', sog, 'Man Overboard Notification', 'm/s', '127233')
    publish_field(hass, instance_name, 'sog_knots', 'SOG Knots', mps_to_knots(sog), 'Man Overboard Notification', 'Kn', '127233')

    # mmsi_of_vessel_of_origin | Offset: 240, Length: 32, Resolution: 1, Field Type: MMSI
    mmsi_of_vessel_of_origin_raw = (data_raw >> 240) & 0xFFFFFFFF
    mmsi_of_vessel_of_origin = mmsi_of_vessel_of_origin_raw * 1
    publish_field(hass, instance_name, 'mmsi_of_vessel_of_origin', 'MMSI of vessel of origin', mmsi_of_vessel_of_origin, 'Man Overboard Notification', '', '127233')

    # mob_emitter_battery_low_status | Offset: 272, Length: 3, Resolution: 1, Field Type: LOOKUP
    mob_emitter_battery_low_status_raw = (data_raw >> 272) & 0x7
    mob_emitter_battery_low_status = mob_emitter_battery_low_status_raw * 1
    publish_field(hass, instance_name, 'mob_emitter_battery_low_status', 'MOB Emitter Battery Low Status', mob_emitter_battery_low_status, 'Man Overboard Notification', '', '127233')

    # reserved | Offset: 275, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 275) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Man Overboard Notification', '', '127233')

def process_pgn_127237(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127237."""
    # rudder_limit_exceeded | Offset: 0, Length: 2, Resolution: 1, Field Type: LOOKUP
    rudder_limit_exceeded_raw = (data_raw >> 0) & 0x3
    rudder_limit_exceeded = rudder_limit_exceeded_raw * 1
    publish_field(hass, instance_name, 'rudder_limit_exceeded', 'Rudder Limit Exceeded', rudder_limit_exceeded, 'Heading/Track control', '', '127237')

    # off_heading_limit_exceeded | Offset: 2, Length: 2, Resolution: 1, Field Type: LOOKUP
    off_heading_limit_exceeded_raw = (data_raw >> 2) & 0x3
    off_heading_limit_exceeded = off_heading_limit_exceeded_raw * 1
    publish_field(hass, instance_name, 'off_heading_limit_exceeded', 'Off-Heading Limit Exceeded', off_heading_limit_exceeded, 'Heading/Track control', '', '127237')

    # off_track_limit_exceeded | Offset: 4, Length: 2, Resolution: 1, Field Type: LOOKUP
    off_track_limit_exceeded_raw = (data_raw >> 4) & 0x3
    off_track_limit_exceeded = off_track_limit_exceeded_raw * 1
    publish_field(hass, instance_name, 'off_track_limit_exceeded', 'Off-Track Limit Exceeded', off_track_limit_exceeded, 'Heading/Track control', '', '127237')

    # override | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    override_raw = (data_raw >> 6) & 0x3
    override = override_raw * 1
    publish_field(hass, instance_name, 'override', 'Override', override, 'Heading/Track control', '', '127237')

    # steering_mode | Offset: 8, Length: 3, Resolution: 1, Field Type: LOOKUP
    steering_mode_raw = (data_raw >> 8) & 0x7
    steering_mode = steering_mode_raw * 1
    publish_field(hass, instance_name, 'steering_mode', 'Steering Mode', steering_mode, 'Heading/Track control', '', '127237')

    # turn_mode | Offset: 11, Length: 3, Resolution: 1, Field Type: LOOKUP
    turn_mode_raw = (data_raw >> 11) & 0x7
    turn_mode = turn_mode_raw * 1
    publish_field(hass, instance_name, 'turn_mode', 'Turn Mode', turn_mode, 'Heading/Track control', '', '127237')

    # heading_reference | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    heading_reference_raw = (data_raw >> 14) & 0x3
    heading_reference = heading_reference_raw * 1
    publish_field(hass, instance_name, 'heading_reference', 'Heading Reference', heading_reference, 'Heading/Track control', '', '127237')

    # reserved | Offset: 16, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Heading/Track control', '', '127237')

    # commanded_rudder_direction | Offset: 21, Length: 3, Resolution: 1, Field Type: LOOKUP
    commanded_rudder_direction_raw = (data_raw >> 21) & 0x7
    commanded_rudder_direction = commanded_rudder_direction_raw * 1
    publish_field(hass, instance_name, 'commanded_rudder_direction', 'Commanded Rudder Direction', commanded_rudder_direction, 'Heading/Track control', '', '127237')

    # commanded_rudder_angle | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    commanded_rudder_angle_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if commanded_rudder_angle_raw & (1 << (16 - 1)):
        commanded_rudder_angle_raw -= (1 << 16)
    commanded_rudder_angle = commanded_rudder_angle_raw * 0.0001
    publish_field(hass, instance_name, 'commanded_rudder_angle', 'Commanded Rudder Angle', commanded_rudder_angle, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'commanded_rudder_angle_degrees', 'Commanded Rudder Angle Degrees', radians_to_degrees(commanded_rudder_angle), 'Heading/Track control', 'Deg', '127237')

    # heading_to_steer__course_ | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_to_steer__course__raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    heading_to_steer__course_ = heading_to_steer__course__raw * 0.0001
    publish_field(hass, instance_name, 'heading_to_steer__course_', 'Heading-To-Steer (Course)', heading_to_steer__course_, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'heading_to_steer__course__degrees', 'Heading-To-Steer (Course) Degrees', radians_to_degrees(heading_to_steer__course_), 'Heading/Track control', 'Deg', '127237')

    # track | Offset: 56, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    track_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    track = track_raw * 0.0001
    publish_field(hass, instance_name, 'track', 'Track', track, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'track_degrees', 'Track Degrees', radians_to_degrees(track), 'Heading/Track control', 'Deg', '127237')

    # rudder_limit | Offset: 72, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    rudder_limit_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    rudder_limit = rudder_limit_raw * 0.0001
    publish_field(hass, instance_name, 'rudder_limit', 'Rudder Limit', rudder_limit, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'rudder_limit_degrees', 'Rudder Limit Degrees', radians_to_degrees(rudder_limit), 'Heading/Track control', 'Deg', '127237')

    # off_heading_limit | Offset: 88, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    off_heading_limit_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    off_heading_limit = off_heading_limit_raw * 0.0001
    publish_field(hass, instance_name, 'off_heading_limit', 'Off-Heading Limit', off_heading_limit, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'off_heading_limit_degrees', 'Off-Heading Limit Degrees', radians_to_degrees(off_heading_limit), 'Heading/Track control', 'Deg', '127237')

    # radius_of_turn_order | Offset: 104, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    radius_of_turn_order_raw = decode_number((data_raw >> 104) & 0xFFFF, 16)
    if radius_of_turn_order_raw & (1 << (16 - 1)):
        radius_of_turn_order_raw -= (1 << 16)
    radius_of_turn_order = radius_of_turn_order_raw * 0.0001
    publish_field(hass, instance_name, 'radius_of_turn_order', 'Radius of Turn Order', radius_of_turn_order, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'radius_of_turn_order_degrees', 'Radius of Turn Order Degrees', radians_to_degrees(radius_of_turn_order), 'Heading/Track control', 'Deg', '127237')

    # rate_of_turn_order | Offset: 120, Length: 16, Resolution: 3.125e-05, Field Type: NUMBER
    rate_of_turn_order_raw = decode_number((data_raw >> 120) & 0xFFFF, 16)
    if rate_of_turn_order_raw & (1 << (16 - 1)):
        rate_of_turn_order_raw -= (1 << 16)
    rate_of_turn_order = rate_of_turn_order_raw * 3.125e-05
    publish_field(hass, instance_name, 'rate_of_turn_order', 'Rate of Turn Order', rate_of_turn_order, 'Heading/Track control', 'rad/s', '127237')

    # off_track_limit | Offset: 136, Length: 16, Resolution: 1, Field Type: NUMBER
    off_track_limit_raw = decode_number((data_raw >> 136) & 0xFFFF, 16)
    if off_track_limit_raw & (1 << (16 - 1)):
        off_track_limit_raw -= (1 << 16)
    off_track_limit = off_track_limit_raw * 1
    publish_field(hass, instance_name, 'off_track_limit', 'Off-Track Limit', off_track_limit, 'Heading/Track control', 'm', '127237')

    # vessel_heading | Offset: 152, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    vessel_heading_raw = decode_number((data_raw >> 152) & 0xFFFF, 16)
    vessel_heading = vessel_heading_raw * 0.0001
    publish_field(hass, instance_name, 'vessel_heading', 'Vessel Heading', vessel_heading, 'Heading/Track control', 'rad', '127237')
    publish_field(hass, instance_name, 'vessel_heading_degrees', 'Vessel Heading Degrees', radians_to_degrees(vessel_heading), 'Heading/Track control', 'Deg', '127237')

def process_pgn_127245(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127245."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Rudder', '', '127245')

    # direction_order | Offset: 8, Length: 3, Resolution: 1, Field Type: LOOKUP
    direction_order_raw = (data_raw >> 8) & 0x7
    direction_order = direction_order_raw * 1
    publish_field(hass, instance_name, 'direction_order', 'Direction Order', direction_order, 'Rudder', '', '127245')

    # reserved | Offset: 11, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Rudder', '', '127245')

    # angle_order | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    angle_order_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    if angle_order_raw & (1 << (16 - 1)):
        angle_order_raw -= (1 << 16)
    angle_order = angle_order_raw * 0.0001
    publish_field(hass, instance_name, 'angle_order', 'Angle Order', angle_order, 'Rudder', 'rad', '127245')
    publish_field(hass, instance_name, 'angle_order_degrees', 'Angle Order Degrees', radians_to_degrees(angle_order), 'Rudder', 'Deg', '127245')

    # position | Offset: 32, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    position_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if position_raw & (1 << (16 - 1)):
        position_raw -= (1 << 16)
    position = position_raw * 0.0001
    publish_field(hass, instance_name, 'position', 'Position', position, 'Rudder', 'rad', '127245')
    publish_field(hass, instance_name, 'position_degrees', 'Position Degrees', radians_to_degrees(position), 'Rudder', 'Deg', '127245')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Rudder', '', '127245')

def process_pgn_127250(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127250."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Vessel Heading', '', '127250')

    # heading | Offset: 8, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    heading = heading_raw * 0.0001
    publish_field(hass, instance_name, 'heading', 'Heading', heading, 'Vessel Heading', 'rad', '127250')
    publish_field(hass, instance_name, 'heading_degrees', 'Heading Degrees', radians_to_degrees(heading), 'Vessel Heading', 'Deg', '127250')

    # deviation | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    deviation_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if deviation_raw & (1 << (16 - 1)):
        deviation_raw -= (1 << 16)
    deviation = deviation_raw * 0.0001
    publish_field(hass, instance_name, 'deviation', 'Deviation', deviation, 'Vessel Heading', 'rad', '127250')
    publish_field(hass, instance_name, 'deviation_degrees', 'Deviation Degrees', radians_to_degrees(deviation), 'Vessel Heading', 'Deg', '127250')

    # variation | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    variation_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if variation_raw & (1 << (16 - 1)):
        variation_raw -= (1 << 16)
    variation = variation_raw * 0.0001
    publish_field(hass, instance_name, 'variation', 'Variation', variation, 'Vessel Heading', 'rad', '127250')
    publish_field(hass, instance_name, 'variation_degrees', 'Variation Degrees', radians_to_degrees(variation), 'Vessel Heading', 'Deg', '127250')

    # reference | Offset: 56, Length: 2, Resolution: 1, Field Type: LOOKUP
    reference_raw = (data_raw >> 56) & 0x3
    reference = reference_raw * 1
    publish_field(hass, instance_name, 'reference', 'Reference', reference, 'Vessel Heading', '', '127250')

    # reserved | Offset: 58, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 58) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Vessel Heading', '', '127250')

def process_pgn_127251(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127251."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Rate of Turn', '', '127251')

    # rate | Offset: 8, Length: 32, Resolution: 3.125e-08, Field Type: NUMBER
    rate_raw = decode_number((data_raw >> 8) & 0xFFFFFFFF, 32)
    if rate_raw & (1 << (32 - 1)):
        rate_raw -= (1 << 32)
    rate = rate_raw * 3.125e-08
    publish_field(hass, instance_name, 'rate', 'Rate', rate, 'Rate of Turn', 'rad/s', '127251')

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Rate of Turn', '', '127251')

def process_pgn_127252(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127252."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Heave', '', '127252')

    # heave | Offset: 8, Length: 16, Resolution: 0.01, Field Type: NUMBER
    heave_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    if heave_raw & (1 << (16 - 1)):
        heave_raw -= (1 << 16)
    heave = heave_raw * 0.01
    publish_field(hass, instance_name, 'heave', 'Heave', heave, 'Heave', 'm', '127252')

    # reserved | Offset: 24, Length: 40, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 24) & 0xFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Heave', '', '127252')

def process_pgn_127257(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127257."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Attitude', '', '127257')

    # yaw | Offset: 8, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    yaw_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    if yaw_raw & (1 << (16 - 1)):
        yaw_raw -= (1 << 16)
    yaw = yaw_raw * 0.0001
    publish_field(hass, instance_name, 'yaw', 'Yaw', yaw, 'Attitude', 'rad', '127257')
    publish_field(hass, instance_name, 'yaw_degrees', 'Yaw Degrees', radians_to_degrees(yaw), 'Attitude', 'Deg', '127257')

    # pitch | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    pitch_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if pitch_raw & (1 << (16 - 1)):
        pitch_raw -= (1 << 16)
    pitch = pitch_raw * 0.0001
    publish_field(hass, instance_name, 'pitch', 'Pitch', pitch, 'Attitude', 'rad', '127257')
    publish_field(hass, instance_name, 'pitch_degrees', 'Pitch Degrees', radians_to_degrees(pitch), 'Attitude', 'Deg', '127257')

    # roll | Offset: 40, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    roll_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if roll_raw & (1 << (16 - 1)):
        roll_raw -= (1 << 16)
    roll = roll_raw * 0.0001
    publish_field(hass, instance_name, 'roll', 'Roll', roll, 'Attitude', 'rad', '127257')
    publish_field(hass, instance_name, 'roll_degrees', 'Roll Degrees', radians_to_degrees(roll), 'Attitude', 'Deg', '127257')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Attitude', '', '127257')

def process_pgn_127258(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127258."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Magnetic Variation', '', '127258')

    # source | Offset: 8, Length: 4, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 8) & 0xF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Magnetic Variation', '', '127258')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Magnetic Variation', '', '127258')

    # age_of_service | Offset: 16, Length: 16, Resolution: 1, Field Type: DATE
    age_of_service_raw = (data_raw >> 16) & 0xFFFF
    age_of_service = decode_date(age_of_service_raw * 1)
    publish_field(hass, instance_name, 'age_of_service', 'Age of service', age_of_service, 'Magnetic Variation', 'd', '127258')

    # variation | Offset: 32, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    variation_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if variation_raw & (1 << (16 - 1)):
        variation_raw -= (1 << 16)
    variation = variation_raw * 0.0001
    publish_field(hass, instance_name, 'variation', 'Variation', variation, 'Magnetic Variation', 'rad', '127258')
    publish_field(hass, instance_name, 'variation_degrees', 'Variation Degrees', radians_to_degrees(variation), 'Magnetic Variation', 'Deg', '127258')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Magnetic Variation', '', '127258')

def process_pgn_127488(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127488."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    instance_raw = (data_raw >> 0) & 0xFF
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Engine Parameters, Rapid Update', '', '127488')

    # speed | Offset: 8, Length: 16, Resolution: 0.25, Field Type: NUMBER
    speed_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    speed = speed_raw * 0.25
    publish_field(hass, instance_name, 'speed', 'Speed', speed, 'Engine Parameters, Rapid Update', 'rpm', '127488')

    # boost_pressure | Offset: 24, Length: 16, Resolution: 100, Field Type: NUMBER
    boost_pressure_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    boost_pressure = boost_pressure_raw * 100
    publish_field(hass, instance_name, 'boost_pressure', 'Boost Pressure', boost_pressure, 'Engine Parameters, Rapid Update', 'Pa', '127488')

    # tilt_trim | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    tilt_trim_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    if tilt_trim_raw & (1 << (8 - 1)):
        tilt_trim_raw -= (1 << 8)
    tilt_trim = tilt_trim_raw * 1
    publish_field(hass, instance_name, 'tilt_trim', 'Tilt/Trim', tilt_trim, 'Engine Parameters, Rapid Update', '', '127488')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Engine Parameters, Rapid Update', '', '127488')

def process_pgn_127489(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127489."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    instance_raw = (data_raw >> 0) & 0xFF
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Engine Parameters, Dynamic', '', '127489')

    # oil_pressure | Offset: 8, Length: 16, Resolution: 100, Field Type: NUMBER
    oil_pressure_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    oil_pressure = oil_pressure_raw * 100
    publish_field(hass, instance_name, 'oil_pressure', 'Oil pressure', oil_pressure, 'Engine Parameters, Dynamic', 'Pa', '127489')

    # oil_temperature | Offset: 24, Length: 16, Resolution: 0.1, Field Type: NUMBER
    oil_temperature_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    oil_temperature = oil_temperature_raw * 0.1
    publish_field(hass, instance_name, 'oil_temperature', 'Oil temperature', oil_temperature, 'Engine Parameters, Dynamic', 'K', '127489')
    publish_field(hass, instance_name, 'oil_temperature_celsius', 'Oil temperature Celsius', kelvin_to_celsius(oil_temperature), 'Engine Parameters, Dynamic', 'C', '127489')
    publish_field(hass, instance_name, 'oil_temperature_fahrenheit', 'Oil temperature Fahrenheit', kelvin_to_fahrenheit(oil_temperature), 'Engine Parameters, Dynamic', 'F', '127489')

    # temperature | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    temperature_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    temperature = temperature_raw * 0.01
    publish_field(hass, instance_name, 'temperature', 'Temperature', temperature, 'Engine Parameters, Dynamic', 'K', '127489')
    publish_field(hass, instance_name, 'temperature_celsius', 'Temperature Celsius', kelvin_to_celsius(temperature), 'Engine Parameters, Dynamic', 'C', '127489')
    publish_field(hass, instance_name, 'temperature_fahrenheit', 'Temperature Fahrenheit', kelvin_to_fahrenheit(temperature), 'Engine Parameters, Dynamic', 'F', '127489')

    # alternator_potential | Offset: 56, Length: 16, Resolution: 0.01, Field Type: NUMBER
    alternator_potential_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    if alternator_potential_raw & (1 << (16 - 1)):
        alternator_potential_raw -= (1 << 16)
    alternator_potential = alternator_potential_raw * 0.01
    publish_field(hass, instance_name, 'alternator_potential', 'Alternator Potential', alternator_potential, 'Engine Parameters, Dynamic', 'V', '127489')

    # fuel_rate | Offset: 72, Length: 16, Resolution: 0.1, Field Type: NUMBER
    fuel_rate_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    if fuel_rate_raw & (1 << (16 - 1)):
        fuel_rate_raw -= (1 << 16)
    fuel_rate = fuel_rate_raw * 0.1
    publish_field(hass, instance_name, 'fuel_rate', 'Fuel Rate', fuel_rate, 'Engine Parameters, Dynamic', 'L/h', '127489')

    # total_engine_hours | Offset: 88, Length: 32, Resolution: 1, Field Type: TIME
    total_engine_hours_raw = (data_raw >> 88) & 0xFFFFFFFF
    total_engine_hours = decode_time(total_engine_hours_raw * 1)
    publish_field(hass, instance_name, 'total_engine_hours', 'Total Engine hours', total_engine_hours, 'Engine Parameters, Dynamic', 's', '127489')

    # coolant_pressure | Offset: 120, Length: 16, Resolution: 100, Field Type: NUMBER
    coolant_pressure_raw = decode_number((data_raw >> 120) & 0xFFFF, 16)
    coolant_pressure = coolant_pressure_raw * 100
    publish_field(hass, instance_name, 'coolant_pressure', 'Coolant Pressure', coolant_pressure, 'Engine Parameters, Dynamic', 'Pa', '127489')

    # fuel_pressure | Offset: 136, Length: 16, Resolution: 1000, Field Type: NUMBER
    fuel_pressure_raw = decode_number((data_raw >> 136) & 0xFFFF, 16)
    fuel_pressure = fuel_pressure_raw * 1000
    publish_field(hass, instance_name, 'fuel_pressure', 'Fuel Pressure', fuel_pressure, 'Engine Parameters, Dynamic', 'Pa', '127489')

    # reserved | Offset: 152, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 152) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Engine Parameters, Dynamic', '', '127489')

    # discrete_status_1 | Offset: 160, Length: 16, Resolution: 1, Field Type: BITLOOKUP
    discrete_status_1_raw = (data_raw >> 160) & 0xFFFF
    discrete_status_1 = discrete_status_1_raw * 1
    publish_field(hass, instance_name, 'discrete_status_1', 'Discrete Status 1', discrete_status_1, 'Engine Parameters, Dynamic', '', '127489')

    # discrete_status_2 | Offset: 176, Length: 16, Resolution: 1, Field Type: BITLOOKUP
    discrete_status_2_raw = (data_raw >> 176) & 0xFFFF
    discrete_status_2 = discrete_status_2_raw * 1
    publish_field(hass, instance_name, 'discrete_status_2', 'Discrete Status 2', discrete_status_2, 'Engine Parameters, Dynamic', '', '127489')

    # engine_load | Offset: 192, Length: 8, Resolution: 1, Field Type: NUMBER
    engine_load_raw = decode_number((data_raw >> 192) & 0xFF, 8)
    if engine_load_raw & (1 << (8 - 1)):
        engine_load_raw -= (1 << 8)
    engine_load = engine_load_raw * 1
    publish_field(hass, instance_name, 'engine_load', 'Engine Load', engine_load, 'Engine Parameters, Dynamic', '%', '127489')

    # engine_torque | Offset: 200, Length: 8, Resolution: 1, Field Type: NUMBER
    engine_torque_raw = decode_number((data_raw >> 200) & 0xFF, 8)
    if engine_torque_raw & (1 << (8 - 1)):
        engine_torque_raw -= (1 << 8)
    engine_torque = engine_torque_raw * 1
    publish_field(hass, instance_name, 'engine_torque', 'Engine Torque', engine_torque, 'Engine Parameters, Dynamic', '%', '127489')

def process_pgn_127490(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127490."""
    # inverter_motor_identifier | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    inverter_motor_identifier_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    inverter_motor_identifier = inverter_motor_identifier_raw * 1
    publish_field(hass, instance_name, 'inverter_motor_identifier', 'Inverter/Motor Identifier', inverter_motor_identifier, 'Electric Drive Status, Dynamic', '', '127490')

    # operating_mode | Offset: 8, Length: 4, Resolution: 1, Field Type: NUMBER
    operating_mode_raw = decode_number((data_raw >> 8) & 0xF, 4)
    operating_mode = operating_mode_raw * 1
    publish_field(hass, instance_name, 'operating_mode', 'Operating Mode', operating_mode, 'Electric Drive Status, Dynamic', '', '127490')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Electric Drive Status, Dynamic', '', '127490')

    # motor_temperature | Offset: 16, Length: 16, Resolution: 0.01, Field Type: NUMBER
    motor_temperature_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    motor_temperature = motor_temperature_raw * 0.01
    publish_field(hass, instance_name, 'motor_temperature', 'Motor Temperature', motor_temperature, 'Electric Drive Status, Dynamic', 'K', '127490')
    publish_field(hass, instance_name, 'motor_temperature_celsius', 'Motor Temperature Celsius', kelvin_to_celsius(motor_temperature), 'Electric Drive Status, Dynamic', 'C', '127490')
    publish_field(hass, instance_name, 'motor_temperature_fahrenheit', 'Motor Temperature Fahrenheit', kelvin_to_fahrenheit(motor_temperature), 'Electric Drive Status, Dynamic', 'F', '127490')

    # inverter_temperature | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    inverter_temperature_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    inverter_temperature = inverter_temperature_raw * 0.01
    publish_field(hass, instance_name, 'inverter_temperature', 'Inverter Temperature', inverter_temperature, 'Electric Drive Status, Dynamic', 'K', '127490')
    publish_field(hass, instance_name, 'inverter_temperature_celsius', 'Inverter Temperature Celsius', kelvin_to_celsius(inverter_temperature), 'Electric Drive Status, Dynamic', 'C', '127490')
    publish_field(hass, instance_name, 'inverter_temperature_fahrenheit', 'Inverter Temperature Fahrenheit', kelvin_to_fahrenheit(inverter_temperature), 'Electric Drive Status, Dynamic', 'F', '127490')

    # coolant_temperature | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    coolant_temperature_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    coolant_temperature = coolant_temperature_raw * 0.01
    publish_field(hass, instance_name, 'coolant_temperature', 'Coolant Temperature', coolant_temperature, 'Electric Drive Status, Dynamic', 'K', '127490')
    publish_field(hass, instance_name, 'coolant_temperature_celsius', 'Coolant Temperature Celsius', kelvin_to_celsius(coolant_temperature), 'Electric Drive Status, Dynamic', 'C', '127490')
    publish_field(hass, instance_name, 'coolant_temperature_fahrenheit', 'Coolant Temperature Fahrenheit', kelvin_to_fahrenheit(coolant_temperature), 'Electric Drive Status, Dynamic', 'F', '127490')

    # gear_temperature | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    gear_temperature_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    gear_temperature = gear_temperature_raw * 0.01
    publish_field(hass, instance_name, 'gear_temperature', 'Gear Temperature', gear_temperature, 'Electric Drive Status, Dynamic', 'K', '127490')
    publish_field(hass, instance_name, 'gear_temperature_celsius', 'Gear Temperature Celsius', kelvin_to_celsius(gear_temperature), 'Electric Drive Status, Dynamic', 'C', '127490')
    publish_field(hass, instance_name, 'gear_temperature_fahrenheit', 'Gear Temperature Fahrenheit', kelvin_to_fahrenheit(gear_temperature), 'Electric Drive Status, Dynamic', 'F', '127490')

    # shaft_torque | Offset: 80, Length: 16, Resolution: 1, Field Type: NUMBER
    shaft_torque_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    shaft_torque = shaft_torque_raw * 1
    publish_field(hass, instance_name, 'shaft_torque', 'Shaft Torque', shaft_torque, 'Electric Drive Status, Dynamic', '', '127490')

def process_pgn_127491(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127491."""
    # energy_storage_identifier | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    energy_storage_identifier_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    energy_storage_identifier = energy_storage_identifier_raw * 1
    publish_field(hass, instance_name, 'energy_storage_identifier', 'Energy Storage Identifier', energy_storage_identifier, 'Electric Energy Storage Status, Dynamic', '', '127491')

    # state_of_charge | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    state_of_charge_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    state_of_charge = state_of_charge_raw * 1
    publish_field(hass, instance_name, 'state_of_charge', 'State of Charge', state_of_charge, 'Electric Energy Storage Status, Dynamic', '', '127491')

    # time_remaining | Offset: 16, Length: 16, Resolution: 60, Field Type: TIME
    time_remaining_raw = (data_raw >> 16) & 0xFFFF
    time_remaining = decode_time(time_remaining_raw * 60)
    publish_field(hass, instance_name, 'time_remaining', 'Time Remaining', time_remaining, 'Electric Energy Storage Status, Dynamic', 's', '127491')

    # highest_cell_temperature | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    highest_cell_temperature_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    highest_cell_temperature = highest_cell_temperature_raw * 0.01
    publish_field(hass, instance_name, 'highest_cell_temperature', 'Highest Cell Temperature', highest_cell_temperature, 'Electric Energy Storage Status, Dynamic', 'K', '127491')
    publish_field(hass, instance_name, 'highest_cell_temperature_celsius', 'Highest Cell Temperature Celsius', kelvin_to_celsius(highest_cell_temperature), 'Electric Energy Storage Status, Dynamic', 'C', '127491')
    publish_field(hass, instance_name, 'highest_cell_temperature_fahrenheit', 'Highest Cell Temperature Fahrenheit', kelvin_to_fahrenheit(highest_cell_temperature), 'Electric Energy Storage Status, Dynamic', 'F', '127491')

    # lowest_cell_temperature | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    lowest_cell_temperature_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    lowest_cell_temperature = lowest_cell_temperature_raw * 0.01
    publish_field(hass, instance_name, 'lowest_cell_temperature', 'Lowest Cell Temperature', lowest_cell_temperature, 'Electric Energy Storage Status, Dynamic', 'K', '127491')
    publish_field(hass, instance_name, 'lowest_cell_temperature_celsius', 'Lowest Cell Temperature Celsius', kelvin_to_celsius(lowest_cell_temperature), 'Electric Energy Storage Status, Dynamic', 'C', '127491')
    publish_field(hass, instance_name, 'lowest_cell_temperature_fahrenheit', 'Lowest Cell Temperature Fahrenheit', kelvin_to_fahrenheit(lowest_cell_temperature), 'Electric Energy Storage Status, Dynamic', 'F', '127491')

    # average_cell_temperature | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    average_cell_temperature_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    average_cell_temperature = average_cell_temperature_raw * 0.01
    publish_field(hass, instance_name, 'average_cell_temperature', 'Average Cell Temperature', average_cell_temperature, 'Electric Energy Storage Status, Dynamic', 'K', '127491')
    publish_field(hass, instance_name, 'average_cell_temperature_celsius', 'Average Cell Temperature Celsius', kelvin_to_celsius(average_cell_temperature), 'Electric Energy Storage Status, Dynamic', 'C', '127491')
    publish_field(hass, instance_name, 'average_cell_temperature_fahrenheit', 'Average Cell Temperature Fahrenheit', kelvin_to_fahrenheit(average_cell_temperature), 'Electric Energy Storage Status, Dynamic', 'F', '127491')

    # max_discharge_current | Offset: 80, Length: 16, Resolution: 0.1, Field Type: NUMBER
    max_discharge_current_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    if max_discharge_current_raw & (1 << (16 - 1)):
        max_discharge_current_raw -= (1 << 16)
    max_discharge_current = max_discharge_current_raw * 0.1
    publish_field(hass, instance_name, 'max_discharge_current', 'Max Discharge Current', max_discharge_current, 'Electric Energy Storage Status, Dynamic', 'A', '127491')

    # max_charge_current | Offset: 96, Length: 16, Resolution: 0.1, Field Type: NUMBER
    max_charge_current_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    if max_charge_current_raw & (1 << (16 - 1)):
        max_charge_current_raw -= (1 << 16)
    max_charge_current = max_charge_current_raw * 0.1
    publish_field(hass, instance_name, 'max_charge_current', 'Max Charge Current', max_charge_current, 'Electric Energy Storage Status, Dynamic', 'A', '127491')

    # cooling_system_status | Offset: 112, Length: 4, Resolution: 1, Field Type: NUMBER
    cooling_system_status_raw = decode_number((data_raw >> 112) & 0xF, 4)
    cooling_system_status = cooling_system_status_raw * 1
    publish_field(hass, instance_name, 'cooling_system_status', 'Cooling System Status', cooling_system_status, 'Electric Energy Storage Status, Dynamic', '', '127491')

    # heating_system_status | Offset: 116, Length: 4, Resolution: 1, Field Type: NUMBER
    heating_system_status_raw = decode_number((data_raw >> 116) & 0xF, 4)
    heating_system_status = heating_system_status_raw * 1
    publish_field(hass, instance_name, 'heating_system_status', 'Heating System Status', heating_system_status, 'Electric Energy Storage Status, Dynamic', '', '127491')

def process_pgn_127493(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127493."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    instance_raw = (data_raw >> 0) & 0xFF
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Transmission Parameters, Dynamic', '', '127493')

    # transmission_gear | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    transmission_gear_raw = (data_raw >> 8) & 0x3
    transmission_gear = transmission_gear_raw * 1
    publish_field(hass, instance_name, 'transmission_gear', 'Transmission Gear', transmission_gear, 'Transmission Parameters, Dynamic', '', '127493')

    # reserved | Offset: 10, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 10) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Transmission Parameters, Dynamic', '', '127493')

    # oil_pressure | Offset: 16, Length: 16, Resolution: 100, Field Type: NUMBER
    oil_pressure_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    oil_pressure = oil_pressure_raw * 100
    publish_field(hass, instance_name, 'oil_pressure', 'Oil pressure', oil_pressure, 'Transmission Parameters, Dynamic', 'Pa', '127493')

    # oil_temperature | Offset: 32, Length: 16, Resolution: 0.1, Field Type: NUMBER
    oil_temperature_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    oil_temperature = oil_temperature_raw * 0.1
    publish_field(hass, instance_name, 'oil_temperature', 'Oil temperature', oil_temperature, 'Transmission Parameters, Dynamic', 'K', '127493')
    publish_field(hass, instance_name, 'oil_temperature_celsius', 'Oil temperature Celsius', kelvin_to_celsius(oil_temperature), 'Transmission Parameters, Dynamic', 'C', '127493')
    publish_field(hass, instance_name, 'oil_temperature_fahrenheit', 'Oil temperature Fahrenheit', kelvin_to_fahrenheit(oil_temperature), 'Transmission Parameters, Dynamic', 'F', '127493')

    # discrete_status_1 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    discrete_status_1_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    discrete_status_1 = discrete_status_1_raw * 1
    publish_field(hass, instance_name, 'discrete_status_1', 'Discrete Status 1', discrete_status_1, 'Transmission Parameters, Dynamic', '', '127493')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Transmission Parameters, Dynamic', '', '127493')

def process_pgn_127494(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127494."""
    # inverter_motor_identifier | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    inverter_motor_identifier_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    inverter_motor_identifier = inverter_motor_identifier_raw * 1
    publish_field(hass, instance_name, 'inverter_motor_identifier', 'Inverter/Motor Identifier', inverter_motor_identifier, 'Electric Drive Information', '', '127494')

    # motor_type | Offset: 8, Length: 4, Resolution: 1, Field Type: NUMBER
    motor_type_raw = decode_number((data_raw >> 8) & 0xF, 4)
    motor_type = motor_type_raw * 1
    publish_field(hass, instance_name, 'motor_type', 'Motor Type', motor_type, 'Electric Drive Information', '', '127494')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Electric Drive Information', '', '127494')

    # motor_voltage_rating | Offset: 16, Length: 16, Resolution: 0.1, Field Type: NUMBER
    motor_voltage_rating_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    motor_voltage_rating = motor_voltage_rating_raw * 0.1
    publish_field(hass, instance_name, 'motor_voltage_rating', 'Motor Voltage Rating', motor_voltage_rating, 'Electric Drive Information', 'V', '127494')

    # maximum_continuous_motor_power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    maximum_continuous_motor_power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    maximum_continuous_motor_power = maximum_continuous_motor_power_raw * 1
    publish_field(hass, instance_name, 'maximum_continuous_motor_power', 'Maximum Continuous Motor Power', maximum_continuous_motor_power, 'Electric Drive Information', 'W', '127494')

    # maximum_boost_motor_power | Offset: 64, Length: 32, Resolution: 1, Field Type: NUMBER
    maximum_boost_motor_power_raw = decode_number((data_raw >> 64) & 0xFFFFFFFF, 32)
    maximum_boost_motor_power = maximum_boost_motor_power_raw * 1
    publish_field(hass, instance_name, 'maximum_boost_motor_power', 'Maximum Boost Motor Power', maximum_boost_motor_power, 'Electric Drive Information', 'W', '127494')

    # maximum_motor_temperature_rating | Offset: 96, Length: 16, Resolution: 0.01, Field Type: NUMBER
    maximum_motor_temperature_rating_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    maximum_motor_temperature_rating = maximum_motor_temperature_rating_raw * 0.01
    publish_field(hass, instance_name, 'maximum_motor_temperature_rating', 'Maximum Motor Temperature Rating', maximum_motor_temperature_rating, 'Electric Drive Information', 'K', '127494')
    publish_field(hass, instance_name, 'maximum_motor_temperature_rating_celsius', 'Maximum Motor Temperature Rating Celsius', kelvin_to_celsius(maximum_motor_temperature_rating), 'Electric Drive Information', 'C', '127494')
    publish_field(hass, instance_name, 'maximum_motor_temperature_rating_fahrenheit', 'Maximum Motor Temperature Rating Fahrenheit', kelvin_to_fahrenheit(maximum_motor_temperature_rating), 'Electric Drive Information', 'F', '127494')

    # rated_motor_speed | Offset: 112, Length: 16, Resolution: 0.25, Field Type: NUMBER
    rated_motor_speed_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    rated_motor_speed = rated_motor_speed_raw * 0.25
    publish_field(hass, instance_name, 'rated_motor_speed', 'Rated Motor Speed', rated_motor_speed, 'Electric Drive Information', 'rpm', '127494')

    # maximum_controller_temperature_rating | Offset: 128, Length: 16, Resolution: 0.01, Field Type: NUMBER
    maximum_controller_temperature_rating_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    maximum_controller_temperature_rating = maximum_controller_temperature_rating_raw * 0.01
    publish_field(hass, instance_name, 'maximum_controller_temperature_rating', 'Maximum Controller Temperature Rating', maximum_controller_temperature_rating, 'Electric Drive Information', 'K', '127494')
    publish_field(hass, instance_name, 'maximum_controller_temperature_rating_celsius', 'Maximum Controller Temperature Rating Celsius', kelvin_to_celsius(maximum_controller_temperature_rating), 'Electric Drive Information', 'C', '127494')
    publish_field(hass, instance_name, 'maximum_controller_temperature_rating_fahrenheit', 'Maximum Controller Temperature Rating Fahrenheit', kelvin_to_fahrenheit(maximum_controller_temperature_rating), 'Electric Drive Information', 'F', '127494')

    # motor_shaft_torque_rating | Offset: 144, Length: 16, Resolution: 1, Field Type: NUMBER
    motor_shaft_torque_rating_raw = decode_number((data_raw >> 144) & 0xFFFF, 16)
    motor_shaft_torque_rating = motor_shaft_torque_rating_raw * 1
    publish_field(hass, instance_name, 'motor_shaft_torque_rating', 'Motor Shaft Torque Rating', motor_shaft_torque_rating, 'Electric Drive Information', '', '127494')

    # motor_dc_voltage_derating_threshold | Offset: 160, Length: 16, Resolution: 0.1, Field Type: NUMBER
    motor_dc_voltage_derating_threshold_raw = decode_number((data_raw >> 160) & 0xFFFF, 16)
    motor_dc_voltage_derating_threshold = motor_dc_voltage_derating_threshold_raw * 0.1
    publish_field(hass, instance_name, 'motor_dc_voltage_derating_threshold', 'Motor DC-Voltage Derating Threshold', motor_dc_voltage_derating_threshold, 'Electric Drive Information', 'V', '127494')

    # motor_dc_voltage_cut_off_threshold | Offset: 176, Length: 16, Resolution: 0.1, Field Type: NUMBER
    motor_dc_voltage_cut_off_threshold_raw = decode_number((data_raw >> 176) & 0xFFFF, 16)
    motor_dc_voltage_cut_off_threshold = motor_dc_voltage_cut_off_threshold_raw * 0.1
    publish_field(hass, instance_name, 'motor_dc_voltage_cut_off_threshold', 'Motor DC-Voltage Cut Off Threshold', motor_dc_voltage_cut_off_threshold, 'Electric Drive Information', 'V', '127494')

    # drive_motor_hours | Offset: 192, Length: 32, Resolution: 1, Field Type: TIME
    drive_motor_hours_raw = (data_raw >> 192) & 0xFFFFFFFF
    drive_motor_hours = decode_time(drive_motor_hours_raw * 1)
    publish_field(hass, instance_name, 'drive_motor_hours', 'Drive/Motor Hours', drive_motor_hours, 'Electric Drive Information', 's', '127494')

def process_pgn_127495(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127495."""
    # energy_storage_identifier | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    energy_storage_identifier_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    energy_storage_identifier = energy_storage_identifier_raw * 1
    publish_field(hass, instance_name, 'energy_storage_identifier', 'Energy Storage Identifier', energy_storage_identifier, 'Electric Energy Storage Information', '', '127495')

    # motor_type | Offset: 8, Length: 4, Resolution: 1, Field Type: NUMBER
    motor_type_raw = decode_number((data_raw >> 8) & 0xF, 4)
    motor_type = motor_type_raw * 1
    publish_field(hass, instance_name, 'motor_type', 'Motor Type', motor_type, 'Electric Energy Storage Information', '', '127495')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Electric Energy Storage Information', '', '127495')

    # storage_chemistry_conversion | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    storage_chemistry_conversion_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    storage_chemistry_conversion = storage_chemistry_conversion_raw * 1
    publish_field(hass, instance_name, 'storage_chemistry_conversion', 'Storage Chemistry/Conversion', storage_chemistry_conversion, 'Electric Energy Storage Information', '', '127495')

    # maximum_temperature_derating | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    maximum_temperature_derating_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    maximum_temperature_derating = maximum_temperature_derating_raw * 0.01
    publish_field(hass, instance_name, 'maximum_temperature_derating', 'Maximum Temperature Derating', maximum_temperature_derating, 'Electric Energy Storage Information', 'K', '127495')
    publish_field(hass, instance_name, 'maximum_temperature_derating_celsius', 'Maximum Temperature Derating Celsius', kelvin_to_celsius(maximum_temperature_derating), 'Electric Energy Storage Information', 'C', '127495')
    publish_field(hass, instance_name, 'maximum_temperature_derating_fahrenheit', 'Maximum Temperature Derating Fahrenheit', kelvin_to_fahrenheit(maximum_temperature_derating), 'Electric Energy Storage Information', 'F', '127495')

    # maximum_temperature_shut_off | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    maximum_temperature_shut_off_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    maximum_temperature_shut_off = maximum_temperature_shut_off_raw * 0.01
    publish_field(hass, instance_name, 'maximum_temperature_shut_off', 'Maximum Temperature Shut Off', maximum_temperature_shut_off, 'Electric Energy Storage Information', 'K', '127495')
    publish_field(hass, instance_name, 'maximum_temperature_shut_off_celsius', 'Maximum Temperature Shut Off Celsius', kelvin_to_celsius(maximum_temperature_shut_off), 'Electric Energy Storage Information', 'C', '127495')
    publish_field(hass, instance_name, 'maximum_temperature_shut_off_fahrenheit', 'Maximum Temperature Shut Off Fahrenheit', kelvin_to_fahrenheit(maximum_temperature_shut_off), 'Electric Energy Storage Information', 'F', '127495')

    # minimum_temperature_derating | Offset: 56, Length: 16, Resolution: 0.01, Field Type: NUMBER
    minimum_temperature_derating_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    minimum_temperature_derating = minimum_temperature_derating_raw * 0.01
    publish_field(hass, instance_name, 'minimum_temperature_derating', 'Minimum Temperature Derating', minimum_temperature_derating, 'Electric Energy Storage Information', 'K', '127495')
    publish_field(hass, instance_name, 'minimum_temperature_derating_celsius', 'Minimum Temperature Derating Celsius', kelvin_to_celsius(minimum_temperature_derating), 'Electric Energy Storage Information', 'C', '127495')
    publish_field(hass, instance_name, 'minimum_temperature_derating_fahrenheit', 'Minimum Temperature Derating Fahrenheit', kelvin_to_fahrenheit(minimum_temperature_derating), 'Electric Energy Storage Information', 'F', '127495')

    # minimum_temperature_shut_off | Offset: 72, Length: 16, Resolution: 0.01, Field Type: NUMBER
    minimum_temperature_shut_off_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    minimum_temperature_shut_off = minimum_temperature_shut_off_raw * 0.01
    publish_field(hass, instance_name, 'minimum_temperature_shut_off', 'Minimum Temperature Shut Off', minimum_temperature_shut_off, 'Electric Energy Storage Information', 'K', '127495')
    publish_field(hass, instance_name, 'minimum_temperature_shut_off_celsius', 'Minimum Temperature Shut Off Celsius', kelvin_to_celsius(minimum_temperature_shut_off), 'Electric Energy Storage Information', 'C', '127495')
    publish_field(hass, instance_name, 'minimum_temperature_shut_off_fahrenheit', 'Minimum Temperature Shut Off Fahrenheit', kelvin_to_fahrenheit(minimum_temperature_shut_off), 'Electric Energy Storage Information', 'F', '127495')

    # usable_battery_energy | Offset: 88, Length: 32, Resolution: 1, Field Type: NUMBER
    usable_battery_energy_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    usable_battery_energy = usable_battery_energy_raw * 1
    publish_field(hass, instance_name, 'usable_battery_energy', 'Usable Battery Energy', usable_battery_energy, 'Electric Energy Storage Information', 'kWh', '127495')

    # state_of_health | Offset: 120, Length: 8, Resolution: 1, Field Type: NUMBER
    state_of_health_raw = decode_number((data_raw >> 120) & 0xFF, 8)
    state_of_health = state_of_health_raw * 1
    publish_field(hass, instance_name, 'state_of_health', 'State of Health', state_of_health, 'Electric Energy Storage Information', '', '127495')

    # battery_cycle_counter | Offset: 128, Length: 16, Resolution: 1, Field Type: NUMBER
    battery_cycle_counter_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    battery_cycle_counter = battery_cycle_counter_raw * 1
    publish_field(hass, instance_name, 'battery_cycle_counter', 'Battery Cycle Counter', battery_cycle_counter, 'Electric Energy Storage Information', '', '127495')

    # battery_full_status | Offset: 144, Length: 2, Resolution: 1, Field Type: NUMBER
    battery_full_status_raw = decode_number((data_raw >> 144) & 0x3, 2)
    battery_full_status = battery_full_status_raw * 1
    publish_field(hass, instance_name, 'battery_full_status', 'Battery Full Status', battery_full_status, 'Electric Energy Storage Information', '', '127495')

    # battery_empty_status | Offset: 146, Length: 2, Resolution: 1, Field Type: NUMBER
    battery_empty_status_raw = decode_number((data_raw >> 146) & 0x3, 2)
    battery_empty_status = battery_empty_status_raw * 1
    publish_field(hass, instance_name, 'battery_empty_status', 'Battery Empty Status', battery_empty_status, 'Electric Energy Storage Information', '', '127495')

    # reserved | Offset: 148, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 148) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Electric Energy Storage Information', '', '127495')

    # maximum_charge__soc_ | Offset: 152, Length: 8, Resolution: 1, Field Type: NUMBER
    maximum_charge__soc__raw = decode_number((data_raw >> 152) & 0xFF, 8)
    maximum_charge__soc_ = maximum_charge__soc__raw * 1
    publish_field(hass, instance_name, 'maximum_charge__soc_', 'Maximum Charge (SOC)', maximum_charge__soc_, 'Electric Energy Storage Information', '', '127495')

    # minimum_charge__soc_ | Offset: 160, Length: 8, Resolution: 1, Field Type: NUMBER
    minimum_charge__soc__raw = decode_number((data_raw >> 160) & 0xFF, 8)
    minimum_charge__soc_ = minimum_charge__soc__raw * 1
    publish_field(hass, instance_name, 'minimum_charge__soc_', 'Minimum Charge (SOC)', minimum_charge__soc_, 'Electric Energy Storage Information', '', '127495')

def process_pgn_127496(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127496."""
    # time_to_empty | Offset: 0, Length: 32, Resolution: 0.001, Field Type: TIME
    time_to_empty_raw = (data_raw >> 0) & 0xFFFFFFFF
    time_to_empty = decode_time(time_to_empty_raw * 0.001)
    publish_field(hass, instance_name, 'time_to_empty', 'Time to Empty', time_to_empty, 'Trip Parameters, Vessel', 's', '127496')

    # distance_to_empty | Offset: 32, Length: 32, Resolution: 0.01, Field Type: NUMBER
    distance_to_empty_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    distance_to_empty = distance_to_empty_raw * 0.01
    publish_field(hass, instance_name, 'distance_to_empty', 'Distance to Empty', distance_to_empty, 'Trip Parameters, Vessel', 'm', '127496')

    # estimated_fuel_remaining | Offset: 64, Length: 16, Resolution: 1, Field Type: NUMBER
    estimated_fuel_remaining_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    estimated_fuel_remaining = estimated_fuel_remaining_raw * 1
    publish_field(hass, instance_name, 'estimated_fuel_remaining', 'Estimated Fuel Remaining', estimated_fuel_remaining, 'Trip Parameters, Vessel', 'L', '127496')

    # trip_run_time | Offset: 80, Length: 32, Resolution: 0.001, Field Type: TIME
    trip_run_time_raw = (data_raw >> 80) & 0xFFFFFFFF
    trip_run_time = decode_time(trip_run_time_raw * 0.001)
    publish_field(hass, instance_name, 'trip_run_time', 'Trip Run Time', trip_run_time, 'Trip Parameters, Vessel', 's', '127496')

def process_pgn_127497(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127497."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    instance_raw = (data_raw >> 0) & 0xFF
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Trip Parameters, Engine', '', '127497')

    # trip_fuel_used | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    trip_fuel_used_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    trip_fuel_used = trip_fuel_used_raw * 1
    publish_field(hass, instance_name, 'trip_fuel_used', 'Trip Fuel Used', trip_fuel_used, 'Trip Parameters, Engine', 'L', '127497')

    # fuel_rate__average | Offset: 24, Length: 16, Resolution: 0.1, Field Type: NUMBER
    fuel_rate__average_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if fuel_rate__average_raw & (1 << (16 - 1)):
        fuel_rate__average_raw -= (1 << 16)
    fuel_rate__average = fuel_rate__average_raw * 0.1
    publish_field(hass, instance_name, 'fuel_rate__average', 'Fuel Rate, Average', fuel_rate__average, 'Trip Parameters, Engine', 'L/h', '127497')

    # fuel_rate__economy | Offset: 40, Length: 16, Resolution: 0.1, Field Type: NUMBER
    fuel_rate__economy_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if fuel_rate__economy_raw & (1 << (16 - 1)):
        fuel_rate__economy_raw -= (1 << 16)
    fuel_rate__economy = fuel_rate__economy_raw * 0.1
    publish_field(hass, instance_name, 'fuel_rate__economy', 'Fuel Rate, Economy', fuel_rate__economy, 'Trip Parameters, Engine', 'L/h', '127497')

    # instantaneous_fuel_economy | Offset: 56, Length: 16, Resolution: 0.1, Field Type: NUMBER
    instantaneous_fuel_economy_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    if instantaneous_fuel_economy_raw & (1 << (16 - 1)):
        instantaneous_fuel_economy_raw -= (1 << 16)
    instantaneous_fuel_economy = instantaneous_fuel_economy_raw * 0.1
    publish_field(hass, instance_name, 'instantaneous_fuel_economy', 'Instantaneous Fuel Economy', instantaneous_fuel_economy, 'Trip Parameters, Engine', 'L/h', '127497')

def process_pgn_127498(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127498."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    instance_raw = (data_raw >> 0) & 0xFF
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Engine Parameters, Static', '', '127498')

    # rated_engine_speed | Offset: 8, Length: 16, Resolution: 0.25, Field Type: NUMBER
    rated_engine_speed_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    rated_engine_speed = rated_engine_speed_raw * 0.25
    publish_field(hass, instance_name, 'rated_engine_speed', 'Rated Engine Speed', rated_engine_speed, 'Engine Parameters, Static', 'rpm', '127498')

    # vin | Offset: 24, Length: 136, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # software_id | Offset: 160, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_127500(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127500."""
    # sequence_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sequence_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sequence_id = sequence_id_raw * 1
    publish_field(hass, instance_name, 'sequence_id', 'Sequence ID', sequence_id, 'Load Controller Connection State/Control', '', '127500')

    # connection_id | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    connection_id_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    connection_id = connection_id_raw * 1
    publish_field(hass, instance_name, 'connection_id', 'Connection ID', connection_id, 'Load Controller Connection State/Control', '', '127500')

    # state | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    state_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    state = state_raw * 1
    publish_field(hass, instance_name, 'state', 'State', state, 'Load Controller Connection State/Control', '', '127500')

    # status | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    status_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Load Controller Connection State/Control', '', '127500')

    # operational_status___control | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    operational_status___control_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    operational_status___control = operational_status___control_raw * 1
    publish_field(hass, instance_name, 'operational_status___control', 'Operational Status & Control', operational_status___control, 'Load Controller Connection State/Control', '', '127500')

    # pwm_duty_cycle | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    pwm_duty_cycle_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    pwm_duty_cycle = pwm_duty_cycle_raw * 1
    publish_field(hass, instance_name, 'pwm_duty_cycle', 'PWM Duty Cycle', pwm_duty_cycle, 'Load Controller Connection State/Control', '', '127500')

    # timeon | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    timeon_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    timeon = timeon_raw * 1
    publish_field(hass, instance_name, 'timeon', 'TimeON', timeon, 'Load Controller Connection State/Control', '', '127500')

    # timeoff | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    timeoff_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    timeoff = timeoff_raw * 1
    publish_field(hass, instance_name, 'timeoff', 'TimeOFF', timeoff, 'Load Controller Connection State/Control', '', '127500')

def process_pgn_127501(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127501."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Binary Switch Bank Status', '', '127501')

    # indicator1 | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator1_raw = (data_raw >> 8) & 0x3
    indicator1 = indicator1_raw * 1
    publish_field(hass, instance_name, 'indicator1', 'Indicator1', indicator1, 'Binary Switch Bank Status', '', '127501')

    # indicator2 | Offset: 10, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator2_raw = (data_raw >> 10) & 0x3
    indicator2 = indicator2_raw * 1
    publish_field(hass, instance_name, 'indicator2', 'Indicator2', indicator2, 'Binary Switch Bank Status', '', '127501')

    # indicator3 | Offset: 12, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator3_raw = (data_raw >> 12) & 0x3
    indicator3 = indicator3_raw * 1
    publish_field(hass, instance_name, 'indicator3', 'Indicator3', indicator3, 'Binary Switch Bank Status', '', '127501')

    # indicator4 | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator4_raw = (data_raw >> 14) & 0x3
    indicator4 = indicator4_raw * 1
    publish_field(hass, instance_name, 'indicator4', 'Indicator4', indicator4, 'Binary Switch Bank Status', '', '127501')

    # indicator5 | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator5_raw = (data_raw >> 16) & 0x3
    indicator5 = indicator5_raw * 1
    publish_field(hass, instance_name, 'indicator5', 'Indicator5', indicator5, 'Binary Switch Bank Status', '', '127501')

    # indicator6 | Offset: 18, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator6_raw = (data_raw >> 18) & 0x3
    indicator6 = indicator6_raw * 1
    publish_field(hass, instance_name, 'indicator6', 'Indicator6', indicator6, 'Binary Switch Bank Status', '', '127501')

    # indicator7 | Offset: 20, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator7_raw = (data_raw >> 20) & 0x3
    indicator7 = indicator7_raw * 1
    publish_field(hass, instance_name, 'indicator7', 'Indicator7', indicator7, 'Binary Switch Bank Status', '', '127501')

    # indicator8 | Offset: 22, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator8_raw = (data_raw >> 22) & 0x3
    indicator8 = indicator8_raw * 1
    publish_field(hass, instance_name, 'indicator8', 'Indicator8', indicator8, 'Binary Switch Bank Status', '', '127501')

    # indicator9 | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator9_raw = (data_raw >> 24) & 0x3
    indicator9 = indicator9_raw * 1
    publish_field(hass, instance_name, 'indicator9', 'Indicator9', indicator9, 'Binary Switch Bank Status', '', '127501')

    # indicator10 | Offset: 26, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator10_raw = (data_raw >> 26) & 0x3
    indicator10 = indicator10_raw * 1
    publish_field(hass, instance_name, 'indicator10', 'Indicator10', indicator10, 'Binary Switch Bank Status', '', '127501')

    # indicator11 | Offset: 28, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator11_raw = (data_raw >> 28) & 0x3
    indicator11 = indicator11_raw * 1
    publish_field(hass, instance_name, 'indicator11', 'Indicator11', indicator11, 'Binary Switch Bank Status', '', '127501')

    # indicator12 | Offset: 30, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator12_raw = (data_raw >> 30) & 0x3
    indicator12 = indicator12_raw * 1
    publish_field(hass, instance_name, 'indicator12', 'Indicator12', indicator12, 'Binary Switch Bank Status', '', '127501')

    # indicator13 | Offset: 32, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator13_raw = (data_raw >> 32) & 0x3
    indicator13 = indicator13_raw * 1
    publish_field(hass, instance_name, 'indicator13', 'Indicator13', indicator13, 'Binary Switch Bank Status', '', '127501')

    # indicator14 | Offset: 34, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator14_raw = (data_raw >> 34) & 0x3
    indicator14 = indicator14_raw * 1
    publish_field(hass, instance_name, 'indicator14', 'Indicator14', indicator14, 'Binary Switch Bank Status', '', '127501')

    # indicator15 | Offset: 36, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator15_raw = (data_raw >> 36) & 0x3
    indicator15 = indicator15_raw * 1
    publish_field(hass, instance_name, 'indicator15', 'Indicator15', indicator15, 'Binary Switch Bank Status', '', '127501')

    # indicator16 | Offset: 38, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator16_raw = (data_raw >> 38) & 0x3
    indicator16 = indicator16_raw * 1
    publish_field(hass, instance_name, 'indicator16', 'Indicator16', indicator16, 'Binary Switch Bank Status', '', '127501')

    # indicator17 | Offset: 40, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator17_raw = (data_raw >> 40) & 0x3
    indicator17 = indicator17_raw * 1
    publish_field(hass, instance_name, 'indicator17', 'Indicator17', indicator17, 'Binary Switch Bank Status', '', '127501')

    # indicator18 | Offset: 42, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator18_raw = (data_raw >> 42) & 0x3
    indicator18 = indicator18_raw * 1
    publish_field(hass, instance_name, 'indicator18', 'Indicator18', indicator18, 'Binary Switch Bank Status', '', '127501')

    # indicator19 | Offset: 44, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator19_raw = (data_raw >> 44) & 0x3
    indicator19 = indicator19_raw * 1
    publish_field(hass, instance_name, 'indicator19', 'Indicator19', indicator19, 'Binary Switch Bank Status', '', '127501')

    # indicator20 | Offset: 46, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator20_raw = (data_raw >> 46) & 0x3
    indicator20 = indicator20_raw * 1
    publish_field(hass, instance_name, 'indicator20', 'Indicator20', indicator20, 'Binary Switch Bank Status', '', '127501')

    # indicator21 | Offset: 48, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator21_raw = (data_raw >> 48) & 0x3
    indicator21 = indicator21_raw * 1
    publish_field(hass, instance_name, 'indicator21', 'Indicator21', indicator21, 'Binary Switch Bank Status', '', '127501')

    # indicator22 | Offset: 50, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator22_raw = (data_raw >> 50) & 0x3
    indicator22 = indicator22_raw * 1
    publish_field(hass, instance_name, 'indicator22', 'Indicator22', indicator22, 'Binary Switch Bank Status', '', '127501')

    # indicator23 | Offset: 52, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator23_raw = (data_raw >> 52) & 0x3
    indicator23 = indicator23_raw * 1
    publish_field(hass, instance_name, 'indicator23', 'Indicator23', indicator23, 'Binary Switch Bank Status', '', '127501')

    # indicator24 | Offset: 54, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator24_raw = (data_raw >> 54) & 0x3
    indicator24 = indicator24_raw * 1
    publish_field(hass, instance_name, 'indicator24', 'Indicator24', indicator24, 'Binary Switch Bank Status', '', '127501')

    # indicator25 | Offset: 56, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator25_raw = (data_raw >> 56) & 0x3
    indicator25 = indicator25_raw * 1
    publish_field(hass, instance_name, 'indicator25', 'Indicator25', indicator25, 'Binary Switch Bank Status', '', '127501')

    # indicator26 | Offset: 58, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator26_raw = (data_raw >> 58) & 0x3
    indicator26 = indicator26_raw * 1
    publish_field(hass, instance_name, 'indicator26', 'Indicator26', indicator26, 'Binary Switch Bank Status', '', '127501')

    # indicator27 | Offset: 60, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator27_raw = (data_raw >> 60) & 0x3
    indicator27 = indicator27_raw * 1
    publish_field(hass, instance_name, 'indicator27', 'Indicator27', indicator27, 'Binary Switch Bank Status', '', '127501')

    # indicator28 | Offset: 62, Length: 2, Resolution: 1, Field Type: LOOKUP
    indicator28_raw = (data_raw >> 62) & 0x3
    indicator28 = indicator28_raw * 1
    publish_field(hass, instance_name, 'indicator28', 'Indicator28', indicator28, 'Binary Switch Bank Status', '', '127501')

def process_pgn_127502(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127502."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Switch Bank Control', '', '127502')

    # switch1 | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch1_raw = (data_raw >> 8) & 0x3
    switch1 = switch1_raw * 1
    publish_field(hass, instance_name, 'switch1', 'Switch1', switch1, 'Switch Bank Control', '', '127502')

    # switch2 | Offset: 10, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch2_raw = (data_raw >> 10) & 0x3
    switch2 = switch2_raw * 1
    publish_field(hass, instance_name, 'switch2', 'Switch2', switch2, 'Switch Bank Control', '', '127502')

    # switch3 | Offset: 12, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch3_raw = (data_raw >> 12) & 0x3
    switch3 = switch3_raw * 1
    publish_field(hass, instance_name, 'switch3', 'Switch3', switch3, 'Switch Bank Control', '', '127502')

    # switch4 | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch4_raw = (data_raw >> 14) & 0x3
    switch4 = switch4_raw * 1
    publish_field(hass, instance_name, 'switch4', 'Switch4', switch4, 'Switch Bank Control', '', '127502')

    # switch5 | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch5_raw = (data_raw >> 16) & 0x3
    switch5 = switch5_raw * 1
    publish_field(hass, instance_name, 'switch5', 'Switch5', switch5, 'Switch Bank Control', '', '127502')

    # switch6 | Offset: 18, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch6_raw = (data_raw >> 18) & 0x3
    switch6 = switch6_raw * 1
    publish_field(hass, instance_name, 'switch6', 'Switch6', switch6, 'Switch Bank Control', '', '127502')

    # switch7 | Offset: 20, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch7_raw = (data_raw >> 20) & 0x3
    switch7 = switch7_raw * 1
    publish_field(hass, instance_name, 'switch7', 'Switch7', switch7, 'Switch Bank Control', '', '127502')

    # switch8 | Offset: 22, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch8_raw = (data_raw >> 22) & 0x3
    switch8 = switch8_raw * 1
    publish_field(hass, instance_name, 'switch8', 'Switch8', switch8, 'Switch Bank Control', '', '127502')

    # switch9 | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch9_raw = (data_raw >> 24) & 0x3
    switch9 = switch9_raw * 1
    publish_field(hass, instance_name, 'switch9', 'Switch9', switch9, 'Switch Bank Control', '', '127502')

    # switch10 | Offset: 26, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch10_raw = (data_raw >> 26) & 0x3
    switch10 = switch10_raw * 1
    publish_field(hass, instance_name, 'switch10', 'Switch10', switch10, 'Switch Bank Control', '', '127502')

    # switch11 | Offset: 28, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch11_raw = (data_raw >> 28) & 0x3
    switch11 = switch11_raw * 1
    publish_field(hass, instance_name, 'switch11', 'Switch11', switch11, 'Switch Bank Control', '', '127502')

    # switch12 | Offset: 30, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch12_raw = (data_raw >> 30) & 0x3
    switch12 = switch12_raw * 1
    publish_field(hass, instance_name, 'switch12', 'Switch12', switch12, 'Switch Bank Control', '', '127502')

    # switch13 | Offset: 32, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch13_raw = (data_raw >> 32) & 0x3
    switch13 = switch13_raw * 1
    publish_field(hass, instance_name, 'switch13', 'Switch13', switch13, 'Switch Bank Control', '', '127502')

    # switch14 | Offset: 34, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch14_raw = (data_raw >> 34) & 0x3
    switch14 = switch14_raw * 1
    publish_field(hass, instance_name, 'switch14', 'Switch14', switch14, 'Switch Bank Control', '', '127502')

    # switch15 | Offset: 36, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch15_raw = (data_raw >> 36) & 0x3
    switch15 = switch15_raw * 1
    publish_field(hass, instance_name, 'switch15', 'Switch15', switch15, 'Switch Bank Control', '', '127502')

    # switch16 | Offset: 38, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch16_raw = (data_raw >> 38) & 0x3
    switch16 = switch16_raw * 1
    publish_field(hass, instance_name, 'switch16', 'Switch16', switch16, 'Switch Bank Control', '', '127502')

    # switch17 | Offset: 40, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch17_raw = (data_raw >> 40) & 0x3
    switch17 = switch17_raw * 1
    publish_field(hass, instance_name, 'switch17', 'Switch17', switch17, 'Switch Bank Control', '', '127502')

    # switch18 | Offset: 42, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch18_raw = (data_raw >> 42) & 0x3
    switch18 = switch18_raw * 1
    publish_field(hass, instance_name, 'switch18', 'Switch18', switch18, 'Switch Bank Control', '', '127502')

    # switch19 | Offset: 44, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch19_raw = (data_raw >> 44) & 0x3
    switch19 = switch19_raw * 1
    publish_field(hass, instance_name, 'switch19', 'Switch19', switch19, 'Switch Bank Control', '', '127502')

    # switch20 | Offset: 46, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch20_raw = (data_raw >> 46) & 0x3
    switch20 = switch20_raw * 1
    publish_field(hass, instance_name, 'switch20', 'Switch20', switch20, 'Switch Bank Control', '', '127502')

    # switch21 | Offset: 48, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch21_raw = (data_raw >> 48) & 0x3
    switch21 = switch21_raw * 1
    publish_field(hass, instance_name, 'switch21', 'Switch21', switch21, 'Switch Bank Control', '', '127502')

    # switch22 | Offset: 50, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch22_raw = (data_raw >> 50) & 0x3
    switch22 = switch22_raw * 1
    publish_field(hass, instance_name, 'switch22', 'Switch22', switch22, 'Switch Bank Control', '', '127502')

    # switch23 | Offset: 52, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch23_raw = (data_raw >> 52) & 0x3
    switch23 = switch23_raw * 1
    publish_field(hass, instance_name, 'switch23', 'Switch23', switch23, 'Switch Bank Control', '', '127502')

    # switch24 | Offset: 54, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch24_raw = (data_raw >> 54) & 0x3
    switch24 = switch24_raw * 1
    publish_field(hass, instance_name, 'switch24', 'Switch24', switch24, 'Switch Bank Control', '', '127502')

    # switch25 | Offset: 56, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch25_raw = (data_raw >> 56) & 0x3
    switch25 = switch25_raw * 1
    publish_field(hass, instance_name, 'switch25', 'Switch25', switch25, 'Switch Bank Control', '', '127502')

    # switch26 | Offset: 58, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch26_raw = (data_raw >> 58) & 0x3
    switch26 = switch26_raw * 1
    publish_field(hass, instance_name, 'switch26', 'Switch26', switch26, 'Switch Bank Control', '', '127502')

    # switch27 | Offset: 60, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch27_raw = (data_raw >> 60) & 0x3
    switch27 = switch27_raw * 1
    publish_field(hass, instance_name, 'switch27', 'Switch27', switch27, 'Switch Bank Control', '', '127502')

    # switch28 | Offset: 62, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch28_raw = (data_raw >> 62) & 0x3
    switch28 = switch28_raw * 1
    publish_field(hass, instance_name, 'switch28', 'Switch28', switch28, 'Switch Bank Control', '', '127502')

def process_pgn_127503(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127503."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'AC Input Status', '', '127503')

    # number_of_lines | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_lines_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    number_of_lines = number_of_lines_raw * 1
    publish_field(hass, instance_name, 'number_of_lines', 'Number of Lines', number_of_lines, 'AC Input Status', '', '127503')

    # line | Offset: 16, Length: 2, Resolution: 1, Field Type: NUMBER
    line_raw = decode_number((data_raw >> 16) & 0x3, 2)
    line = line_raw * 1
    publish_field(hass, instance_name, 'line', 'Line', line, 'AC Input Status', '', '127503')

    # acceptability | Offset: 18, Length: 2, Resolution: 1, Field Type: LOOKUP
    acceptability_raw = (data_raw >> 18) & 0x3
    acceptability = acceptability_raw * 1
    publish_field(hass, instance_name, 'acceptability', 'Acceptability', acceptability, 'AC Input Status', '', '127503')

    # reserved | Offset: 20, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 20) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AC Input Status', '', '127503')

    # voltage | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    voltage_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    voltage = voltage_raw * 0.01
    publish_field(hass, instance_name, 'voltage', 'Voltage', voltage, 'AC Input Status', 'V', '127503')

    # current | Offset: 40, Length: 16, Resolution: 0.1, Field Type: NUMBER
    current_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    current = current_raw * 0.1
    publish_field(hass, instance_name, 'current', 'Current', current, 'AC Input Status', 'A', '127503')

    # frequency | Offset: 56, Length: 16, Resolution: 0.01, Field Type: NUMBER
    frequency_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    frequency = frequency_raw * 0.01
    publish_field(hass, instance_name, 'frequency', 'Frequency', frequency, 'AC Input Status', 'Hz', '127503')

    # breaker_size | Offset: 72, Length: 16, Resolution: 0.1, Field Type: NUMBER
    breaker_size_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    breaker_size = breaker_size_raw * 0.1
    publish_field(hass, instance_name, 'breaker_size', 'Breaker Size', breaker_size, 'AC Input Status', 'A', '127503')

    # real_power | Offset: 88, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'AC Input Status', 'W', '127503')

    # reactive_power | Offset: 120, Length: 32, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 120) & 0xFFFFFFFF, 32)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'AC Input Status', 'VAR', '127503')

    # power_factor | Offset: 152, Length: 8, Resolution: 0.01, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 152) & 0xFF, 8)
    power_factor = power_factor_raw * 0.01
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'AC Input Status', 'Cos Phi', '127503')

def process_pgn_127504(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127504."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'AC Output Status', '', '127504')

    # number_of_lines | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_lines_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    number_of_lines = number_of_lines_raw * 1
    publish_field(hass, instance_name, 'number_of_lines', 'Number of Lines', number_of_lines, 'AC Output Status', '', '127504')

    # line | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    line_raw = (data_raw >> 16) & 0x3
    line = line_raw * 1
    publish_field(hass, instance_name, 'line', 'Line', line, 'AC Output Status', '', '127504')

    # waveform | Offset: 18, Length: 3, Resolution: 1, Field Type: LOOKUP
    waveform_raw = (data_raw >> 18) & 0x7
    waveform = waveform_raw * 1
    publish_field(hass, instance_name, 'waveform', 'Waveform', waveform, 'AC Output Status', '', '127504')

    # reserved | Offset: 21, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 21) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AC Output Status', '', '127504')

    # voltage | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    voltage_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    voltage = voltage_raw * 0.01
    publish_field(hass, instance_name, 'voltage', 'Voltage', voltage, 'AC Output Status', 'V', '127504')

    # current | Offset: 40, Length: 16, Resolution: 0.1, Field Type: NUMBER
    current_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    current = current_raw * 0.1
    publish_field(hass, instance_name, 'current', 'Current', current, 'AC Output Status', 'A', '127504')

    # frequency | Offset: 56, Length: 16, Resolution: 0.01, Field Type: NUMBER
    frequency_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    frequency = frequency_raw * 0.01
    publish_field(hass, instance_name, 'frequency', 'Frequency', frequency, 'AC Output Status', 'Hz', '127504')

    # breaker_size | Offset: 72, Length: 16, Resolution: 0.1, Field Type: NUMBER
    breaker_size_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    breaker_size = breaker_size_raw * 0.1
    publish_field(hass, instance_name, 'breaker_size', 'Breaker Size', breaker_size, 'AC Output Status', 'A', '127504')

    # real_power | Offset: 88, Length: 32, Resolution: 1, Field Type: NUMBER
    real_power_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    real_power = real_power_raw * 1
    publish_field(hass, instance_name, 'real_power', 'Real Power', real_power, 'AC Output Status', 'W', '127504')

    # reactive_power | Offset: 120, Length: 32, Resolution: 1, Field Type: NUMBER
    reactive_power_raw = decode_number((data_raw >> 120) & 0xFFFFFFFF, 32)
    reactive_power = reactive_power_raw * 1
    publish_field(hass, instance_name, 'reactive_power', 'Reactive Power', reactive_power, 'AC Output Status', 'VAR', '127504')

    # power_factor | Offset: 152, Length: 8, Resolution: 0.01, Field Type: NUMBER
    power_factor_raw = decode_number((data_raw >> 152) & 0xFF, 8)
    power_factor = power_factor_raw * 0.01
    publish_field(hass, instance_name, 'power_factor', 'Power factor', power_factor, 'AC Output Status', 'Cos Phi', '127504')

def process_pgn_127505(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127505."""
    # instance | Offset: 0, Length: 4, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xF, 4)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Fluid Level', '', '127505')

    # type | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    type_raw = (data_raw >> 4) & 0xF
    type = type_raw * 1
    publish_field(hass, instance_name, 'type', 'Type', type, 'Fluid Level', '', '127505')

    # level | Offset: 8, Length: 16, Resolution: 0.004, Field Type: NUMBER
    level_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    if level_raw & (1 << (16 - 1)):
        level_raw -= (1 << 16)
    level = level_raw * 0.004
    publish_field(hass, instance_name, 'level', 'Level', level, 'Fluid Level', '%', '127505')

    # capacity | Offset: 24, Length: 32, Resolution: 0.1, Field Type: NUMBER
    capacity_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    capacity = capacity_raw * 0.1
    publish_field(hass, instance_name, 'capacity', 'Capacity', capacity, 'Fluid Level', 'L', '127505')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fluid Level', '', '127505')

def process_pgn_127506(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127506."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'DC Detailed Status', '', '127506')

    # instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'DC Detailed Status', '', '127506')

    # dc_type | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    dc_type_raw = (data_raw >> 16) & 0xFF
    dc_type = dc_type_raw * 1
    publish_field(hass, instance_name, 'dc_type', 'DC Type', dc_type, 'DC Detailed Status', '', '127506')

    # state_of_charge | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    state_of_charge_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    state_of_charge = state_of_charge_raw * 1
    publish_field(hass, instance_name, 'state_of_charge', 'State of Charge', state_of_charge, 'DC Detailed Status', '', '127506')

    # state_of_health | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    state_of_health_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    state_of_health = state_of_health_raw * 1
    publish_field(hass, instance_name, 'state_of_health', 'State of Health', state_of_health, 'DC Detailed Status', '', '127506')

    # time_remaining | Offset: 40, Length: 16, Resolution: 60, Field Type: TIME
    time_remaining_raw = (data_raw >> 40) & 0xFFFF
    time_remaining = decode_time(time_remaining_raw * 60)
    publish_field(hass, instance_name, 'time_remaining', 'Time Remaining', time_remaining, 'DC Detailed Status', 's', '127506')

    # ripple_voltage | Offset: 56, Length: 16, Resolution: 0.01, Field Type: NUMBER
    ripple_voltage_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    ripple_voltage = ripple_voltage_raw * 0.01
    publish_field(hass, instance_name, 'ripple_voltage', 'Ripple Voltage', ripple_voltage, 'DC Detailed Status', 'V', '127506')

    # remaining_capacity | Offset: 72, Length: 16, Resolution: 1, Field Type: NUMBER
    remaining_capacity_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    remaining_capacity = remaining_capacity_raw * 1
    publish_field(hass, instance_name, 'remaining_capacity', 'Remaining capacity', remaining_capacity, 'DC Detailed Status', 'Ah', '127506')

def process_pgn_127507(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127507."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Charger Status', '', '127507')

    # battery_instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    battery_instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    battery_instance = battery_instance_raw * 1
    publish_field(hass, instance_name, 'battery_instance', 'Battery Instance', battery_instance, 'Charger Status', '', '127507')

    # operating_state | Offset: 16, Length: 4, Resolution: 1, Field Type: LOOKUP
    operating_state_raw = (data_raw >> 16) & 0xF
    operating_state = operating_state_raw * 1
    publish_field(hass, instance_name, 'operating_state', 'Operating State', operating_state, 'Charger Status', '', '127507')

    # charge_mode | Offset: 20, Length: 4, Resolution: 1, Field Type: LOOKUP
    charge_mode_raw = (data_raw >> 20) & 0xF
    charge_mode = charge_mode_raw * 1
    publish_field(hass, instance_name, 'charge_mode', 'Charge Mode', charge_mode, 'Charger Status', '', '127507')

    # enabled | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    enabled_raw = (data_raw >> 24) & 0x3
    enabled = enabled_raw * 1
    publish_field(hass, instance_name, 'enabled', 'Enabled', enabled, 'Charger Status', '', '127507')

    # equalization_pending | Offset: 26, Length: 2, Resolution: 1, Field Type: LOOKUP
    equalization_pending_raw = (data_raw >> 26) & 0x3
    equalization_pending = equalization_pending_raw * 1
    publish_field(hass, instance_name, 'equalization_pending', 'Equalization Pending', equalization_pending, 'Charger Status', '', '127507')

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Charger Status', '', '127507')

    # equalization_time_remaining | Offset: 32, Length: 16, Resolution: 60, Field Type: TIME
    equalization_time_remaining_raw = (data_raw >> 32) & 0xFFFF
    equalization_time_remaining = decode_time(equalization_time_remaining_raw * 60)
    publish_field(hass, instance_name, 'equalization_time_remaining', 'Equalization Time Remaining', equalization_time_remaining, 'Charger Status', 's', '127507')

def process_pgn_127508(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127508."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Battery Status', '', '127508')

    # voltage | Offset: 8, Length: 16, Resolution: 0.01, Field Type: NUMBER
    voltage_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    voltage = voltage_raw * 0.01
    publish_field(hass, instance_name, 'voltage', 'Voltage', voltage, 'Battery Status', 'V', '127508')

    # current | Offset: 24, Length: 16, Resolution: 0.1, Field Type: NUMBER
    current_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if current_raw & (1 << (16 - 1)):
        current_raw -= (1 << 16)
    current = current_raw * 0.1
    publish_field(hass, instance_name, 'current', 'Current', current, 'Battery Status', 'A', '127508')

    # temperature | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    temperature_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    temperature = temperature_raw * 0.01
    publish_field(hass, instance_name, 'temperature', 'Temperature', temperature, 'Battery Status', 'K', '127508')
    publish_field(hass, instance_name, 'temperature_celsius', 'Temperature Celsius', kelvin_to_celsius(temperature), 'Battery Status', 'C', '127508')
    publish_field(hass, instance_name, 'temperature_fahrenheit', 'Temperature Fahrenheit', kelvin_to_fahrenheit(temperature), 'Battery Status', 'F', '127508')

    # sid | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Battery Status', '', '127508')

def process_pgn_127509(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127509."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Inverter Status', '', '127509')

    # ac_instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    ac_instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    ac_instance = ac_instance_raw * 1
    publish_field(hass, instance_name, 'ac_instance', 'AC Instance', ac_instance, 'Inverter Status', '', '127509')

    # dc_instance | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    dc_instance_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    dc_instance = dc_instance_raw * 1
    publish_field(hass, instance_name, 'dc_instance', 'DC Instance', dc_instance, 'Inverter Status', '', '127509')

    # operating_state | Offset: 24, Length: 4, Resolution: 1, Field Type: LOOKUP
    operating_state_raw = (data_raw >> 24) & 0xF
    operating_state = operating_state_raw * 1
    publish_field(hass, instance_name, 'operating_state', 'Operating State', operating_state, 'Inverter Status', '', '127509')

    # inverter_enable | Offset: 28, Length: 2, Resolution: 1, Field Type: LOOKUP
    inverter_enable_raw = (data_raw >> 28) & 0x3
    inverter_enable = inverter_enable_raw * 1
    publish_field(hass, instance_name, 'inverter_enable', 'Inverter Enable', inverter_enable, 'Inverter Status', '', '127509')

    # reserved | Offset: 30, Length: 34, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 30) & 0x3FFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Inverter Status', '', '127509')

def process_pgn_127510(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127510."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Charger Configuration Status', '', '127510')

    # battery_instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    battery_instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    battery_instance = battery_instance_raw * 1
    publish_field(hass, instance_name, 'battery_instance', 'Battery Instance', battery_instance, 'Charger Configuration Status', '', '127510')

    # charger_enable_disable | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    charger_enable_disable_raw = (data_raw >> 16) & 0x3
    charger_enable_disable = charger_enable_disable_raw * 1
    publish_field(hass, instance_name, 'charger_enable_disable', 'Charger Enable/Disable', charger_enable_disable, 'Charger Configuration Status', '', '127510')

    # reserved | Offset: 18, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 18) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Charger Configuration Status', '', '127510')

    # charge_current_limit | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    charge_current_limit_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    charge_current_limit = charge_current_limit_raw * 1
    publish_field(hass, instance_name, 'charge_current_limit', 'Charge Current Limit', charge_current_limit, 'Charger Configuration Status', '%', '127510')

    # charging_algorithm | Offset: 32, Length: 4, Resolution: 1, Field Type: LOOKUP
    charging_algorithm_raw = (data_raw >> 32) & 0xF
    charging_algorithm = charging_algorithm_raw * 1
    publish_field(hass, instance_name, 'charging_algorithm', 'Charging Algorithm', charging_algorithm, 'Charger Configuration Status', '', '127510')

    # charger_mode | Offset: 36, Length: 4, Resolution: 1, Field Type: LOOKUP
    charger_mode_raw = (data_raw >> 36) & 0xF
    charger_mode = charger_mode_raw * 1
    publish_field(hass, instance_name, 'charger_mode', 'Charger Mode', charger_mode, 'Charger Configuration Status', '', '127510')

    # estimated_temperature | Offset: 40, Length: 4, Resolution: 1, Field Type: LOOKUP
    estimated_temperature_raw = (data_raw >> 40) & 0xF
    estimated_temperature = estimated_temperature_raw * 1
    publish_field(hass, instance_name, 'estimated_temperature', 'Estimated Temperature', estimated_temperature, 'Charger Configuration Status', '', '127510')

    # equalize_one_time_enable_disable | Offset: 44, Length: 2, Resolution: 1, Field Type: LOOKUP
    equalize_one_time_enable_disable_raw = (data_raw >> 44) & 0x3
    equalize_one_time_enable_disable = equalize_one_time_enable_disable_raw * 1
    publish_field(hass, instance_name, 'equalize_one_time_enable_disable', 'Equalize One Time Enable/Disable', equalize_one_time_enable_disable, 'Charger Configuration Status', '', '127510')

    # over_charge_enable_disable | Offset: 46, Length: 2, Resolution: 1, Field Type: LOOKUP
    over_charge_enable_disable_raw = (data_raw >> 46) & 0x3
    over_charge_enable_disable = over_charge_enable_disable_raw * 1
    publish_field(hass, instance_name, 'over_charge_enable_disable', 'Over Charge Enable/Disable', over_charge_enable_disable, 'Charger Configuration Status', '', '127510')

    # equalize_time | Offset: 48, Length: 16, Resolution: 60, Field Type: TIME
    equalize_time_raw = (data_raw >> 48) & 0xFFFF
    equalize_time = decode_time(equalize_time_raw * 60)
    publish_field(hass, instance_name, 'equalize_time', 'Equalize Time', equalize_time, 'Charger Configuration Status', 's', '127510')

def process_pgn_127511(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127511."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Inverter Configuration Status', '', '127511')

    # ac_instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    ac_instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    ac_instance = ac_instance_raw * 1
    publish_field(hass, instance_name, 'ac_instance', 'AC Instance', ac_instance, 'Inverter Configuration Status', '', '127511')

    # dc_instance | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    dc_instance_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    dc_instance = dc_instance_raw * 1
    publish_field(hass, instance_name, 'dc_instance', 'DC Instance', dc_instance, 'Inverter Configuration Status', '', '127511')

    # inverter_enable_disable | Offset: 24, Length: 2, Resolution: 1, Field Type: NUMBER
    inverter_enable_disable_raw = decode_number((data_raw >> 24) & 0x3, 2)
    inverter_enable_disable = inverter_enable_disable_raw * 1
    publish_field(hass, instance_name, 'inverter_enable_disable', 'Inverter Enable/Disable', inverter_enable_disable, 'Inverter Configuration Status', '', '127511')

    # reserved | Offset: 26, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 26) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Inverter Configuration Status', '', '127511')

    # inverter_mode | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    inverter_mode_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    inverter_mode = inverter_mode_raw * 1
    publish_field(hass, instance_name, 'inverter_mode', 'Inverter Mode', inverter_mode, 'Inverter Configuration Status', '', '127511')

    # load_sense_enable_disable | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    load_sense_enable_disable_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    load_sense_enable_disable = load_sense_enable_disable_raw * 1
    publish_field(hass, instance_name, 'load_sense_enable_disable', 'Load Sense Enable/Disable', load_sense_enable_disable, 'Inverter Configuration Status', '', '127511')

    # load_sense_power_threshold | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    load_sense_power_threshold_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    load_sense_power_threshold = load_sense_power_threshold_raw * 1
    publish_field(hass, instance_name, 'load_sense_power_threshold', 'Load Sense Power Threshold', load_sense_power_threshold, 'Inverter Configuration Status', '', '127511')

    # load_sense_interval | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    load_sense_interval_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    load_sense_interval = load_sense_interval_raw * 1
    publish_field(hass, instance_name, 'load_sense_interval', 'Load Sense Interval', load_sense_interval, 'Inverter Configuration Status', '', '127511')

def process_pgn_127512(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127512."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'AGS Configuration Status', '', '127512')

    # generator_instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    generator_instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    generator_instance = generator_instance_raw * 1
    publish_field(hass, instance_name, 'generator_instance', 'Generator Instance', generator_instance, 'AGS Configuration Status', '', '127512')

    # ags_mode | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    ags_mode_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    ags_mode = ags_mode_raw * 1
    publish_field(hass, instance_name, 'ags_mode', 'AGS Mode', ags_mode, 'AGS Configuration Status', '', '127512')

    # reserved | Offset: 24, Length: 40, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 24) & 0xFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AGS Configuration Status', '', '127512')

def process_pgn_127513(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127513."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Battery Configuration Status', '', '127513')

    # battery_type | Offset: 8, Length: 4, Resolution: 1, Field Type: LOOKUP
    battery_type_raw = (data_raw >> 8) & 0xF
    battery_type = battery_type_raw * 1
    publish_field(hass, instance_name, 'battery_type', 'Battery Type', battery_type, 'Battery Configuration Status', '', '127513')

    # supports_equalization | Offset: 12, Length: 2, Resolution: 1, Field Type: LOOKUP
    supports_equalization_raw = (data_raw >> 12) & 0x3
    supports_equalization = supports_equalization_raw * 1
    publish_field(hass, instance_name, 'supports_equalization', 'Supports Equalization', supports_equalization, 'Battery Configuration Status', '', '127513')

    # reserved | Offset: 14, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 14) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Battery Configuration Status', '', '127513')

    # nominal_voltage | Offset: 16, Length: 4, Resolution: 1, Field Type: LOOKUP
    nominal_voltage_raw = (data_raw >> 16) & 0xF
    nominal_voltage = nominal_voltage_raw * 1
    publish_field(hass, instance_name, 'nominal_voltage', 'Nominal Voltage', nominal_voltage, 'Battery Configuration Status', '', '127513')

    # chemistry | Offset: 20, Length: 4, Resolution: 1, Field Type: LOOKUP
    chemistry_raw = (data_raw >> 20) & 0xF
    chemistry = chemistry_raw * 1
    publish_field(hass, instance_name, 'chemistry', 'Chemistry', chemistry, 'Battery Configuration Status', '', '127513')

    # capacity | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    capacity_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    capacity = capacity_raw * 1
    publish_field(hass, instance_name, 'capacity', 'Capacity', capacity, 'Battery Configuration Status', 'Ah', '127513')

    # temperature_coefficient | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    temperature_coefficient_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    if temperature_coefficient_raw & (1 << (8 - 1)):
        temperature_coefficient_raw -= (1 << 8)
    temperature_coefficient = temperature_coefficient_raw * 1
    publish_field(hass, instance_name, 'temperature_coefficient', 'Temperature Coefficient', temperature_coefficient, 'Battery Configuration Status', '%', '127513')

    # peukert_exponent | Offset: 48, Length: 8, Resolution: 0.002, Field Type: NUMBER
    peukert_exponent_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    peukert_exponent = peukert_exponent_raw * 0.002
    publish_field(hass, instance_name, 'peukert_exponent', 'Peukert Exponent', peukert_exponent, 'Battery Configuration Status', '', '127513')

    # charge_efficiency_factor | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    charge_efficiency_factor_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    if charge_efficiency_factor_raw & (1 << (8 - 1)):
        charge_efficiency_factor_raw -= (1 << 8)
    charge_efficiency_factor = charge_efficiency_factor_raw * 1
    publish_field(hass, instance_name, 'charge_efficiency_factor', 'Charge Efficiency Factor', charge_efficiency_factor, 'Battery Configuration Status', '%', '127513')

def process_pgn_127514(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127514."""
    # instance | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'AGS Status', '', '127514')

    # generator_instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    generator_instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    generator_instance = generator_instance_raw * 1
    publish_field(hass, instance_name, 'generator_instance', 'Generator Instance', generator_instance, 'AGS Status', '', '127514')

    # ags_operating_state | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    ags_operating_state_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    ags_operating_state = ags_operating_state_raw * 1
    publish_field(hass, instance_name, 'ags_operating_state', 'AGS Operating State', ags_operating_state, 'AGS Status', '', '127514')

    # generator_state | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    generator_state_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    generator_state = generator_state_raw * 1
    publish_field(hass, instance_name, 'generator_state', 'Generator State', generator_state, 'AGS Status', '', '127514')

    # generator_on_reason | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    generator_on_reason_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    generator_on_reason = generator_on_reason_raw * 1
    publish_field(hass, instance_name, 'generator_on_reason', 'Generator On Reason', generator_on_reason, 'AGS Status', '', '127514')

    # generator_off_reason | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    generator_off_reason_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    generator_off_reason = generator_off_reason_raw * 1
    publish_field(hass, instance_name, 'generator_off_reason', 'Generator Off Reason', generator_off_reason, 'AGS Status', '', '127514')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AGS Status', '', '127514')

def process_pgn_127744(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127744."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'AC Power / Current - Phase A', '', '127744')

    # connection_number | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    connection_number_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    connection_number = connection_number_raw * 1
    publish_field(hass, instance_name, 'connection_number', 'Connection Number', connection_number, 'AC Power / Current - Phase A', '', '127744')

    # ac_rms_current | Offset: 16, Length: 16, Resolution: 0.1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 0.1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'AC Power / Current - Phase A', 'A', '127744')

    # power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if power_raw & (1 << (32 - 1)):
        power_raw -= (1 << 32)
    power = power_raw * 1
    publish_field(hass, instance_name, 'power', 'Power', power, 'AC Power / Current - Phase A', 'W', '127744')

def process_pgn_127745(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127745."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'AC Power / Current - Phase B', '', '127745')

    # connection_number | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    connection_number_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    connection_number = connection_number_raw * 1
    publish_field(hass, instance_name, 'connection_number', 'Connection Number', connection_number, 'AC Power / Current - Phase B', '', '127745')

    # ac_rms_current | Offset: 16, Length: 16, Resolution: 0.1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 0.1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'AC Power / Current - Phase B', 'A', '127745')

    # power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if power_raw & (1 << (32 - 1)):
        power_raw -= (1 << 32)
    power = power_raw * 1
    publish_field(hass, instance_name, 'power', 'Power', power, 'AC Power / Current - Phase B', 'W', '127745')

def process_pgn_127746(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127746."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'AC Power / Current - Phase C', '', '127746')

    # connection_number | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    connection_number_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    connection_number = connection_number_raw * 1
    publish_field(hass, instance_name, 'connection_number', 'Connection Number', connection_number, 'AC Power / Current - Phase C', '', '127746')

    # ac_rms_current | Offset: 16, Length: 16, Resolution: 0.1, Field Type: NUMBER
    ac_rms_current_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    ac_rms_current = ac_rms_current_raw * 0.1
    publish_field(hass, instance_name, 'ac_rms_current', 'AC RMS Current', ac_rms_current, 'AC Power / Current - Phase C', 'A', '127746')

    # power | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    power_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if power_raw & (1 << (32 - 1)):
        power_raw -= (1 << 32)
    power = power_raw * 1
    publish_field(hass, instance_name, 'power', 'Power', power, 'AC Power / Current - Phase C', 'W', '127746')

def process_pgn_127750(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127750."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: BINARY
    sid_raw = (data_raw >> 0) & 0xFF
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Converter Status', '', '127750')

    # connection_number | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    connection_number_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    connection_number = connection_number_raw * 1
    publish_field(hass, instance_name, 'connection_number', 'Connection Number', connection_number, 'Converter Status', '', '127750')

    # operating_state | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    operating_state_raw = (data_raw >> 16) & 0xFF
    operating_state = operating_state_raw * 1
    publish_field(hass, instance_name, 'operating_state', 'Operating State', operating_state, 'Converter Status', '', '127750')

    # temperature_state | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    temperature_state_raw = (data_raw >> 24) & 0x3
    temperature_state = temperature_state_raw * 1
    publish_field(hass, instance_name, 'temperature_state', 'Temperature State', temperature_state, 'Converter Status', '', '127750')

    # overload_state | Offset: 26, Length: 2, Resolution: 1, Field Type: LOOKUP
    overload_state_raw = (data_raw >> 26) & 0x3
    overload_state = overload_state_raw * 1
    publish_field(hass, instance_name, 'overload_state', 'Overload State', overload_state, 'Converter Status', '', '127750')

    # low_dc_voltage_state | Offset: 28, Length: 2, Resolution: 1, Field Type: LOOKUP
    low_dc_voltage_state_raw = (data_raw >> 28) & 0x3
    low_dc_voltage_state = low_dc_voltage_state_raw * 1
    publish_field(hass, instance_name, 'low_dc_voltage_state', 'Low DC Voltage State', low_dc_voltage_state, 'Converter Status', '', '127750')

    # ripple_state | Offset: 30, Length: 2, Resolution: 1, Field Type: LOOKUP
    ripple_state_raw = (data_raw >> 30) & 0x3
    ripple_state = ripple_state_raw * 1
    publish_field(hass, instance_name, 'ripple_state', 'Ripple State', ripple_state, 'Converter Status', '', '127750')

    # reserved | Offset: 32, Length: 32, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Converter Status', '', '127750')

def process_pgn_127751(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 127751."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: BINARY
    sid_raw = (data_raw >> 0) & 0xFF
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'DC Voltage/Current', '', '127751')

    # connection_number | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    connection_number_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    connection_number = connection_number_raw * 1
    publish_field(hass, instance_name, 'connection_number', 'Connection Number', connection_number, 'DC Voltage/Current', '', '127751')

    # dc_voltage | Offset: 16, Length: 16, Resolution: 0.1, Field Type: NUMBER
    dc_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    dc_voltage = dc_voltage_raw * 0.1
    publish_field(hass, instance_name, 'dc_voltage', 'DC Voltage', dc_voltage, 'DC Voltage/Current', 'V', '127751')

    # dc_current | Offset: 32, Length: 24, Resolution: 0.01, Field Type: NUMBER
    dc_current_raw = decode_number((data_raw >> 32) & 0xFFFFFF, 24)
    if dc_current_raw & (1 << (24 - 1)):
        dc_current_raw -= (1 << 24)
    dc_current = dc_current_raw * 0.01
    publish_field(hass, instance_name, 'dc_current', 'DC Current', dc_current, 'DC Voltage/Current', 'A', '127751')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'DC Voltage/Current', '', '127751')

def process_pgn_128000(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128000."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Leeway Angle', '', '128000')

    # leeway_angle | Offset: 8, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    leeway_angle_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    if leeway_angle_raw & (1 << (16 - 1)):
        leeway_angle_raw -= (1 << 16)
    leeway_angle = leeway_angle_raw * 0.0001
    publish_field(hass, instance_name, 'leeway_angle', 'Leeway Angle', leeway_angle, 'Leeway Angle', 'rad', '128000')
    publish_field(hass, instance_name, 'leeway_angle_degrees', 'Leeway Angle Degrees', radians_to_degrees(leeway_angle), 'Leeway Angle', 'Deg', '128000')

    # reserved | Offset: 24, Length: 40, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 24) & 0xFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Leeway Angle', '', '128000')

def process_pgn_128001(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128001."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Vessel Acceleration', '', '128001')

    # longitudinal_acceleration | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    longitudinal_acceleration_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    if longitudinal_acceleration_raw & (1 << (16 - 1)):
        longitudinal_acceleration_raw -= (1 << 16)
    longitudinal_acceleration = longitudinal_acceleration_raw * 1
    publish_field(hass, instance_name, 'longitudinal_acceleration', 'Longitudinal Acceleration', longitudinal_acceleration, 'Vessel Acceleration', '', '128001')

    # transverse_acceleration | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    transverse_acceleration_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if transverse_acceleration_raw & (1 << (16 - 1)):
        transverse_acceleration_raw -= (1 << 16)
    transverse_acceleration = transverse_acceleration_raw * 1
    publish_field(hass, instance_name, 'transverse_acceleration', 'Transverse Acceleration', transverse_acceleration, 'Vessel Acceleration', '', '128001')

    # vertical_acceleration | Offset: 40, Length: 16, Resolution: 1, Field Type: NUMBER
    vertical_acceleration_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if vertical_acceleration_raw & (1 << (16 - 1)):
        vertical_acceleration_raw -= (1 << 16)
    vertical_acceleration = vertical_acceleration_raw * 1
    publish_field(hass, instance_name, 'vertical_acceleration', 'Vertical Acceleration', vertical_acceleration, 'Vessel Acceleration', '', '128001')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Vessel Acceleration', '', '128001')

def process_pgn_128002(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128002."""
    # inverter_motor_controller | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    inverter_motor_controller_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    inverter_motor_controller = inverter_motor_controller_raw * 1
    publish_field(hass, instance_name, 'inverter_motor_controller', 'Inverter/Motor Controller', inverter_motor_controller, 'Electric Drive Status, Rapid Update', '', '128002')

    # active_motor_mode | Offset: 8, Length: 2, Resolution: 1, Field Type: NUMBER
    active_motor_mode_raw = decode_number((data_raw >> 8) & 0x3, 2)
    active_motor_mode = active_motor_mode_raw * 1
    publish_field(hass, instance_name, 'active_motor_mode', 'Active Motor Mode', active_motor_mode, 'Electric Drive Status, Rapid Update', '', '128002')

    # brake_mode | Offset: 10, Length: 2, Resolution: 1, Field Type: NUMBER
    brake_mode_raw = decode_number((data_raw >> 10) & 0x3, 2)
    brake_mode = brake_mode_raw * 1
    publish_field(hass, instance_name, 'brake_mode', 'Brake Mode', brake_mode, 'Electric Drive Status, Rapid Update', '', '128002')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Electric Drive Status, Rapid Update', '', '128002')

    # rotational_shaft_speed | Offset: 16, Length: 16, Resolution: 0.25, Field Type: NUMBER
    rotational_shaft_speed_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    rotational_shaft_speed = rotational_shaft_speed_raw * 0.25
    publish_field(hass, instance_name, 'rotational_shaft_speed', 'Rotational Shaft Speed', rotational_shaft_speed, 'Electric Drive Status, Rapid Update', 'rpm', '128002')

    # motor_dc_voltage | Offset: 32, Length: 16, Resolution: 0.1, Field Type: NUMBER
    motor_dc_voltage_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    motor_dc_voltage = motor_dc_voltage_raw * 0.1
    publish_field(hass, instance_name, 'motor_dc_voltage', 'Motor DC Voltage', motor_dc_voltage, 'Electric Drive Status, Rapid Update', 'V', '128002')

    # motor_dc_current | Offset: 48, Length: 16, Resolution: 0.1, Field Type: NUMBER
    motor_dc_current_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    if motor_dc_current_raw & (1 << (16 - 1)):
        motor_dc_current_raw -= (1 << 16)
    motor_dc_current = motor_dc_current_raw * 0.1
    publish_field(hass, instance_name, 'motor_dc_current', 'Motor DC Current', motor_dc_current, 'Electric Drive Status, Rapid Update', 'A', '128002')

def process_pgn_128003(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128003."""
    # energy_storage_identifier | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    energy_storage_identifier_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    energy_storage_identifier = energy_storage_identifier_raw * 1
    publish_field(hass, instance_name, 'energy_storage_identifier', 'Energy Storage Identifier', energy_storage_identifier, 'Electric Energy Storage Status, Rapid Update', '', '128003')

    # battery_status | Offset: 8, Length: 2, Resolution: 1, Field Type: NUMBER
    battery_status_raw = decode_number((data_raw >> 8) & 0x3, 2)
    battery_status = battery_status_raw * 1
    publish_field(hass, instance_name, 'battery_status', 'Battery Status', battery_status, 'Electric Energy Storage Status, Rapid Update', '', '128003')

    # isolation_status | Offset: 10, Length: 2, Resolution: 1, Field Type: NUMBER
    isolation_status_raw = decode_number((data_raw >> 10) & 0x3, 2)
    isolation_status = isolation_status_raw * 1
    publish_field(hass, instance_name, 'isolation_status', 'Isolation Status', isolation_status, 'Electric Energy Storage Status, Rapid Update', '', '128003')

    # battery_error | Offset: 12, Length: 4, Resolution: 1, Field Type: NUMBER
    battery_error_raw = decode_number((data_raw >> 12) & 0xF, 4)
    battery_error = battery_error_raw * 1
    publish_field(hass, instance_name, 'battery_error', 'Battery Error', battery_error, 'Electric Energy Storage Status, Rapid Update', '', '128003')

    # battery_voltage | Offset: 16, Length: 16, Resolution: 0.1, Field Type: NUMBER
    battery_voltage_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    battery_voltage = battery_voltage_raw * 0.1
    publish_field(hass, instance_name, 'battery_voltage', 'Battery Voltage', battery_voltage, 'Electric Energy Storage Status, Rapid Update', 'V', '128003')

    # battery_current | Offset: 32, Length: 16, Resolution: 0.1, Field Type: NUMBER
    battery_current_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if battery_current_raw & (1 << (16 - 1)):
        battery_current_raw -= (1 << 16)
    battery_current = battery_current_raw * 0.1
    publish_field(hass, instance_name, 'battery_current', 'Battery Current', battery_current, 'Electric Energy Storage Status, Rapid Update', 'A', '128003')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Electric Energy Storage Status, Rapid Update', '', '128003')

def process_pgn_128006(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128006."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Thruster Control Status', '', '128006')

    # identifier | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    identifier_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    identifier = identifier_raw * 1
    publish_field(hass, instance_name, 'identifier', 'Identifier', identifier, 'Thruster Control Status', '', '128006')

    # direction_control | Offset: 16, Length: 4, Resolution: 1, Field Type: LOOKUP
    direction_control_raw = (data_raw >> 16) & 0xF
    direction_control = direction_control_raw * 1
    publish_field(hass, instance_name, 'direction_control', 'Direction Control', direction_control, 'Thruster Control Status', '', '128006')

    # power_enabled | Offset: 20, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_enabled_raw = (data_raw >> 20) & 0x3
    power_enabled = power_enabled_raw * 1
    publish_field(hass, instance_name, 'power_enabled', 'Power Enabled', power_enabled, 'Thruster Control Status', '', '128006')

    # retract_control | Offset: 22, Length: 2, Resolution: 1, Field Type: LOOKUP
    retract_control_raw = (data_raw >> 22) & 0x3
    retract_control = retract_control_raw * 1
    publish_field(hass, instance_name, 'retract_control', 'Retract Control', retract_control, 'Thruster Control Status', '', '128006')

    # speed_control | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    speed_control_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    speed_control = speed_control_raw * 1
    publish_field(hass, instance_name, 'speed_control', 'Speed Control', speed_control, 'Thruster Control Status', '%', '128006')

    # control_events | Offset: 32, Length: 8, Resolution: 1, Field Type: BITLOOKUP
    control_events_raw = (data_raw >> 32) & 0xFF
    control_events = control_events_raw * 1
    publish_field(hass, instance_name, 'control_events', 'Control Events', control_events, 'Thruster Control Status', '', '128006')

    # command_timeout | Offset: 40, Length: 8, Resolution: 0.005, Field Type: TIME
    command_timeout_raw = (data_raw >> 40) & 0xFF
    command_timeout = decode_time(command_timeout_raw * 0.005)
    publish_field(hass, instance_name, 'command_timeout', 'Command Timeout', command_timeout, 'Thruster Control Status', 's', '128006')

    # azimuth_control | Offset: 48, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    azimuth_control_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    azimuth_control = azimuth_control_raw * 0.0001
    publish_field(hass, instance_name, 'azimuth_control', 'Azimuth Control', azimuth_control, 'Thruster Control Status', 'rad', '128006')
    publish_field(hass, instance_name, 'azimuth_control_degrees', 'Azimuth Control Degrees', radians_to_degrees(azimuth_control), 'Thruster Control Status', 'Deg', '128006')

def process_pgn_128007(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128007."""
    # identifier | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    identifier_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    identifier = identifier_raw * 1
    publish_field(hass, instance_name, 'identifier', 'Identifier', identifier, 'Thruster Information', '', '128007')

    # motor_type | Offset: 8, Length: 4, Resolution: 1, Field Type: LOOKUP
    motor_type_raw = (data_raw >> 8) & 0xF
    motor_type = motor_type_raw * 1
    publish_field(hass, instance_name, 'motor_type', 'Motor Type', motor_type, 'Thruster Information', '', '128007')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Thruster Information', '', '128007')

    # power_rating | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    power_rating_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    power_rating = power_rating_raw * 1
    publish_field(hass, instance_name, 'power_rating', 'Power Rating', power_rating, 'Thruster Information', 'W', '128007')

    # maximum_temperature_rating | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    maximum_temperature_rating_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    maximum_temperature_rating = maximum_temperature_rating_raw * 0.01
    publish_field(hass, instance_name, 'maximum_temperature_rating', 'Maximum Temperature Rating', maximum_temperature_rating, 'Thruster Information', 'K', '128007')
    publish_field(hass, instance_name, 'maximum_temperature_rating_celsius', 'Maximum Temperature Rating Celsius', kelvin_to_celsius(maximum_temperature_rating), 'Thruster Information', 'C', '128007')
    publish_field(hass, instance_name, 'maximum_temperature_rating_fahrenheit', 'Maximum Temperature Rating Fahrenheit', kelvin_to_fahrenheit(maximum_temperature_rating), 'Thruster Information', 'F', '128007')

    # maximum_rotational_speed | Offset: 48, Length: 16, Resolution: 0.25, Field Type: NUMBER
    maximum_rotational_speed_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    maximum_rotational_speed = maximum_rotational_speed_raw * 0.25
    publish_field(hass, instance_name, 'maximum_rotational_speed', 'Maximum Rotational Speed', maximum_rotational_speed, 'Thruster Information', 'rpm', '128007')

def process_pgn_128008(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128008."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Thruster Motor Status', '', '128008')

    # identifier | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    identifier_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    identifier = identifier_raw * 1
    publish_field(hass, instance_name, 'identifier', 'Identifier', identifier, 'Thruster Motor Status', '', '128008')

    # motor_events | Offset: 16, Length: 8, Resolution: 1, Field Type: BITLOOKUP
    motor_events_raw = (data_raw >> 16) & 0xFF
    motor_events = motor_events_raw * 1
    publish_field(hass, instance_name, 'motor_events', 'Motor Events', motor_events, 'Thruster Motor Status', '', '128008')

    # current | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    current_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    current = current_raw * 1
    publish_field(hass, instance_name, 'current', 'Current', current, 'Thruster Motor Status', 'A', '128008')

    # temperature | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    temperature_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    temperature = temperature_raw * 0.01
    publish_field(hass, instance_name, 'temperature', 'Temperature', temperature, 'Thruster Motor Status', 'K', '128008')
    publish_field(hass, instance_name, 'temperature_celsius', 'Temperature Celsius', kelvin_to_celsius(temperature), 'Thruster Motor Status', 'C', '128008')
    publish_field(hass, instance_name, 'temperature_fahrenheit', 'Temperature Fahrenheit', kelvin_to_fahrenheit(temperature), 'Thruster Motor Status', 'F', '128008')

    # operating_time | Offset: 48, Length: 16, Resolution: 60, Field Type: TIME
    operating_time_raw = (data_raw >> 48) & 0xFFFF
    operating_time = decode_time(operating_time_raw * 60)
    publish_field(hass, instance_name, 'operating_time', 'Operating Time', operating_time, 'Thruster Motor Status', 's', '128008')

def process_pgn_128259(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128259."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Speed', '', '128259')

    # speed_water_referenced | Offset: 8, Length: 16, Resolution: 0.01, Field Type: NUMBER
    speed_water_referenced_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    speed_water_referenced = speed_water_referenced_raw * 0.01
    publish_field(hass, instance_name, 'speed_water_referenced', 'Speed Water Referenced', speed_water_referenced, 'Speed', 'm/s', '128259')
    publish_field(hass, instance_name, 'speed_water_referenced_knots', 'Speed Water Referenced Knots', mps_to_knots(speed_water_referenced), 'Speed', 'Kn', '128259')

    # speed_ground_referenced | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    speed_ground_referenced_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    speed_ground_referenced = speed_ground_referenced_raw * 0.01
    publish_field(hass, instance_name, 'speed_ground_referenced', 'Speed Ground Referenced', speed_ground_referenced, 'Speed', 'm/s', '128259')
    publish_field(hass, instance_name, 'speed_ground_referenced_knots', 'Speed Ground Referenced Knots', mps_to_knots(speed_ground_referenced), 'Speed', 'Kn', '128259')

    # speed_water_referenced_type | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    speed_water_referenced_type_raw = (data_raw >> 40) & 0xFF
    speed_water_referenced_type = speed_water_referenced_type_raw * 1
    publish_field(hass, instance_name, 'speed_water_referenced_type', 'Speed Water Referenced Type', speed_water_referenced_type, 'Speed', '', '128259')

    # speed_direction | Offset: 48, Length: 4, Resolution: 1, Field Type: NUMBER
    speed_direction_raw = decode_number((data_raw >> 48) & 0xF, 4)
    speed_direction = speed_direction_raw * 1
    publish_field(hass, instance_name, 'speed_direction', 'Speed Direction', speed_direction, 'Speed', '', '128259')

    # reserved | Offset: 52, Length: 12, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 52) & 0xFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Speed', '', '128259')

def process_pgn_128267(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128267."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Water Depth', '', '128267')

    # depth | Offset: 8, Length: 32, Resolution: 0.01, Field Type: NUMBER
    depth_raw = decode_number((data_raw >> 8) & 0xFFFFFFFF, 32)
    depth = depth_raw * 0.01
    publish_field(hass, instance_name, 'depth', 'Depth', depth, 'Water Depth', 'm', '128267')

    # offset | Offset: 40, Length: 16, Resolution: 0.001, Field Type: NUMBER
    offset_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if offset_raw & (1 << (16 - 1)):
        offset_raw -= (1 << 16)
    offset = offset_raw * 0.001
    publish_field(hass, instance_name, 'offset', 'Offset', offset, 'Water Depth', 'm', '128267')

    # range | Offset: 56, Length: 8, Resolution: 10, Field Type: NUMBER
    range_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    range = range_raw * 10
    publish_field(hass, instance_name, 'range', 'Range', range, 'Water Depth', 'm', '128267')

def process_pgn_128275(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128275."""
    # date | Offset: 0, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 0) & 0xFFFF
    date = decode_date(date_raw * 1)
    publish_field(hass, instance_name, 'date', 'Date', date, 'Distance Log', 'd', '128275')

    # time | Offset: 16, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 16) & 0xFFFFFFFF
    time = decode_time(time_raw * 0.0001)
    publish_field(hass, instance_name, 'time', 'Time', time, 'Distance Log', 's', '128275')

    # log | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    log_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    log = log_raw * 1
    publish_field(hass, instance_name, 'log', 'Log', log, 'Distance Log', 'm', '128275')

    # trip_log | Offset: 80, Length: 32, Resolution: 1, Field Type: NUMBER
    trip_log_raw = decode_number((data_raw >> 80) & 0xFFFFFFFF, 32)
    trip_log = trip_log_raw * 1
    publish_field(hass, instance_name, 'trip_log', 'Trip Log', trip_log, 'Distance Log', 'm', '128275')

def process_pgn_128520(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128520."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Tracked Target Data', '', '128520')

    # target_id__ | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    target_id___raw = decode_number((data_raw >> 8) & 0xFF, 8)
    target_id__ = target_id___raw * 1
    publish_field(hass, instance_name, 'target_id__', 'Target ID #', target_id__, 'Tracked Target Data', '', '128520')

    # track_status | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    track_status_raw = (data_raw >> 16) & 0x3
    track_status = track_status_raw * 1
    publish_field(hass, instance_name, 'track_status', 'Track Status', track_status, 'Tracked Target Data', '', '128520')

    # reported_target | Offset: 18, Length: 1, Resolution: 1, Field Type: LOOKUP
    reported_target_raw = (data_raw >> 18) & 0x1
    reported_target = reported_target_raw * 1
    publish_field(hass, instance_name, 'reported_target', 'Reported Target', reported_target, 'Tracked Target Data', '', '128520')

    # target_acquisition | Offset: 19, Length: 1, Resolution: 1, Field Type: LOOKUP
    target_acquisition_raw = (data_raw >> 19) & 0x1
    target_acquisition = target_acquisition_raw * 1
    publish_field(hass, instance_name, 'target_acquisition', 'Target Acquisition', target_acquisition, 'Tracked Target Data', '', '128520')

    # bearing_reference | Offset: 20, Length: 2, Resolution: 1, Field Type: LOOKUP
    bearing_reference_raw = (data_raw >> 20) & 0x3
    bearing_reference = bearing_reference_raw * 1
    publish_field(hass, instance_name, 'bearing_reference', 'Bearing Reference', bearing_reference, 'Tracked Target Data', '', '128520')

    # reserved | Offset: 22, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 22) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Tracked Target Data', '', '128520')

    # bearing | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    bearing_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    bearing = bearing_raw * 0.0001
    publish_field(hass, instance_name, 'bearing', 'Bearing', bearing, 'Tracked Target Data', 'rad', '128520')
    publish_field(hass, instance_name, 'bearing_degrees', 'Bearing Degrees', radians_to_degrees(bearing), 'Tracked Target Data', 'Deg', '128520')

    # distance | Offset: 40, Length: 32, Resolution: 0.001, Field Type: NUMBER
    distance_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    distance = distance_raw * 0.001
    publish_field(hass, instance_name, 'distance', 'Distance', distance, 'Tracked Target Data', 'm', '128520')

    # course | Offset: 72, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    course_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    course = course_raw * 0.0001
    publish_field(hass, instance_name, 'course', 'Course', course, 'Tracked Target Data', 'rad', '128520')
    publish_field(hass, instance_name, 'course_degrees', 'Course Degrees', radians_to_degrees(course), 'Tracked Target Data', 'Deg', '128520')

    # speed | Offset: 88, Length: 16, Resolution: 0.01, Field Type: NUMBER
    speed_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    speed = speed_raw * 0.01
    publish_field(hass, instance_name, 'speed', 'Speed', speed, 'Tracked Target Data', 'm/s', '128520')
    publish_field(hass, instance_name, 'speed_knots', 'Speed Knots', mps_to_knots(speed), 'Tracked Target Data', 'Kn', '128520')

    # cpa | Offset: 104, Length: 32, Resolution: 0.01, Field Type: NUMBER
    cpa_raw = decode_number((data_raw >> 104) & 0xFFFFFFFF, 32)
    cpa = cpa_raw * 0.01
    publish_field(hass, instance_name, 'cpa', 'CPA', cpa, 'Tracked Target Data', 'm', '128520')

    # tcpa | Offset: 136, Length: 32, Resolution: 0.001, Field Type: TIME
    tcpa_raw = (data_raw >> 136) & 0xFFFFFFFF
    if tcpa_raw & (1 << (32 - 1)):
        tcpa_raw -= (1 << 32)
    tcpa = decode_time(tcpa_raw * 0.001)
    publish_field(hass, instance_name, 'tcpa', 'TCPA', tcpa, 'Tracked Target Data', 's', '128520')

    # utc_of_fix | Offset: 168, Length: 32, Resolution: 0.0001, Field Type: TIME
    utc_of_fix_raw = (data_raw >> 168) & 0xFFFFFFFF
    utc_of_fix = decode_time(utc_of_fix_raw * 0.0001)
    publish_field(hass, instance_name, 'utc_of_fix', 'UTC of Fix', utc_of_fix, 'Tracked Target Data', 's', '128520')

    # name | Offset: 200, Length: 1784, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_128538(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128538."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Elevator Car Status', '', '128538')

    # elevator_car_id | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    elevator_car_id_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    elevator_car_id = elevator_car_id_raw * 1
    publish_field(hass, instance_name, 'elevator_car_id', 'Elevator Car ID', elevator_car_id, 'Elevator Car Status', '', '128538')

    # elevator_car_usage | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    elevator_car_usage_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    elevator_car_usage = elevator_car_usage_raw * 1
    publish_field(hass, instance_name, 'elevator_car_usage', 'Elevator Car Usage', elevator_car_usage, 'Elevator Car Status', '', '128538')

    # smoke_sensor_status | Offset: 24, Length: 2, Resolution: 1, Field Type: NUMBER
    smoke_sensor_status_raw = decode_number((data_raw >> 24) & 0x3, 2)
    smoke_sensor_status = smoke_sensor_status_raw * 1
    publish_field(hass, instance_name, 'smoke_sensor_status', 'Smoke Sensor Status', smoke_sensor_status, 'Elevator Car Status', '', '128538')

    # limit_switch_sensor_status | Offset: 26, Length: 2, Resolution: 1, Field Type: NUMBER
    limit_switch_sensor_status_raw = decode_number((data_raw >> 26) & 0x3, 2)
    limit_switch_sensor_status = limit_switch_sensor_status_raw * 1
    publish_field(hass, instance_name, 'limit_switch_sensor_status', 'Limit Switch Sensor Status', limit_switch_sensor_status, 'Elevator Car Status', '', '128538')

    # proximity_switch_sensor_status | Offset: 28, Length: 2, Resolution: 1, Field Type: NUMBER
    proximity_switch_sensor_status_raw = decode_number((data_raw >> 28) & 0x3, 2)
    proximity_switch_sensor_status = proximity_switch_sensor_status_raw * 1
    publish_field(hass, instance_name, 'proximity_switch_sensor_status', 'Proximity Switch Sensor Status', proximity_switch_sensor_status, 'Elevator Car Status', '', '128538')

    # inertial_measurement_unit__imu__sensor_status | Offset: 30, Length: 2, Resolution: 1, Field Type: NUMBER
    inertial_measurement_unit__imu__sensor_status_raw = decode_number((data_raw >> 30) & 0x3, 2)
    inertial_measurement_unit__imu__sensor_status = inertial_measurement_unit__imu__sensor_status_raw * 1
    publish_field(hass, instance_name, 'inertial_measurement_unit__imu__sensor_status', 'Inertial Measurement Unit (IMU) Sensor Status', inertial_measurement_unit__imu__sensor_status, 'Elevator Car Status', '', '128538')

    # elevator_load_limit_status | Offset: 32, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_load_limit_status_raw = decode_number((data_raw >> 32) & 0x3, 2)
    elevator_load_limit_status = elevator_load_limit_status_raw * 1
    publish_field(hass, instance_name, 'elevator_load_limit_status', 'Elevator Load Limit Status', elevator_load_limit_status, 'Elevator Car Status', '', '128538')

    # elevator_load_balance_status | Offset: 34, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_load_balance_status_raw = decode_number((data_raw >> 34) & 0x3, 2)
    elevator_load_balance_status = elevator_load_balance_status_raw * 1
    publish_field(hass, instance_name, 'elevator_load_balance_status', 'Elevator Load Balance Status', elevator_load_balance_status, 'Elevator Car Status', '', '128538')

    # elevator_load_sensor_1_status | Offset: 36, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_load_sensor_1_status_raw = decode_number((data_raw >> 36) & 0x3, 2)
    elevator_load_sensor_1_status = elevator_load_sensor_1_status_raw * 1
    publish_field(hass, instance_name, 'elevator_load_sensor_1_status', 'Elevator Load Sensor 1 Status', elevator_load_sensor_1_status, 'Elevator Car Status', '', '128538')

    # elevator_load_sensor_2_status | Offset: 38, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_load_sensor_2_status_raw = decode_number((data_raw >> 38) & 0x3, 2)
    elevator_load_sensor_2_status = elevator_load_sensor_2_status_raw * 1
    publish_field(hass, instance_name, 'elevator_load_sensor_2_status', 'Elevator Load Sensor 2 Status', elevator_load_sensor_2_status, 'Elevator Car Status', '', '128538')

    # elevator_load_sensor_3_status | Offset: 40, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_load_sensor_3_status_raw = decode_number((data_raw >> 40) & 0x3, 2)
    elevator_load_sensor_3_status = elevator_load_sensor_3_status_raw * 1
    publish_field(hass, instance_name, 'elevator_load_sensor_3_status', 'Elevator Load Sensor 3 Status', elevator_load_sensor_3_status, 'Elevator Car Status', '', '128538')

    # elevator_load_sensor_4_status | Offset: 42, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_load_sensor_4_status_raw = decode_number((data_raw >> 42) & 0x3, 2)
    elevator_load_sensor_4_status = elevator_load_sensor_4_status_raw * 1
    publish_field(hass, instance_name, 'elevator_load_sensor_4_status', 'Elevator Load Sensor 4 Status', elevator_load_sensor_4_status, 'Elevator Car Status', '', '128538')

    # reserved | Offset: 44, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 44) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Elevator Car Status', '', '128538')

    # elevator_car_motion_status | Offset: 48, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_car_motion_status_raw = decode_number((data_raw >> 48) & 0x3, 2)
    elevator_car_motion_status = elevator_car_motion_status_raw * 1
    publish_field(hass, instance_name, 'elevator_car_motion_status', 'Elevator Car Motion Status', elevator_car_motion_status, 'Elevator Car Status', '', '128538')

    # elevator_car_door_status | Offset: 50, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_car_door_status_raw = decode_number((data_raw >> 50) & 0x3, 2)
    elevator_car_door_status = elevator_car_door_status_raw * 1
    publish_field(hass, instance_name, 'elevator_car_door_status', 'Elevator Car Door Status', elevator_car_door_status, 'Elevator Car Status', '', '128538')

    # elevator_car_emergency_button_status | Offset: 52, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_car_emergency_button_status_raw = decode_number((data_raw >> 52) & 0x3, 2)
    elevator_car_emergency_button_status = elevator_car_emergency_button_status_raw * 1
    publish_field(hass, instance_name, 'elevator_car_emergency_button_status', 'Elevator Car Emergency Button Status', elevator_car_emergency_button_status, 'Elevator Car Status', '', '128538')

    # elevator_car_buzzer_status | Offset: 54, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_car_buzzer_status_raw = decode_number((data_raw >> 54) & 0x3, 2)
    elevator_car_buzzer_status = elevator_car_buzzer_status_raw * 1
    publish_field(hass, instance_name, 'elevator_car_buzzer_status', 'Elevator Car Buzzer Status', elevator_car_buzzer_status, 'Elevator Car Status', '', '128538')

    # open_door_button_status | Offset: 56, Length: 2, Resolution: 1, Field Type: NUMBER
    open_door_button_status_raw = decode_number((data_raw >> 56) & 0x3, 2)
    open_door_button_status = open_door_button_status_raw * 1
    publish_field(hass, instance_name, 'open_door_button_status', 'Open Door Button Status', open_door_button_status, 'Elevator Car Status', '', '128538')

    # close_door_button_status | Offset: 58, Length: 2, Resolution: 1, Field Type: NUMBER
    close_door_button_status_raw = decode_number((data_raw >> 58) & 0x3, 2)
    close_door_button_status = close_door_button_status_raw * 1
    publish_field(hass, instance_name, 'close_door_button_status', 'Close Door Button Status', close_door_button_status, 'Elevator Car Status', '', '128538')

    # reserved | Offset: 60, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 60) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Elevator Car Status', '', '128538')

    # current_deck | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    current_deck_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    current_deck = current_deck_raw * 1
    publish_field(hass, instance_name, 'current_deck', 'Current Deck', current_deck, 'Elevator Car Status', '', '128538')

    # destination_deck | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    destination_deck_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    destination_deck = destination_deck_raw * 1
    publish_field(hass, instance_name, 'destination_deck', 'Destination Deck', destination_deck, 'Elevator Car Status', '', '128538')

    # total_number_of_decks | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    total_number_of_decks_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    total_number_of_decks = total_number_of_decks_raw * 1
    publish_field(hass, instance_name, 'total_number_of_decks', 'Total Number of Decks', total_number_of_decks, 'Elevator Car Status', '', '128538')

    # weight_of_load_cell_1 | Offset: 88, Length: 16, Resolution: 1, Field Type: NUMBER
    weight_of_load_cell_1_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    weight_of_load_cell_1 = weight_of_load_cell_1_raw * 1
    publish_field(hass, instance_name, 'weight_of_load_cell_1', 'Weight of Load Cell 1', weight_of_load_cell_1, 'Elevator Car Status', '', '128538')

    # weight_of_load_cell_2 | Offset: 104, Length: 16, Resolution: 1, Field Type: NUMBER
    weight_of_load_cell_2_raw = decode_number((data_raw >> 104) & 0xFFFF, 16)
    weight_of_load_cell_2 = weight_of_load_cell_2_raw * 1
    publish_field(hass, instance_name, 'weight_of_load_cell_2', 'Weight of Load Cell 2', weight_of_load_cell_2, 'Elevator Car Status', '', '128538')

    # weight_of_load_cell_3 | Offset: 120, Length: 16, Resolution: 1, Field Type: NUMBER
    weight_of_load_cell_3_raw = decode_number((data_raw >> 120) & 0xFFFF, 16)
    weight_of_load_cell_3 = weight_of_load_cell_3_raw * 1
    publish_field(hass, instance_name, 'weight_of_load_cell_3', 'Weight of Load Cell 3', weight_of_load_cell_3, 'Elevator Car Status', '', '128538')

    # weight_of_load_cell_4 | Offset: 136, Length: 16, Resolution: 1, Field Type: NUMBER
    weight_of_load_cell_4_raw = decode_number((data_raw >> 136) & 0xFFFF, 16)
    weight_of_load_cell_4 = weight_of_load_cell_4_raw * 1
    publish_field(hass, instance_name, 'weight_of_load_cell_4', 'Weight of Load Cell 4', weight_of_load_cell_4, 'Elevator Car Status', '', '128538')

    # speed_of_elevator_car | Offset: 152, Length: 16, Resolution: 0.01, Field Type: NUMBER
    speed_of_elevator_car_raw = decode_number((data_raw >> 152) & 0xFFFF, 16)
    if speed_of_elevator_car_raw & (1 << (16 - 1)):
        speed_of_elevator_car_raw -= (1 << 16)
    speed_of_elevator_car = speed_of_elevator_car_raw * 0.01
    publish_field(hass, instance_name, 'speed_of_elevator_car', 'Speed of Elevator Car', speed_of_elevator_car, 'Elevator Car Status', 'm/s', '128538')
    publish_field(hass, instance_name, 'speed_of_elevator_car_knots', 'Speed of Elevator Car Knots', mps_to_knots(speed_of_elevator_car), 'Elevator Car Status', 'Kn', '128538')

    # elevator_brake_status | Offset: 168, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_brake_status_raw = decode_number((data_raw >> 168) & 0x3, 2)
    elevator_brake_status = elevator_brake_status_raw * 1
    publish_field(hass, instance_name, 'elevator_brake_status', 'Elevator Brake Status', elevator_brake_status, 'Elevator Car Status', '', '128538')

    # elevator_motor_rotation_control_status | Offset: 170, Length: 2, Resolution: 1, Field Type: NUMBER
    elevator_motor_rotation_control_status_raw = decode_number((data_raw >> 170) & 0x3, 2)
    elevator_motor_rotation_control_status = elevator_motor_rotation_control_status_raw * 1
    publish_field(hass, instance_name, 'elevator_motor_rotation_control_status', 'Elevator Motor rotation control Status', elevator_motor_rotation_control_status, 'Elevator Car Status', '', '128538')

    # reserved | Offset: 172, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 172) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Elevator Car Status', '', '128538')

def process_pgn_128768(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128768."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Elevator Motor Control', '', '128768')

    # elevator_car_id | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    elevator_car_id_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    elevator_car_id = elevator_car_id_raw * 1
    publish_field(hass, instance_name, 'elevator_car_id', 'Elevator Car ID', elevator_car_id, 'Elevator Motor Control', '', '128768')

    # elevator_car_usage | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    elevator_car_usage_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    elevator_car_usage = elevator_car_usage_raw * 1
    publish_field(hass, instance_name, 'elevator_car_usage', 'Elevator Car Usage', elevator_car_usage, 'Elevator Motor Control', '', '128768')

    # motor_acceleration_deceleration_profile_selection | Offset: 24, Length: 4, Resolution: 1, Field Type: NUMBER
    motor_acceleration_deceleration_profile_selection_raw = decode_number((data_raw >> 24) & 0xF, 4)
    motor_acceleration_deceleration_profile_selection = motor_acceleration_deceleration_profile_selection_raw * 1
    publish_field(hass, instance_name, 'motor_acceleration_deceleration_profile_selection', 'Motor Acceleration/Deceleration profile selection', motor_acceleration_deceleration_profile_selection, 'Elevator Motor Control', '', '128768')

    # motor_rotational_control_status | Offset: 28, Length: 2, Resolution: 1, Field Type: NUMBER
    motor_rotational_control_status_raw = decode_number((data_raw >> 28) & 0x3, 2)
    motor_rotational_control_status = motor_rotational_control_status_raw * 1
    publish_field(hass, instance_name, 'motor_rotational_control_status', 'Motor Rotational Control Status', motor_rotational_control_status, 'Elevator Motor Control', '', '128768')

    # reserved | Offset: 30, Length: 34, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 30) & 0x3FFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Elevator Motor Control', '', '128768')

def process_pgn_128769(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128769."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Elevator Deck Push Button', '', '128769')

    # elevator_call_button_id | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    elevator_call_button_id_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    elevator_call_button_id = elevator_call_button_id_raw * 1
    publish_field(hass, instance_name, 'elevator_call_button_id', 'Elevator Call Button ID', elevator_call_button_id, 'Elevator Deck Push Button', '', '128769')

    # deck_button_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    deck_button_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    deck_button_id = deck_button_id_raw * 1
    publish_field(hass, instance_name, 'deck_button_id', 'Deck Button ID', deck_button_id, 'Elevator Deck Push Button', '', '128769')

    # elevator_car_usage | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    elevator_car_usage_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    elevator_car_usage = elevator_car_usage_raw * 1
    publish_field(hass, instance_name, 'elevator_car_usage', 'Elevator Car Usage', elevator_car_usage, 'Elevator Deck Push Button', '', '128769')

    # elevator_car_button_selection | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    elevator_car_button_selection_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    elevator_car_button_selection = elevator_car_button_selection_raw * 1
    publish_field(hass, instance_name, 'elevator_car_button_selection', 'Elevator Car Button Selection', elevator_car_button_selection, 'Elevator Deck Push Button', '', '128769')

    # reserved | Offset: 40, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Elevator Deck Push Button', '', '128769')

def process_pgn_128776(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128776."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Windlass Control Status', '', '128776')

    # windlass_id | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    windlass_id_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    windlass_id = windlass_id_raw * 1
    publish_field(hass, instance_name, 'windlass_id', 'Windlass ID', windlass_id, 'Windlass Control Status', '', '128776')

    # windlass_direction_control | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    windlass_direction_control_raw = (data_raw >> 16) & 0x3
    windlass_direction_control = windlass_direction_control_raw * 1
    publish_field(hass, instance_name, 'windlass_direction_control', 'Windlass Direction Control', windlass_direction_control, 'Windlass Control Status', '', '128776')

    # anchor_docking_control | Offset: 18, Length: 2, Resolution: 1, Field Type: LOOKUP
    anchor_docking_control_raw = (data_raw >> 18) & 0x3
    anchor_docking_control = anchor_docking_control_raw * 1
    publish_field(hass, instance_name, 'anchor_docking_control', 'Anchor Docking Control', anchor_docking_control, 'Windlass Control Status', '', '128776')

    # speed_control_type | Offset: 20, Length: 2, Resolution: 1, Field Type: LOOKUP
    speed_control_type_raw = (data_raw >> 20) & 0x3
    speed_control_type = speed_control_type_raw * 1
    publish_field(hass, instance_name, 'speed_control_type', 'Speed Control Type', speed_control_type, 'Windlass Control Status', '', '128776')

    # reserved | Offset: 22, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 22) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Windlass Control Status', '', '128776')

    # speed_control | Offset: 24, Length: 8, Resolution: 1, Field Type: BINARY
    speed_control_raw = (data_raw >> 24) & 0xFF
    speed_control = speed_control_raw * 1
    publish_field(hass, instance_name, 'speed_control', 'Speed Control', speed_control, 'Windlass Control Status', '', '128776')

    # power_enable | Offset: 32, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_enable_raw = (data_raw >> 32) & 0x3
    power_enable = power_enable_raw * 1
    publish_field(hass, instance_name, 'power_enable', 'Power Enable', power_enable, 'Windlass Control Status', '', '128776')

    # mechanical_lock | Offset: 34, Length: 2, Resolution: 1, Field Type: LOOKUP
    mechanical_lock_raw = (data_raw >> 34) & 0x3
    mechanical_lock = mechanical_lock_raw * 1
    publish_field(hass, instance_name, 'mechanical_lock', 'Mechanical Lock', mechanical_lock, 'Windlass Control Status', '', '128776')

    # deck_and_anchor_wash | Offset: 36, Length: 2, Resolution: 1, Field Type: LOOKUP
    deck_and_anchor_wash_raw = (data_raw >> 36) & 0x3
    deck_and_anchor_wash = deck_and_anchor_wash_raw * 1
    publish_field(hass, instance_name, 'deck_and_anchor_wash', 'Deck and Anchor Wash', deck_and_anchor_wash, 'Windlass Control Status', '', '128776')

    # anchor_light | Offset: 38, Length: 2, Resolution: 1, Field Type: LOOKUP
    anchor_light_raw = (data_raw >> 38) & 0x3
    anchor_light = anchor_light_raw * 1
    publish_field(hass, instance_name, 'anchor_light', 'Anchor Light', anchor_light, 'Windlass Control Status', '', '128776')

    # command_timeout | Offset: 40, Length: 8, Resolution: 0.005, Field Type: TIME
    command_timeout_raw = (data_raw >> 40) & 0xFF
    command_timeout = decode_time(command_timeout_raw * 0.005)
    publish_field(hass, instance_name, 'command_timeout', 'Command Timeout', command_timeout, 'Windlass Control Status', 's', '128776')

    # windlass_control_events | Offset: 48, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    windlass_control_events_raw = (data_raw >> 48) & 0xF
    windlass_control_events = windlass_control_events_raw * 1
    publish_field(hass, instance_name, 'windlass_control_events', 'Windlass Control Events', windlass_control_events, 'Windlass Control Status', '', '128776')

    # reserved | Offset: 52, Length: 12, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 52) & 0xFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Windlass Control Status', '', '128776')

def process_pgn_128777(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128777."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Anchor Windlass Operating Status', '', '128777')

    # windlass_id | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    windlass_id_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    windlass_id = windlass_id_raw * 1
    publish_field(hass, instance_name, 'windlass_id', 'Windlass ID', windlass_id, 'Anchor Windlass Operating Status', '', '128777')

    # windlass_direction_control | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    windlass_direction_control_raw = (data_raw >> 16) & 0x3
    windlass_direction_control = windlass_direction_control_raw * 1
    publish_field(hass, instance_name, 'windlass_direction_control', 'Windlass Direction Control', windlass_direction_control, 'Anchor Windlass Operating Status', '', '128777')

    # windlass_motion_status | Offset: 18, Length: 2, Resolution: 1, Field Type: LOOKUP
    windlass_motion_status_raw = (data_raw >> 18) & 0x3
    windlass_motion_status = windlass_motion_status_raw * 1
    publish_field(hass, instance_name, 'windlass_motion_status', 'Windlass Motion Status', windlass_motion_status, 'Anchor Windlass Operating Status', '', '128777')

    # rode_type_status | Offset: 20, Length: 2, Resolution: 1, Field Type: LOOKUP
    rode_type_status_raw = (data_raw >> 20) & 0x3
    rode_type_status = rode_type_status_raw * 1
    publish_field(hass, instance_name, 'rode_type_status', 'Rode Type Status', rode_type_status, 'Anchor Windlass Operating Status', '', '128777')

    # reserved | Offset: 22, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 22) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Anchor Windlass Operating Status', '', '128777')

    # rode_counter_value | Offset: 24, Length: 16, Resolution: 0.1, Field Type: NUMBER
    rode_counter_value_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    rode_counter_value = rode_counter_value_raw * 0.1
    publish_field(hass, instance_name, 'rode_counter_value', 'Rode Counter Value', rode_counter_value, 'Anchor Windlass Operating Status', 'm', '128777')

    # windlass_line_speed | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    windlass_line_speed_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    windlass_line_speed = windlass_line_speed_raw * 0.01
    publish_field(hass, instance_name, 'windlass_line_speed', 'Windlass Line Speed', windlass_line_speed, 'Anchor Windlass Operating Status', 'm/s', '128777')
    publish_field(hass, instance_name, 'windlass_line_speed_knots', 'Windlass Line Speed Knots', mps_to_knots(windlass_line_speed), 'Anchor Windlass Operating Status', 'Kn', '128777')

    # anchor_docking_status | Offset: 56, Length: 2, Resolution: 1, Field Type: LOOKUP
    anchor_docking_status_raw = (data_raw >> 56) & 0x3
    anchor_docking_status = anchor_docking_status_raw * 1
    publish_field(hass, instance_name, 'anchor_docking_status', 'Anchor Docking Status', anchor_docking_status, 'Anchor Windlass Operating Status', '', '128777')

    # windlass_operating_events | Offset: 58, Length: 6, Resolution: 1, Field Type: BITLOOKUP
    windlass_operating_events_raw = (data_raw >> 58) & 0x3F
    windlass_operating_events = windlass_operating_events_raw * 1
    publish_field(hass, instance_name, 'windlass_operating_events', 'Windlass Operating Events', windlass_operating_events, 'Anchor Windlass Operating Status', '', '128777')

def process_pgn_128778(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128778."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Anchor Windlass Monitoring Status', '', '128778')

    # windlass_id | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    windlass_id_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    windlass_id = windlass_id_raw * 1
    publish_field(hass, instance_name, 'windlass_id', 'Windlass ID', windlass_id, 'Anchor Windlass Monitoring Status', '', '128778')

    # windlass_monitoring_events | Offset: 16, Length: 8, Resolution: 1, Field Type: BITLOOKUP
    windlass_monitoring_events_raw = (data_raw >> 16) & 0xFF
    windlass_monitoring_events = windlass_monitoring_events_raw * 1
    publish_field(hass, instance_name, 'windlass_monitoring_events', 'Windlass Monitoring Events', windlass_monitoring_events, 'Anchor Windlass Monitoring Status', '', '128778')

    # controller_voltage | Offset: 24, Length: 8, Resolution: 0.2, Field Type: NUMBER
    controller_voltage_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    controller_voltage = controller_voltage_raw * 0.2
    publish_field(hass, instance_name, 'controller_voltage', 'Controller voltage', controller_voltage, 'Anchor Windlass Monitoring Status', 'V', '128778')

    # motor_current | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    motor_current_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    motor_current = motor_current_raw * 1
    publish_field(hass, instance_name, 'motor_current', 'Motor current', motor_current, 'Anchor Windlass Monitoring Status', 'A', '128778')

    # total_motor_time | Offset: 40, Length: 16, Resolution: 60, Field Type: TIME
    total_motor_time_raw = (data_raw >> 40) & 0xFFFF
    total_motor_time = decode_time(total_motor_time_raw * 60)
    publish_field(hass, instance_name, 'total_motor_time', 'Total Motor Time', total_motor_time, 'Anchor Windlass Monitoring Status', 's', '128778')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Anchor Windlass Monitoring Status', '', '128778')

def process_pgn_128780(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 128780."""
    # actuator_identifier | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    actuator_identifier_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    actuator_identifier = actuator_identifier_raw * 1
    publish_field(hass, instance_name, 'actuator_identifier', 'Actuator Identifier', actuator_identifier, 'Linear Actuator Control/Status', '', '128780')

    # commanded_device_position | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    commanded_device_position_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    commanded_device_position = commanded_device_position_raw * 1
    publish_field(hass, instance_name, 'commanded_device_position', 'Commanded Device Position', commanded_device_position, 'Linear Actuator Control/Status', '', '128780')

    # device_position | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    device_position_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    device_position = device_position_raw * 1
    publish_field(hass, instance_name, 'device_position', 'Device Position', device_position, 'Linear Actuator Control/Status', '', '128780')

    # maximum_device_travel | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    maximum_device_travel_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    maximum_device_travel = maximum_device_travel_raw * 1
    publish_field(hass, instance_name, 'maximum_device_travel', 'Maximum Device Travel', maximum_device_travel, 'Linear Actuator Control/Status', '', '128780')

    # direction_of_travel | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    direction_of_travel_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    direction_of_travel = direction_of_travel_raw * 1
    publish_field(hass, instance_name, 'direction_of_travel', 'Direction of Travel', direction_of_travel, 'Linear Actuator Control/Status', '', '128780')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Linear Actuator Control/Status', '', '128780')

def process_pgn_129025(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129025."""
    # latitude | Offset: 0, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'Position, Rapid Update', 'deg', '129025')

    # longitude | Offset: 32, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'Position, Rapid Update', 'deg', '129025')

def process_pgn_129026(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129026."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'COG & SOG, Rapid Update', '', '129026')

    # cog_reference | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    cog_reference_raw = (data_raw >> 8) & 0x3
    cog_reference = cog_reference_raw * 1
    publish_field(hass, instance_name, 'cog_reference', 'COG Reference', cog_reference, 'COG & SOG, Rapid Update', '', '129026')

    # reserved | Offset: 10, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 10) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'COG & SOG, Rapid Update', '', '129026')

    # cog | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'COG & SOG, Rapid Update', 'rad', '129026')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'COG & SOG, Rapid Update', 'Deg', '129026')

    # sog | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    sog_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    sog = sog_raw * 0.01
    publish_field(hass, instance_name, 'sog', 'SOG', sog, 'COG & SOG, Rapid Update', 'm/s', '129026')
    publish_field(hass, instance_name, 'sog_knots', 'SOG Knots', mps_to_knots(sog), 'COG & SOG, Rapid Update', 'Kn', '129026')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'COG & SOG, Rapid Update', '', '129026')

def process_pgn_129027(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129027."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Position Delta, Rapid Update', '', '129027')

    # time_delta | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    time_delta_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    time_delta = time_delta_raw * 1
    publish_field(hass, instance_name, 'time_delta', 'Time Delta', time_delta, 'Position Delta, Rapid Update', '', '129027')

    # latitude_delta | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    latitude_delta_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if latitude_delta_raw & (1 << (16 - 1)):
        latitude_delta_raw -= (1 << 16)
    latitude_delta = latitude_delta_raw * 1
    publish_field(hass, instance_name, 'latitude_delta', 'Latitude Delta', latitude_delta, 'Position Delta, Rapid Update', '', '129027')

    # longitude_delta | Offset: 40, Length: 16, Resolution: 1, Field Type: NUMBER
    longitude_delta_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if longitude_delta_raw & (1 << (16 - 1)):
        longitude_delta_raw -= (1 << 16)
    longitude_delta = longitude_delta_raw * 1
    publish_field(hass, instance_name, 'longitude_delta', 'Longitude Delta', longitude_delta, 'Position Delta, Rapid Update', '', '129027')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Position Delta, Rapid Update', '', '129027')

def process_pgn_129028(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129028."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Altitude Delta, Rapid Update', '', '129028')

    # time_delta | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    time_delta_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    if time_delta_raw & (1 << (16 - 1)):
        time_delta_raw -= (1 << 16)
    time_delta = time_delta_raw * 1
    publish_field(hass, instance_name, 'time_delta', 'Time Delta', time_delta, 'Altitude Delta, Rapid Update', '', '129028')

    # gnss_quality | Offset: 24, Length: 2, Resolution: 1, Field Type: NUMBER
    gnss_quality_raw = decode_number((data_raw >> 24) & 0x3, 2)
    gnss_quality = gnss_quality_raw * 1
    publish_field(hass, instance_name, 'gnss_quality', 'GNSS Quality', gnss_quality, 'Altitude Delta, Rapid Update', '', '129028')

    # direction | Offset: 26, Length: 2, Resolution: 1, Field Type: NUMBER
    direction_raw = decode_number((data_raw >> 26) & 0x3, 2)
    direction = direction_raw * 1
    publish_field(hass, instance_name, 'direction', 'Direction', direction, 'Altitude Delta, Rapid Update', '', '129028')

    # reserved | Offset: 28, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 28) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Altitude Delta, Rapid Update', '', '129028')

    # cog | Offset: 32, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'Altitude Delta, Rapid Update', 'rad', '129028')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'Altitude Delta, Rapid Update', 'Deg', '129028')

    # altitude_delta | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    altitude_delta_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    if altitude_delta_raw & (1 << (16 - 1)):
        altitude_delta_raw -= (1 << 16)
    altitude_delta = altitude_delta_raw * 1
    publish_field(hass, instance_name, 'altitude_delta', 'Altitude Delta', altitude_delta, 'Altitude Delta, Rapid Update', '', '129028')

def process_pgn_129029(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129029."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS Position Data', '', '129029')

    # date | Offset: 8, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 8) & 0xFFFF
    date = decode_date(date_raw * 1)
    publish_field(hass, instance_name, 'date', 'Date', date, 'GNSS Position Data', 'd', '129029')

    # time | Offset: 24, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 24) & 0xFFFFFFFF
    time = decode_time(time_raw * 0.0001)
    publish_field(hass, instance_name, 'time', 'Time', time, 'GNSS Position Data', 's', '129029')

    # latitude | Offset: 56, Length: 64, Resolution: 1e-16, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 56) & 0xFFFFFFFFFFFFFFFF, 64)
    if latitude_raw & (1 << (64 - 1)):
        latitude_raw -= (1 << 64)
    latitude = latitude_raw * 1e-16
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'GNSS Position Data', 'deg', '129029')

    # longitude | Offset: 120, Length: 64, Resolution: 1e-16, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 120) & 0xFFFFFFFFFFFFFFFF, 64)
    if longitude_raw & (1 << (64 - 1)):
        longitude_raw -= (1 << 64)
    longitude = longitude_raw * 1e-16
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'GNSS Position Data', 'deg', '129029')

    # altitude | Offset: 184, Length: 64, Resolution: 1e-06, Field Type: NUMBER
    altitude_raw = decode_number((data_raw >> 184) & 0xFFFFFFFFFFFFFFFF, 64)
    if altitude_raw & (1 << (64 - 1)):
        altitude_raw -= (1 << 64)
    altitude = altitude_raw * 1e-06
    publish_field(hass, instance_name, 'altitude', 'Altitude', altitude, 'GNSS Position Data', 'm', '129029')

    # gnss_type | Offset: 248, Length: 4, Resolution: 1, Field Type: LOOKUP
    gnss_type_raw = (data_raw >> 248) & 0xF
    gnss_type = gnss_type_raw * 1
    publish_field(hass, instance_name, 'gnss_type', 'GNSS type', gnss_type, 'GNSS Position Data', '', '129029')

    # method | Offset: 252, Length: 4, Resolution: 1, Field Type: LOOKUP
    method_raw = (data_raw >> 252) & 0xF
    method = method_raw * 1
    publish_field(hass, instance_name, 'method', 'Method', method, 'GNSS Position Data', '', '129029')

    # integrity | Offset: 256, Length: 2, Resolution: 1, Field Type: LOOKUP
    integrity_raw = (data_raw >> 256) & 0x3
    integrity = integrity_raw * 1
    publish_field(hass, instance_name, 'integrity', 'Integrity', integrity, 'GNSS Position Data', '', '129029')

    # reserved | Offset: 258, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 258) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS Position Data', '', '129029')

    # number_of_svs | Offset: 264, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_svs_raw = decode_number((data_raw >> 264) & 0xFF, 8)
    number_of_svs = number_of_svs_raw * 1
    publish_field(hass, instance_name, 'number_of_svs', 'Number of SVs', number_of_svs, 'GNSS Position Data', '', '129029')

    # hdop | Offset: 272, Length: 16, Resolution: 0.01, Field Type: NUMBER
    hdop_raw = decode_number((data_raw >> 272) & 0xFFFF, 16)
    if hdop_raw & (1 << (16 - 1)):
        hdop_raw -= (1 << 16)
    hdop = hdop_raw * 0.01
    publish_field(hass, instance_name, 'hdop', 'HDOP', hdop, 'GNSS Position Data', '', '129029')

    # pdop | Offset: 288, Length: 16, Resolution: 0.01, Field Type: NUMBER
    pdop_raw = decode_number((data_raw >> 288) & 0xFFFF, 16)
    if pdop_raw & (1 << (16 - 1)):
        pdop_raw -= (1 << 16)
    pdop = pdop_raw * 0.01
    publish_field(hass, instance_name, 'pdop', 'PDOP', pdop, 'GNSS Position Data', '', '129029')

    # geoidal_separation | Offset: 304, Length: 32, Resolution: 0.01, Field Type: NUMBER
    geoidal_separation_raw = decode_number((data_raw >> 304) & 0xFFFFFFFF, 32)
    if geoidal_separation_raw & (1 << (32 - 1)):
        geoidal_separation_raw -= (1 << 32)
    geoidal_separation = geoidal_separation_raw * 0.01
    publish_field(hass, instance_name, 'geoidal_separation', 'Geoidal Separation', geoidal_separation, 'GNSS Position Data', 'm', '129029')

    # reference_stations | Offset: 336, Length: 8, Resolution: 1, Field Type: NUMBER
    reference_stations_raw = decode_number((data_raw >> 336) & 0xFF, 8)
    reference_stations = reference_stations_raw * 1
    publish_field(hass, instance_name, 'reference_stations', 'Reference Stations', reference_stations, 'GNSS Position Data', '', '129029')

    # reference_station_type | Offset: 344, Length: 4, Resolution: 1, Field Type: LOOKUP
    reference_station_type_raw = (data_raw >> 344) & 0xF
    reference_station_type = reference_station_type_raw * 1
    publish_field(hass, instance_name, 'reference_station_type', 'Reference Station Type', reference_station_type, 'GNSS Position Data', '', '129029')

    # reference_station_id | Offset: 348, Length: 12, Resolution: 1, Field Type: NUMBER
    reference_station_id_raw = decode_number((data_raw >> 348) & 0xFFF, 12)
    reference_station_id = reference_station_id_raw * 1
    publish_field(hass, instance_name, 'reference_station_id', 'Reference Station ID', reference_station_id, 'GNSS Position Data', '', '129029')

    # age_of_dgnss_corrections | Offset: 360, Length: 16, Resolution: 0.01, Field Type: TIME
    age_of_dgnss_corrections_raw = (data_raw >> 360) & 0xFFFF
    age_of_dgnss_corrections = decode_time(age_of_dgnss_corrections_raw * 0.01)
    publish_field(hass, instance_name, 'age_of_dgnss_corrections', 'Age of DGNSS Corrections', age_of_dgnss_corrections, 'GNSS Position Data', 's', '129029')

def process_pgn_129033(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129033."""
    # date | Offset: 0, Length: 16, Resolution: 1, Field Type: DATE
    date_raw = (data_raw >> 0) & 0xFFFF
    date = decode_date(date_raw * 1)
    publish_field(hass, instance_name, 'date', 'Date', date, 'Time & Date', 'd', '129033')

    # time | Offset: 16, Length: 32, Resolution: 0.0001, Field Type: TIME
    time_raw = (data_raw >> 16) & 0xFFFFFFFF
    time = decode_time(time_raw * 0.0001)
    publish_field(hass, instance_name, 'time', 'Time', time, 'Time & Date', 's', '129033')

    # local_offset | Offset: 48, Length: 16, Resolution: 60, Field Type: TIME
    local_offset_raw = (data_raw >> 48) & 0xFFFF
    if local_offset_raw & (1 << (16 - 1)):
        local_offset_raw -= (1 << 16)
    local_offset = decode_time(local_offset_raw * 60)
    publish_field(hass, instance_name, 'local_offset', 'Local Offset', local_offset, 'Time & Date', 's', '129033')

def process_pgn_129038(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129038."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Class A Position Report', '', '129038')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Class A Position Report', '', '129038')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS Class A Position Report', '', '129038')

    # longitude | Offset: 40, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'AIS Class A Position Report', 'deg', '129038')

    # latitude | Offset: 72, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 72) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'AIS Class A Position Report', 'deg', '129038')

    # position_accuracy | Offset: 104, Length: 1, Resolution: 1, Field Type: LOOKUP
    position_accuracy_raw = (data_raw >> 104) & 0x1
    position_accuracy = position_accuracy_raw * 1
    publish_field(hass, instance_name, 'position_accuracy', 'Position Accuracy', position_accuracy, 'AIS Class A Position Report', '', '129038')

    # raim | Offset: 105, Length: 1, Resolution: 1, Field Type: LOOKUP
    raim_raw = (data_raw >> 105) & 0x1
    raim = raim_raw * 1
    publish_field(hass, instance_name, 'raim', 'RAIM', raim, 'AIS Class A Position Report', '', '129038')

    # time_stamp | Offset: 106, Length: 6, Resolution: 1, Field Type: LOOKUP
    time_stamp_raw = (data_raw >> 106) & 0x3F
    time_stamp = time_stamp_raw * 1
    publish_field(hass, instance_name, 'time_stamp', 'Time Stamp', time_stamp, 'AIS Class A Position Report', '', '129038')

    # cog | Offset: 112, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'AIS Class A Position Report', 'rad', '129038')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'AIS Class A Position Report', 'Deg', '129038')

    # sog | Offset: 128, Length: 16, Resolution: 0.01, Field Type: NUMBER
    sog_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    sog = sog_raw * 0.01
    publish_field(hass, instance_name, 'sog', 'SOG', sog, 'AIS Class A Position Report', 'm/s', '129038')
    publish_field(hass, instance_name, 'sog_knots', 'SOG Knots', mps_to_knots(sog), 'AIS Class A Position Report', 'Kn', '129038')

    # communication_state | Offset: 144, Length: 19, Resolution: 1, Field Type: BINARY
    communication_state_raw = (data_raw >> 144) & 0x7FFFF
    communication_state = communication_state_raw * 1
    publish_field(hass, instance_name, 'communication_state', 'Communication State', communication_state, 'AIS Class A Position Report', '', '129038')

    # ais_transceiver_information | Offset: 163, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 163) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Class A Position Report', '', '129038')

    # heading | Offset: 168, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_raw = decode_number((data_raw >> 168) & 0xFFFF, 16)
    heading = heading_raw * 0.0001
    publish_field(hass, instance_name, 'heading', 'Heading', heading, 'AIS Class A Position Report', 'rad', '129038')
    publish_field(hass, instance_name, 'heading_degrees', 'Heading Degrees', radians_to_degrees(heading), 'AIS Class A Position Report', 'Deg', '129038')

    # rate_of_turn | Offset: 184, Length: 16, Resolution: 3.125e-05, Field Type: NUMBER
    rate_of_turn_raw = decode_number((data_raw >> 184) & 0xFFFF, 16)
    if rate_of_turn_raw & (1 << (16 - 1)):
        rate_of_turn_raw -= (1 << 16)
    rate_of_turn = rate_of_turn_raw * 3.125e-05
    publish_field(hass, instance_name, 'rate_of_turn', 'Rate of Turn', rate_of_turn, 'AIS Class A Position Report', 'rad/s', '129038')

    # nav_status | Offset: 200, Length: 4, Resolution: 1, Field Type: LOOKUP
    nav_status_raw = (data_raw >> 200) & 0xF
    nav_status = nav_status_raw * 1
    publish_field(hass, instance_name, 'nav_status', 'Nav Status', nav_status, 'AIS Class A Position Report', '', '129038')

    # special_maneuver_indicator | Offset: 204, Length: 2, Resolution: 1, Field Type: LOOKUP
    special_maneuver_indicator_raw = (data_raw >> 204) & 0x3
    special_maneuver_indicator = special_maneuver_indicator_raw * 1
    publish_field(hass, instance_name, 'special_maneuver_indicator', 'Special Maneuver Indicator', special_maneuver_indicator, 'AIS Class A Position Report', '', '129038')

    # reserved | Offset: 206, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 206) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class A Position Report', '', '129038')

    # spare | Offset: 208, Length: 3, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 208) & 0x7
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Class A Position Report', '', '129038')

    # reserved | Offset: 211, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 211) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class A Position Report', '', '129038')

    # sequence_id | Offset: 216, Length: 8, Resolution: 1, Field Type: NUMBER
    sequence_id_raw = decode_number((data_raw >> 216) & 0xFF, 8)
    sequence_id = sequence_id_raw * 1
    publish_field(hass, instance_name, 'sequence_id', 'Sequence ID', sequence_id, 'AIS Class A Position Report', '', '129038')

def process_pgn_129039(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129039."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Class B Position Report', '', '129039')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Class B Position Report', '', '129039')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS Class B Position Report', '', '129039')

    # longitude | Offset: 40, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'AIS Class B Position Report', 'deg', '129039')

    # latitude | Offset: 72, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 72) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'AIS Class B Position Report', 'deg', '129039')

    # position_accuracy | Offset: 104, Length: 1, Resolution: 1, Field Type: LOOKUP
    position_accuracy_raw = (data_raw >> 104) & 0x1
    position_accuracy = position_accuracy_raw * 1
    publish_field(hass, instance_name, 'position_accuracy', 'Position Accuracy', position_accuracy, 'AIS Class B Position Report', '', '129039')

    # raim | Offset: 105, Length: 1, Resolution: 1, Field Type: LOOKUP
    raim_raw = (data_raw >> 105) & 0x1
    raim = raim_raw * 1
    publish_field(hass, instance_name, 'raim', 'RAIM', raim, 'AIS Class B Position Report', '', '129039')

    # time_stamp | Offset: 106, Length: 6, Resolution: 1, Field Type: LOOKUP
    time_stamp_raw = (data_raw >> 106) & 0x3F
    time_stamp = time_stamp_raw * 1
    publish_field(hass, instance_name, 'time_stamp', 'Time Stamp', time_stamp, 'AIS Class B Position Report', '', '129039')

    # cog | Offset: 112, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'AIS Class B Position Report', 'rad', '129039')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'AIS Class B Position Report', 'Deg', '129039')

    # sog | Offset: 128, Length: 16, Resolution: 0.01, Field Type: NUMBER
    sog_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    sog = sog_raw * 0.01
    publish_field(hass, instance_name, 'sog', 'SOG', sog, 'AIS Class B Position Report', 'm/s', '129039')
    publish_field(hass, instance_name, 'sog_knots', 'SOG Knots', mps_to_knots(sog), 'AIS Class B Position Report', 'Kn', '129039')

    # communication_state | Offset: 144, Length: 19, Resolution: 1, Field Type: BINARY
    communication_state_raw = (data_raw >> 144) & 0x7FFFF
    communication_state = communication_state_raw * 1
    publish_field(hass, instance_name, 'communication_state', 'Communication State', communication_state, 'AIS Class B Position Report', '', '129039')

    # ais_transceiver_information | Offset: 163, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 163) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Class B Position Report', '', '129039')

    # heading | Offset: 168, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_raw = decode_number((data_raw >> 168) & 0xFFFF, 16)
    heading = heading_raw * 0.0001
    publish_field(hass, instance_name, 'heading', 'Heading', heading, 'AIS Class B Position Report', 'rad', '129039')
    publish_field(hass, instance_name, 'heading_degrees', 'Heading Degrees', radians_to_degrees(heading), 'AIS Class B Position Report', 'Deg', '129039')

    # regional_application | Offset: 184, Length: 8, Resolution: 1, Field Type: SPARE
    regional_application_raw = (data_raw >> 184) & 0xFF
    regional_application = regional_application_raw * 1
    publish_field(hass, instance_name, 'regional_application', 'Regional Application', regional_application, 'AIS Class B Position Report', '', '129039')

    # regional_application_b | Offset: 192, Length: 2, Resolution: 1, Field Type: SPARE
    regional_application_b_raw = (data_raw >> 192) & 0x3
    regional_application_b = regional_application_b_raw * 1
    publish_field(hass, instance_name, 'regional_application_b', 'Regional Application B', regional_application_b, 'AIS Class B Position Report', '', '129039')

    # unit_type | Offset: 194, Length: 1, Resolution: 1, Field Type: LOOKUP
    unit_type_raw = (data_raw >> 194) & 0x1
    unit_type = unit_type_raw * 1
    publish_field(hass, instance_name, 'unit_type', 'Unit type', unit_type, 'AIS Class B Position Report', '', '129039')

    # integrated_display | Offset: 195, Length: 1, Resolution: 1, Field Type: LOOKUP
    integrated_display_raw = (data_raw >> 195) & 0x1
    integrated_display = integrated_display_raw * 1
    publish_field(hass, instance_name, 'integrated_display', 'Integrated Display', integrated_display, 'AIS Class B Position Report', '', '129039')

    # dsc | Offset: 196, Length: 1, Resolution: 1, Field Type: LOOKUP
    dsc_raw = (data_raw >> 196) & 0x1
    dsc = dsc_raw * 1
    publish_field(hass, instance_name, 'dsc', 'DSC', dsc, 'AIS Class B Position Report', '', '129039')

    # band | Offset: 197, Length: 1, Resolution: 1, Field Type: LOOKUP
    band_raw = (data_raw >> 197) & 0x1
    band = band_raw * 1
    publish_field(hass, instance_name, 'band', 'Band', band, 'AIS Class B Position Report', '', '129039')

    # can_handle_msg_22 | Offset: 198, Length: 1, Resolution: 1, Field Type: LOOKUP
    can_handle_msg_22_raw = (data_raw >> 198) & 0x1
    can_handle_msg_22 = can_handle_msg_22_raw * 1
    publish_field(hass, instance_name, 'can_handle_msg_22', 'Can handle Msg 22', can_handle_msg_22, 'AIS Class B Position Report', '', '129039')

    # ais_mode | Offset: 199, Length: 1, Resolution: 1, Field Type: LOOKUP
    ais_mode_raw = (data_raw >> 199) & 0x1
    ais_mode = ais_mode_raw * 1
    publish_field(hass, instance_name, 'ais_mode', 'AIS mode', ais_mode, 'AIS Class B Position Report', '', '129039')

    # ais_communication_state | Offset: 200, Length: 1, Resolution: 1, Field Type: LOOKUP
    ais_communication_state_raw = (data_raw >> 200) & 0x1
    ais_communication_state = ais_communication_state_raw * 1
    publish_field(hass, instance_name, 'ais_communication_state', 'AIS communication state', ais_communication_state, 'AIS Class B Position Report', '', '129039')

    # reserved | Offset: 201, Length: 15, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 201) & 0x7FFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B Position Report', '', '129039')

def process_pgn_129040(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129040."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Class B Extended Position Report', '', '129040')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Class B Extended Position Report', '', '129040')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS Class B Extended Position Report', '', '129040')

    # longitude | Offset: 40, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'AIS Class B Extended Position Report', 'deg', '129040')

    # latitude | Offset: 72, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 72) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'AIS Class B Extended Position Report', 'deg', '129040')

    # position_accuracy | Offset: 104, Length: 1, Resolution: 1, Field Type: LOOKUP
    position_accuracy_raw = (data_raw >> 104) & 0x1
    position_accuracy = position_accuracy_raw * 1
    publish_field(hass, instance_name, 'position_accuracy', 'Position Accuracy', position_accuracy, 'AIS Class B Extended Position Report', '', '129040')

    # raim | Offset: 105, Length: 1, Resolution: 1, Field Type: LOOKUP
    raim_raw = (data_raw >> 105) & 0x1
    raim = raim_raw * 1
    publish_field(hass, instance_name, 'raim', 'RAIM', raim, 'AIS Class B Extended Position Report', '', '129040')

    # time_stamp | Offset: 106, Length: 6, Resolution: 1, Field Type: LOOKUP
    time_stamp_raw = (data_raw >> 106) & 0x3F
    time_stamp = time_stamp_raw * 1
    publish_field(hass, instance_name, 'time_stamp', 'Time Stamp', time_stamp, 'AIS Class B Extended Position Report', '', '129040')

    # cog | Offset: 112, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'AIS Class B Extended Position Report', 'rad', '129040')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'AIS Class B Extended Position Report', 'Deg', '129040')

    # sog | Offset: 128, Length: 16, Resolution: 0.01, Field Type: NUMBER
    sog_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    sog = sog_raw * 0.01
    publish_field(hass, instance_name, 'sog', 'SOG', sog, 'AIS Class B Extended Position Report', 'm/s', '129040')
    publish_field(hass, instance_name, 'sog_knots', 'SOG Knots', mps_to_knots(sog), 'AIS Class B Extended Position Report', 'Kn', '129040')

    # regional_application | Offset: 144, Length: 8, Resolution: 1, Field Type: SPARE
    regional_application_raw = (data_raw >> 144) & 0xFF
    regional_application = regional_application_raw * 1
    publish_field(hass, instance_name, 'regional_application', 'Regional Application', regional_application, 'AIS Class B Extended Position Report', '', '129040')

    # regional_application_b | Offset: 152, Length: 4, Resolution: 1, Field Type: SPARE
    regional_application_b_raw = (data_raw >> 152) & 0xF
    regional_application_b = regional_application_b_raw * 1
    publish_field(hass, instance_name, 'regional_application_b', 'Regional Application B', regional_application_b, 'AIS Class B Extended Position Report', '', '129040')

    # reserved | Offset: 156, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 156) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B Extended Position Report', '', '129040')

    # type_of_ship | Offset: 160, Length: 8, Resolution: 1, Field Type: LOOKUP
    type_of_ship_raw = (data_raw >> 160) & 0xFF
    type_of_ship = type_of_ship_raw * 1
    publish_field(hass, instance_name, 'type_of_ship', 'Type of ship', type_of_ship, 'AIS Class B Extended Position Report', '', '129040')

    # true_heading | Offset: 168, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    true_heading_raw = decode_number((data_raw >> 168) & 0xFFFF, 16)
    true_heading = true_heading_raw * 0.0001
    publish_field(hass, instance_name, 'true_heading', 'True Heading', true_heading, 'AIS Class B Extended Position Report', 'rad', '129040')
    publish_field(hass, instance_name, 'true_heading_degrees', 'True Heading Degrees', radians_to_degrees(true_heading), 'AIS Class B Extended Position Report', 'Deg', '129040')

    # reserved | Offset: 184, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 184) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B Extended Position Report', '', '129040')

    # gnss_type | Offset: 188, Length: 4, Resolution: 1, Field Type: LOOKUP
    gnss_type_raw = (data_raw >> 188) & 0xF
    gnss_type = gnss_type_raw * 1
    publish_field(hass, instance_name, 'gnss_type', 'GNSS type', gnss_type, 'AIS Class B Extended Position Report', '', '129040')

    # length | Offset: 192, Length: 16, Resolution: 0.1, Field Type: NUMBER
    length_raw = decode_number((data_raw >> 192) & 0xFFFF, 16)
    length = length_raw * 0.1
    publish_field(hass, instance_name, 'length', 'Length', length, 'AIS Class B Extended Position Report', 'm', '129040')

    # beam | Offset: 208, Length: 16, Resolution: 0.1, Field Type: NUMBER
    beam_raw = decode_number((data_raw >> 208) & 0xFFFF, 16)
    beam = beam_raw * 0.1
    publish_field(hass, instance_name, 'beam', 'Beam', beam, 'AIS Class B Extended Position Report', 'm', '129040')

    # position_reference_from_starboard | Offset: 224, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_starboard_raw = decode_number((data_raw >> 224) & 0xFFFF, 16)
    position_reference_from_starboard = position_reference_from_starboard_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_starboard', 'Position reference from Starboard', position_reference_from_starboard, 'AIS Class B Extended Position Report', 'm', '129040')

    # position_reference_from_bow | Offset: 240, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_bow_raw = decode_number((data_raw >> 240) & 0xFFFF, 16)
    position_reference_from_bow = position_reference_from_bow_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_bow', 'Position reference from Bow', position_reference_from_bow, 'AIS Class B Extended Position Report', 'm', '129040')

    # name | Offset: 256, Length: 160, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # dte | Offset: 416, Length: 1, Resolution: 1, Field Type: LOOKUP
    dte_raw = (data_raw >> 416) & 0x1
    dte = dte_raw * 1
    publish_field(hass, instance_name, 'dte', 'DTE', dte, 'AIS Class B Extended Position Report', '', '129040')

    # ais_mode | Offset: 417, Length: 1, Resolution: 1, Field Type: LOOKUP
    ais_mode_raw = (data_raw >> 417) & 0x1
    ais_mode = ais_mode_raw * 1
    publish_field(hass, instance_name, 'ais_mode', 'AIS mode', ais_mode, 'AIS Class B Extended Position Report', '', '129040')

    # spare | Offset: 418, Length: 4, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 418) & 0xF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Class B Extended Position Report', '', '129040')

    # ais_transceiver_information | Offset: 422, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 422) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Class B Extended Position Report', '', '129040')

    # reserved | Offset: 427, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 427) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B Extended Position Report', '', '129040')

def process_pgn_129041(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129041."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # longitude | Offset: 40, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'AIS Aids to Navigation (AtoN) Report', 'deg', '129041')

    # latitude | Offset: 72, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 72) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'AIS Aids to Navigation (AtoN) Report', 'deg', '129041')

    # position_accuracy | Offset: 104, Length: 1, Resolution: 1, Field Type: LOOKUP
    position_accuracy_raw = (data_raw >> 104) & 0x1
    position_accuracy = position_accuracy_raw * 1
    publish_field(hass, instance_name, 'position_accuracy', 'Position Accuracy', position_accuracy, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # raim | Offset: 105, Length: 1, Resolution: 1, Field Type: LOOKUP
    raim_raw = (data_raw >> 105) & 0x1
    raim = raim_raw * 1
    publish_field(hass, instance_name, 'raim', 'RAIM', raim, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # time_stamp | Offset: 106, Length: 6, Resolution: 1, Field Type: LOOKUP
    time_stamp_raw = (data_raw >> 106) & 0x3F
    time_stamp = time_stamp_raw * 1
    publish_field(hass, instance_name, 'time_stamp', 'Time Stamp', time_stamp, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # length_diameter | Offset: 112, Length: 16, Resolution: 0.1, Field Type: NUMBER
    length_diameter_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    length_diameter = length_diameter_raw * 0.1
    publish_field(hass, instance_name, 'length_diameter', 'Length/Diameter', length_diameter, 'AIS Aids to Navigation (AtoN) Report', 'm', '129041')

    # beam_diameter | Offset: 128, Length: 16, Resolution: 0.1, Field Type: NUMBER
    beam_diameter_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    beam_diameter = beam_diameter_raw * 0.1
    publish_field(hass, instance_name, 'beam_diameter', 'Beam/Diameter', beam_diameter, 'AIS Aids to Navigation (AtoN) Report', 'm', '129041')

    # position_reference_from_starboard_edge | Offset: 144, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_starboard_edge_raw = decode_number((data_raw >> 144) & 0xFFFF, 16)
    position_reference_from_starboard_edge = position_reference_from_starboard_edge_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_starboard_edge', 'Position Reference from Starboard Edge', position_reference_from_starboard_edge, 'AIS Aids to Navigation (AtoN) Report', 'm', '129041')

    # position_reference_from_true_north_facing_edge | Offset: 160, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_true_north_facing_edge_raw = decode_number((data_raw >> 160) & 0xFFFF, 16)
    position_reference_from_true_north_facing_edge = position_reference_from_true_north_facing_edge_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_true_north_facing_edge', 'Position Reference from True North Facing Edge', position_reference_from_true_north_facing_edge, 'AIS Aids to Navigation (AtoN) Report', 'm', '129041')

    # aton_type | Offset: 176, Length: 5, Resolution: 1, Field Type: LOOKUP
    aton_type_raw = (data_raw >> 176) & 0x1F
    aton_type = aton_type_raw * 1
    publish_field(hass, instance_name, 'aton_type', 'AtoN Type', aton_type, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # off_position_indicator | Offset: 181, Length: 1, Resolution: 1, Field Type: LOOKUP
    off_position_indicator_raw = (data_raw >> 181) & 0x1
    off_position_indicator = off_position_indicator_raw * 1
    publish_field(hass, instance_name, 'off_position_indicator', 'Off Position Indicator', off_position_indicator, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # virtual_aton_flag | Offset: 182, Length: 1, Resolution: 1, Field Type: LOOKUP
    virtual_aton_flag_raw = (data_raw >> 182) & 0x1
    virtual_aton_flag = virtual_aton_flag_raw * 1
    publish_field(hass, instance_name, 'virtual_aton_flag', 'Virtual AtoN Flag', virtual_aton_flag, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # assigned_mode_flag | Offset: 183, Length: 1, Resolution: 1, Field Type: LOOKUP
    assigned_mode_flag_raw = (data_raw >> 183) & 0x1
    assigned_mode_flag = assigned_mode_flag_raw * 1
    publish_field(hass, instance_name, 'assigned_mode_flag', 'Assigned Mode Flag', assigned_mode_flag, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # spare | Offset: 184, Length: 1, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 184) & 0x1
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # position_fixing_device_type | Offset: 185, Length: 4, Resolution: 1, Field Type: LOOKUP
    position_fixing_device_type_raw = (data_raw >> 185) & 0xF
    position_fixing_device_type = position_fixing_device_type_raw * 1
    publish_field(hass, instance_name, 'position_fixing_device_type', 'Position Fixing Device Type', position_fixing_device_type, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # reserved | Offset: 189, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 189) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # aton_status | Offset: 192, Length: 8, Resolution: 1, Field Type: BINARY
    aton_status_raw = (data_raw >> 192) & 0xFF
    aton_status = aton_status_raw * 1
    publish_field(hass, instance_name, 'aton_status', 'AtoN Status', aton_status, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # ais_transceiver_information | Offset: 200, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 200) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

    # reserved | Offset: 205, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 205) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Aids to Navigation (AtoN) Report', '', '129041')

def process_pgn_129044(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129044."""
    # local_datum | Offset: 0, Length: 32, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # delta_latitude | Offset: 32, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    delta_latitude_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if delta_latitude_raw & (1 << (32 - 1)):
        delta_latitude_raw -= (1 << 32)
    delta_latitude = delta_latitude_raw * 1e-07
    publish_field(hass, instance_name, 'delta_latitude', 'Delta Latitude', delta_latitude, 'Datum', 'deg', '129044')

    # delta_longitude | Offset: 64, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    delta_longitude_raw = decode_number((data_raw >> 64) & 0xFFFFFFFF, 32)
    if delta_longitude_raw & (1 << (32 - 1)):
        delta_longitude_raw -= (1 << 32)
    delta_longitude = delta_longitude_raw * 1e-07
    publish_field(hass, instance_name, 'delta_longitude', 'Delta Longitude', delta_longitude, 'Datum', 'deg', '129044')

    # delta_altitude | Offset: 96, Length: 32, Resolution: 0.01, Field Type: NUMBER
    delta_altitude_raw = decode_number((data_raw >> 96) & 0xFFFFFFFF, 32)
    if delta_altitude_raw & (1 << (32 - 1)):
        delta_altitude_raw -= (1 << 32)
    delta_altitude = delta_altitude_raw * 0.01
    publish_field(hass, instance_name, 'delta_altitude', 'Delta Altitude', delta_altitude, 'Datum', 'm', '129044')

    # reference_datum | Offset: 128, Length: 32, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_129045(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129045."""
    # delta_x | Offset: 0, Length: 32, Resolution: 0.01, Field Type: NUMBER
    delta_x_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if delta_x_raw & (1 << (32 - 1)):
        delta_x_raw -= (1 << 32)
    delta_x = delta_x_raw * 0.01
    publish_field(hass, instance_name, 'delta_x', 'Delta X', delta_x, 'User Datum', 'm', '129045')

    # delta_y | Offset: 32, Length: 32, Resolution: 0.01, Field Type: NUMBER
    delta_y_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if delta_y_raw & (1 << (32 - 1)):
        delta_y_raw -= (1 << 32)
    delta_y = delta_y_raw * 0.01
    publish_field(hass, instance_name, 'delta_y', 'Delta Y', delta_y, 'User Datum', 'm', '129045')

    # delta_z | Offset: 64, Length: 32, Resolution: 0.01, Field Type: NUMBER
    delta_z_raw = decode_number((data_raw >> 64) & 0xFFFFFFFF, 32)
    if delta_z_raw & (1 << (32 - 1)):
        delta_z_raw -= (1 << 32)
    delta_z = delta_z_raw * 0.01
    publish_field(hass, instance_name, 'delta_z', 'Delta Z', delta_z, 'User Datum', 'm', '129045')

    # rotation_in_x | Offset: 96, Length: 32, Resolution: 1, Field Type: FLOAT
    rotation_in_x_raw = decode_float((data_raw >> 96) & 0xFFFFFFFF, 32)
    if rotation_in_x_raw & (1 << (32 - 1)):
        rotation_in_x_raw -= (1 << 32)
    rotation_in_x = rotation_in_x_raw * 1
    publish_field(hass, instance_name, 'rotation_in_x', 'Rotation in X', rotation_in_x, 'User Datum', '', '129045')

    # rotation_in_y | Offset: 128, Length: 32, Resolution: 1, Field Type: FLOAT
    rotation_in_y_raw = decode_float((data_raw >> 128) & 0xFFFFFFFF, 32)
    if rotation_in_y_raw & (1 << (32 - 1)):
        rotation_in_y_raw -= (1 << 32)
    rotation_in_y = rotation_in_y_raw * 1
    publish_field(hass, instance_name, 'rotation_in_y', 'Rotation in Y', rotation_in_y, 'User Datum', '', '129045')

    # rotation_in_z | Offset: 160, Length: 32, Resolution: 1, Field Type: FLOAT
    rotation_in_z_raw = decode_float((data_raw >> 160) & 0xFFFFFFFF, 32)
    if rotation_in_z_raw & (1 << (32 - 1)):
        rotation_in_z_raw -= (1 << 32)
    rotation_in_z = rotation_in_z_raw * 1
    publish_field(hass, instance_name, 'rotation_in_z', 'Rotation in Z', rotation_in_z, 'User Datum', '', '129045')

    # scale | Offset: 192, Length: 32, Resolution: 1, Field Type: FLOAT
    scale_raw = decode_float((data_raw >> 192) & 0xFFFFFFFF, 32)
    if scale_raw & (1 << (32 - 1)):
        scale_raw -= (1 << 32)
    scale = scale_raw * 1
    publish_field(hass, instance_name, 'scale', 'Scale', scale, 'User Datum', 'ppm', '129045')

    # ellipsoid_semi_major_axis | Offset: 224, Length: 32, Resolution: 0.01, Field Type: NUMBER
    ellipsoid_semi_major_axis_raw = decode_number((data_raw >> 224) & 0xFFFFFFFF, 32)
    if ellipsoid_semi_major_axis_raw & (1 << (32 - 1)):
        ellipsoid_semi_major_axis_raw -= (1 << 32)
    ellipsoid_semi_major_axis = ellipsoid_semi_major_axis_raw * 0.01
    publish_field(hass, instance_name, 'ellipsoid_semi_major_axis', 'Ellipsoid Semi-major Axis', ellipsoid_semi_major_axis, 'User Datum', 'm', '129045')

    # ellipsoid_flattening_inverse | Offset: 256, Length: 32, Resolution: 1, Field Type: FLOAT
    ellipsoid_flattening_inverse_raw = decode_float((data_raw >> 256) & 0xFFFFFFFF, 32)
    if ellipsoid_flattening_inverse_raw & (1 << (32 - 1)):
        ellipsoid_flattening_inverse_raw -= (1 << 32)
    ellipsoid_flattening_inverse = ellipsoid_flattening_inverse_raw * 1
    publish_field(hass, instance_name, 'ellipsoid_flattening_inverse', 'Ellipsoid Flattening Inverse', ellipsoid_flattening_inverse, 'User Datum', '', '129045')

    # datum_name | Offset: 288, Length: 32, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_129283(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129283."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Cross Track Error', '', '129283')

    # xte_mode | Offset: 8, Length: 4, Resolution: 1, Field Type: LOOKUP
    xte_mode_raw = (data_raw >> 8) & 0xF
    xte_mode = xte_mode_raw * 1
    publish_field(hass, instance_name, 'xte_mode', 'XTE mode', xte_mode, 'Cross Track Error', '', '129283')

    # reserved | Offset: 12, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Cross Track Error', '', '129283')

    # navigation_terminated | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    navigation_terminated_raw = (data_raw >> 14) & 0x3
    navigation_terminated = navigation_terminated_raw * 1
    publish_field(hass, instance_name, 'navigation_terminated', 'Navigation Terminated', navigation_terminated, 'Cross Track Error', '', '129283')

    # xte | Offset: 16, Length: 32, Resolution: 0.01, Field Type: NUMBER
    xte_raw = decode_number((data_raw >> 16) & 0xFFFFFFFF, 32)
    if xte_raw & (1 << (32 - 1)):
        xte_raw -= (1 << 32)
    xte = xte_raw * 0.01
    publish_field(hass, instance_name, 'xte', 'XTE', xte, 'Cross Track Error', 'm', '129283')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Cross Track Error', '', '129283')

def process_pgn_129284(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129284."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Navigation Data', '', '129284')

    # distance_to_waypoint | Offset: 8, Length: 32, Resolution: 0.01, Field Type: NUMBER
    distance_to_waypoint_raw = decode_number((data_raw >> 8) & 0xFFFFFFFF, 32)
    distance_to_waypoint = distance_to_waypoint_raw * 0.01
    publish_field(hass, instance_name, 'distance_to_waypoint', 'Distance to Waypoint', distance_to_waypoint, 'Navigation Data', 'm', '129284')

    # course_bearing_reference | Offset: 40, Length: 2, Resolution: 1, Field Type: LOOKUP
    course_bearing_reference_raw = (data_raw >> 40) & 0x3
    course_bearing_reference = course_bearing_reference_raw * 1
    publish_field(hass, instance_name, 'course_bearing_reference', 'Course/Bearing reference', course_bearing_reference, 'Navigation Data', '', '129284')

    # perpendicular_crossed | Offset: 42, Length: 2, Resolution: 1, Field Type: LOOKUP
    perpendicular_crossed_raw = (data_raw >> 42) & 0x3
    perpendicular_crossed = perpendicular_crossed_raw * 1
    publish_field(hass, instance_name, 'perpendicular_crossed', 'Perpendicular Crossed', perpendicular_crossed, 'Navigation Data', '', '129284')

    # arrival_circle_entered | Offset: 44, Length: 2, Resolution: 1, Field Type: LOOKUP
    arrival_circle_entered_raw = (data_raw >> 44) & 0x3
    arrival_circle_entered = arrival_circle_entered_raw * 1
    publish_field(hass, instance_name, 'arrival_circle_entered', 'Arrival Circle Entered', arrival_circle_entered, 'Navigation Data', '', '129284')

    # calculation_type | Offset: 46, Length: 2, Resolution: 1, Field Type: LOOKUP
    calculation_type_raw = (data_raw >> 46) & 0x3
    calculation_type = calculation_type_raw * 1
    publish_field(hass, instance_name, 'calculation_type', 'Calculation Type', calculation_type, 'Navigation Data', '', '129284')

    # eta_time | Offset: 48, Length: 32, Resolution: 0.0001, Field Type: TIME
    eta_time_raw = (data_raw >> 48) & 0xFFFFFFFF
    eta_time = decode_time(eta_time_raw * 0.0001)
    publish_field(hass, instance_name, 'eta_time', 'ETA Time', eta_time, 'Navigation Data', 's', '129284')

    # eta_date | Offset: 80, Length: 16, Resolution: 1, Field Type: DATE
    eta_date_raw = (data_raw >> 80) & 0xFFFF
    eta_date = decode_date(eta_date_raw * 1)
    publish_field(hass, instance_name, 'eta_date', 'ETA Date', eta_date, 'Navigation Data', 'd', '129284')

    # bearing__origin_to_destination_waypoint | Offset: 96, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    bearing__origin_to_destination_waypoint_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    bearing__origin_to_destination_waypoint = bearing__origin_to_destination_waypoint_raw * 0.0001
    publish_field(hass, instance_name, 'bearing__origin_to_destination_waypoint', 'Bearing, Origin to Destination Waypoint', bearing__origin_to_destination_waypoint, 'Navigation Data', 'rad', '129284')
    publish_field(hass, instance_name, 'bearing__origin_to_destination_waypoint_degrees', 'Bearing, Origin to Destination Waypoint Degrees', radians_to_degrees(bearing__origin_to_destination_waypoint), 'Navigation Data', 'Deg', '129284')

    # bearing__position_to_destination_waypoint | Offset: 112, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    bearing__position_to_destination_waypoint_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    bearing__position_to_destination_waypoint = bearing__position_to_destination_waypoint_raw * 0.0001
    publish_field(hass, instance_name, 'bearing__position_to_destination_waypoint', 'Bearing, Position to Destination Waypoint', bearing__position_to_destination_waypoint, 'Navigation Data', 'rad', '129284')
    publish_field(hass, instance_name, 'bearing__position_to_destination_waypoint_degrees', 'Bearing, Position to Destination Waypoint Degrees', radians_to_degrees(bearing__position_to_destination_waypoint), 'Navigation Data', 'Deg', '129284')

    # origin_waypoint_number | Offset: 128, Length: 32, Resolution: 1, Field Type: NUMBER
    origin_waypoint_number_raw = decode_number((data_raw >> 128) & 0xFFFFFFFF, 32)
    origin_waypoint_number = origin_waypoint_number_raw * 1
    publish_field(hass, instance_name, 'origin_waypoint_number', 'Origin Waypoint Number', origin_waypoint_number, 'Navigation Data', '', '129284')

    # destination_waypoint_number | Offset: 160, Length: 32, Resolution: 1, Field Type: NUMBER
    destination_waypoint_number_raw = decode_number((data_raw >> 160) & 0xFFFFFFFF, 32)
    destination_waypoint_number = destination_waypoint_number_raw * 1
    publish_field(hass, instance_name, 'destination_waypoint_number', 'Destination Waypoint Number', destination_waypoint_number, 'Navigation Data', '', '129284')

    # destination_latitude | Offset: 192, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    destination_latitude_raw = decode_number((data_raw >> 192) & 0xFFFFFFFF, 32)
    if destination_latitude_raw & (1 << (32 - 1)):
        destination_latitude_raw -= (1 << 32)
    destination_latitude = destination_latitude_raw * 1e-07
    publish_field(hass, instance_name, 'destination_latitude', 'Destination Latitude', destination_latitude, 'Navigation Data', 'deg', '129284')

    # destination_longitude | Offset: 224, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    destination_longitude_raw = decode_number((data_raw >> 224) & 0xFFFFFFFF, 32)
    if destination_longitude_raw & (1 << (32 - 1)):
        destination_longitude_raw -= (1 << 32)
    destination_longitude = destination_longitude_raw * 1e-07
    publish_field(hass, instance_name, 'destination_longitude', 'Destination Longitude', destination_longitude, 'Navigation Data', 'deg', '129284')

    # waypoint_closing_velocity | Offset: 256, Length: 16, Resolution: 0.01, Field Type: NUMBER
    waypoint_closing_velocity_raw = decode_number((data_raw >> 256) & 0xFFFF, 16)
    if waypoint_closing_velocity_raw & (1 << (16 - 1)):
        waypoint_closing_velocity_raw -= (1 << 16)
    waypoint_closing_velocity = waypoint_closing_velocity_raw * 0.01
    publish_field(hass, instance_name, 'waypoint_closing_velocity', 'Waypoint Closing Velocity', waypoint_closing_velocity, 'Navigation Data', 'm/s', '129284')
    publish_field(hass, instance_name, 'waypoint_closing_velocity_knots', 'Waypoint Closing Velocity Knots', mps_to_knots(waypoint_closing_velocity), 'Navigation Data', 'Kn', '129284')

def process_pgn_129285(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129285."""
    # start_rps_ | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    start_rps__raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    start_rps_ = start_rps__raw * 1
    publish_field(hass, instance_name, 'start_rps_', 'Start RPS#', start_rps_, 'Navigation - Route/WP Information', '', '129285')

    # nitems | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Navigation - Route/WP Information', '', '129285')

    # database_id | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Navigation - Route/WP Information', '', '129285')

    # route_id | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Navigation - Route/WP Information', '', '129285')

    # navigation_direction_in_route | Offset: 64, Length: 3, Resolution: 1, Field Type: LOOKUP
    navigation_direction_in_route_raw = (data_raw >> 64) & 0x7
    navigation_direction_in_route = navigation_direction_in_route_raw * 1
    publish_field(hass, instance_name, 'navigation_direction_in_route', 'Navigation direction in route', navigation_direction_in_route, 'Navigation - Route/WP Information', '', '129285')

    # supplementary_route_wp_data_available | Offset: 67, Length: 2, Resolution: 1, Field Type: LOOKUP
    supplementary_route_wp_data_available_raw = (data_raw >> 67) & 0x3
    supplementary_route_wp_data_available = supplementary_route_wp_data_available_raw * 1
    publish_field(hass, instance_name, 'supplementary_route_wp_data_available', 'Supplementary Route/WP data available', supplementary_route_wp_data_available, 'Navigation - Route/WP Information', '', '129285')

    # reserved | Offset: 69, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 69) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navigation - Route/WP Information', '', '129285')

def process_pgn_129291(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129291."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Set & Drift, Rapid Update', '', '129291')

    # set_reference | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    set_reference_raw = (data_raw >> 8) & 0x3
    set_reference = set_reference_raw * 1
    publish_field(hass, instance_name, 'set_reference', 'Set Reference', set_reference, 'Set & Drift, Rapid Update', '', '129291')

    # reserved | Offset: 10, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 10) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Set & Drift, Rapid Update', '', '129291')

    # set | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    set_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    set = set_raw * 0.0001
    publish_field(hass, instance_name, 'set', 'Set', set, 'Set & Drift, Rapid Update', 'rad', '129291')
    publish_field(hass, instance_name, 'set_degrees', 'Set Degrees', radians_to_degrees(set), 'Set & Drift, Rapid Update', 'Deg', '129291')

    # drift | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    drift_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    drift = drift_raw * 0.01
    publish_field(hass, instance_name, 'drift', 'Drift', drift, 'Set & Drift, Rapid Update', 'm/s', '129291')
    publish_field(hass, instance_name, 'drift_knots', 'Drift Knots', mps_to_knots(drift), 'Set & Drift, Rapid Update', 'Kn', '129291')

    # reserved | Offset: 48, Length: 16, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 48) & 0xFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Set & Drift, Rapid Update', '', '129291')

def process_pgn_129301(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129301."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Navigation - Route / Time to+from Mark', '', '129301')

    # time_to_mark | Offset: 8, Length: 32, Resolution: 0.001, Field Type: TIME
    time_to_mark_raw = (data_raw >> 8) & 0xFFFFFFFF
    if time_to_mark_raw & (1 << (32 - 1)):
        time_to_mark_raw -= (1 << 32)
    time_to_mark = decode_time(time_to_mark_raw * 0.001)
    publish_field(hass, instance_name, 'time_to_mark', 'Time to mark', time_to_mark, 'Navigation - Route / Time to+from Mark', 's', '129301')

    # mark_type | Offset: 40, Length: 4, Resolution: 1, Field Type: LOOKUP
    mark_type_raw = (data_raw >> 40) & 0xF
    mark_type = mark_type_raw * 1
    publish_field(hass, instance_name, 'mark_type', 'Mark Type', mark_type, 'Navigation - Route / Time to+from Mark', '', '129301')

    # reserved | Offset: 44, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 44) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navigation - Route / Time to+from Mark', '', '129301')

    # mark_id | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    mark_id_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    mark_id = mark_id_raw * 1
    publish_field(hass, instance_name, 'mark_id', 'Mark ID', mark_id, 'Navigation - Route / Time to+from Mark', '', '129301')

def process_pgn_129302(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129302."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Bearing and Distance between two Marks', '', '129302')

    # bearing_reference | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    bearing_reference_raw = (data_raw >> 8) & 0x3
    bearing_reference = bearing_reference_raw * 1
    publish_field(hass, instance_name, 'bearing_reference', 'Bearing Reference', bearing_reference, 'Bearing and Distance between two Marks', '', '129302')

    # calculation_type | Offset: 10, Length: 2, Resolution: 1, Field Type: LOOKUP
    calculation_type_raw = (data_raw >> 10) & 0x3
    calculation_type = calculation_type_raw * 1
    publish_field(hass, instance_name, 'calculation_type', 'Calculation Type', calculation_type, 'Bearing and Distance between two Marks', '', '129302')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Bearing and Distance between two Marks', '', '129302')

    # bearing__origin_to_destination | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    bearing__origin_to_destination_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    bearing__origin_to_destination = bearing__origin_to_destination_raw * 0.0001
    publish_field(hass, instance_name, 'bearing__origin_to_destination', 'Bearing, Origin to Destination', bearing__origin_to_destination, 'Bearing and Distance between two Marks', 'rad', '129302')
    publish_field(hass, instance_name, 'bearing__origin_to_destination_degrees', 'Bearing, Origin to Destination Degrees', radians_to_degrees(bearing__origin_to_destination), 'Bearing and Distance between two Marks', 'Deg', '129302')

    # distance | Offset: 32, Length: 32, Resolution: 0.01, Field Type: NUMBER
    distance_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    distance = distance_raw * 0.01
    publish_field(hass, instance_name, 'distance', 'Distance', distance, 'Bearing and Distance between two Marks', 'm', '129302')

    # origin_mark_type | Offset: 64, Length: 4, Resolution: 1, Field Type: LOOKUP
    origin_mark_type_raw = (data_raw >> 64) & 0xF
    origin_mark_type = origin_mark_type_raw * 1
    publish_field(hass, instance_name, 'origin_mark_type', 'Origin Mark Type', origin_mark_type, 'Bearing and Distance between two Marks', '', '129302')

    # destination_mark_type | Offset: 68, Length: 4, Resolution: 1, Field Type: LOOKUP
    destination_mark_type_raw = (data_raw >> 68) & 0xF
    destination_mark_type = destination_mark_type_raw * 1
    publish_field(hass, instance_name, 'destination_mark_type', 'Destination Mark Type', destination_mark_type, 'Bearing and Distance between two Marks', '', '129302')

    # origin_mark_id | Offset: 72, Length: 32, Resolution: 1, Field Type: NUMBER
    origin_mark_id_raw = decode_number((data_raw >> 72) & 0xFFFFFFFF, 32)
    origin_mark_id = origin_mark_id_raw * 1
    publish_field(hass, instance_name, 'origin_mark_id', 'Origin Mark ID', origin_mark_id, 'Bearing and Distance between two Marks', '', '129302')

    # destination_mark_id | Offset: 104, Length: 32, Resolution: 1, Field Type: NUMBER
    destination_mark_id_raw = decode_number((data_raw >> 104) & 0xFFFFFFFF, 32)
    destination_mark_id = destination_mark_id_raw * 1
    publish_field(hass, instance_name, 'destination_mark_id', 'Destination Mark ID', destination_mark_id, 'Bearing and Distance between two Marks', '', '129302')

def process_pgn_129538(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129538."""
    # sv_elevation_mask | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    sv_elevation_mask_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    sv_elevation_mask = sv_elevation_mask_raw * 1
    publish_field(hass, instance_name, 'sv_elevation_mask', 'SV Elevation Mask', sv_elevation_mask, 'GNSS Control Status', '', '129538')

    # pdop_mask | Offset: 16, Length: 16, Resolution: 0.01, Field Type: NUMBER
    pdop_mask_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    pdop_mask = pdop_mask_raw * 0.01
    publish_field(hass, instance_name, 'pdop_mask', 'PDOP Mask', pdop_mask, 'GNSS Control Status', '', '129538')

    # pdop_switch | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    pdop_switch_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    pdop_switch = pdop_switch_raw * 0.01
    publish_field(hass, instance_name, 'pdop_switch', 'PDOP Switch', pdop_switch, 'GNSS Control Status', '', '129538')

    # snr_mask | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    snr_mask_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    snr_mask = snr_mask_raw * 0.01
    publish_field(hass, instance_name, 'snr_mask', 'SNR Mask', snr_mask, 'GNSS Control Status', 'dB', '129538')

    # gnss_mode__desired_ | Offset: 64, Length: 3, Resolution: 1, Field Type: LOOKUP
    gnss_mode__desired__raw = (data_raw >> 64) & 0x7
    gnss_mode__desired_ = gnss_mode__desired__raw * 1
    publish_field(hass, instance_name, 'gnss_mode__desired_', 'GNSS Mode (desired)', gnss_mode__desired_, 'GNSS Control Status', '', '129538')

    # dgnss_mode__desired_ | Offset: 67, Length: 3, Resolution: 1, Field Type: LOOKUP
    dgnss_mode__desired__raw = (data_raw >> 67) & 0x7
    dgnss_mode__desired_ = dgnss_mode__desired__raw * 1
    publish_field(hass, instance_name, 'dgnss_mode__desired_', 'DGNSS Mode (desired)', dgnss_mode__desired_, 'GNSS Control Status', '', '129538')

    # position_velocity_filter | Offset: 70, Length: 2, Resolution: 1, Field Type: NUMBER
    position_velocity_filter_raw = decode_number((data_raw >> 70) & 0x3, 2)
    position_velocity_filter = position_velocity_filter_raw * 1
    publish_field(hass, instance_name, 'position_velocity_filter', 'Position/Velocity Filter', position_velocity_filter, 'GNSS Control Status', '', '129538')

    # max_correction_age | Offset: 72, Length: 16, Resolution: 1, Field Type: NUMBER
    max_correction_age_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    max_correction_age = max_correction_age_raw * 1
    publish_field(hass, instance_name, 'max_correction_age', 'Max Correction Age', max_correction_age, 'GNSS Control Status', '', '129538')

    # antenna_altitude_for_2d_mode | Offset: 88, Length: 16, Resolution: 0.01, Field Type: NUMBER
    antenna_altitude_for_2d_mode_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    antenna_altitude_for_2d_mode = antenna_altitude_for_2d_mode_raw * 0.01
    publish_field(hass, instance_name, 'antenna_altitude_for_2d_mode', 'Antenna Altitude for 2D Mode', antenna_altitude_for_2d_mode, 'GNSS Control Status', 'm', '129538')

    # use_antenna_altitude_for_2d_mode | Offset: 104, Length: 2, Resolution: 1, Field Type: LOOKUP
    use_antenna_altitude_for_2d_mode_raw = (data_raw >> 104) & 0x3
    use_antenna_altitude_for_2d_mode = use_antenna_altitude_for_2d_mode_raw * 1
    publish_field(hass, instance_name, 'use_antenna_altitude_for_2d_mode', 'Use Antenna Altitude for 2D Mode', use_antenna_altitude_for_2d_mode, 'GNSS Control Status', '', '129538')

    # reserved | Offset: 106, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 106) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS Control Status', '', '129538')

def process_pgn_129539(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129539."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS DOPs', '', '129539')

    # desired_mode | Offset: 8, Length: 3, Resolution: 1, Field Type: LOOKUP
    desired_mode_raw = (data_raw >> 8) & 0x7
    desired_mode = desired_mode_raw * 1
    publish_field(hass, instance_name, 'desired_mode', 'Desired Mode', desired_mode, 'GNSS DOPs', '', '129539')

    # actual_mode | Offset: 11, Length: 3, Resolution: 1, Field Type: LOOKUP
    actual_mode_raw = (data_raw >> 11) & 0x7
    actual_mode = actual_mode_raw * 1
    publish_field(hass, instance_name, 'actual_mode', 'Actual Mode', actual_mode, 'GNSS DOPs', '', '129539')

    # reserved | Offset: 14, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 14) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS DOPs', '', '129539')

    # hdop | Offset: 16, Length: 16, Resolution: 0.01, Field Type: NUMBER
    hdop_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    if hdop_raw & (1 << (16 - 1)):
        hdop_raw -= (1 << 16)
    hdop = hdop_raw * 0.01
    publish_field(hass, instance_name, 'hdop', 'HDOP', hdop, 'GNSS DOPs', '', '129539')

    # vdop | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    vdop_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if vdop_raw & (1 << (16 - 1)):
        vdop_raw -= (1 << 16)
    vdop = vdop_raw * 0.01
    publish_field(hass, instance_name, 'vdop', 'VDOP', vdop, 'GNSS DOPs', '', '129539')

    # tdop | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    tdop_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    if tdop_raw & (1 << (16 - 1)):
        tdop_raw -= (1 << 16)
    tdop = tdop_raw * 0.01
    publish_field(hass, instance_name, 'tdop', 'TDOP', tdop, 'GNSS DOPs', '', '129539')

def process_pgn_129540(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129540."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS Sats in View', '', '129540')

    # range_residual_mode | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    range_residual_mode_raw = (data_raw >> 8) & 0x3
    range_residual_mode = range_residual_mode_raw * 1
    publish_field(hass, instance_name, 'range_residual_mode', 'Range Residual Mode', range_residual_mode, 'GNSS Sats in View', '', '129540')

    # reserved | Offset: 10, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 10) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS Sats in View', '', '129540')

    # sats_in_view | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    sats_in_view_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    sats_in_view = sats_in_view_raw * 1
    publish_field(hass, instance_name, 'sats_in_view', 'Sats in View', sats_in_view, 'GNSS Sats in View', '', '129540')

    # prn | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    prn_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    prn = prn_raw * 1
    publish_field(hass, instance_name, 'prn', 'PRN', prn, 'GNSS Sats in View', '', '129540')

    # elevation | Offset: 32, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    elevation_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if elevation_raw & (1 << (16 - 1)):
        elevation_raw -= (1 << 16)
    elevation = elevation_raw * 0.0001
    publish_field(hass, instance_name, 'elevation', 'Elevation', elevation, 'GNSS Sats in View', 'rad', '129540')
    publish_field(hass, instance_name, 'elevation_degrees', 'Elevation Degrees', radians_to_degrees(elevation), 'GNSS Sats in View', 'Deg', '129540')

    # azimuth | Offset: 48, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    azimuth_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    azimuth = azimuth_raw * 0.0001
    publish_field(hass, instance_name, 'azimuth', 'Azimuth', azimuth, 'GNSS Sats in View', 'rad', '129540')
    publish_field(hass, instance_name, 'azimuth_degrees', 'Azimuth Degrees', radians_to_degrees(azimuth), 'GNSS Sats in View', 'Deg', '129540')

    # snr | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    snr_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    snr = snr_raw * 0.01
    publish_field(hass, instance_name, 'snr', 'SNR', snr, 'GNSS Sats in View', 'dB', '129540')

    # range_residuals | Offset: 80, Length: 32, Resolution: 1, Field Type: NUMBER
    range_residuals_raw = decode_number((data_raw >> 80) & 0xFFFFFFFF, 32)
    if range_residuals_raw & (1 << (32 - 1)):
        range_residuals_raw -= (1 << 32)
    range_residuals = range_residuals_raw * 1
    publish_field(hass, instance_name, 'range_residuals', 'Range residuals', range_residuals, 'GNSS Sats in View', '', '129540')

    # status | Offset: 112, Length: 4, Resolution: 1, Field Type: LOOKUP
    status_raw = (data_raw >> 112) & 0xF
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'GNSS Sats in View', '', '129540')

    # reserved | Offset: 116, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 116) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS Sats in View', '', '129540')

def process_pgn_129541(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129541."""
    # prn | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    prn_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    prn = prn_raw * 1
    publish_field(hass, instance_name, 'prn', 'PRN', prn, 'GPS Almanac Data', '', '129541')

    # gps_week_number | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    gps_week_number_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    gps_week_number = gps_week_number_raw * 1
    publish_field(hass, instance_name, 'gps_week_number', 'GPS Week number', gps_week_number, 'GPS Almanac Data', '', '129541')

    # sv_health_bits | Offset: 24, Length: 8, Resolution: 1, Field Type: BINARY
    sv_health_bits_raw = (data_raw >> 24) & 0xFF
    sv_health_bits = sv_health_bits_raw * 1
    publish_field(hass, instance_name, 'sv_health_bits', 'SV Health Bits', sv_health_bits, 'GPS Almanac Data', '', '129541')

    # eccentricity | Offset: 32, Length: 16, Resolution: 4.76837e-07, Field Type: NUMBER
    eccentricity_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    eccentricity = eccentricity_raw * 4.76837e-07
    publish_field(hass, instance_name, 'eccentricity', 'Eccentricity', eccentricity, 'GPS Almanac Data', 'm/m', '129541')

    # almanac_reference_time | Offset: 48, Length: 8, Resolution: 4096, Field Type: NUMBER
    almanac_reference_time_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    almanac_reference_time = almanac_reference_time_raw * 4096
    publish_field(hass, instance_name, 'almanac_reference_time', 'Almanac Reference Time', almanac_reference_time, 'GPS Almanac Data', 's', '129541')

    # inclination_angle | Offset: 56, Length: 16, Resolution: 1.90735e-06, Field Type: NUMBER
    inclination_angle_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    if inclination_angle_raw & (1 << (16 - 1)):
        inclination_angle_raw -= (1 << 16)
    inclination_angle = inclination_angle_raw * 1.90735e-06
    publish_field(hass, instance_name, 'inclination_angle', 'Inclination Angle', inclination_angle, 'GPS Almanac Data', 'semi-circle', '129541')

    # rate_of_right_ascension | Offset: 72, Length: 16, Resolution: 3.63798e-12, Field Type: NUMBER
    rate_of_right_ascension_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    if rate_of_right_ascension_raw & (1 << (16 - 1)):
        rate_of_right_ascension_raw -= (1 << 16)
    rate_of_right_ascension = rate_of_right_ascension_raw * 3.63798e-12
    publish_field(hass, instance_name, 'rate_of_right_ascension', 'Rate of Right Ascension', rate_of_right_ascension, 'GPS Almanac Data', 'semi-circle/s', '129541')

    # root_of_semi_major_axis | Offset: 88, Length: 24, Resolution: 0.000488281, Field Type: NUMBER
    root_of_semi_major_axis_raw = decode_number((data_raw >> 88) & 0xFFFFFF, 24)
    root_of_semi_major_axis = root_of_semi_major_axis_raw * 0.000488281
    publish_field(hass, instance_name, 'root_of_semi_major_axis', 'Root of Semi-major Axis', root_of_semi_major_axis, 'GPS Almanac Data', 'sqrt(m)', '129541')

    # argument_of_perigee | Offset: 112, Length: 24, Resolution: 1.19209e-07, Field Type: NUMBER
    argument_of_perigee_raw = decode_number((data_raw >> 112) & 0xFFFFFF, 24)
    if argument_of_perigee_raw & (1 << (24 - 1)):
        argument_of_perigee_raw -= (1 << 24)
    argument_of_perigee = argument_of_perigee_raw * 1.19209e-07
    publish_field(hass, instance_name, 'argument_of_perigee', 'Argument of Perigee', argument_of_perigee, 'GPS Almanac Data', 'semi-circle', '129541')

    # longitude_of_ascension_node | Offset: 136, Length: 24, Resolution: 1.19209e-07, Field Type: NUMBER
    longitude_of_ascension_node_raw = decode_number((data_raw >> 136) & 0xFFFFFF, 24)
    if longitude_of_ascension_node_raw & (1 << (24 - 1)):
        longitude_of_ascension_node_raw -= (1 << 24)
    longitude_of_ascension_node = longitude_of_ascension_node_raw * 1.19209e-07
    publish_field(hass, instance_name, 'longitude_of_ascension_node', 'Longitude of Ascension Node', longitude_of_ascension_node, 'GPS Almanac Data', 'semi-circle', '129541')

    # mean_anomaly | Offset: 160, Length: 24, Resolution: 1.19209e-07, Field Type: NUMBER
    mean_anomaly_raw = decode_number((data_raw >> 160) & 0xFFFFFF, 24)
    if mean_anomaly_raw & (1 << (24 - 1)):
        mean_anomaly_raw -= (1 << 24)
    mean_anomaly = mean_anomaly_raw * 1.19209e-07
    publish_field(hass, instance_name, 'mean_anomaly', 'Mean Anomaly', mean_anomaly, 'GPS Almanac Data', 'semi-circle', '129541')

    # clock_parameter_1 | Offset: 184, Length: 11, Resolution: 9.53674e-07, Field Type: NUMBER
    clock_parameter_1_raw = decode_number((data_raw >> 184) & 0x7FF, 11)
    if clock_parameter_1_raw & (1 << (11 - 1)):
        clock_parameter_1_raw -= (1 << 11)
    clock_parameter_1 = clock_parameter_1_raw * 9.53674e-07
    publish_field(hass, instance_name, 'clock_parameter_1', 'Clock Parameter 1', clock_parameter_1, 'GPS Almanac Data', 's', '129541')

    # clock_parameter_2 | Offset: 195, Length: 11, Resolution: 3.63798e-12, Field Type: NUMBER
    clock_parameter_2_raw = decode_number((data_raw >> 195) & 0x7FF, 11)
    if clock_parameter_2_raw & (1 << (11 - 1)):
        clock_parameter_2_raw -= (1 << 11)
    clock_parameter_2 = clock_parameter_2_raw * 3.63798e-12
    publish_field(hass, instance_name, 'clock_parameter_2', 'Clock Parameter 2', clock_parameter_2, 'GPS Almanac Data', 's/s', '129541')

    # reserved | Offset: 206, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 206) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GPS Almanac Data', '', '129541')

def process_pgn_129542(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129542."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS Pseudorange Noise Statistics', '', '129542')

    # rms_of_position_uncertainty | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    rms_of_position_uncertainty_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    rms_of_position_uncertainty = rms_of_position_uncertainty_raw * 1
    publish_field(hass, instance_name, 'rms_of_position_uncertainty', 'RMS of Position Uncertainty', rms_of_position_uncertainty, 'GNSS Pseudorange Noise Statistics', '', '129542')

    # std_of_major_axis | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_major_axis_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    std_of_major_axis = std_of_major_axis_raw * 1
    publish_field(hass, instance_name, 'std_of_major_axis', 'STD of Major axis', std_of_major_axis, 'GNSS Pseudorange Noise Statistics', '', '129542')

    # std_of_minor_axis | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_minor_axis_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    std_of_minor_axis = std_of_minor_axis_raw * 1
    publish_field(hass, instance_name, 'std_of_minor_axis', 'STD of Minor axis', std_of_minor_axis, 'GNSS Pseudorange Noise Statistics', '', '129542')

    # orientation_of_major_axis | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    orientation_of_major_axis_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    orientation_of_major_axis = orientation_of_major_axis_raw * 1
    publish_field(hass, instance_name, 'orientation_of_major_axis', 'Orientation of Major axis', orientation_of_major_axis, 'GNSS Pseudorange Noise Statistics', '', '129542')

    # std_of_lat_error | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_lat_error_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    std_of_lat_error = std_of_lat_error_raw * 1
    publish_field(hass, instance_name, 'std_of_lat_error', 'STD of Lat Error', std_of_lat_error, 'GNSS Pseudorange Noise Statistics', '', '129542')

    # std_of_lon_error | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_lon_error_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    std_of_lon_error = std_of_lon_error_raw * 1
    publish_field(hass, instance_name, 'std_of_lon_error', 'STD of Lon Error', std_of_lon_error, 'GNSS Pseudorange Noise Statistics', '', '129542')

    # std_of_alt_error | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    std_of_alt_error_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    std_of_alt_error = std_of_alt_error_raw * 1
    publish_field(hass, instance_name, 'std_of_alt_error', 'STD of Alt Error', std_of_alt_error, 'GNSS Pseudorange Noise Statistics', '', '129542')

def process_pgn_129545(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129545."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS RAIM Output', '', '129545')

    # integrity_flag | Offset: 8, Length: 4, Resolution: 1, Field Type: NUMBER
    integrity_flag_raw = decode_number((data_raw >> 8) & 0xF, 4)
    integrity_flag = integrity_flag_raw * 1
    publish_field(hass, instance_name, 'integrity_flag', 'Integrity flag', integrity_flag, 'GNSS RAIM Output', '', '129545')

    # reserved | Offset: 12, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 12) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS RAIM Output', '', '129545')

    # latitude_expected_error | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    latitude_expected_error_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    latitude_expected_error = latitude_expected_error_raw * 1
    publish_field(hass, instance_name, 'latitude_expected_error', 'Latitude expected error', latitude_expected_error, 'GNSS RAIM Output', '', '129545')

    # longitude_expected_error | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    longitude_expected_error_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    longitude_expected_error = longitude_expected_error_raw * 1
    publish_field(hass, instance_name, 'longitude_expected_error', 'Longitude expected error', longitude_expected_error, 'GNSS RAIM Output', '', '129545')

    # altitude_expected_error | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    altitude_expected_error_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    altitude_expected_error = altitude_expected_error_raw * 1
    publish_field(hass, instance_name, 'altitude_expected_error', 'Altitude expected error', altitude_expected_error, 'GNSS RAIM Output', '', '129545')

    # sv_id_of_most_likely_failed_sat | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    sv_id_of_most_likely_failed_sat_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    sv_id_of_most_likely_failed_sat = sv_id_of_most_likely_failed_sat_raw * 1
    publish_field(hass, instance_name, 'sv_id_of_most_likely_failed_sat', 'SV ID of most likely failed sat', sv_id_of_most_likely_failed_sat, 'GNSS RAIM Output', '', '129545')

    # probability_of_missed_detection | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    probability_of_missed_detection_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    probability_of_missed_detection = probability_of_missed_detection_raw * 1
    publish_field(hass, instance_name, 'probability_of_missed_detection', 'Probability of missed detection', probability_of_missed_detection, 'GNSS RAIM Output', '', '129545')

    # estimate_of_pseudorange_bias | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    estimate_of_pseudorange_bias_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    estimate_of_pseudorange_bias = estimate_of_pseudorange_bias_raw * 1
    publish_field(hass, instance_name, 'estimate_of_pseudorange_bias', 'Estimate of pseudorange bias', estimate_of_pseudorange_bias, 'GNSS RAIM Output', '', '129545')

    # std_deviation_of_bias | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    std_deviation_of_bias_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    std_deviation_of_bias = std_deviation_of_bias_raw * 1
    publish_field(hass, instance_name, 'std_deviation_of_bias', 'Std Deviation of bias', std_deviation_of_bias, 'GNSS RAIM Output', '', '129545')

def process_pgn_129546(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129546."""
    # radial_position_error_maximum_threshold | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    radial_position_error_maximum_threshold_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    radial_position_error_maximum_threshold = radial_position_error_maximum_threshold_raw * 1
    publish_field(hass, instance_name, 'radial_position_error_maximum_threshold', 'Radial Position Error Maximum Threshold', radial_position_error_maximum_threshold, 'GNSS RAIM Settings', '', '129546')

    # probability_of_false_alarm | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    probability_of_false_alarm_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    probability_of_false_alarm = probability_of_false_alarm_raw * 1
    publish_field(hass, instance_name, 'probability_of_false_alarm', 'Probability of False Alarm', probability_of_false_alarm, 'GNSS RAIM Settings', '', '129546')

    # probability_of_missed_detection | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    probability_of_missed_detection_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    probability_of_missed_detection = probability_of_missed_detection_raw * 1
    publish_field(hass, instance_name, 'probability_of_missed_detection', 'Probability of Missed Detection', probability_of_missed_detection, 'GNSS RAIM Settings', '', '129546')

    # pseudorange_residual_filtering_time_constant | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    pseudorange_residual_filtering_time_constant_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    pseudorange_residual_filtering_time_constant = pseudorange_residual_filtering_time_constant_raw * 1
    publish_field(hass, instance_name, 'pseudorange_residual_filtering_time_constant', 'Pseudorange Residual Filtering Time Constant', pseudorange_residual_filtering_time_constant, 'GNSS RAIM Settings', '', '129546')

    # reserved | Offset: 32, Length: 32, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS RAIM Settings', '', '129546')

def process_pgn_129547(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129547."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS Pseudorange Error Statistics', '', '129547')

    # rms_std_dev_of_range_inputs | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    rms_std_dev_of_range_inputs_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    rms_std_dev_of_range_inputs = rms_std_dev_of_range_inputs_raw * 1
    publish_field(hass, instance_name, 'rms_std_dev_of_range_inputs', 'RMS Std Dev of Range Inputs', rms_std_dev_of_range_inputs, 'GNSS Pseudorange Error Statistics', '', '129547')

    # std_dev_of_major_error_ellipse | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    std_dev_of_major_error_ellipse_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    std_dev_of_major_error_ellipse = std_dev_of_major_error_ellipse_raw * 1
    publish_field(hass, instance_name, 'std_dev_of_major_error_ellipse', 'Std Dev of Major error ellipse', std_dev_of_major_error_ellipse, 'GNSS Pseudorange Error Statistics', '', '129547')

    # std_dev_of_minor_error_ellipse | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    std_dev_of_minor_error_ellipse_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    std_dev_of_minor_error_ellipse = std_dev_of_minor_error_ellipse_raw * 1
    publish_field(hass, instance_name, 'std_dev_of_minor_error_ellipse', 'Std Dev of Minor error ellipse', std_dev_of_minor_error_ellipse, 'GNSS Pseudorange Error Statistics', '', '129547')

    # orientation_of_error_ellipse | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    orientation_of_error_ellipse_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    orientation_of_error_ellipse = orientation_of_error_ellipse_raw * 1
    publish_field(hass, instance_name, 'orientation_of_error_ellipse', 'Orientation of error ellipse', orientation_of_error_ellipse, 'GNSS Pseudorange Error Statistics', '', '129547')

    # std_dev_lat_error | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    std_dev_lat_error_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    std_dev_lat_error = std_dev_lat_error_raw * 1
    publish_field(hass, instance_name, 'std_dev_lat_error', 'Std Dev Lat Error', std_dev_lat_error, 'GNSS Pseudorange Error Statistics', '', '129547')

    # std_dev_lon_error | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    std_dev_lon_error_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    std_dev_lon_error = std_dev_lon_error_raw * 1
    publish_field(hass, instance_name, 'std_dev_lon_error', 'Std Dev Lon Error', std_dev_lon_error, 'GNSS Pseudorange Error Statistics', '', '129547')

    # std_dev_alt_error | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    std_dev_alt_error_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    std_dev_alt_error = std_dev_alt_error_raw * 1
    publish_field(hass, instance_name, 'std_dev_alt_error', 'Std Dev Alt Error', std_dev_alt_error, 'GNSS Pseudorange Error Statistics', '', '129547')

def process_pgn_129549(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129549."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'DGNSS Corrections', '', '129549')

    # reference_station_id | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    reference_station_id_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    reference_station_id = reference_station_id_raw * 1
    publish_field(hass, instance_name, 'reference_station_id', 'Reference Station ID', reference_station_id, 'DGNSS Corrections', '', '129549')

    # reference_station_type | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    reference_station_type_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    reference_station_type = reference_station_type_raw * 1
    publish_field(hass, instance_name, 'reference_station_type', 'Reference Station Type', reference_station_type, 'DGNSS Corrections', '', '129549')

    # time_of_corrections | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    time_of_corrections_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    time_of_corrections = time_of_corrections_raw * 1
    publish_field(hass, instance_name, 'time_of_corrections', 'Time of corrections', time_of_corrections, 'DGNSS Corrections', '', '129549')

    # station_health | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    station_health_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    station_health = station_health_raw * 1
    publish_field(hass, instance_name, 'station_health', 'Station Health', station_health, 'DGNSS Corrections', '', '129549')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'DGNSS Corrections', '', '129549')

    # satellite_id | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    satellite_id_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    satellite_id = satellite_id_raw * 1
    publish_field(hass, instance_name, 'satellite_id', 'Satellite ID', satellite_id, 'DGNSS Corrections', '', '129549')

    # prc | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    prc_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    prc = prc_raw * 1
    publish_field(hass, instance_name, 'prc', 'PRC', prc, 'DGNSS Corrections', '', '129549')

    # rrc | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    rrc_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    rrc = rrc_raw * 1
    publish_field(hass, instance_name, 'rrc', 'RRC', rrc, 'DGNSS Corrections', '', '129549')

    # udre | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    udre_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    udre = udre_raw * 1
    publish_field(hass, instance_name, 'udre', 'UDRE', udre, 'DGNSS Corrections', '', '129549')

    # iod | Offset: 96, Length: 8, Resolution: 1, Field Type: NUMBER
    iod_raw = decode_number((data_raw >> 96) & 0xFF, 8)
    iod = iod_raw * 1
    publish_field(hass, instance_name, 'iod', 'IOD', iod, 'DGNSS Corrections', '', '129549')

def process_pgn_129550(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129550."""
    # channel | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    channel_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    channel = channel_raw * 1
    publish_field(hass, instance_name, 'channel', 'Channel', channel, 'GNSS Differential Correction Receiver Interface', '', '129550')

    # frequency | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    frequency_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    frequency = frequency_raw * 1
    publish_field(hass, instance_name, 'frequency', 'Frequency', frequency, 'GNSS Differential Correction Receiver Interface', '', '129550')

    # serial_interface_bit_rate | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    serial_interface_bit_rate_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    serial_interface_bit_rate = serial_interface_bit_rate_raw * 1
    publish_field(hass, instance_name, 'serial_interface_bit_rate', 'Serial Interface Bit Rate', serial_interface_bit_rate, 'GNSS Differential Correction Receiver Interface', '', '129550')

    # serial_interface_detection_mode | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    serial_interface_detection_mode_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    serial_interface_detection_mode = serial_interface_detection_mode_raw * 1
    publish_field(hass, instance_name, 'serial_interface_detection_mode', 'Serial Interface Detection Mode', serial_interface_detection_mode, 'GNSS Differential Correction Receiver Interface', '', '129550')

    # differential_source | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    differential_source_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    differential_source = differential_source_raw * 1
    publish_field(hass, instance_name, 'differential_source', 'Differential Source', differential_source, 'GNSS Differential Correction Receiver Interface', '', '129550')

    # differential_operation_mode | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    differential_operation_mode_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    differential_operation_mode = differential_operation_mode_raw * 1
    publish_field(hass, instance_name, 'differential_operation_mode', 'Differential Operation Mode', differential_operation_mode, 'GNSS Differential Correction Receiver Interface', '', '129550')

def process_pgn_129551(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129551."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # channel | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    channel_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    channel = channel_raw * 1
    publish_field(hass, instance_name, 'channel', 'Channel', channel, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # signal_strength | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    signal_strength_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    signal_strength = signal_strength_raw * 1
    publish_field(hass, instance_name, 'signal_strength', 'Signal Strength', signal_strength, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # signal_snr | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    signal_snr_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    signal_snr = signal_snr_raw * 1
    publish_field(hass, instance_name, 'signal_snr', 'Signal SNR', signal_snr, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # frequency | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    frequency_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    frequency = frequency_raw * 1
    publish_field(hass, instance_name, 'frequency', 'Frequency', frequency, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # station_type | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    station_type_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    station_type = station_type_raw * 1
    publish_field(hass, instance_name, 'station_type', 'Station Type', station_type, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # station_id | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    station_id_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    station_id = station_id_raw * 1
    publish_field(hass, instance_name, 'station_id', 'Station ID', station_id, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # differential_signal_bit_rate | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    differential_signal_bit_rate_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    differential_signal_bit_rate = differential_signal_bit_rate_raw * 1
    publish_field(hass, instance_name, 'differential_signal_bit_rate', 'Differential Signal Bit Rate', differential_signal_bit_rate, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # differential_signal_detection_mode | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    differential_signal_detection_mode_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    differential_signal_detection_mode = differential_signal_detection_mode_raw * 1
    publish_field(hass, instance_name, 'differential_signal_detection_mode', 'Differential Signal Detection Mode', differential_signal_detection_mode, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # used_as_correction_source | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    used_as_correction_source_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    used_as_correction_source = used_as_correction_source_raw * 1
    publish_field(hass, instance_name, 'used_as_correction_source', 'Used as Correction Source', used_as_correction_source, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # reserved | Offset: 80, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 80) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # differential_source | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    differential_source_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    differential_source = differential_source_raw * 1
    publish_field(hass, instance_name, 'differential_source', 'Differential Source', differential_source, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # time_since_last_sat_differential_sync | Offset: 96, Length: 8, Resolution: 1, Field Type: NUMBER
    time_since_last_sat_differential_sync_raw = decode_number((data_raw >> 96) & 0xFF, 8)
    time_since_last_sat_differential_sync = time_since_last_sat_differential_sync_raw * 1
    publish_field(hass, instance_name, 'time_since_last_sat_differential_sync', 'Time since Last Sat Differential Sync', time_since_last_sat_differential_sync, 'GNSS Differential Correction Receiver Signal', '', '129551')

    # satellite_service_id_no_ | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    satellite_service_id_no__raw = decode_number((data_raw >> 104) & 0xFF, 8)
    satellite_service_id_no_ = satellite_service_id_no__raw * 1
    publish_field(hass, instance_name, 'satellite_service_id_no_', 'Satellite Service ID No.', satellite_service_id_no_, 'GNSS Differential Correction Receiver Signal', '', '129551')

def process_pgn_129556(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129556."""
    # prn | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    prn_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    prn = prn_raw * 1
    publish_field(hass, instance_name, 'prn', 'PRN', prn, 'GLONASS Almanac Data', '', '129556')

    # na | Offset: 8, Length: 16, Resolution: 1, Field Type: NUMBER
    na_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    na = na_raw * 1
    publish_field(hass, instance_name, 'na', 'NA', na, 'GLONASS Almanac Data', '', '129556')

    # reserved | Offset: 24, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 24) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'GLONASS Almanac Data', '', '129556')

    # cna | Offset: 26, Length: 1, Resolution: 1, Field Type: NUMBER
    cna_raw = decode_number((data_raw >> 26) & 0x1, 1)
    cna = cna_raw * 1
    publish_field(hass, instance_name, 'cna', 'CnA', cna, 'GLONASS Almanac Data', '', '129556')

    # hna | Offset: 27, Length: 5, Resolution: 1, Field Type: NUMBER
    hna_raw = decode_number((data_raw >> 27) & 0x1F, 5)
    hna = hna_raw * 1
    publish_field(hass, instance_name, 'hna', 'HnA', hna, 'GLONASS Almanac Data', '', '129556')

    # __epsilon_na | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    __epsilon_na_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    __epsilon_na = __epsilon_na_raw * 1
    publish_field(hass, instance_name, '__epsilon_na', '(epsilon)nA', __epsilon_na, 'GLONASS Almanac Data', '', '129556')

    # __deltatna_dot | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    __deltatna_dot_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    __deltatna_dot = __deltatna_dot_raw * 1
    publish_field(hass, instance_name, '__deltatna_dot', '(deltaTnA)DOT', __deltatna_dot, 'GLONASS Almanac Data', '', '129556')

    # __omega_na | Offset: 56, Length: 16, Resolution: 1, Field Type: NUMBER
    __omega_na_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    __omega_na = __omega_na_raw * 1
    publish_field(hass, instance_name, '__omega_na', '(omega)nA', __omega_na, 'GLONASS Almanac Data', '', '129556')

    # __delta_tna | Offset: 72, Length: 24, Resolution: 1, Field Type: NUMBER
    __delta_tna_raw = decode_number((data_raw >> 72) & 0xFFFFFF, 24)
    __delta_tna = __delta_tna_raw * 1
    publish_field(hass, instance_name, '__delta_tna', '(delta)TnA', __delta_tna, 'GLONASS Almanac Data', '', '129556')

    # tna | Offset: 96, Length: 24, Resolution: 1, Field Type: NUMBER
    tna_raw = decode_number((data_raw >> 96) & 0xFFFFFF, 24)
    tna = tna_raw * 1
    publish_field(hass, instance_name, 'tna', 'tnA', tna, 'GLONASS Almanac Data', '', '129556')

    # __lambda_na | Offset: 120, Length: 24, Resolution: 1, Field Type: NUMBER
    __lambda_na_raw = decode_number((data_raw >> 120) & 0xFFFFFF, 24)
    __lambda_na = __lambda_na_raw * 1
    publish_field(hass, instance_name, '__lambda_na', '(lambda)nA', __lambda_na, 'GLONASS Almanac Data', '', '129556')

    # __delta_ina | Offset: 144, Length: 24, Resolution: 1, Field Type: NUMBER
    __delta_ina_raw = decode_number((data_raw >> 144) & 0xFFFFFF, 24)
    __delta_ina = __delta_ina_raw * 1
    publish_field(hass, instance_name, '__delta_ina', '(delta)inA', __delta_ina, 'GLONASS Almanac Data', '', '129556')

    # __tau_ca | Offset: 168, Length: 28, Resolution: 1, Field Type: NUMBER
    __tau_ca_raw = decode_number((data_raw >> 168) & 0xFFFFFFF, 28)
    __tau_ca = __tau_ca_raw * 1
    publish_field(hass, instance_name, '__tau_ca', '(tau)cA', __tau_ca, 'GLONASS Almanac Data', '', '129556')

    # __tau_na | Offset: 196, Length: 12, Resolution: 1, Field Type: NUMBER
    __tau_na_raw = decode_number((data_raw >> 196) & 0xFFF, 12)
    __tau_na = __tau_na_raw * 1
    publish_field(hass, instance_name, '__tau_na', '(tau)nA', __tau_na, 'GLONASS Almanac Data', '', '129556')

def process_pgn_129792(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129792."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS DGNSS Broadcast Binary Message', '', '129792')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: NUMBER
    repeat_indicator_raw = decode_number((data_raw >> 6) & 0x3, 2)
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS DGNSS Broadcast Binary Message', '', '129792')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS DGNSS Broadcast Binary Message', '', '129792')

    # reserved | Offset: 40, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS DGNSS Broadcast Binary Message', '', '129792')

    # ais_transceiver_information | Offset: 41, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 41) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS DGNSS Broadcast Binary Message', '', '129792')

    # spare | Offset: 46, Length: 2, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 46) & 0x3
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS DGNSS Broadcast Binary Message', '', '129792')

    # longitude | Offset: 48, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'AIS DGNSS Broadcast Binary Message', 'deg', '129792')

    # latitude | Offset: 80, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 80) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'AIS DGNSS Broadcast Binary Message', 'deg', '129792')

    # reserved | Offset: 112, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 112) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS DGNSS Broadcast Binary Message', '', '129792')

    # spare | Offset: 115, Length: 5, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 115) & 0x1F
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS DGNSS Broadcast Binary Message', '', '129792')

    # number_of_bits_in_binary_data_field | Offset: 120, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_bits_in_binary_data_field_raw = decode_number((data_raw >> 120) & 0xFFFF, 16)
    number_of_bits_in_binary_data_field = number_of_bits_in_binary_data_field_raw * 1
    publish_field(hass, instance_name, 'number_of_bits_in_binary_data_field', 'Number of Bits in Binary Data Field', number_of_bits_in_binary_data_field, 'AIS DGNSS Broadcast Binary Message', '', '129792')

def process_pgn_129793(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129793."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS UTC and Date Report', '', '129793')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS UTC and Date Report', '', '129793')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS UTC and Date Report', '', '129793')

    # longitude | Offset: 40, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'AIS UTC and Date Report', 'deg', '129793')

    # latitude | Offset: 72, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 72) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'AIS UTC and Date Report', 'deg', '129793')

    # position_accuracy | Offset: 104, Length: 1, Resolution: 1, Field Type: LOOKUP
    position_accuracy_raw = (data_raw >> 104) & 0x1
    position_accuracy = position_accuracy_raw * 1
    publish_field(hass, instance_name, 'position_accuracy', 'Position Accuracy', position_accuracy, 'AIS UTC and Date Report', '', '129793')

    # raim | Offset: 105, Length: 1, Resolution: 1, Field Type: LOOKUP
    raim_raw = (data_raw >> 105) & 0x1
    raim = raim_raw * 1
    publish_field(hass, instance_name, 'raim', 'RAIM', raim, 'AIS UTC and Date Report', '', '129793')

    # reserved | Offset: 106, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 106) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS UTC and Date Report', '', '129793')

    # position_time | Offset: 112, Length: 32, Resolution: 0.0001, Field Type: TIME
    position_time_raw = (data_raw >> 112) & 0xFFFFFFFF
    position_time = decode_time(position_time_raw * 0.0001)
    publish_field(hass, instance_name, 'position_time', 'Position Time', position_time, 'AIS UTC and Date Report', 's', '129793')

    # communication_state | Offset: 144, Length: 19, Resolution: 1, Field Type: BINARY
    communication_state_raw = (data_raw >> 144) & 0x7FFFF
    communication_state = communication_state_raw * 1
    publish_field(hass, instance_name, 'communication_state', 'Communication State', communication_state, 'AIS UTC and Date Report', '', '129793')

    # ais_transceiver_information | Offset: 163, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 163) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS UTC and Date Report', '', '129793')

    # position_date | Offset: 168, Length: 16, Resolution: 1, Field Type: DATE
    position_date_raw = (data_raw >> 168) & 0xFFFF
    position_date = decode_date(position_date_raw * 1)
    publish_field(hass, instance_name, 'position_date', 'Position Date', position_date, 'AIS UTC and Date Report', 'd', '129793')

    # reserved | Offset: 184, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 184) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS UTC and Date Report', '', '129793')

    # gnss_type | Offset: 188, Length: 4, Resolution: 1, Field Type: LOOKUP
    gnss_type_raw = (data_raw >> 188) & 0xF
    gnss_type = gnss_type_raw * 1
    publish_field(hass, instance_name, 'gnss_type', 'GNSS type', gnss_type, 'AIS UTC and Date Report', '', '129793')

    # spare | Offset: 192, Length: 8, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 192) & 0xFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS UTC and Date Report', '', '129793')

def process_pgn_129794(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129794."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # imo_number | Offset: 40, Length: 32, Resolution: 1, Field Type: NUMBER
    imo_number_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    imo_number = imo_number_raw * 1
    publish_field(hass, instance_name, 'imo_number', 'IMO number', imo_number, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # callsign | Offset: 72, Length: 56, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # name | Offset: 128, Length: 160, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # type_of_ship | Offset: 288, Length: 8, Resolution: 1, Field Type: LOOKUP
    type_of_ship_raw = (data_raw >> 288) & 0xFF
    type_of_ship = type_of_ship_raw * 1
    publish_field(hass, instance_name, 'type_of_ship', 'Type of ship', type_of_ship, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # length | Offset: 296, Length: 16, Resolution: 0.1, Field Type: NUMBER
    length_raw = decode_number((data_raw >> 296) & 0xFFFF, 16)
    length = length_raw * 0.1
    publish_field(hass, instance_name, 'length', 'Length', length, 'AIS Class A Static and Voyage Related Data', 'm', '129794')

    # beam | Offset: 312, Length: 16, Resolution: 0.1, Field Type: NUMBER
    beam_raw = decode_number((data_raw >> 312) & 0xFFFF, 16)
    beam = beam_raw * 0.1
    publish_field(hass, instance_name, 'beam', 'Beam', beam, 'AIS Class A Static and Voyage Related Data', 'm', '129794')

    # position_reference_from_starboard | Offset: 328, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_starboard_raw = decode_number((data_raw >> 328) & 0xFFFF, 16)
    position_reference_from_starboard = position_reference_from_starboard_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_starboard', 'Position reference from Starboard', position_reference_from_starboard, 'AIS Class A Static and Voyage Related Data', 'm', '129794')

    # position_reference_from_bow | Offset: 344, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_bow_raw = decode_number((data_raw >> 344) & 0xFFFF, 16)
    position_reference_from_bow = position_reference_from_bow_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_bow', 'Position reference from Bow', position_reference_from_bow, 'AIS Class A Static and Voyage Related Data', 'm', '129794')

    # eta_date | Offset: 360, Length: 16, Resolution: 1, Field Type: DATE
    eta_date_raw = (data_raw >> 360) & 0xFFFF
    eta_date = decode_date(eta_date_raw * 1)
    publish_field(hass, instance_name, 'eta_date', 'ETA Date', eta_date, 'AIS Class A Static and Voyage Related Data', 'd', '129794')

    # eta_time | Offset: 376, Length: 32, Resolution: 0.0001, Field Type: TIME
    eta_time_raw = (data_raw >> 376) & 0xFFFFFFFF
    eta_time = decode_time(eta_time_raw * 0.0001)
    publish_field(hass, instance_name, 'eta_time', 'ETA Time', eta_time, 'AIS Class A Static and Voyage Related Data', 's', '129794')

    # draft | Offset: 408, Length: 16, Resolution: 0.01, Field Type: NUMBER
    draft_raw = decode_number((data_raw >> 408) & 0xFFFF, 16)
    draft = draft_raw * 0.01
    publish_field(hass, instance_name, 'draft', 'Draft', draft, 'AIS Class A Static and Voyage Related Data', 'm', '129794')

    # destination | Offset: 424, Length: 160, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # ais_version_indicator | Offset: 584, Length: 2, Resolution: 1, Field Type: LOOKUP
    ais_version_indicator_raw = (data_raw >> 584) & 0x3
    ais_version_indicator = ais_version_indicator_raw * 1
    publish_field(hass, instance_name, 'ais_version_indicator', 'AIS version indicator', ais_version_indicator, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # gnss_type | Offset: 586, Length: 4, Resolution: 1, Field Type: LOOKUP
    gnss_type_raw = (data_raw >> 586) & 0xF
    gnss_type = gnss_type_raw * 1
    publish_field(hass, instance_name, 'gnss_type', 'GNSS type', gnss_type, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # dte | Offset: 590, Length: 1, Resolution: 1, Field Type: LOOKUP
    dte_raw = (data_raw >> 590) & 0x1
    dte = dte_raw * 1
    publish_field(hass, instance_name, 'dte', 'DTE', dte, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # reserved | Offset: 591, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 591) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # ais_transceiver_information | Offset: 592, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 592) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Class A Static and Voyage Related Data', '', '129794')

    # reserved | Offset: 597, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 597) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class A Static and Voyage Related Data', '', '129794')

def process_pgn_129795(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129795."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Addressed Binary Message', '', '129795')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Addressed Binary Message', '', '129795')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Addressed Binary Message', '', '129795')

    # reserved | Offset: 40, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Addressed Binary Message', '', '129795')

    # ais_transceiver_information | Offset: 41, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 41) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Addressed Binary Message', '', '129795')

    # sequence_number | Offset: 46, Length: 2, Resolution: 1, Field Type: NUMBER
    sequence_number_raw = decode_number((data_raw >> 46) & 0x3, 2)
    sequence_number = sequence_number_raw * 1
    publish_field(hass, instance_name, 'sequence_number', 'Sequence Number', sequence_number, 'AIS Addressed Binary Message', '', '129795')

    # destination_id | Offset: 48, Length: 32, Resolution: 1, Field Type: MMSI
    destination_id_raw = (data_raw >> 48) & 0xFFFFFFFF
    destination_id = destination_id_raw * 1
    publish_field(hass, instance_name, 'destination_id', 'Destination ID', destination_id, 'AIS Addressed Binary Message', '', '129795')

    # reserved | Offset: 80, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 80) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Addressed Binary Message', '', '129795')

    # retransmit_flag | Offset: 86, Length: 1, Resolution: 1, Field Type: NUMBER
    retransmit_flag_raw = decode_number((data_raw >> 86) & 0x1, 1)
    retransmit_flag = retransmit_flag_raw * 1
    publish_field(hass, instance_name, 'retransmit_flag', 'Retransmit flag', retransmit_flag, 'AIS Addressed Binary Message', '', '129795')

    # reserved | Offset: 87, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 87) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Addressed Binary Message', '', '129795')

    # number_of_bits_in_binary_data_field | Offset: 88, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_bits_in_binary_data_field_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    number_of_bits_in_binary_data_field = number_of_bits_in_binary_data_field_raw * 1
    publish_field(hass, instance_name, 'number_of_bits_in_binary_data_field', 'Number of Bits in Binary Data Field', number_of_bits_in_binary_data_field, 'AIS Addressed Binary Message', '', '129795')

def process_pgn_129796(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129796."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Acknowledge', '', '129796')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Acknowledge', '', '129796')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Acknowledge', '', '129796')

    # reserved | Offset: 40, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Acknowledge', '', '129796')

    # ais_transceiver_information | Offset: 41, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 41) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Acknowledge', '', '129796')

    # reserved | Offset: 46, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 46) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Acknowledge', '', '129796')

    # destination_id__1 | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    destination_id__1_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    destination_id__1 = destination_id__1_raw * 1
    publish_field(hass, instance_name, 'destination_id__1', 'Destination ID #1', destination_id__1, 'AIS Acknowledge', '', '129796')

    # sequence_number_for_id_1 | Offset: 80, Length: 2, Resolution: 1, Field Type: BINARY
    sequence_number_for_id_1_raw = (data_raw >> 80) & 0x3
    sequence_number_for_id_1 = sequence_number_for_id_1_raw * 1
    publish_field(hass, instance_name, 'sequence_number_for_id_1', 'Sequence Number for ID 1', sequence_number_for_id_1, 'AIS Acknowledge', '', '129796')

    # reserved | Offset: 82, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 82) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Acknowledge', '', '129796')

    # sequence_number_for_id_n | Offset: 88, Length: 2, Resolution: 1, Field Type: BINARY
    sequence_number_for_id_n_raw = (data_raw >> 88) & 0x3
    sequence_number_for_id_n = sequence_number_for_id_n_raw * 1
    publish_field(hass, instance_name, 'sequence_number_for_id_n', 'Sequence Number for ID n', sequence_number_for_id_n, 'AIS Acknowledge', '', '129796')

    # reserved | Offset: 90, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 90) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Acknowledge', '', '129796')

def process_pgn_129797(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129797."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Binary Broadcast Message', '', '129797')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Binary Broadcast Message', '', '129797')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 8) & 0xFFFFFFFF, 32)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Binary Broadcast Message', '', '129797')

    # reserved | Offset: 40, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Binary Broadcast Message', '', '129797')

    # ais_transceiver_information | Offset: 41, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 41) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Binary Broadcast Message', '', '129797')

    # reserved | Offset: 46, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 46) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Binary Broadcast Message', '', '129797')

    # number_of_bits_in_binary_data_field | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_bits_in_binary_data_field_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    number_of_bits_in_binary_data_field = number_of_bits_in_binary_data_field_raw * 1
    publish_field(hass, instance_name, 'number_of_bits_in_binary_data_field', 'Number of Bits in Binary Data Field', number_of_bits_in_binary_data_field, 'AIS Binary Broadcast Message', '', '129797')

def process_pgn_129798(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129798."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS SAR Aircraft Position Report', '', '129798')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS SAR Aircraft Position Report', '', '129798')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS SAR Aircraft Position Report', '', '129798')

    # longitude | Offset: 40, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    longitude_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    if longitude_raw & (1 << (32 - 1)):
        longitude_raw -= (1 << 32)
    longitude = longitude_raw * 1e-07
    publish_field(hass, instance_name, 'longitude', 'Longitude', longitude, 'AIS SAR Aircraft Position Report', 'deg', '129798')

    # latitude | Offset: 72, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    latitude_raw = decode_number((data_raw >> 72) & 0xFFFFFFFF, 32)
    if latitude_raw & (1 << (32 - 1)):
        latitude_raw -= (1 << 32)
    latitude = latitude_raw * 1e-07
    publish_field(hass, instance_name, 'latitude', 'Latitude', latitude, 'AIS SAR Aircraft Position Report', 'deg', '129798')

    # position_accuracy | Offset: 104, Length: 1, Resolution: 1, Field Type: LOOKUP
    position_accuracy_raw = (data_raw >> 104) & 0x1
    position_accuracy = position_accuracy_raw * 1
    publish_field(hass, instance_name, 'position_accuracy', 'Position Accuracy', position_accuracy, 'AIS SAR Aircraft Position Report', '', '129798')

    # raim | Offset: 105, Length: 1, Resolution: 1, Field Type: LOOKUP
    raim_raw = (data_raw >> 105) & 0x1
    raim = raim_raw * 1
    publish_field(hass, instance_name, 'raim', 'RAIM', raim, 'AIS SAR Aircraft Position Report', '', '129798')

    # time_stamp | Offset: 106, Length: 6, Resolution: 1, Field Type: LOOKUP
    time_stamp_raw = (data_raw >> 106) & 0x3F
    time_stamp = time_stamp_raw * 1
    publish_field(hass, instance_name, 'time_stamp', 'Time Stamp', time_stamp, 'AIS SAR Aircraft Position Report', '', '129798')

    # cog | Offset: 112, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'AIS SAR Aircraft Position Report', 'rad', '129798')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'AIS SAR Aircraft Position Report', 'Deg', '129798')

    # sog | Offset: 128, Length: 16, Resolution: 0.1, Field Type: NUMBER
    sog_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    sog = sog_raw * 0.1
    publish_field(hass, instance_name, 'sog', 'SOG', sog, 'AIS SAR Aircraft Position Report', 'm/s', '129798')
    publish_field(hass, instance_name, 'sog_knots', 'SOG Knots', mps_to_knots(sog), 'AIS SAR Aircraft Position Report', 'Kn', '129798')

    # communication_state | Offset: 144, Length: 19, Resolution: 1, Field Type: BINARY
    communication_state_raw = (data_raw >> 144) & 0x7FFFF
    communication_state = communication_state_raw * 1
    publish_field(hass, instance_name, 'communication_state', 'Communication State', communication_state, 'AIS SAR Aircraft Position Report', '', '129798')

    # ais_transceiver_information | Offset: 163, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 163) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS SAR Aircraft Position Report', '', '129798')

    # altitude | Offset: 168, Length: 32, Resolution: 0.01, Field Type: NUMBER
    altitude_raw = decode_number((data_raw >> 168) & 0xFFFFFFFF, 32)
    if altitude_raw & (1 << (32 - 1)):
        altitude_raw -= (1 << 32)
    altitude = altitude_raw * 0.01
    publish_field(hass, instance_name, 'altitude', 'Altitude', altitude, 'AIS SAR Aircraft Position Report', 'm', '129798')

    # reserved_for_regional_applications | Offset: 200, Length: 8, Resolution: 1, Field Type: BINARY
    reserved_for_regional_applications_raw = (data_raw >> 200) & 0xFF
    reserved_for_regional_applications = reserved_for_regional_applications_raw * 1
    publish_field(hass, instance_name, 'reserved_for_regional_applications', 'Reserved for Regional Applications', reserved_for_regional_applications, 'AIS SAR Aircraft Position Report', '', '129798')

    # dte | Offset: 208, Length: 1, Resolution: 1, Field Type: LOOKUP
    dte_raw = (data_raw >> 208) & 0x1
    dte = dte_raw * 1
    publish_field(hass, instance_name, 'dte', 'DTE', dte, 'AIS SAR Aircraft Position Report', '', '129798')

    # reserved | Offset: 209, Length: 7, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 209) & 0x7F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS SAR Aircraft Position Report', '', '129798')

def process_pgn_129799(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129799."""
    # rx_frequency | Offset: 0, Length: 32, Resolution: 10, Field Type: NUMBER
    rx_frequency_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    rx_frequency = rx_frequency_raw * 10
    publish_field(hass, instance_name, 'rx_frequency', 'Rx Frequency', rx_frequency, 'Radio Frequency/Mode/Power', 'Hz', '129799')

    # tx_frequency | Offset: 32, Length: 32, Resolution: 10, Field Type: NUMBER
    tx_frequency_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    tx_frequency = tx_frequency_raw * 10
    publish_field(hass, instance_name, 'tx_frequency', 'Tx Frequency', tx_frequency, 'Radio Frequency/Mode/Power', 'Hz', '129799')

    # radio_channel | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    radio_channel_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    radio_channel = radio_channel_raw * 1
    publish_field(hass, instance_name, 'radio_channel', 'Radio Channel', radio_channel, 'Radio Frequency/Mode/Power', '', '129799')

    # tx_power | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    tx_power_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    tx_power = tx_power_raw * 1
    publish_field(hass, instance_name, 'tx_power', 'Tx Power', tx_power, 'Radio Frequency/Mode/Power', '', '129799')

    # mode | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    mode_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Radio Frequency/Mode/Power', '', '129799')

    # channel_bandwidth | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    channel_bandwidth_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    channel_bandwidth = channel_bandwidth_raw * 1
    publish_field(hass, instance_name, 'channel_bandwidth', 'Channel Bandwidth', channel_bandwidth, 'Radio Frequency/Mode/Power', '', '129799')

def process_pgn_129800(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129800."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS UTC/Date Inquiry', '', '129800')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS UTC/Date Inquiry', '', '129800')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS UTC/Date Inquiry', '', '129800')

    # ais_transceiver_information | Offset: 40, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 40) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS UTC/Date Inquiry', '', '129800')

    # reserved | Offset: 45, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 45) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS UTC/Date Inquiry', '', '129800')

    # destination_id | Offset: 48, Length: 32, Resolution: 1, Field Type: MMSI
    destination_id_raw = (data_raw >> 48) & 0xFFFFFFFF
    destination_id = destination_id_raw * 1
    publish_field(hass, instance_name, 'destination_id', 'Destination ID', destination_id, 'AIS UTC/Date Inquiry', '', '129800')

def process_pgn_129801(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129801."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Addressed Safety Related Message', '', '129801')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Addressed Safety Related Message', '', '129801')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Addressed Safety Related Message', '', '129801')

    # ais_transceiver_information | Offset: 40, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 40) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Addressed Safety Related Message', '', '129801')

    # sequence_number | Offset: 45, Length: 2, Resolution: 1, Field Type: NUMBER
    sequence_number_raw = decode_number((data_raw >> 45) & 0x3, 2)
    sequence_number = sequence_number_raw * 1
    publish_field(hass, instance_name, 'sequence_number', 'Sequence Number', sequence_number, 'AIS Addressed Safety Related Message', '', '129801')

    # reserved | Offset: 47, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 47) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Addressed Safety Related Message', '', '129801')

    # destination_id | Offset: 48, Length: 32, Resolution: 1, Field Type: MMSI
    destination_id_raw = (data_raw >> 48) & 0xFFFFFFFF
    destination_id = destination_id_raw * 1
    publish_field(hass, instance_name, 'destination_id', 'Destination ID', destination_id, 'AIS Addressed Safety Related Message', '', '129801')

    # retransmit_flag | Offset: 80, Length: 1, Resolution: 1, Field Type: NUMBER
    retransmit_flag_raw = decode_number((data_raw >> 80) & 0x1, 1)
    retransmit_flag = retransmit_flag_raw * 1
    publish_field(hass, instance_name, 'retransmit_flag', 'Retransmit flag', retransmit_flag, 'AIS Addressed Safety Related Message', '', '129801')

    # reserved | Offset: 81, Length: 7, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 81) & 0x7F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Addressed Safety Related Message', '', '129801')

    # safety_related_text | Offset: 88, Length: 936, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_129802(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129802."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Safety Related Broadcast Message', '', '129802')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Safety Related Broadcast Message', '', '129802')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Safety Related Broadcast Message', '', '129802')

    # ais_transceiver_information | Offset: 40, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 40) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Safety Related Broadcast Message', '', '129802')

    # reserved | Offset: 45, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 45) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Safety Related Broadcast Message', '', '129802')

    # safety_related_text | Offset: 48, Length: 1296, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_129803(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129803."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Interrogation', '', '129803')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Interrogation', '', '129803')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Interrogation', '', '129803')

    # reserved | Offset: 40, Length: 1, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0x1
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Interrogation', '', '129803')

    # ais_transceiver_information | Offset: 41, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 41) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Interrogation', '', '129803')

    # spare | Offset: 46, Length: 2, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 46) & 0x3
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Interrogation', '', '129803')

    # destination_id_1 | Offset: 48, Length: 32, Resolution: 1, Field Type: MMSI
    destination_id_1_raw = (data_raw >> 48) & 0xFFFFFFFF
    destination_id_1 = destination_id_1_raw * 1
    publish_field(hass, instance_name, 'destination_id_1', 'Destination ID 1', destination_id_1, 'AIS Interrogation', '', '129803')

    # message_id_1_1 | Offset: 80, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_1_1_raw = (data_raw >> 80) & 0x3F
    message_id_1_1 = message_id_1_1_raw * 1
    publish_field(hass, instance_name, 'message_id_1_1', 'Message ID 1.1', message_id_1_1, 'AIS Interrogation', '', '129803')

    # slot_offset_1_1 | Offset: 86, Length: 12, Resolution: 1, Field Type: NUMBER
    slot_offset_1_1_raw = decode_number((data_raw >> 86) & 0xFFF, 12)
    slot_offset_1_1 = slot_offset_1_1_raw * 1
    publish_field(hass, instance_name, 'slot_offset_1_1', 'Slot Offset 1.1', slot_offset_1_1, 'AIS Interrogation', '', '129803')

    # spare | Offset: 98, Length: 2, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 98) & 0x3
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Interrogation', '', '129803')

    # message_id_1_2 | Offset: 100, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_1_2_raw = (data_raw >> 100) & 0x3F
    message_id_1_2 = message_id_1_2_raw * 1
    publish_field(hass, instance_name, 'message_id_1_2', 'Message ID 1.2', message_id_1_2, 'AIS Interrogation', '', '129803')

    # slot_offset_1_2 | Offset: 106, Length: 12, Resolution: 1, Field Type: NUMBER
    slot_offset_1_2_raw = decode_number((data_raw >> 106) & 0xFFF, 12)
    slot_offset_1_2 = slot_offset_1_2_raw * 1
    publish_field(hass, instance_name, 'slot_offset_1_2', 'Slot Offset 1.2', slot_offset_1_2, 'AIS Interrogation', '', '129803')

    # spare | Offset: 118, Length: 2, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 118) & 0x3
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Interrogation', '', '129803')

    # destination_id_2 | Offset: 120, Length: 32, Resolution: 1, Field Type: MMSI
    destination_id_2_raw = (data_raw >> 120) & 0xFFFFFFFF
    destination_id_2 = destination_id_2_raw * 1
    publish_field(hass, instance_name, 'destination_id_2', 'Destination ID 2', destination_id_2, 'AIS Interrogation', '', '129803')

    # message_id_2_1 | Offset: 152, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_2_1_raw = (data_raw >> 152) & 0x3F
    message_id_2_1 = message_id_2_1_raw * 1
    publish_field(hass, instance_name, 'message_id_2_1', 'Message ID 2.1', message_id_2_1, 'AIS Interrogation', '', '129803')

    # slot_offset_2_1 | Offset: 158, Length: 12, Resolution: 1, Field Type: NUMBER
    slot_offset_2_1_raw = decode_number((data_raw >> 158) & 0xFFF, 12)
    slot_offset_2_1 = slot_offset_2_1_raw * 1
    publish_field(hass, instance_name, 'slot_offset_2_1', 'Slot Offset 2.1', slot_offset_2_1, 'AIS Interrogation', '', '129803')

    # spare | Offset: 170, Length: 2, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 170) & 0x3
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Interrogation', '', '129803')

    # reserved | Offset: 172, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 172) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Interrogation', '', '129803')

    # sid | Offset: 176, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 176) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'AIS Interrogation', '', '129803')

def process_pgn_129804(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129804."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Assignment Mode Command', '', '129804')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Assignment Mode Command', '', '129804')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Assignment Mode Command', '', '129804')

    # ais_transceiver_information | Offset: 40, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 40) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Assignment Mode Command', '', '129804')

    # reserved | Offset: 45, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 45) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Assignment Mode Command', '', '129804')

    # destination_id_a | Offset: 48, Length: 32, Resolution: 1, Field Type: MMSI
    destination_id_a_raw = (data_raw >> 48) & 0xFFFFFFFF
    destination_id_a = destination_id_a_raw * 1
    publish_field(hass, instance_name, 'destination_id_a', 'Destination ID A', destination_id_a, 'AIS Assignment Mode Command', '', '129804')

    # offset_a | Offset: 80, Length: 16, Resolution: 1, Field Type: NUMBER
    offset_a_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    offset_a = offset_a_raw * 1
    publish_field(hass, instance_name, 'offset_a', 'Offset A', offset_a, 'AIS Assignment Mode Command', '', '129804')

    # increment_a | Offset: 96, Length: 16, Resolution: 1, Field Type: NUMBER
    increment_a_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    increment_a = increment_a_raw * 1
    publish_field(hass, instance_name, 'increment_a', 'Increment A', increment_a, 'AIS Assignment Mode Command', '', '129804')

    # destination_id_b | Offset: 112, Length: 32, Resolution: 1, Field Type: MMSI
    destination_id_b_raw = (data_raw >> 112) & 0xFFFFFFFF
    destination_id_b = destination_id_b_raw * 1
    publish_field(hass, instance_name, 'destination_id_b', 'Destination ID B', destination_id_b, 'AIS Assignment Mode Command', '', '129804')

    # offset_b | Offset: 144, Length: 16, Resolution: 1, Field Type: NUMBER
    offset_b_raw = decode_number((data_raw >> 144) & 0xFFFF, 16)
    offset_b = offset_b_raw * 1
    publish_field(hass, instance_name, 'offset_b', 'Offset B', offset_b, 'AIS Assignment Mode Command', '', '129804')

    # increment_b | Offset: 160, Length: 16, Resolution: 1, Field Type: NUMBER
    increment_b_raw = decode_number((data_raw >> 160) & 0xFFFF, 16)
    increment_b = increment_b_raw * 1
    publish_field(hass, instance_name, 'increment_b', 'Increment B', increment_b, 'AIS Assignment Mode Command', '', '129804')

def process_pgn_129805(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129805."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Data Link Management Message', '', '129805')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Data Link Management Message', '', '129805')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Data Link Management Message', '', '129805')

    # ais_transceiver_information | Offset: 40, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 40) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Data Link Management Message', '', '129805')

    # reserved | Offset: 45, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 45) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Data Link Management Message', '', '129805')

    # offset | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    offset_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    offset = offset_raw * 1
    publish_field(hass, instance_name, 'offset', 'Offset', offset, 'AIS Data Link Management Message', '', '129805')

    # number_of_slots | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_slots_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    number_of_slots = number_of_slots_raw * 1
    publish_field(hass, instance_name, 'number_of_slots', 'Number of Slots', number_of_slots, 'AIS Data Link Management Message', '', '129805')

    # timeout | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    timeout_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    timeout = timeout_raw * 1
    publish_field(hass, instance_name, 'timeout', 'Timeout', timeout, 'AIS Data Link Management Message', '', '129805')

    # increment | Offset: 80, Length: 16, Resolution: 1, Field Type: NUMBER
    increment_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    increment = increment_raw * 1
    publish_field(hass, instance_name, 'increment', 'Increment', increment, 'AIS Data Link Management Message', '', '129805')

def process_pgn_129806(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129806."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Channel Management', '', '129806')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Channel Management', '', '129806')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Channel Management', '', '129806')

    # ais_transceiver_information | Offset: 40, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 40) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Channel Management', '', '129806')

    # reserved | Offset: 45, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 45) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Channel Management', '', '129806')

    # channel_a | Offset: 48, Length: 7, Resolution: 1, Field Type: NUMBER
    channel_a_raw = decode_number((data_raw >> 48) & 0x7F, 7)
    channel_a = channel_a_raw * 1
    publish_field(hass, instance_name, 'channel_a', 'Channel A', channel_a, 'AIS Channel Management', '', '129806')

    # channel_b | Offset: 55, Length: 7, Resolution: 1, Field Type: NUMBER
    channel_b_raw = decode_number((data_raw >> 55) & 0x7F, 7)
    channel_b = channel_b_raw * 1
    publish_field(hass, instance_name, 'channel_b', 'Channel B', channel_b, 'AIS Channel Management', '', '129806')

    # reserved | Offset: 62, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 62) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Channel Management', '', '129806')

    # power | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    power_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    power = power_raw * 1
    publish_field(hass, instance_name, 'power', 'Power', power, 'AIS Channel Management', '', '129806')

    # tx_rx_mode | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    tx_rx_mode_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    tx_rx_mode = tx_rx_mode_raw * 1
    publish_field(hass, instance_name, 'tx_rx_mode', 'Tx/Rx Mode', tx_rx_mode, 'AIS Channel Management', '', '129806')

    # north_east_longitude_corner_1 | Offset: 80, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    north_east_longitude_corner_1_raw = decode_number((data_raw >> 80) & 0xFFFFFFFF, 32)
    if north_east_longitude_corner_1_raw & (1 << (32 - 1)):
        north_east_longitude_corner_1_raw -= (1 << 32)
    north_east_longitude_corner_1 = north_east_longitude_corner_1_raw * 1e-07
    publish_field(hass, instance_name, 'north_east_longitude_corner_1', 'North East Longitude Corner 1', north_east_longitude_corner_1, 'AIS Channel Management', 'deg', '129806')

    # north_east_latitude_corner_1 | Offset: 112, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    north_east_latitude_corner_1_raw = decode_number((data_raw >> 112) & 0xFFFFFFFF, 32)
    if north_east_latitude_corner_1_raw & (1 << (32 - 1)):
        north_east_latitude_corner_1_raw -= (1 << 32)
    north_east_latitude_corner_1 = north_east_latitude_corner_1_raw * 1e-07
    publish_field(hass, instance_name, 'north_east_latitude_corner_1', 'North East Latitude Corner 1', north_east_latitude_corner_1, 'AIS Channel Management', 'deg', '129806')

    # south_west_longitude_corner_1 | Offset: 144, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    south_west_longitude_corner_1_raw = decode_number((data_raw >> 144) & 0xFFFFFFFF, 32)
    if south_west_longitude_corner_1_raw & (1 << (32 - 1)):
        south_west_longitude_corner_1_raw -= (1 << 32)
    south_west_longitude_corner_1 = south_west_longitude_corner_1_raw * 1e-07
    publish_field(hass, instance_name, 'south_west_longitude_corner_1', 'South West Longitude Corner 1', south_west_longitude_corner_1, 'AIS Channel Management', 'deg', '129806')

    # south_west_latitude_corner_2 | Offset: 176, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    south_west_latitude_corner_2_raw = decode_number((data_raw >> 176) & 0xFFFFFFFF, 32)
    if south_west_latitude_corner_2_raw & (1 << (32 - 1)):
        south_west_latitude_corner_2_raw -= (1 << 32)
    south_west_latitude_corner_2 = south_west_latitude_corner_2_raw * 1e-07
    publish_field(hass, instance_name, 'south_west_latitude_corner_2', 'South West Latitude Corner 2', south_west_latitude_corner_2, 'AIS Channel Management', 'deg', '129806')

    # reserved | Offset: 208, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 208) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Channel Management', '', '129806')

    # addressed_or_broadcast_message_indicator | Offset: 214, Length: 2, Resolution: 1, Field Type: NUMBER
    addressed_or_broadcast_message_indicator_raw = decode_number((data_raw >> 214) & 0x3, 2)
    addressed_or_broadcast_message_indicator = addressed_or_broadcast_message_indicator_raw * 1
    publish_field(hass, instance_name, 'addressed_or_broadcast_message_indicator', 'Addressed or Broadcast Message Indicator', addressed_or_broadcast_message_indicator, 'AIS Channel Management', '', '129806')

    # channel_a_bandwidth | Offset: 216, Length: 7, Resolution: 1, Field Type: NUMBER
    channel_a_bandwidth_raw = decode_number((data_raw >> 216) & 0x7F, 7)
    channel_a_bandwidth = channel_a_bandwidth_raw * 1
    publish_field(hass, instance_name, 'channel_a_bandwidth', 'Channel A Bandwidth', channel_a_bandwidth, 'AIS Channel Management', '', '129806')

    # channel_b_bandwidth | Offset: 223, Length: 7, Resolution: 1, Field Type: NUMBER
    channel_b_bandwidth_raw = decode_number((data_raw >> 223) & 0x7F, 7)
    channel_b_bandwidth = channel_b_bandwidth_raw * 1
    publish_field(hass, instance_name, 'channel_b_bandwidth', 'Channel B Bandwidth', channel_b_bandwidth, 'AIS Channel Management', '', '129806')

    # reserved | Offset: 230, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 230) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Channel Management', '', '129806')

    # transitional_zone_size | Offset: 232, Length: 8, Resolution: 1, Field Type: NUMBER
    transitional_zone_size_raw = decode_number((data_raw >> 232) & 0xFF, 8)
    transitional_zone_size = transitional_zone_size_raw * 1
    publish_field(hass, instance_name, 'transitional_zone_size', 'Transitional Zone Size', transitional_zone_size, 'AIS Channel Management', '', '129806')

def process_pgn_129807(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129807."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Class B Group Assignment', '', '129807')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Class B Group Assignment', '', '129807')

    # source_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    source_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'AIS Class B Group Assignment', '', '129807')

    # spare | Offset: 40, Length: 2, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 40) & 0x3
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Class B Group Assignment', '', '129807')

    # tx_rx_mode | Offset: 42, Length: 4, Resolution: 1, Field Type: LOOKUP
    tx_rx_mode_raw = (data_raw >> 42) & 0xF
    tx_rx_mode = tx_rx_mode_raw * 1
    publish_field(hass, instance_name, 'tx_rx_mode', 'Tx/Rx Mode', tx_rx_mode, 'AIS Class B Group Assignment', '', '129807')

    # reserved | Offset: 46, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 46) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B Group Assignment', '', '129807')

    # north_east_longitude_corner_1 | Offset: 48, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    north_east_longitude_corner_1_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    if north_east_longitude_corner_1_raw & (1 << (32 - 1)):
        north_east_longitude_corner_1_raw -= (1 << 32)
    north_east_longitude_corner_1 = north_east_longitude_corner_1_raw * 1e-07
    publish_field(hass, instance_name, 'north_east_longitude_corner_1', 'North East Longitude Corner 1', north_east_longitude_corner_1, 'AIS Class B Group Assignment', 'deg', '129807')

    # north_east_latitude_corner_1 | Offset: 80, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    north_east_latitude_corner_1_raw = decode_number((data_raw >> 80) & 0xFFFFFFFF, 32)
    if north_east_latitude_corner_1_raw & (1 << (32 - 1)):
        north_east_latitude_corner_1_raw -= (1 << 32)
    north_east_latitude_corner_1 = north_east_latitude_corner_1_raw * 1e-07
    publish_field(hass, instance_name, 'north_east_latitude_corner_1', 'North East Latitude Corner 1', north_east_latitude_corner_1, 'AIS Class B Group Assignment', 'deg', '129807')

    # south_west_longitude_corner_1 | Offset: 112, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    south_west_longitude_corner_1_raw = decode_number((data_raw >> 112) & 0xFFFFFFFF, 32)
    if south_west_longitude_corner_1_raw & (1 << (32 - 1)):
        south_west_longitude_corner_1_raw -= (1 << 32)
    south_west_longitude_corner_1 = south_west_longitude_corner_1_raw * 1e-07
    publish_field(hass, instance_name, 'south_west_longitude_corner_1', 'South West Longitude Corner 1', south_west_longitude_corner_1, 'AIS Class B Group Assignment', 'deg', '129807')

    # south_west_latitude_corner_2 | Offset: 144, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    south_west_latitude_corner_2_raw = decode_number((data_raw >> 144) & 0xFFFFFFFF, 32)
    if south_west_latitude_corner_2_raw & (1 << (32 - 1)):
        south_west_latitude_corner_2_raw -= (1 << 32)
    south_west_latitude_corner_2 = south_west_latitude_corner_2_raw * 1e-07
    publish_field(hass, instance_name, 'south_west_latitude_corner_2', 'South West Latitude Corner 2', south_west_latitude_corner_2, 'AIS Class B Group Assignment', 'deg', '129807')

    # station_type | Offset: 176, Length: 4, Resolution: 1, Field Type: LOOKUP
    station_type_raw = (data_raw >> 176) & 0xF
    station_type = station_type_raw * 1
    publish_field(hass, instance_name, 'station_type', 'Station Type', station_type, 'AIS Class B Group Assignment', '', '129807')

    # reserved | Offset: 180, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 180) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B Group Assignment', '', '129807')

    # ship_and_cargo_filter | Offset: 184, Length: 8, Resolution: 1, Field Type: NUMBER
    ship_and_cargo_filter_raw = decode_number((data_raw >> 184) & 0xFF, 8)
    ship_and_cargo_filter = ship_and_cargo_filter_raw * 1
    publish_field(hass, instance_name, 'ship_and_cargo_filter', 'Ship and Cargo Filter', ship_and_cargo_filter, 'AIS Class B Group Assignment', '', '129807')

    # spare | Offset: 192, Length: 22, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 192) & 0x3FFFFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Class B Group Assignment', '', '129807')

    # reserved | Offset: 214, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 214) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B Group Assignment', '', '129807')

    # reporting_interval | Offset: 216, Length: 4, Resolution: 1, Field Type: LOOKUP
    reporting_interval_raw = (data_raw >> 216) & 0xF
    reporting_interval = reporting_interval_raw * 1
    publish_field(hass, instance_name, 'reporting_interval', 'Reporting Interval', reporting_interval, 'AIS Class B Group Assignment', '', '129807')

    # quiet_time | Offset: 220, Length: 4, Resolution: 1, Field Type: NUMBER
    quiet_time_raw = decode_number((data_raw >> 220) & 0xF, 4)
    quiet_time = quiet_time_raw * 1
    publish_field(hass, instance_name, 'quiet_time', 'Quiet Time', quiet_time, 'AIS Class B Group Assignment', '', '129807')

def process_pgn_129808(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129808."""
    # dsc_format | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    dsc_format_raw = (data_raw >> 0) & 0xFF
    dsc_format = dsc_format_raw * 1
    publish_field(hass, instance_name, 'dsc_format', 'DSC Format', dsc_format, 'DSC Distress Call Information', '', '129808')

    # dsc_category | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    dsc_category_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    dsc_category = dsc_category_raw * 1
    publish_field(hass, instance_name, 'dsc_category', 'DSC Category', dsc_category, 'DSC Distress Call Information', '', '129808')

    # dsc_message_address | Offset: 16, Length: 40, Resolution: 1, Field Type: DECIMAL
    dsc_message_address_raw = decode_decimal((data_raw >> 16) & 0xFFFFFFFFFF, 40)
    dsc_message_address = dsc_message_address_raw * 1
    publish_field(hass, instance_name, 'dsc_message_address', 'DSC Message Address', dsc_message_address, 'DSC Distress Call Information', '', '129808')

    # nature_of_distress | Offset: 56, Length: 8, Resolution: 1, Field Type: LOOKUP
    nature_of_distress_raw = (data_raw >> 56) & 0xFF
    nature_of_distress = nature_of_distress_raw * 1
    publish_field(hass, instance_name, 'nature_of_distress', 'Nature of Distress', nature_of_distress, 'DSC Distress Call Information', '', '129808')

    # subsequent_communication_mode_or_2nd_telecommand | Offset: 64, Length: 8, Resolution: 1, Field Type: LOOKUP
    subsequent_communication_mode_or_2nd_telecommand_raw = (data_raw >> 64) & 0xFF
    subsequent_communication_mode_or_2nd_telecommand = subsequent_communication_mode_or_2nd_telecommand_raw * 1
    publish_field(hass, instance_name, 'subsequent_communication_mode_or_2nd_telecommand', 'Subsequent Communication Mode or 2nd Telecommand', subsequent_communication_mode_or_2nd_telecommand, 'DSC Distress Call Information', '', '129808')

    # proposed_rx_frequency_channel | Offset: 72, Length: 48, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # proposed_tx_frequency_channel | Offset: 120, Length: 48, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_129808(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129808."""
    # dsc_format_symbol | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    dsc_format_symbol_raw = (data_raw >> 0) & 0xFF
    dsc_format_symbol = dsc_format_symbol_raw * 1
    publish_field(hass, instance_name, 'dsc_format_symbol', 'DSC Format Symbol', dsc_format_symbol, 'DSC Call Information', '', '129808')

    # dsc_category_symbol | Offset: 8, Length: 8, Resolution: 1, Field Type: LOOKUP
    dsc_category_symbol_raw = (data_raw >> 8) & 0xFF
    dsc_category_symbol = dsc_category_symbol_raw * 1
    publish_field(hass, instance_name, 'dsc_category_symbol', 'DSC Category Symbol', dsc_category_symbol, 'DSC Call Information', '', '129808')

    # dsc_message_address | Offset: 16, Length: 40, Resolution: 1, Field Type: DECIMAL
    dsc_message_address_raw = decode_decimal((data_raw >> 16) & 0xFFFFFFFFFF, 40)
    dsc_message_address = dsc_message_address_raw * 1
    publish_field(hass, instance_name, 'dsc_message_address', 'DSC Message Address', dsc_message_address, 'DSC Call Information', '', '129808')

    # __1st_telecommand | Offset: 56, Length: 8, Resolution: 1, Field Type: LOOKUP
    __1st_telecommand_raw = (data_raw >> 56) & 0xFF
    __1st_telecommand = __1st_telecommand_raw * 1
    publish_field(hass, instance_name, '__1st_telecommand', '1st Telecommand', __1st_telecommand, 'DSC Call Information', '', '129808')

    # subsequent_communication_mode_or_2nd_telecommand | Offset: 64, Length: 8, Resolution: 1, Field Type: LOOKUP
    subsequent_communication_mode_or_2nd_telecommand_raw = (data_raw >> 64) & 0xFF
    subsequent_communication_mode_or_2nd_telecommand = subsequent_communication_mode_or_2nd_telecommand_raw * 1
    publish_field(hass, instance_name, 'subsequent_communication_mode_or_2nd_telecommand', 'Subsequent Communication Mode or 2nd Telecommand', subsequent_communication_mode_or_2nd_telecommand, 'DSC Call Information', '', '129808')

    # proposed_rx_frequency_channel | Offset: 72, Length: 48, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # proposed_tx_frequency_channel | Offset: 120, Length: 48, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_129809(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129809."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Class B static data (msg 24 Part A)', '', '129809')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Class B static data (msg 24 Part A)', '', '129809')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS Class B static data (msg 24 Part A)', '', '129809')

    # name | Offset: 40, Length: 160, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # ais_transceiver_information | Offset: 200, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 200) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Class B static data (msg 24 Part A)', '', '129809')

    # reserved | Offset: 205, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 205) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B static data (msg 24 Part A)', '', '129809')

    # sequence_id | Offset: 208, Length: 8, Resolution: 1, Field Type: NUMBER
    sequence_id_raw = decode_number((data_raw >> 208) & 0xFF, 8)
    sequence_id = sequence_id_raw * 1
    publish_field(hass, instance_name, 'sequence_id', 'Sequence ID', sequence_id, 'AIS Class B static data (msg 24 Part A)', '', '129809')

def process_pgn_129810(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 129810."""
    # message_id | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 0) & 0x3F
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # repeat_indicator | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 6) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # user_id | Offset: 8, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 8) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # type_of_ship | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    type_of_ship_raw = (data_raw >> 40) & 0xFF
    type_of_ship = type_of_ship_raw * 1
    publish_field(hass, instance_name, 'type_of_ship', 'Type of ship', type_of_ship, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # vendor_id | Offset: 48, Length: 56, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # callsign | Offset: 104, Length: 56, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # length | Offset: 160, Length: 16, Resolution: 0.1, Field Type: NUMBER
    length_raw = decode_number((data_raw >> 160) & 0xFFFF, 16)
    length = length_raw * 0.1
    publish_field(hass, instance_name, 'length', 'Length', length, 'AIS Class B static data (msg 24 Part B)', 'm', '129810')

    # beam | Offset: 176, Length: 16, Resolution: 0.1, Field Type: NUMBER
    beam_raw = decode_number((data_raw >> 176) & 0xFFFF, 16)
    beam = beam_raw * 0.1
    publish_field(hass, instance_name, 'beam', 'Beam', beam, 'AIS Class B static data (msg 24 Part B)', 'm', '129810')

    # position_reference_from_starboard | Offset: 192, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_starboard_raw = decode_number((data_raw >> 192) & 0xFFFF, 16)
    position_reference_from_starboard = position_reference_from_starboard_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_starboard', 'Position reference from Starboard', position_reference_from_starboard, 'AIS Class B static data (msg 24 Part B)', 'm', '129810')

    # position_reference_from_bow | Offset: 208, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_bow_raw = decode_number((data_raw >> 208) & 0xFFFF, 16)
    position_reference_from_bow = position_reference_from_bow_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_bow', 'Position reference from Bow', position_reference_from_bow, 'AIS Class B static data (msg 24 Part B)', 'm', '129810')

    # mothership_user_id | Offset: 224, Length: 32, Resolution: 1, Field Type: MMSI
    mothership_user_id_raw = (data_raw >> 224) & 0xFFFFFFFF
    mothership_user_id = mothership_user_id_raw * 1
    publish_field(hass, instance_name, 'mothership_user_id', 'Mothership User ID', mothership_user_id, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # reserved | Offset: 256, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 256) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # spare | Offset: 258, Length: 6, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 258) & 0x3F
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # ais_transceiver_information | Offset: 264, Length: 5, Resolution: 1, Field Type: LOOKUP
    ais_transceiver_information_raw = (data_raw >> 264) & 0x1F
    ais_transceiver_information = ais_transceiver_information_raw * 1
    publish_field(hass, instance_name, 'ais_transceiver_information', 'AIS Transceiver information', ais_transceiver_information, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # reserved | Offset: 269, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 269) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'AIS Class B static data (msg 24 Part B)', '', '129810')

    # sequence_id | Offset: 272, Length: 8, Resolution: 1, Field Type: NUMBER
    sequence_id_raw = decode_number((data_raw >> 272) & 0xFF, 8)
    sequence_id = sequence_id_raw * 1
    publish_field(hass, instance_name, 'sequence_id', 'Sequence ID', sequence_id, 'AIS Class B static data (msg 24 Part B)', '', '129810')

def process_pgn_130052(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130052."""
    # group_repetition_interval__gri_ | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    group_repetition_interval__gri__raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if group_repetition_interval__gri__raw & (1 << (32 - 1)):
        group_repetition_interval__gri__raw -= (1 << 32)
    group_repetition_interval__gri_ = group_repetition_interval__gri__raw * 1
    publish_field(hass, instance_name, 'group_repetition_interval__gri_', 'Group Repetition Interval (GRI)', group_repetition_interval__gri_, 'Loran-C TD Data', '', '130052')

    # master_range | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    master_range_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if master_range_raw & (1 << (32 - 1)):
        master_range_raw -= (1 << 32)
    master_range = master_range_raw * 1
    publish_field(hass, instance_name, 'master_range', 'Master Range', master_range, 'Loran-C TD Data', '', '130052')

    # v_secondary_td | Offset: 64, Length: 32, Resolution: 1, Field Type: NUMBER
    v_secondary_td_raw = decode_number((data_raw >> 64) & 0xFFFFFFFF, 32)
    if v_secondary_td_raw & (1 << (32 - 1)):
        v_secondary_td_raw -= (1 << 32)
    v_secondary_td = v_secondary_td_raw * 1
    publish_field(hass, instance_name, 'v_secondary_td', 'V Secondary TD', v_secondary_td, 'Loran-C TD Data', '', '130052')

    # w_secondary_td | Offset: 96, Length: 32, Resolution: 1, Field Type: NUMBER
    w_secondary_td_raw = decode_number((data_raw >> 96) & 0xFFFFFFFF, 32)
    if w_secondary_td_raw & (1 << (32 - 1)):
        w_secondary_td_raw -= (1 << 32)
    w_secondary_td = w_secondary_td_raw * 1
    publish_field(hass, instance_name, 'w_secondary_td', 'W Secondary TD', w_secondary_td, 'Loran-C TD Data', '', '130052')

    # x_secondary_td | Offset: 128, Length: 32, Resolution: 1, Field Type: NUMBER
    x_secondary_td_raw = decode_number((data_raw >> 128) & 0xFFFFFFFF, 32)
    if x_secondary_td_raw & (1 << (32 - 1)):
        x_secondary_td_raw -= (1 << 32)
    x_secondary_td = x_secondary_td_raw * 1
    publish_field(hass, instance_name, 'x_secondary_td', 'X Secondary TD', x_secondary_td, 'Loran-C TD Data', '', '130052')

    # y_secondary_td | Offset: 160, Length: 32, Resolution: 1, Field Type: NUMBER
    y_secondary_td_raw = decode_number((data_raw >> 160) & 0xFFFFFFFF, 32)
    if y_secondary_td_raw & (1 << (32 - 1)):
        y_secondary_td_raw -= (1 << 32)
    y_secondary_td = y_secondary_td_raw * 1
    publish_field(hass, instance_name, 'y_secondary_td', 'Y Secondary TD', y_secondary_td, 'Loran-C TD Data', '', '130052')

    # z_secondary_td | Offset: 192, Length: 32, Resolution: 1, Field Type: NUMBER
    z_secondary_td_raw = decode_number((data_raw >> 192) & 0xFFFFFFFF, 32)
    if z_secondary_td_raw & (1 << (32 - 1)):
        z_secondary_td_raw -= (1 << 32)
    z_secondary_td = z_secondary_td_raw * 1
    publish_field(hass, instance_name, 'z_secondary_td', 'Z Secondary TD', z_secondary_td, 'Loran-C TD Data', '', '130052')

    # station_status__master | Offset: 224, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__master_raw = (data_raw >> 224) & 0xF
    station_status__master = station_status__master_raw * 1
    publish_field(hass, instance_name, 'station_status__master', 'Station status: Master', station_status__master, 'Loran-C TD Data', '', '130052')

    # station_status__v | Offset: 228, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__v_raw = (data_raw >> 228) & 0xF
    station_status__v = station_status__v_raw * 1
    publish_field(hass, instance_name, 'station_status__v', 'Station status: V', station_status__v, 'Loran-C TD Data', '', '130052')

    # station_status__w | Offset: 232, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__w_raw = (data_raw >> 232) & 0xF
    station_status__w = station_status__w_raw * 1
    publish_field(hass, instance_name, 'station_status__w', 'Station status: W', station_status__w, 'Loran-C TD Data', '', '130052')

    # station_status__x | Offset: 236, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__x_raw = (data_raw >> 236) & 0xF
    station_status__x = station_status__x_raw * 1
    publish_field(hass, instance_name, 'station_status__x', 'Station status: X', station_status__x, 'Loran-C TD Data', '', '130052')

    # station_status__y | Offset: 240, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__y_raw = (data_raw >> 240) & 0xF
    station_status__y = station_status__y_raw * 1
    publish_field(hass, instance_name, 'station_status__y', 'Station status: Y', station_status__y, 'Loran-C TD Data', '', '130052')

    # station_status__z | Offset: 244, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__z_raw = (data_raw >> 244) & 0xF
    station_status__z = station_status__z_raw * 1
    publish_field(hass, instance_name, 'station_status__z', 'Station status: Z', station_status__z, 'Loran-C TD Data', '', '130052')

    # mode | Offset: 248, Length: 4, Resolution: 1, Field Type: LOOKUP
    mode_raw = (data_raw >> 248) & 0xF
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Loran-C TD Data', '', '130052')

    # reserved | Offset: 252, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 252) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Loran-C TD Data', '', '130052')

def process_pgn_130053(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130053."""
    # group_repetition_interval__gri_ | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    group_repetition_interval__gri__raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if group_repetition_interval__gri__raw & (1 << (32 - 1)):
        group_repetition_interval__gri__raw -= (1 << 32)
    group_repetition_interval__gri_ = group_repetition_interval__gri__raw * 1
    publish_field(hass, instance_name, 'group_repetition_interval__gri_', 'Group Repetition Interval (GRI)', group_repetition_interval__gri_, 'Loran-C Range Data', '', '130053')

    # master_range | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    master_range_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    if master_range_raw & (1 << (32 - 1)):
        master_range_raw -= (1 << 32)
    master_range = master_range_raw * 1
    publish_field(hass, instance_name, 'master_range', 'Master Range', master_range, 'Loran-C Range Data', '', '130053')

    # v_secondary_range | Offset: 64, Length: 32, Resolution: 1, Field Type: NUMBER
    v_secondary_range_raw = decode_number((data_raw >> 64) & 0xFFFFFFFF, 32)
    if v_secondary_range_raw & (1 << (32 - 1)):
        v_secondary_range_raw -= (1 << 32)
    v_secondary_range = v_secondary_range_raw * 1
    publish_field(hass, instance_name, 'v_secondary_range', 'V Secondary Range', v_secondary_range, 'Loran-C Range Data', '', '130053')

    # w_secondary_range | Offset: 96, Length: 32, Resolution: 1, Field Type: NUMBER
    w_secondary_range_raw = decode_number((data_raw >> 96) & 0xFFFFFFFF, 32)
    if w_secondary_range_raw & (1 << (32 - 1)):
        w_secondary_range_raw -= (1 << 32)
    w_secondary_range = w_secondary_range_raw * 1
    publish_field(hass, instance_name, 'w_secondary_range', 'W Secondary Range', w_secondary_range, 'Loran-C Range Data', '', '130053')

    # x_secondary_range | Offset: 128, Length: 32, Resolution: 1, Field Type: NUMBER
    x_secondary_range_raw = decode_number((data_raw >> 128) & 0xFFFFFFFF, 32)
    if x_secondary_range_raw & (1 << (32 - 1)):
        x_secondary_range_raw -= (1 << 32)
    x_secondary_range = x_secondary_range_raw * 1
    publish_field(hass, instance_name, 'x_secondary_range', 'X Secondary Range', x_secondary_range, 'Loran-C Range Data', '', '130053')

    # y_secondary_range | Offset: 160, Length: 32, Resolution: 1, Field Type: NUMBER
    y_secondary_range_raw = decode_number((data_raw >> 160) & 0xFFFFFFFF, 32)
    if y_secondary_range_raw & (1 << (32 - 1)):
        y_secondary_range_raw -= (1 << 32)
    y_secondary_range = y_secondary_range_raw * 1
    publish_field(hass, instance_name, 'y_secondary_range', 'Y Secondary Range', y_secondary_range, 'Loran-C Range Data', '', '130053')

    # z_secondary_range | Offset: 192, Length: 32, Resolution: 1, Field Type: NUMBER
    z_secondary_range_raw = decode_number((data_raw >> 192) & 0xFFFFFFFF, 32)
    if z_secondary_range_raw & (1 << (32 - 1)):
        z_secondary_range_raw -= (1 << 32)
    z_secondary_range = z_secondary_range_raw * 1
    publish_field(hass, instance_name, 'z_secondary_range', 'Z Secondary Range', z_secondary_range, 'Loran-C Range Data', '', '130053')

    # station_status__master | Offset: 224, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__master_raw = (data_raw >> 224) & 0xF
    station_status__master = station_status__master_raw * 1
    publish_field(hass, instance_name, 'station_status__master', 'Station status: Master', station_status__master, 'Loran-C Range Data', '', '130053')

    # station_status__v | Offset: 228, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__v_raw = (data_raw >> 228) & 0xF
    station_status__v = station_status__v_raw * 1
    publish_field(hass, instance_name, 'station_status__v', 'Station status: V', station_status__v, 'Loran-C Range Data', '', '130053')

    # station_status__w | Offset: 232, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__w_raw = (data_raw >> 232) & 0xF
    station_status__w = station_status__w_raw * 1
    publish_field(hass, instance_name, 'station_status__w', 'Station status: W', station_status__w, 'Loran-C Range Data', '', '130053')

    # station_status__x | Offset: 236, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__x_raw = (data_raw >> 236) & 0xF
    station_status__x = station_status__x_raw * 1
    publish_field(hass, instance_name, 'station_status__x', 'Station status: X', station_status__x, 'Loran-C Range Data', '', '130053')

    # station_status__y | Offset: 240, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__y_raw = (data_raw >> 240) & 0xF
    station_status__y = station_status__y_raw * 1
    publish_field(hass, instance_name, 'station_status__y', 'Station status: Y', station_status__y, 'Loran-C Range Data', '', '130053')

    # station_status__z | Offset: 244, Length: 4, Resolution: 1, Field Type: BITLOOKUP
    station_status__z_raw = (data_raw >> 244) & 0xF
    station_status__z = station_status__z_raw * 1
    publish_field(hass, instance_name, 'station_status__z', 'Station status: Z', station_status__z, 'Loran-C Range Data', '', '130053')

    # mode | Offset: 248, Length: 4, Resolution: 1, Field Type: LOOKUP
    mode_raw = (data_raw >> 248) & 0xF
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Loran-C Range Data', '', '130053')

    # reserved | Offset: 252, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 252) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Loran-C Range Data', '', '130053')

def process_pgn_130054(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130054."""
    # group_repetition_interval__gri_ | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    group_repetition_interval__gri__raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    if group_repetition_interval__gri__raw & (1 << (32 - 1)):
        group_repetition_interval__gri__raw -= (1 << 32)
    group_repetition_interval__gri_ = group_repetition_interval__gri__raw * 1
    publish_field(hass, instance_name, 'group_repetition_interval__gri_', 'Group Repetition Interval (GRI)', group_repetition_interval__gri_, 'Loran-C Signal Data', '', '130054')

    # station_identifier | Offset: 32, Length: 8, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # station_snr | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    station_snr_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if station_snr_raw & (1 << (16 - 1)):
        station_snr_raw -= (1 << 16)
    station_snr = station_snr_raw * 0.01
    publish_field(hass, instance_name, 'station_snr', 'Station SNR', station_snr, 'Loran-C Signal Data', 'dB', '130054')

    # station_ecd | Offset: 56, Length: 32, Resolution: 1, Field Type: NUMBER
    station_ecd_raw = decode_number((data_raw >> 56) & 0xFFFFFFFF, 32)
    if station_ecd_raw & (1 << (32 - 1)):
        station_ecd_raw -= (1 << 32)
    station_ecd = station_ecd_raw * 1
    publish_field(hass, instance_name, 'station_ecd', 'Station ECD', station_ecd, 'Loran-C Signal Data', '', '130054')

    # station_asf | Offset: 88, Length: 32, Resolution: 1, Field Type: NUMBER
    station_asf_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    if station_asf_raw & (1 << (32 - 1)):
        station_asf_raw -= (1 << 32)
    station_asf = station_asf_raw * 1
    publish_field(hass, instance_name, 'station_asf', 'Station ASF', station_asf, 'Loran-C Signal Data', '', '130054')

def process_pgn_130060(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130060."""
    # hardware_channel_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    hardware_channel_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    hardware_channel_id = hardware_channel_id_raw * 1
    publish_field(hass, instance_name, 'hardware_channel_id', 'Hardware Channel ID', hardware_channel_id, 'Label', '', '130060')

    # pgn | Offset: 8, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 8) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'Label', '', '130060')

    # data_source_instance_field_number | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_field_number_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    data_source_instance_field_number = data_source_instance_field_number_raw * 1
    publish_field(hass, instance_name, 'data_source_instance_field_number', 'Data Source Instance Field Number', data_source_instance_field_number, 'Label', '', '130060')

    # data_source_instance_value | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_value_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    data_source_instance_value = data_source_instance_value_raw * 1
    publish_field(hass, instance_name, 'data_source_instance_value', 'Data Source Instance Value', data_source_instance_value, 'Label', '', '130060')

    # secondary_enumeration_field_number | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    secondary_enumeration_field_number_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    secondary_enumeration_field_number = secondary_enumeration_field_number_raw * 1
    publish_field(hass, instance_name, 'secondary_enumeration_field_number', 'Secondary Enumeration Field Number', secondary_enumeration_field_number, 'Label', '', '130060')

    # secondary_enumeration_field_value | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    secondary_enumeration_field_value_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    secondary_enumeration_field_value = secondary_enumeration_field_value_raw * 1
    publish_field(hass, instance_name, 'secondary_enumeration_field_value', 'Secondary Enumeration Field Value', secondary_enumeration_field_value, 'Label', '', '130060')

    # parameter_field_number | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    parameter_field_number_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    parameter_field_number = parameter_field_number_raw * 1
    publish_field(hass, instance_name, 'parameter_field_number', 'Parameter Field Number', parameter_field_number, 'Label', '', '130060')

def process_pgn_130061(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130061."""
    # data_source_channel_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_channel_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    data_source_channel_id = data_source_channel_id_raw * 1
    publish_field(hass, instance_name, 'data_source_channel_id', 'Data Source Channel ID', data_source_channel_id, 'Channel Source Configuration', '', '130061')

    # source_selection_status | Offset: 8, Length: 2, Resolution: 1, Field Type: NUMBER
    source_selection_status_raw = decode_number((data_raw >> 8) & 0x3, 2)
    source_selection_status = source_selection_status_raw * 1
    publish_field(hass, instance_name, 'source_selection_status', 'Source Selection Status', source_selection_status, 'Channel Source Configuration', '', '130061')

    # reserved | Offset: 10, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 10) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Channel Source Configuration', '', '130061')

    # name_selection_criteria_mask | Offset: 12, Length: 12, Resolution: 1, Field Type: BINARY
    name_selection_criteria_mask_raw = (data_raw >> 12) & 0xFFF
    name_selection_criteria_mask = name_selection_criteria_mask_raw * 1
    publish_field(hass, instance_name, 'name_selection_criteria_mask', 'NAME Selection Criteria Mask', name_selection_criteria_mask, 'Channel Source Configuration', '', '130061')

    # source_name | Offset: 24, Length: 64, Resolution: 1, Field Type: NUMBER
    source_name_raw = decode_number((data_raw >> 24) & 0xFFFFFFFFFFFFFFFF, 64)
    source_name = source_name_raw * 1
    publish_field(hass, instance_name, 'source_name', 'Source NAME', source_name, 'Channel Source Configuration', '', '130061')

    # pgn | Offset: 88, Length: 24, Resolution: 1, Field Type: NUMBER
    pgn_raw = decode_number((data_raw >> 88) & 0xFFFFFF, 24)
    pgn = pgn_raw * 1
    publish_field(hass, instance_name, 'pgn', 'PGN', pgn, 'Channel Source Configuration', '', '130061')

    # data_source_instance_field_number | Offset: 112, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_field_number_raw = decode_number((data_raw >> 112) & 0xFF, 8)
    data_source_instance_field_number = data_source_instance_field_number_raw * 1
    publish_field(hass, instance_name, 'data_source_instance_field_number', 'Data Source Instance Field Number', data_source_instance_field_number, 'Channel Source Configuration', '', '130061')

    # data_source_instance_value | Offset: 120, Length: 8, Resolution: 1, Field Type: NUMBER
    data_source_instance_value_raw = decode_number((data_raw >> 120) & 0xFF, 8)
    data_source_instance_value = data_source_instance_value_raw * 1
    publish_field(hass, instance_name, 'data_source_instance_value', 'Data Source Instance Value', data_source_instance_value, 'Channel Source Configuration', '', '130061')

    # secondary_enumeration_field_number | Offset: 128, Length: 8, Resolution: 1, Field Type: NUMBER
    secondary_enumeration_field_number_raw = decode_number((data_raw >> 128) & 0xFF, 8)
    secondary_enumeration_field_number = secondary_enumeration_field_number_raw * 1
    publish_field(hass, instance_name, 'secondary_enumeration_field_number', 'Secondary Enumeration Field Number', secondary_enumeration_field_number, 'Channel Source Configuration', '', '130061')

    # secondary_enumeration_field_value | Offset: 136, Length: 8, Resolution: 1, Field Type: NUMBER
    secondary_enumeration_field_value_raw = decode_number((data_raw >> 136) & 0xFF, 8)
    secondary_enumeration_field_value = secondary_enumeration_field_value_raw * 1
    publish_field(hass, instance_name, 'secondary_enumeration_field_value', 'Secondary Enumeration Field Value', secondary_enumeration_field_value, 'Channel Source Configuration', '', '130061')

    # parameter_field_number | Offset: 144, Length: 8, Resolution: 1, Field Type: NUMBER
    parameter_field_number_raw = decode_number((data_raw >> 144) & 0xFF, 8)
    parameter_field_number = parameter_field_number_raw * 1
    publish_field(hass, instance_name, 'parameter_field_number', 'Parameter Field Number', parameter_field_number, 'Channel Source Configuration', '', '130061')

def process_pgn_130064(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130064."""
    # start_database_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_database_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_database_id = start_database_id_raw * 1
    publish_field(hass, instance_name, 'start_database_id', 'Start Database ID', start_database_id, 'Route and WP Service - Database List', '', '130064')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - Database List', '', '130064')

    # number_of_databases_available | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_databases_available_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    number_of_databases_available = number_of_databases_available_raw * 1
    publish_field(hass, instance_name, 'number_of_databases_available', 'Number of Databases Available', number_of_databases_available, 'Route and WP Service - Database List', '', '130064')

    # database_id | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - Database List', '', '130064')

def process_pgn_130065(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130065."""
    # start_route_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_route_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_route_id = start_route_id_raw * 1
    publish_field(hass, instance_name, 'start_route_id', 'Start Route ID', start_route_id, 'Route and WP Service - Route List', '', '130065')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - Route List', '', '130065')

    # number_of_routes_in_database | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_routes_in_database_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    number_of_routes_in_database = number_of_routes_in_database_raw * 1
    publish_field(hass, instance_name, 'number_of_routes_in_database', 'Number of Routes in Database', number_of_routes_in_database, 'Route and WP Service - Route List', '', '130065')

    # database_id | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - Route List', '', '130065')

    # route_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Route and WP Service - Route List', '', '130065')

def process_pgn_130066(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130066."""
    # database_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - Route/WP-List Attributes', '', '130066')

    # route_id | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Route and WP Service - Route/WP-List Attributes', '', '130066')

def process_pgn_130067(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130067."""
    # start_rps_ | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_rps__raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_rps_ = start_rps__raw * 1
    publish_field(hass, instance_name, 'start_rps_', 'Start RPS#', start_rps_, 'Route and WP Service - Route - WP Name & Position', '', '130067')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - Route - WP Name & Position', '', '130067')

    # number_of_wps_in_the_route_wp_list | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_wps_in_the_route_wp_list_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    number_of_wps_in_the_route_wp_list = number_of_wps_in_the_route_wp_list_raw * 1
    publish_field(hass, instance_name, 'number_of_wps_in_the_route_wp_list', 'Number of WPs in the Route/WP-List', number_of_wps_in_the_route_wp_list, 'Route and WP Service - Route - WP Name & Position', '', '130067')

    # database_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - Route - WP Name & Position', '', '130067')

    # route_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Route and WP Service - Route - WP Name & Position', '', '130067')

    # wp_id | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    wp_id_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    wp_id = wp_id_raw * 1
    publish_field(hass, instance_name, 'wp_id', 'WP ID', wp_id, 'Route and WP Service - Route - WP Name & Position', '', '130067')

def process_pgn_130068(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130068."""
    # start_rps_ | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_rps__raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_rps_ = start_rps__raw * 1
    publish_field(hass, instance_name, 'start_rps_', 'Start RPS#', start_rps_, 'Route and WP Service - Route - WP Name', '', '130068')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - Route - WP Name', '', '130068')

    # number_of_wps_in_the_route_wp_list | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_wps_in_the_route_wp_list_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    number_of_wps_in_the_route_wp_list = number_of_wps_in_the_route_wp_list_raw * 1
    publish_field(hass, instance_name, 'number_of_wps_in_the_route_wp_list', 'Number of WPs in the Route/WP-List', number_of_wps_in_the_route_wp_list, 'Route and WP Service - Route - WP Name', '', '130068')

    # database_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - Route - WP Name', '', '130068')

    # route_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Route and WP Service - Route - WP Name', '', '130068')

    # wp_id | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    wp_id_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    wp_id = wp_id_raw * 1
    publish_field(hass, instance_name, 'wp_id', 'WP ID', wp_id, 'Route and WP Service - Route - WP Name', '', '130068')

def process_pgn_130069(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130069."""
    # start_rps_ | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_rps__raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_rps_ = start_rps__raw * 1
    publish_field(hass, instance_name, 'start_rps_', 'Start RPS#', start_rps_, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

    # number_of_wps_with_a_specific_xte_limit_or_nav__method | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_wps_with_a_specific_xte_limit_or_nav__method_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    number_of_wps_with_a_specific_xte_limit_or_nav__method = number_of_wps_with_a_specific_xte_limit_or_nav__method_raw * 1
    publish_field(hass, instance_name, 'number_of_wps_with_a_specific_xte_limit_or_nav__method', 'Number of WPs with a specific XTE Limit or Nav. Method', number_of_wps_with_a_specific_xte_limit_or_nav__method, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

    # database_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

    # route_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

    # rps_ | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    rps__raw = decode_number((data_raw >> 48) & 0xFF, 8)
    rps_ = rps__raw * 1
    publish_field(hass, instance_name, 'rps_', 'RPS#', rps_, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

    # xte_limit_in_the_leg_after_wp | Offset: 56, Length: 16, Resolution: 1, Field Type: NUMBER
    xte_limit_in_the_leg_after_wp_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    xte_limit_in_the_leg_after_wp = xte_limit_in_the_leg_after_wp_raw * 1
    publish_field(hass, instance_name, 'xte_limit_in_the_leg_after_wp', 'XTE limit in the leg after WP', xte_limit_in_the_leg_after_wp, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

    # nav__method_in_the_leg_after_wp | Offset: 72, Length: 4, Resolution: 1, Field Type: NUMBER
    nav__method_in_the_leg_after_wp_raw = decode_number((data_raw >> 72) & 0xF, 4)
    nav__method_in_the_leg_after_wp = nav__method_in_the_leg_after_wp_raw * 1
    publish_field(hass, instance_name, 'nav__method_in_the_leg_after_wp', 'Nav. Method in the leg after WP', nav__method_in_the_leg_after_wp, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

    # reserved | Offset: 76, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 76) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Route and WP Service - XTE Limit & Navigation Method', '', '130069')

def process_pgn_130070(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130070."""
    # start_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_id = start_id_raw * 1
    publish_field(hass, instance_name, 'start_id', 'Start ID', start_id, 'Route and WP Service - WP Comment', '', '130070')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - WP Comment', '', '130070')

    # number_of_wps_with_comments | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_wps_with_comments_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    number_of_wps_with_comments = number_of_wps_with_comments_raw * 1
    publish_field(hass, instance_name, 'number_of_wps_with_comments', 'Number of WPs with Comments', number_of_wps_with_comments, 'Route and WP Service - WP Comment', '', '130070')

    # database_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - WP Comment', '', '130070')

    # route_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Route and WP Service - WP Comment', '', '130070')

    # wp_id___rps_ | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    wp_id___rps__raw = decode_number((data_raw >> 48) & 0xFF, 8)
    wp_id___rps_ = wp_id___rps__raw * 1
    publish_field(hass, instance_name, 'wp_id___rps_', 'WP ID / RPS#', wp_id___rps_, 'Route and WP Service - WP Comment', '', '130070')

def process_pgn_130071(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130071."""
    # start_route_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_route_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_route_id = start_route_id_raw * 1
    publish_field(hass, instance_name, 'start_route_id', 'Start Route ID', start_route_id, 'Route and WP Service - Route Comment', '', '130071')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - Route Comment', '', '130071')

    # number_of_routes_with_comments | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_routes_with_comments_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    number_of_routes_with_comments = number_of_routes_with_comments_raw * 1
    publish_field(hass, instance_name, 'number_of_routes_with_comments', 'Number of Routes with Comments', number_of_routes_with_comments, 'Route and WP Service - Route Comment', '', '130071')

    # database_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - Route Comment', '', '130071')

    # route_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Route and WP Service - Route Comment', '', '130071')

def process_pgn_130072(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130072."""
    # start_database_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_database_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_database_id = start_database_id_raw * 1
    publish_field(hass, instance_name, 'start_database_id', 'Start Database ID', start_database_id, 'Route and WP Service - Database Comment', '', '130072')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - Database Comment', '', '130072')

    # number_of_databases_with_comments | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_databases_with_comments_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    number_of_databases_with_comments = number_of_databases_with_comments_raw * 1
    publish_field(hass, instance_name, 'number_of_databases_with_comments', 'Number of Databases with Comments', number_of_databases_with_comments, 'Route and WP Service - Database Comment', '', '130072')

    # database_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - Database Comment', '', '130072')

def process_pgn_130073(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130073."""
    # start_rps_ | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_rps__raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_rps_ = start_rps__raw * 1
    publish_field(hass, instance_name, 'start_rps_', 'Start RPS#', start_rps_, 'Route and WP Service - Radius of Turn', '', '130073')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - Radius of Turn', '', '130073')

    # number_of_wps_with_a_specific_radius_of_turn | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_wps_with_a_specific_radius_of_turn_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    number_of_wps_with_a_specific_radius_of_turn = number_of_wps_with_a_specific_radius_of_turn_raw * 1
    publish_field(hass, instance_name, 'number_of_wps_with_a_specific_radius_of_turn', 'Number of WPs with a specific Radius of Turn', number_of_wps_with_a_specific_radius_of_turn, 'Route and WP Service - Radius of Turn', '', '130073')

    # database_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - Radius of Turn', '', '130073')

    # route_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    route_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    route_id = route_id_raw * 1
    publish_field(hass, instance_name, 'route_id', 'Route ID', route_id, 'Route and WP Service - Radius of Turn', '', '130073')

    # rps_ | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    rps__raw = decode_number((data_raw >> 48) & 0xFF, 8)
    rps_ = rps__raw * 1
    publish_field(hass, instance_name, 'rps_', 'RPS#', rps_, 'Route and WP Service - Radius of Turn', '', '130073')

    # radius_of_turn | Offset: 56, Length: 16, Resolution: 1, Field Type: NUMBER
    radius_of_turn_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    radius_of_turn = radius_of_turn_raw * 1
    publish_field(hass, instance_name, 'radius_of_turn', 'Radius of Turn', radius_of_turn, 'Route and WP Service - Radius of Turn', '', '130073')

def process_pgn_130074(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130074."""
    # start_wp_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    start_wp_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    start_wp_id = start_wp_id_raw * 1
    publish_field(hass, instance_name, 'start_wp_id', 'Start WP ID', start_wp_id, 'Route and WP Service - WP List - WP Name & Position', '', '130074')

    # nitems | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    nitems_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    nitems = nitems_raw * 1
    publish_field(hass, instance_name, 'nitems', 'nItems', nitems, 'Route and WP Service - WP List - WP Name & Position', '', '130074')

    # number_of_valid_wps_in_the_wp_list | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_valid_wps_in_the_wp_list_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    number_of_valid_wps_in_the_wp_list = number_of_valid_wps_in_the_wp_list_raw * 1
    publish_field(hass, instance_name, 'number_of_valid_wps_in_the_wp_list', 'Number of valid WPs in the WP-List', number_of_valid_wps_in_the_wp_list, 'Route and WP Service - WP List - WP Name & Position', '', '130074')

    # database_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    database_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    database_id = database_id_raw * 1
    publish_field(hass, instance_name, 'database_id', 'Database ID', database_id, 'Route and WP Service - WP List - WP Name & Position', '', '130074')

    # reserved | Offset: 40, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Route and WP Service - WP List - WP Name & Position', '', '130074')

    # wp_id | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    wp_id_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    wp_id = wp_id_raw * 1
    publish_field(hass, instance_name, 'wp_id', 'WP ID', wp_id, 'Route and WP Service - WP List - WP Name & Position', '', '130074')

def process_pgn_130306(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130306."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Wind Data', '', '130306')

    # wind_speed | Offset: 8, Length: 16, Resolution: 0.01, Field Type: NUMBER
    wind_speed_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    wind_speed = wind_speed_raw * 0.01
    publish_field(hass, instance_name, 'wind_speed', 'Wind Speed', wind_speed, 'Wind Data', 'm/s', '130306')
    publish_field(hass, instance_name, 'wind_speed_knots', 'Wind Speed Knots', mps_to_knots(wind_speed), 'Wind Data', 'Kn', '130306')

    # wind_angle | Offset: 24, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    wind_angle_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    wind_angle = wind_angle_raw * 0.0001
    publish_field(hass, instance_name, 'wind_angle', 'Wind Angle', wind_angle, 'Wind Data', 'rad', '130306')
    publish_field(hass, instance_name, 'wind_angle_degrees', 'Wind Angle Degrees', radians_to_degrees(wind_angle), 'Wind Data', 'Deg', '130306')

    # reference | Offset: 40, Length: 3, Resolution: 1, Field Type: LOOKUP
    reference_raw = (data_raw >> 40) & 0x7
    reference = reference_raw * 1
    publish_field(hass, instance_name, 'reference', 'Reference', reference, 'Wind Data', '', '130306')

    # reserved | Offset: 43, Length: 21, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 43) & 0x1FFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Wind Data', '', '130306')

def process_pgn_130310(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130310."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Environmental Parameters (obsolete)', '', '130310')

    # water_temperature | Offset: 8, Length: 16, Resolution: 0.01, Field Type: NUMBER
    water_temperature_raw = decode_number((data_raw >> 8) & 0xFFFF, 16)
    water_temperature = water_temperature_raw * 0.01
    publish_field(hass, instance_name, 'water_temperature', 'Water Temperature', water_temperature, 'Environmental Parameters (obsolete)', 'K', '130310')
    publish_field(hass, instance_name, 'water_temperature_celsius', 'Water Temperature Celsius', kelvin_to_celsius(water_temperature), 'Environmental Parameters (obsolete)', 'C', '130310')
    publish_field(hass, instance_name, 'water_temperature_fahrenheit', 'Water Temperature Fahrenheit', kelvin_to_fahrenheit(water_temperature), 'Environmental Parameters (obsolete)', 'F', '130310')

    # outside_ambient_air_temperature | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    outside_ambient_air_temperature_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    outside_ambient_air_temperature = outside_ambient_air_temperature_raw * 0.01
    publish_field(hass, instance_name, 'outside_ambient_air_temperature', 'Outside Ambient Air Temperature', outside_ambient_air_temperature, 'Environmental Parameters (obsolete)', 'K', '130310')
    publish_field(hass, instance_name, 'outside_ambient_air_temperature_celsius', 'Outside Ambient Air Temperature Celsius', kelvin_to_celsius(outside_ambient_air_temperature), 'Environmental Parameters (obsolete)', 'C', '130310')
    publish_field(hass, instance_name, 'outside_ambient_air_temperature_fahrenheit', 'Outside Ambient Air Temperature Fahrenheit', kelvin_to_fahrenheit(outside_ambient_air_temperature), 'Environmental Parameters (obsolete)', 'F', '130310')

    # atmospheric_pressure | Offset: 40, Length: 16, Resolution: 100, Field Type: NUMBER
    atmospheric_pressure_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    atmospheric_pressure = atmospheric_pressure_raw * 100
    publish_field(hass, instance_name, 'atmospheric_pressure', 'Atmospheric Pressure', atmospheric_pressure, 'Environmental Parameters (obsolete)', 'Pa', '130310')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Environmental Parameters (obsolete)', '', '130310')

def process_pgn_130311(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130311."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Environmental Parameters', '', '130311')

    # temperature_source | Offset: 8, Length: 6, Resolution: 1, Field Type: LOOKUP
    temperature_source_raw = (data_raw >> 8) & 0x3F
    temperature_source = temperature_source_raw * 1
    publish_field(hass, instance_name, 'temperature_source', 'Temperature Source', temperature_source, 'Environmental Parameters', '', '130311')

    # humidity_source | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    humidity_source_raw = (data_raw >> 14) & 0x3
    humidity_source = humidity_source_raw * 1
    publish_field(hass, instance_name, 'humidity_source', 'Humidity Source', humidity_source, 'Environmental Parameters', '', '130311')

    # temperature | Offset: 16, Length: 16, Resolution: 0.01, Field Type: NUMBER
    temperature_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    temperature = temperature_raw * 0.01
    publish_field(hass, instance_name, 'temperature', 'Temperature', temperature, 'Environmental Parameters', 'K', '130311')
    publish_field(hass, instance_name, 'temperature_celsius', 'Temperature Celsius', kelvin_to_celsius(temperature), 'Environmental Parameters', 'C', '130311')
    publish_field(hass, instance_name, 'temperature_fahrenheit', 'Temperature Fahrenheit', kelvin_to_fahrenheit(temperature), 'Environmental Parameters', 'F', '130311')

    # humidity | Offset: 32, Length: 16, Resolution: 0.004, Field Type: NUMBER
    humidity_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if humidity_raw & (1 << (16 - 1)):
        humidity_raw -= (1 << 16)
    humidity = humidity_raw * 0.004
    publish_field(hass, instance_name, 'humidity', 'Humidity', humidity, 'Environmental Parameters', '%', '130311')

    # atmospheric_pressure | Offset: 48, Length: 16, Resolution: 100, Field Type: NUMBER
    atmospheric_pressure_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    atmospheric_pressure = atmospheric_pressure_raw * 100
    publish_field(hass, instance_name, 'atmospheric_pressure', 'Atmospheric Pressure', atmospheric_pressure, 'Environmental Parameters', 'Pa', '130311')

def process_pgn_130312(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130312."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Temperature', '', '130312')

    # instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Temperature', '', '130312')

    # source | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 16) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Temperature', '', '130312')

    # actual_temperature | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    actual_temperature_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    actual_temperature = actual_temperature_raw * 0.01
    publish_field(hass, instance_name, 'actual_temperature', 'Actual Temperature', actual_temperature, 'Temperature', 'K', '130312')
    publish_field(hass, instance_name, 'actual_temperature_celsius', 'Actual Temperature Celsius', kelvin_to_celsius(actual_temperature), 'Temperature', 'C', '130312')
    publish_field(hass, instance_name, 'actual_temperature_fahrenheit', 'Actual Temperature Fahrenheit', kelvin_to_fahrenheit(actual_temperature), 'Temperature', 'F', '130312')

    # set_temperature | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    set_temperature_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    set_temperature = set_temperature_raw * 0.01
    publish_field(hass, instance_name, 'set_temperature', 'Set Temperature', set_temperature, 'Temperature', 'K', '130312')
    publish_field(hass, instance_name, 'set_temperature_celsius', 'Set Temperature Celsius', kelvin_to_celsius(set_temperature), 'Temperature', 'C', '130312')
    publish_field(hass, instance_name, 'set_temperature_fahrenheit', 'Set Temperature Fahrenheit', kelvin_to_fahrenheit(set_temperature), 'Temperature', 'F', '130312')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Temperature', '', '130312')

def process_pgn_130313(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130313."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Humidity', '', '130313')

    # instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Humidity', '', '130313')

    # source | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 16) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Humidity', '', '130313')

    # actual_humidity | Offset: 24, Length: 16, Resolution: 0.004, Field Type: NUMBER
    actual_humidity_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    if actual_humidity_raw & (1 << (16 - 1)):
        actual_humidity_raw -= (1 << 16)
    actual_humidity = actual_humidity_raw * 0.004
    publish_field(hass, instance_name, 'actual_humidity', 'Actual Humidity', actual_humidity, 'Humidity', '%', '130313')

    # set_humidity | Offset: 40, Length: 16, Resolution: 0.004, Field Type: NUMBER
    set_humidity_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    if set_humidity_raw & (1 << (16 - 1)):
        set_humidity_raw -= (1 << 16)
    set_humidity = set_humidity_raw * 0.004
    publish_field(hass, instance_name, 'set_humidity', 'Set Humidity', set_humidity, 'Humidity', '%', '130313')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Humidity', '', '130313')

def process_pgn_130314(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130314."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Actual Pressure', '', '130314')

    # instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Actual Pressure', '', '130314')

    # source | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 16) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Actual Pressure', '', '130314')

    # pressure | Offset: 24, Length: 32, Resolution: 0.1, Field Type: NUMBER
    pressure_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    if pressure_raw & (1 << (32 - 1)):
        pressure_raw -= (1 << 32)
    pressure = pressure_raw * 0.1
    publish_field(hass, instance_name, 'pressure', 'Pressure', pressure, 'Actual Pressure', 'Pa', '130314')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Actual Pressure', '', '130314')

def process_pgn_130315(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130315."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Set Pressure', '', '130315')

    # instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Set Pressure', '', '130315')

    # source | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 16) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Set Pressure', '', '130315')

    # pressure | Offset: 24, Length: 32, Resolution: 0.1, Field Type: NUMBER
    pressure_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    pressure = pressure_raw * 0.1
    publish_field(hass, instance_name, 'pressure', 'Pressure', pressure, 'Set Pressure', 'Pa', '130315')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Set Pressure', '', '130315')

def process_pgn_130316(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130316."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Temperature Extended Range', '', '130316')

    # instance | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Temperature Extended Range', '', '130316')

    # source | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 16) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Temperature Extended Range', '', '130316')

    # temperature | Offset: 24, Length: 24, Resolution: 0.001, Field Type: NUMBER
    temperature_raw = decode_number((data_raw >> 24) & 0xFFFFFF, 24)
    temperature = temperature_raw * 0.001
    publish_field(hass, instance_name, 'temperature', 'Temperature', temperature, 'Temperature Extended Range', 'K', '130316')
    publish_field(hass, instance_name, 'temperature_celsius', 'Temperature Celsius', kelvin_to_celsius(temperature), 'Temperature Extended Range', 'C', '130316')
    publish_field(hass, instance_name, 'temperature_fahrenheit', 'Temperature Fahrenheit', kelvin_to_fahrenheit(temperature), 'Temperature Extended Range', 'F', '130316')

    # set_temperature | Offset: 48, Length: 16, Resolution: 0.1, Field Type: NUMBER
    set_temperature_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    set_temperature = set_temperature_raw * 0.1
    publish_field(hass, instance_name, 'set_temperature', 'Set Temperature', set_temperature, 'Temperature Extended Range', 'K', '130316')
    publish_field(hass, instance_name, 'set_temperature_celsius', 'Set Temperature Celsius', kelvin_to_celsius(set_temperature), 'Temperature Extended Range', 'C', '130316')
    publish_field(hass, instance_name, 'set_temperature_fahrenheit', 'Set Temperature Fahrenheit', kelvin_to_fahrenheit(set_temperature), 'Temperature Extended Range', 'F', '130316')

def process_pgn_130320(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130320."""
    # mode | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    mode_raw = (data_raw >> 0) & 0xF
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Tide Station Data', '', '130320')

    # tide_tendency | Offset: 4, Length: 2, Resolution: 1, Field Type: LOOKUP
    tide_tendency_raw = (data_raw >> 4) & 0x3
    tide_tendency = tide_tendency_raw * 1
    publish_field(hass, instance_name, 'tide_tendency', 'Tide Tendency', tide_tendency, 'Tide Station Data', '', '130320')

    # reserved | Offset: 6, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 6) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Tide Station Data', '', '130320')

    # measurement_date | Offset: 8, Length: 16, Resolution: 1, Field Type: DATE
    measurement_date_raw = (data_raw >> 8) & 0xFFFF
    measurement_date = decode_date(measurement_date_raw * 1)
    publish_field(hass, instance_name, 'measurement_date', 'Measurement Date', measurement_date, 'Tide Station Data', 'd', '130320')

    # measurement_time | Offset: 24, Length: 32, Resolution: 0.0001, Field Type: TIME
    measurement_time_raw = (data_raw >> 24) & 0xFFFFFFFF
    measurement_time = decode_time(measurement_time_raw * 0.0001)
    publish_field(hass, instance_name, 'measurement_time', 'Measurement Time', measurement_time, 'Tide Station Data', 's', '130320')

    # station_latitude | Offset: 56, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_latitude_raw = decode_number((data_raw >> 56) & 0xFFFFFFFF, 32)
    if station_latitude_raw & (1 << (32 - 1)):
        station_latitude_raw -= (1 << 32)
    station_latitude = station_latitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_latitude', 'Station Latitude', station_latitude, 'Tide Station Data', 'deg', '130320')

    # station_longitude | Offset: 88, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_longitude_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    if station_longitude_raw & (1 << (32 - 1)):
        station_longitude_raw -= (1 << 32)
    station_longitude = station_longitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_longitude', 'Station Longitude', station_longitude, 'Tide Station Data', 'deg', '130320')

    # tide_level | Offset: 120, Length: 16, Resolution: 0.001, Field Type: NUMBER
    tide_level_raw = decode_number((data_raw >> 120) & 0xFFFF, 16)
    if tide_level_raw & (1 << (16 - 1)):
        tide_level_raw -= (1 << 16)
    tide_level = tide_level_raw * 0.001
    publish_field(hass, instance_name, 'tide_level', 'Tide Level', tide_level, 'Tide Station Data', 'm', '130320')

    # tide_level_standard_deviation | Offset: 136, Length: 16, Resolution: 0.01, Field Type: NUMBER
    tide_level_standard_deviation_raw = decode_number((data_raw >> 136) & 0xFFFF, 16)
    tide_level_standard_deviation = tide_level_standard_deviation_raw * 0.01
    publish_field(hass, instance_name, 'tide_level_standard_deviation', 'Tide Level standard deviation', tide_level_standard_deviation, 'Tide Station Data', 'm', '130320')

def process_pgn_130321(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130321."""
    # mode | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    mode_raw = (data_raw >> 0) & 0xF
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Salinity Station Data', '', '130321')

    # reserved | Offset: 4, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 4) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Salinity Station Data', '', '130321')

    # measurement_date | Offset: 8, Length: 16, Resolution: 1, Field Type: DATE
    measurement_date_raw = (data_raw >> 8) & 0xFFFF
    measurement_date = decode_date(measurement_date_raw * 1)
    publish_field(hass, instance_name, 'measurement_date', 'Measurement Date', measurement_date, 'Salinity Station Data', 'd', '130321')

    # measurement_time | Offset: 24, Length: 32, Resolution: 0.0001, Field Type: TIME
    measurement_time_raw = (data_raw >> 24) & 0xFFFFFFFF
    measurement_time = decode_time(measurement_time_raw * 0.0001)
    publish_field(hass, instance_name, 'measurement_time', 'Measurement Time', measurement_time, 'Salinity Station Data', 's', '130321')

    # station_latitude | Offset: 56, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_latitude_raw = decode_number((data_raw >> 56) & 0xFFFFFFFF, 32)
    if station_latitude_raw & (1 << (32 - 1)):
        station_latitude_raw -= (1 << 32)
    station_latitude = station_latitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_latitude', 'Station Latitude', station_latitude, 'Salinity Station Data', 'deg', '130321')

    # station_longitude | Offset: 88, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_longitude_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    if station_longitude_raw & (1 << (32 - 1)):
        station_longitude_raw -= (1 << 32)
    station_longitude = station_longitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_longitude', 'Station Longitude', station_longitude, 'Salinity Station Data', 'deg', '130321')

    # salinity | Offset: 120, Length: 32, Resolution: 1, Field Type: FLOAT
    salinity_raw = decode_float((data_raw >> 120) & 0xFFFFFFFF, 32)
    if salinity_raw & (1 << (32 - 1)):
        salinity_raw -= (1 << 32)
    salinity = salinity_raw * 1
    publish_field(hass, instance_name, 'salinity', 'Salinity', salinity, 'Salinity Station Data', 'ppt', '130321')

    # water_temperature | Offset: 152, Length: 16, Resolution: 0.01, Field Type: NUMBER
    water_temperature_raw = decode_number((data_raw >> 152) & 0xFFFF, 16)
    water_temperature = water_temperature_raw * 0.01
    publish_field(hass, instance_name, 'water_temperature', 'Water Temperature', water_temperature, 'Salinity Station Data', 'K', '130321')
    publish_field(hass, instance_name, 'water_temperature_celsius', 'Water Temperature Celsius', kelvin_to_celsius(water_temperature), 'Salinity Station Data', 'C', '130321')
    publish_field(hass, instance_name, 'water_temperature_fahrenheit', 'Water Temperature Fahrenheit', kelvin_to_fahrenheit(water_temperature), 'Salinity Station Data', 'F', '130321')

def process_pgn_130322(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130322."""
    # mode | Offset: 0, Length: 4, Resolution: 1, Field Type: NUMBER
    mode_raw = decode_number((data_raw >> 0) & 0xF, 4)
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Current Station Data', '', '130322')

    # reserved | Offset: 4, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 4) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Current Station Data', '', '130322')

    # measurement_date | Offset: 8, Length: 16, Resolution: 1, Field Type: DATE
    measurement_date_raw = (data_raw >> 8) & 0xFFFF
    measurement_date = decode_date(measurement_date_raw * 1)
    publish_field(hass, instance_name, 'measurement_date', 'Measurement Date', measurement_date, 'Current Station Data', 'd', '130322')

    # measurement_time | Offset: 24, Length: 32, Resolution: 0.0001, Field Type: TIME
    measurement_time_raw = (data_raw >> 24) & 0xFFFFFFFF
    measurement_time = decode_time(measurement_time_raw * 0.0001)
    publish_field(hass, instance_name, 'measurement_time', 'Measurement Time', measurement_time, 'Current Station Data', 's', '130322')

    # station_latitude | Offset: 56, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_latitude_raw = decode_number((data_raw >> 56) & 0xFFFFFFFF, 32)
    if station_latitude_raw & (1 << (32 - 1)):
        station_latitude_raw -= (1 << 32)
    station_latitude = station_latitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_latitude', 'Station Latitude', station_latitude, 'Current Station Data', 'deg', '130322')

    # station_longitude | Offset: 88, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_longitude_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    if station_longitude_raw & (1 << (32 - 1)):
        station_longitude_raw -= (1 << 32)
    station_longitude = station_longitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_longitude', 'Station Longitude', station_longitude, 'Current Station Data', 'deg', '130322')

    # measurement_depth | Offset: 120, Length: 32, Resolution: 0.01, Field Type: NUMBER
    measurement_depth_raw = decode_number((data_raw >> 120) & 0xFFFFFFFF, 32)
    measurement_depth = measurement_depth_raw * 0.01
    publish_field(hass, instance_name, 'measurement_depth', 'Measurement Depth', measurement_depth, 'Current Station Data', 'm', '130322')

    # current_speed | Offset: 152, Length: 16, Resolution: 0.01, Field Type: NUMBER
    current_speed_raw = decode_number((data_raw >> 152) & 0xFFFF, 16)
    current_speed = current_speed_raw * 0.01
    publish_field(hass, instance_name, 'current_speed', 'Current speed', current_speed, 'Current Station Data', 'm/s', '130322')
    publish_field(hass, instance_name, 'current_speed_knots', 'Current speed Knots', mps_to_knots(current_speed), 'Current Station Data', 'Kn', '130322')

    # current_flow_direction | Offset: 168, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    current_flow_direction_raw = decode_number((data_raw >> 168) & 0xFFFF, 16)
    current_flow_direction = current_flow_direction_raw * 0.0001
    publish_field(hass, instance_name, 'current_flow_direction', 'Current flow direction', current_flow_direction, 'Current Station Data', 'rad', '130322')
    publish_field(hass, instance_name, 'current_flow_direction_degrees', 'Current flow direction Degrees', radians_to_degrees(current_flow_direction), 'Current Station Data', 'Deg', '130322')

    # water_temperature | Offset: 184, Length: 16, Resolution: 0.01, Field Type: NUMBER
    water_temperature_raw = decode_number((data_raw >> 184) & 0xFFFF, 16)
    water_temperature = water_temperature_raw * 0.01
    publish_field(hass, instance_name, 'water_temperature', 'Water Temperature', water_temperature, 'Current Station Data', 'K', '130322')
    publish_field(hass, instance_name, 'water_temperature_celsius', 'Water Temperature Celsius', kelvin_to_celsius(water_temperature), 'Current Station Data', 'C', '130322')
    publish_field(hass, instance_name, 'water_temperature_fahrenheit', 'Water Temperature Fahrenheit', kelvin_to_fahrenheit(water_temperature), 'Current Station Data', 'F', '130322')

def process_pgn_130323(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130323."""
    # mode | Offset: 0, Length: 4, Resolution: 1, Field Type: NUMBER
    mode_raw = decode_number((data_raw >> 0) & 0xF, 4)
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Meteorological Station Data', '', '130323')

    # reserved | Offset: 4, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 4) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Meteorological Station Data', '', '130323')

    # measurement_date | Offset: 8, Length: 16, Resolution: 1, Field Type: DATE
    measurement_date_raw = (data_raw >> 8) & 0xFFFF
    measurement_date = decode_date(measurement_date_raw * 1)
    publish_field(hass, instance_name, 'measurement_date', 'Measurement Date', measurement_date, 'Meteorological Station Data', 'd', '130323')

    # measurement_time | Offset: 24, Length: 32, Resolution: 0.0001, Field Type: TIME
    measurement_time_raw = (data_raw >> 24) & 0xFFFFFFFF
    measurement_time = decode_time(measurement_time_raw * 0.0001)
    publish_field(hass, instance_name, 'measurement_time', 'Measurement Time', measurement_time, 'Meteorological Station Data', 's', '130323')

    # station_latitude | Offset: 56, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_latitude_raw = decode_number((data_raw >> 56) & 0xFFFFFFFF, 32)
    if station_latitude_raw & (1 << (32 - 1)):
        station_latitude_raw -= (1 << 32)
    station_latitude = station_latitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_latitude', 'Station Latitude', station_latitude, 'Meteorological Station Data', 'deg', '130323')

    # station_longitude | Offset: 88, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_longitude_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    if station_longitude_raw & (1 << (32 - 1)):
        station_longitude_raw -= (1 << 32)
    station_longitude = station_longitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_longitude', 'Station Longitude', station_longitude, 'Meteorological Station Data', 'deg', '130323')

    # wind_speed | Offset: 120, Length: 16, Resolution: 0.01, Field Type: NUMBER
    wind_speed_raw = decode_number((data_raw >> 120) & 0xFFFF, 16)
    wind_speed = wind_speed_raw * 0.01
    publish_field(hass, instance_name, 'wind_speed', 'Wind Speed', wind_speed, 'Meteorological Station Data', 'm/s', '130323')
    publish_field(hass, instance_name, 'wind_speed_knots', 'Wind Speed Knots', mps_to_knots(wind_speed), 'Meteorological Station Data', 'Kn', '130323')

    # wind_direction | Offset: 136, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    wind_direction_raw = decode_number((data_raw >> 136) & 0xFFFF, 16)
    wind_direction = wind_direction_raw * 0.0001
    publish_field(hass, instance_name, 'wind_direction', 'Wind Direction', wind_direction, 'Meteorological Station Data', 'rad', '130323')
    publish_field(hass, instance_name, 'wind_direction_degrees', 'Wind Direction Degrees', radians_to_degrees(wind_direction), 'Meteorological Station Data', 'Deg', '130323')

    # wind_reference | Offset: 152, Length: 3, Resolution: 1, Field Type: LOOKUP
    wind_reference_raw = (data_raw >> 152) & 0x7
    wind_reference = wind_reference_raw * 1
    publish_field(hass, instance_name, 'wind_reference', 'Wind Reference', wind_reference, 'Meteorological Station Data', '', '130323')

    # reserved | Offset: 155, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 155) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Meteorological Station Data', '', '130323')

    # wind_gusts | Offset: 160, Length: 16, Resolution: 0.01, Field Type: NUMBER
    wind_gusts_raw = decode_number((data_raw >> 160) & 0xFFFF, 16)
    wind_gusts = wind_gusts_raw * 0.01
    publish_field(hass, instance_name, 'wind_gusts', 'Wind Gusts', wind_gusts, 'Meteorological Station Data', 'm/s', '130323')
    publish_field(hass, instance_name, 'wind_gusts_knots', 'Wind Gusts Knots', mps_to_knots(wind_gusts), 'Meteorological Station Data', 'Kn', '130323')

    # atmospheric_pressure | Offset: 176, Length: 16, Resolution: 100, Field Type: NUMBER
    atmospheric_pressure_raw = decode_number((data_raw >> 176) & 0xFFFF, 16)
    atmospheric_pressure = atmospheric_pressure_raw * 100
    publish_field(hass, instance_name, 'atmospheric_pressure', 'Atmospheric Pressure', atmospheric_pressure, 'Meteorological Station Data', 'Pa', '130323')

    # ambient_temperature | Offset: 192, Length: 16, Resolution: 0.01, Field Type: NUMBER
    ambient_temperature_raw = decode_number((data_raw >> 192) & 0xFFFF, 16)
    ambient_temperature = ambient_temperature_raw * 0.01
    publish_field(hass, instance_name, 'ambient_temperature', 'Ambient Temperature', ambient_temperature, 'Meteorological Station Data', 'K', '130323')
    publish_field(hass, instance_name, 'ambient_temperature_celsius', 'Ambient Temperature Celsius', kelvin_to_celsius(ambient_temperature), 'Meteorological Station Data', 'C', '130323')
    publish_field(hass, instance_name, 'ambient_temperature_fahrenheit', 'Ambient Temperature Fahrenheit', kelvin_to_fahrenheit(ambient_temperature), 'Meteorological Station Data', 'F', '130323')

def process_pgn_130324(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130324."""
    # mode | Offset: 0, Length: 4, Resolution: 1, Field Type: NUMBER
    mode_raw = decode_number((data_raw >> 0) & 0xF, 4)
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Moored Buoy Station Data', '', '130324')

    # reserved | Offset: 4, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 4) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Moored Buoy Station Data', '', '130324')

    # measurement_date | Offset: 8, Length: 16, Resolution: 1, Field Type: DATE
    measurement_date_raw = (data_raw >> 8) & 0xFFFF
    measurement_date = decode_date(measurement_date_raw * 1)
    publish_field(hass, instance_name, 'measurement_date', 'Measurement Date', measurement_date, 'Moored Buoy Station Data', 'd', '130324')

    # measurement_time | Offset: 24, Length: 32, Resolution: 0.0001, Field Type: TIME
    measurement_time_raw = (data_raw >> 24) & 0xFFFFFFFF
    measurement_time = decode_time(measurement_time_raw * 0.0001)
    publish_field(hass, instance_name, 'measurement_time', 'Measurement Time', measurement_time, 'Moored Buoy Station Data', 's', '130324')

    # station_latitude | Offset: 56, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_latitude_raw = decode_number((data_raw >> 56) & 0xFFFFFFFF, 32)
    if station_latitude_raw & (1 << (32 - 1)):
        station_latitude_raw -= (1 << 32)
    station_latitude = station_latitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_latitude', 'Station Latitude', station_latitude, 'Moored Buoy Station Data', 'deg', '130324')

    # station_longitude | Offset: 88, Length: 32, Resolution: 1e-07, Field Type: NUMBER
    station_longitude_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    if station_longitude_raw & (1 << (32 - 1)):
        station_longitude_raw -= (1 << 32)
    station_longitude = station_longitude_raw * 1e-07
    publish_field(hass, instance_name, 'station_longitude', 'Station Longitude', station_longitude, 'Moored Buoy Station Data', 'deg', '130324')

    # wind_speed | Offset: 120, Length: 16, Resolution: 0.01, Field Type: NUMBER
    wind_speed_raw = decode_number((data_raw >> 120) & 0xFFFF, 16)
    wind_speed = wind_speed_raw * 0.01
    publish_field(hass, instance_name, 'wind_speed', 'Wind Speed', wind_speed, 'Moored Buoy Station Data', 'm/s', '130324')
    publish_field(hass, instance_name, 'wind_speed_knots', 'Wind Speed Knots', mps_to_knots(wind_speed), 'Moored Buoy Station Data', 'Kn', '130324')

    # wind_direction | Offset: 136, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    wind_direction_raw = decode_number((data_raw >> 136) & 0xFFFF, 16)
    wind_direction = wind_direction_raw * 0.0001
    publish_field(hass, instance_name, 'wind_direction', 'Wind Direction', wind_direction, 'Moored Buoy Station Data', 'rad', '130324')
    publish_field(hass, instance_name, 'wind_direction_degrees', 'Wind Direction Degrees', radians_to_degrees(wind_direction), 'Moored Buoy Station Data', 'Deg', '130324')

    # wind_reference | Offset: 152, Length: 3, Resolution: 1, Field Type: LOOKUP
    wind_reference_raw = (data_raw >> 152) & 0x7
    wind_reference = wind_reference_raw * 1
    publish_field(hass, instance_name, 'wind_reference', 'Wind Reference', wind_reference, 'Moored Buoy Station Data', '', '130324')

    # reserved | Offset: 155, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 155) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Moored Buoy Station Data', '', '130324')

    # wind_gusts | Offset: 160, Length: 16, Resolution: 0.01, Field Type: NUMBER
    wind_gusts_raw = decode_number((data_raw >> 160) & 0xFFFF, 16)
    wind_gusts = wind_gusts_raw * 0.01
    publish_field(hass, instance_name, 'wind_gusts', 'Wind Gusts', wind_gusts, 'Moored Buoy Station Data', 'm/s', '130324')
    publish_field(hass, instance_name, 'wind_gusts_knots', 'Wind Gusts Knots', mps_to_knots(wind_gusts), 'Moored Buoy Station Data', 'Kn', '130324')

    # wave_height | Offset: 176, Length: 16, Resolution: 1, Field Type: NUMBER
    wave_height_raw = decode_number((data_raw >> 176) & 0xFFFF, 16)
    wave_height = wave_height_raw * 1
    publish_field(hass, instance_name, 'wave_height', 'Wave Height', wave_height, 'Moored Buoy Station Data', '', '130324')

    # dominant_wave_period | Offset: 192, Length: 16, Resolution: 1, Field Type: NUMBER
    dominant_wave_period_raw = decode_number((data_raw >> 192) & 0xFFFF, 16)
    dominant_wave_period = dominant_wave_period_raw * 1
    publish_field(hass, instance_name, 'dominant_wave_period', 'Dominant Wave Period', dominant_wave_period, 'Moored Buoy Station Data', '', '130324')

    # atmospheric_pressure | Offset: 208, Length: 16, Resolution: 100, Field Type: NUMBER
    atmospheric_pressure_raw = decode_number((data_raw >> 208) & 0xFFFF, 16)
    atmospheric_pressure = atmospheric_pressure_raw * 100
    publish_field(hass, instance_name, 'atmospheric_pressure', 'Atmospheric Pressure', atmospheric_pressure, 'Moored Buoy Station Data', 'Pa', '130324')

    # pressure_tendency_rate | Offset: 224, Length: 16, Resolution: 1, Field Type: NUMBER
    pressure_tendency_rate_raw = decode_number((data_raw >> 224) & 0xFFFF, 16)
    if pressure_tendency_rate_raw & (1 << (16 - 1)):
        pressure_tendency_rate_raw -= (1 << 16)
    pressure_tendency_rate = pressure_tendency_rate_raw * 1
    publish_field(hass, instance_name, 'pressure_tendency_rate', 'Pressure Tendency Rate', pressure_tendency_rate, 'Moored Buoy Station Data', 'Pa/hr', '130324')

    # air_temperature | Offset: 240, Length: 16, Resolution: 0.01, Field Type: NUMBER
    air_temperature_raw = decode_number((data_raw >> 240) & 0xFFFF, 16)
    air_temperature = air_temperature_raw * 0.01
    publish_field(hass, instance_name, 'air_temperature', 'Air Temperature', air_temperature, 'Moored Buoy Station Data', 'K', '130324')
    publish_field(hass, instance_name, 'air_temperature_celsius', 'Air Temperature Celsius', kelvin_to_celsius(air_temperature), 'Moored Buoy Station Data', 'C', '130324')
    publish_field(hass, instance_name, 'air_temperature_fahrenheit', 'Air Temperature Fahrenheit', kelvin_to_fahrenheit(air_temperature), 'Moored Buoy Station Data', 'F', '130324')

    # water_temperature | Offset: 256, Length: 16, Resolution: 0.01, Field Type: NUMBER
    water_temperature_raw = decode_number((data_raw >> 256) & 0xFFFF, 16)
    water_temperature = water_temperature_raw * 0.01
    publish_field(hass, instance_name, 'water_temperature', 'Water Temperature', water_temperature, 'Moored Buoy Station Data', 'K', '130324')
    publish_field(hass, instance_name, 'water_temperature_celsius', 'Water Temperature Celsius', kelvin_to_celsius(water_temperature), 'Moored Buoy Station Data', 'C', '130324')
    publish_field(hass, instance_name, 'water_temperature_fahrenheit', 'Water Temperature Fahrenheit', kelvin_to_fahrenheit(water_temperature), 'Moored Buoy Station Data', 'F', '130324')

    # station_id | Offset: 272, Length: 64, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_130330(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130330."""
    # global_enable | Offset: 0, Length: 2, Resolution: 1, Field Type: NUMBER
    global_enable_raw = decode_number((data_raw >> 0) & 0x3, 2)
    global_enable = global_enable_raw * 1
    publish_field(hass, instance_name, 'global_enable', 'Global Enable', global_enable, 'Lighting System Settings', '', '130330')

    # default_settings_command | Offset: 2, Length: 3, Resolution: 1, Field Type: LOOKUP
    default_settings_command_raw = (data_raw >> 2) & 0x7
    default_settings_command = default_settings_command_raw * 1
    publish_field(hass, instance_name, 'default_settings_command', 'Default Settings/Command', default_settings_command, 'Lighting System Settings', '', '130330')

    # reserved | Offset: 5, Length: 3, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 5) & 0x7
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Lighting System Settings', '', '130330')

def process_pgn_130560(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130560."""
    # sid | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Payload Mass', '', '130560')

    # measurement_status | Offset: 8, Length: 3, Resolution: 1, Field Type: NUMBER
    measurement_status_raw = decode_number((data_raw >> 8) & 0x7, 3)
    measurement_status = measurement_status_raw * 1
    publish_field(hass, instance_name, 'measurement_status', 'Measurement Status', measurement_status, 'Payload Mass', '', '130560')

    # reserved | Offset: 11, Length: 5, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x1F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Payload Mass', '', '130560')

    # measurement_id | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    measurement_id_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    measurement_id = measurement_id_raw * 1
    publish_field(hass, instance_name, 'measurement_id', 'Measurement ID', measurement_id, 'Payload Mass', '', '130560')

    # payload_mass | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    payload_mass_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    payload_mass = payload_mass_raw * 1
    publish_field(hass, instance_name, 'payload_mass', 'Payload Mass', payload_mass, 'Payload Mass', '', '130560')

    # reserved | Offset: 56, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 56) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Payload Mass', '', '130560')

def process_pgn_130561(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130561."""
    # zone_index | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_index_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    zone_index = zone_index_raw * 1
    publish_field(hass, instance_name, 'zone_index', 'Zone Index', zone_index, 'Lighting Zone', '', '130561')

def process_pgn_130562(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130562."""
    # scene_index | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    scene_index_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    scene_index = scene_index_raw * 1
    publish_field(hass, instance_name, 'scene_index', 'Scene Index', scene_index, 'Lighting Scene', '', '130562')

def process_pgn_130563(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130563."""
    # device_id | Offset: 0, Length: 32, Resolution: 1, Field Type: NUMBER
    device_id_raw = decode_number((data_raw >> 0) & 0xFFFFFFFF, 32)
    device_id = device_id_raw * 1
    publish_field(hass, instance_name, 'device_id', 'Device ID', device_id, 'Lighting Device', '', '130563')

    # device_capabilities | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    device_capabilities_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    device_capabilities = device_capabilities_raw * 1
    publish_field(hass, instance_name, 'device_capabilities', 'Device Capabilities', device_capabilities, 'Lighting Device', '', '130563')

    # color_capabilities | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    color_capabilities_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    color_capabilities = color_capabilities_raw * 1
    publish_field(hass, instance_name, 'color_capabilities', 'Color Capabilities', color_capabilities, 'Lighting Device', '', '130563')

    # zone_index | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_index_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    zone_index = zone_index_raw * 1
    publish_field(hass, instance_name, 'zone_index', 'Zone Index', zone_index, 'Lighting Device', '', '130563')

def process_pgn_130564(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130564."""
    # index_of_first_device | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    index_of_first_device_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    index_of_first_device = index_of_first_device_raw * 1
    publish_field(hass, instance_name, 'index_of_first_device', 'Index of First Device', index_of_first_device, 'Lighting Device Enumeration', '', '130564')

    # total_number_of_devices | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    total_number_of_devices_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    total_number_of_devices = total_number_of_devices_raw * 1
    publish_field(hass, instance_name, 'total_number_of_devices', 'Total Number of Devices', total_number_of_devices, 'Lighting Device Enumeration', '', '130564')

    # number_of_devices | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    number_of_devices_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    number_of_devices = number_of_devices_raw * 1
    publish_field(hass, instance_name, 'number_of_devices', 'Number of Devices', number_of_devices, 'Lighting Device Enumeration', '', '130564')

    # device_id | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    device_id_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    device_id = device_id_raw * 1
    publish_field(hass, instance_name, 'device_id', 'Device ID', device_id, 'Lighting Device Enumeration', '', '130564')

    # status | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    status_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Lighting Device Enumeration', '', '130564')

def process_pgn_130565(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130565."""
    # sequence_index | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    sequence_index_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    sequence_index = sequence_index_raw * 1
    publish_field(hass, instance_name, 'sequence_index', 'Sequence Index', sequence_index, 'Lighting Color Sequence', '', '130565')

    # color_count | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    color_count_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    color_count = color_count_raw * 1
    publish_field(hass, instance_name, 'color_count', 'Color Count', color_count, 'Lighting Color Sequence', '', '130565')

    # color_index | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    color_index_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    color_index = color_index_raw * 1
    publish_field(hass, instance_name, 'color_index', 'Color Index', color_index, 'Lighting Color Sequence', '', '130565')

    # red_component | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    red_component_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    red_component = red_component_raw * 1
    publish_field(hass, instance_name, 'red_component', 'Red Component', red_component, 'Lighting Color Sequence', '', '130565')

    # green_component | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    green_component_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    green_component = green_component_raw * 1
    publish_field(hass, instance_name, 'green_component', 'Green Component', green_component, 'Lighting Color Sequence', '', '130565')

    # blue_component | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    blue_component_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    blue_component = blue_component_raw * 1
    publish_field(hass, instance_name, 'blue_component', 'Blue Component', blue_component, 'Lighting Color Sequence', '', '130565')

    # color_temperature | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    color_temperature_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    color_temperature = color_temperature_raw * 1
    publish_field(hass, instance_name, 'color_temperature', 'Color Temperature', color_temperature, 'Lighting Color Sequence', '', '130565')

    # intensity | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    intensity_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    intensity = intensity_raw * 1
    publish_field(hass, instance_name, 'intensity', 'Intensity', intensity, 'Lighting Color Sequence', '', '130565')

def process_pgn_130566(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130566."""
    # program_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    program_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    program_id = program_id_raw * 1
    publish_field(hass, instance_name, 'program_id', 'Program ID', program_id, 'Lighting Program', '', '130566')

def process_pgn_130567(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130567."""
    # watermaker_operating_state | Offset: 0, Length: 6, Resolution: 1, Field Type: LOOKUP
    watermaker_operating_state_raw = (data_raw >> 0) & 0x3F
    watermaker_operating_state = watermaker_operating_state_raw * 1
    publish_field(hass, instance_name, 'watermaker_operating_state', 'Watermaker Operating State', watermaker_operating_state, 'Watermaker Input Setting and Status', '', '130567')

    # production_start_stop | Offset: 6, Length: 2, Resolution: 1, Field Type: LOOKUP
    production_start_stop_raw = (data_raw >> 6) & 0x3
    production_start_stop = production_start_stop_raw * 1
    publish_field(hass, instance_name, 'production_start_stop', 'Production Start/Stop', production_start_stop, 'Watermaker Input Setting and Status', '', '130567')

    # rinse_start_stop | Offset: 8, Length: 2, Resolution: 1, Field Type: LOOKUP
    rinse_start_stop_raw = (data_raw >> 8) & 0x3
    rinse_start_stop = rinse_start_stop_raw * 1
    publish_field(hass, instance_name, 'rinse_start_stop', 'Rinse Start/Stop', rinse_start_stop, 'Watermaker Input Setting and Status', '', '130567')

    # low_pressure_pump_status | Offset: 10, Length: 2, Resolution: 1, Field Type: LOOKUP
    low_pressure_pump_status_raw = (data_raw >> 10) & 0x3
    low_pressure_pump_status = low_pressure_pump_status_raw * 1
    publish_field(hass, instance_name, 'low_pressure_pump_status', 'Low Pressure Pump Status', low_pressure_pump_status, 'Watermaker Input Setting and Status', '', '130567')

    # high_pressure_pump_status | Offset: 12, Length: 2, Resolution: 1, Field Type: LOOKUP
    high_pressure_pump_status_raw = (data_raw >> 12) & 0x3
    high_pressure_pump_status = high_pressure_pump_status_raw * 1
    publish_field(hass, instance_name, 'high_pressure_pump_status', 'High Pressure Pump Status', high_pressure_pump_status, 'Watermaker Input Setting and Status', '', '130567')

    # emergency_stop | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    emergency_stop_raw = (data_raw >> 14) & 0x3
    emergency_stop = emergency_stop_raw * 1
    publish_field(hass, instance_name, 'emergency_stop', 'Emergency Stop', emergency_stop, 'Watermaker Input Setting and Status', '', '130567')

    # product_solenoid_valve_status | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    product_solenoid_valve_status_raw = (data_raw >> 16) & 0x3
    product_solenoid_valve_status = product_solenoid_valve_status_raw * 1
    publish_field(hass, instance_name, 'product_solenoid_valve_status', 'Product Solenoid Valve Status', product_solenoid_valve_status, 'Watermaker Input Setting and Status', '', '130567')

    # flush_mode_status | Offset: 18, Length: 2, Resolution: 1, Field Type: LOOKUP
    flush_mode_status_raw = (data_raw >> 18) & 0x3
    flush_mode_status = flush_mode_status_raw * 1
    publish_field(hass, instance_name, 'flush_mode_status', 'Flush Mode Status', flush_mode_status, 'Watermaker Input Setting and Status', '', '130567')

    # salinity_status | Offset: 20, Length: 2, Resolution: 1, Field Type: LOOKUP
    salinity_status_raw = (data_raw >> 20) & 0x3
    salinity_status = salinity_status_raw * 1
    publish_field(hass, instance_name, 'salinity_status', 'Salinity Status', salinity_status, 'Watermaker Input Setting and Status', '', '130567')

    # sensor_status | Offset: 22, Length: 2, Resolution: 1, Field Type: LOOKUP
    sensor_status_raw = (data_raw >> 22) & 0x3
    sensor_status = sensor_status_raw * 1
    publish_field(hass, instance_name, 'sensor_status', 'Sensor Status', sensor_status, 'Watermaker Input Setting and Status', '', '130567')

    # oil_change_indicator_status | Offset: 24, Length: 2, Resolution: 1, Field Type: LOOKUP
    oil_change_indicator_status_raw = (data_raw >> 24) & 0x3
    oil_change_indicator_status = oil_change_indicator_status_raw * 1
    publish_field(hass, instance_name, 'oil_change_indicator_status', 'Oil Change Indicator Status', oil_change_indicator_status, 'Watermaker Input Setting and Status', '', '130567')

    # filter_status | Offset: 26, Length: 2, Resolution: 1, Field Type: LOOKUP
    filter_status_raw = (data_raw >> 26) & 0x3
    filter_status = filter_status_raw * 1
    publish_field(hass, instance_name, 'filter_status', 'Filter Status', filter_status, 'Watermaker Input Setting and Status', '', '130567')

    # system_status | Offset: 28, Length: 2, Resolution: 1, Field Type: LOOKUP
    system_status_raw = (data_raw >> 28) & 0x3
    system_status = system_status_raw * 1
    publish_field(hass, instance_name, 'system_status', 'System Status', system_status, 'Watermaker Input Setting and Status', '', '130567')

    # reserved | Offset: 30, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 30) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Watermaker Input Setting and Status', '', '130567')

    # salinity | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    salinity_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    salinity = salinity_raw * 1
    publish_field(hass, instance_name, 'salinity', 'Salinity', salinity, 'Watermaker Input Setting and Status', 'ppm', '130567')

    # product_water_temperature | Offset: 48, Length: 16, Resolution: 0.01, Field Type: NUMBER
    product_water_temperature_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    product_water_temperature = product_water_temperature_raw * 0.01
    publish_field(hass, instance_name, 'product_water_temperature', 'Product Water Temperature', product_water_temperature, 'Watermaker Input Setting and Status', 'K', '130567')
    publish_field(hass, instance_name, 'product_water_temperature_celsius', 'Product Water Temperature Celsius', kelvin_to_celsius(product_water_temperature), 'Watermaker Input Setting and Status', 'C', '130567')
    publish_field(hass, instance_name, 'product_water_temperature_fahrenheit', 'Product Water Temperature Fahrenheit', kelvin_to_fahrenheit(product_water_temperature), 'Watermaker Input Setting and Status', 'F', '130567')

    # pre_filter_pressure | Offset: 64, Length: 16, Resolution: 100, Field Type: NUMBER
    pre_filter_pressure_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    pre_filter_pressure = pre_filter_pressure_raw * 100
    publish_field(hass, instance_name, 'pre_filter_pressure', 'Pre-filter Pressure', pre_filter_pressure, 'Watermaker Input Setting and Status', 'Pa', '130567')

    # post_filter_pressure | Offset: 80, Length: 16, Resolution: 100, Field Type: NUMBER
    post_filter_pressure_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    post_filter_pressure = post_filter_pressure_raw * 100
    publish_field(hass, instance_name, 'post_filter_pressure', 'Post-filter Pressure', post_filter_pressure, 'Watermaker Input Setting and Status', 'Pa', '130567')

    # feed_pressure | Offset: 96, Length: 16, Resolution: 1000, Field Type: NUMBER
    feed_pressure_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    if feed_pressure_raw & (1 << (16 - 1)):
        feed_pressure_raw -= (1 << 16)
    feed_pressure = feed_pressure_raw * 1000
    publish_field(hass, instance_name, 'feed_pressure', 'Feed Pressure', feed_pressure, 'Watermaker Input Setting and Status', 'Pa', '130567')

    # system_high_pressure | Offset: 112, Length: 16, Resolution: 1000, Field Type: NUMBER
    system_high_pressure_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    system_high_pressure = system_high_pressure_raw * 1000
    publish_field(hass, instance_name, 'system_high_pressure', 'System High Pressure', system_high_pressure, 'Watermaker Input Setting and Status', 'Pa', '130567')

    # product_water_flow | Offset: 128, Length: 16, Resolution: 0.1, Field Type: NUMBER
    product_water_flow_raw = decode_number((data_raw >> 128) & 0xFFFF, 16)
    if product_water_flow_raw & (1 << (16 - 1)):
        product_water_flow_raw -= (1 << 16)
    product_water_flow = product_water_flow_raw * 0.1
    publish_field(hass, instance_name, 'product_water_flow', 'Product Water Flow', product_water_flow, 'Watermaker Input Setting and Status', 'L/h', '130567')

    # brine_water_flow | Offset: 144, Length: 16, Resolution: 0.1, Field Type: NUMBER
    brine_water_flow_raw = decode_number((data_raw >> 144) & 0xFFFF, 16)
    if brine_water_flow_raw & (1 << (16 - 1)):
        brine_water_flow_raw -= (1 << 16)
    brine_water_flow = brine_water_flow_raw * 0.1
    publish_field(hass, instance_name, 'brine_water_flow', 'Brine Water Flow', brine_water_flow, 'Watermaker Input Setting and Status', 'L/h', '130567')

    # run_time | Offset: 160, Length: 32, Resolution: 1, Field Type: TIME
    run_time_raw = (data_raw >> 160) & 0xFFFFFFFF
    run_time = decode_time(run_time_raw * 1)
    publish_field(hass, instance_name, 'run_time', 'Run Time', run_time, 'Watermaker Input Setting and Status', 's', '130567')

def process_pgn_130569(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130569."""
    # zone | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    zone_raw = (data_raw >> 0) & 0xFF
    zone = zone_raw * 1
    publish_field(hass, instance_name, 'zone', 'Zone', zone, 'Current Status and File', '', '130569')

    # source | Offset: 8, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 8) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Current Status and File', '', '130569')

    # number | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    number_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    number = number_raw * 1
    publish_field(hass, instance_name, 'number', 'Number', number, 'Current Status and File', '', '130569')

    # id | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    id_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    id = id_raw * 1
    publish_field(hass, instance_name, 'id', 'ID', id, 'Current Status and File', '', '130569')

    # play_status | Offset: 56, Length: 8, Resolution: 1, Field Type: LOOKUP
    play_status_raw = (data_raw >> 56) & 0xFF
    play_status = play_status_raw * 1
    publish_field(hass, instance_name, 'play_status', 'Play status', play_status, 'Current Status and File', '', '130569')

    # elapsed_track_time | Offset: 64, Length: 16, Resolution: 1, Field Type: TIME
    elapsed_track_time_raw = (data_raw >> 64) & 0xFFFF
    elapsed_track_time = decode_time(elapsed_track_time_raw * 1)
    publish_field(hass, instance_name, 'elapsed_track_time', 'Elapsed Track Time', elapsed_track_time, 'Current Status and File', 's', '130569')

    # track_time | Offset: 80, Length: 16, Resolution: 1, Field Type: TIME
    track_time_raw = (data_raw >> 80) & 0xFFFF
    track_time = decode_time(track_time_raw * 1)
    publish_field(hass, instance_name, 'track_time', 'Track Time', track_time, 'Current Status and File', 's', '130569')

    # repeat_status | Offset: 96, Length: 4, Resolution: 1, Field Type: LOOKUP
    repeat_status_raw = (data_raw >> 96) & 0xF
    repeat_status = repeat_status_raw * 1
    publish_field(hass, instance_name, 'repeat_status', 'Repeat Status', repeat_status, 'Current Status and File', '', '130569')

    # shuffle_status | Offset: 100, Length: 4, Resolution: 1, Field Type: LOOKUP
    shuffle_status_raw = (data_raw >> 100) & 0xF
    shuffle_status = shuffle_status_raw * 1
    publish_field(hass, instance_name, 'shuffle_status', 'Shuffle Status', shuffle_status, 'Current Status and File', '', '130569')

    # save_favorite_number | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    save_favorite_number_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    save_favorite_number = save_favorite_number_raw * 1
    publish_field(hass, instance_name, 'save_favorite_number', 'Save Favorite Number', save_favorite_number, 'Current Status and File', '', '130569')

    # play_favorite_number | Offset: 112, Length: 16, Resolution: 1, Field Type: NUMBER
    play_favorite_number_raw = decode_number((data_raw >> 112) & 0xFFFF, 16)
    play_favorite_number = play_favorite_number_raw * 1
    publish_field(hass, instance_name, 'play_favorite_number', 'Play Favorite Number', play_favorite_number, 'Current Status and File', '', '130569')

    # thumbs_up_down | Offset: 128, Length: 8, Resolution: 1, Field Type: LOOKUP
    thumbs_up_down_raw = (data_raw >> 128) & 0xFF
    thumbs_up_down = thumbs_up_down_raw * 1
    publish_field(hass, instance_name, 'thumbs_up_down', 'Thumbs Up/Down', thumbs_up_down, 'Current Status and File', '', '130569')

    # signal_strength | Offset: 136, Length: 8, Resolution: 1, Field Type: NUMBER
    signal_strength_raw = decode_number((data_raw >> 136) & 0xFF, 8)
    signal_strength = signal_strength_raw * 1
    publish_field(hass, instance_name, 'signal_strength', 'Signal Strength', signal_strength, 'Current Status and File', '%', '130569')

    # radio_frequency | Offset: 144, Length: 32, Resolution: 10, Field Type: NUMBER
    radio_frequency_raw = decode_number((data_raw >> 144) & 0xFFFFFFFF, 32)
    radio_frequency = radio_frequency_raw * 10
    publish_field(hass, instance_name, 'radio_frequency', 'Radio Frequency', radio_frequency, 'Current Status and File', 'Hz', '130569')

    # hd_frequency_multicast | Offset: 176, Length: 8, Resolution: 1, Field Type: NUMBER
    hd_frequency_multicast_raw = decode_number((data_raw >> 176) & 0xFF, 8)
    hd_frequency_multicast = hd_frequency_multicast_raw * 1
    publish_field(hass, instance_name, 'hd_frequency_multicast', 'HD Frequency Multicast', hd_frequency_multicast, 'Current Status and File', '', '130569')

    # delete_favorite_number | Offset: 184, Length: 8, Resolution: 1, Field Type: NUMBER
    delete_favorite_number_raw = decode_number((data_raw >> 184) & 0xFF, 8)
    delete_favorite_number = delete_favorite_number_raw * 1
    publish_field(hass, instance_name, 'delete_favorite_number', 'Delete Favorite Number', delete_favorite_number, 'Current Status and File', '', '130569')

    # total_number_of_tracks | Offset: 192, Length: 16, Resolution: 1, Field Type: NUMBER
    total_number_of_tracks_raw = decode_number((data_raw >> 192) & 0xFFFF, 16)
    total_number_of_tracks = total_number_of_tracks_raw * 1
    publish_field(hass, instance_name, 'total_number_of_tracks', 'Total Number of Tracks', total_number_of_tracks, 'Current Status and File', '', '130569')

def process_pgn_130570(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130570."""
    # source | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 0) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Library Data File', '', '130570')

    # number | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    number_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    number = number_raw * 1
    publish_field(hass, instance_name, 'number', 'Number', number, 'Library Data File', '', '130570')

    # id | Offset: 16, Length: 32, Resolution: 1, Field Type: NUMBER
    id_raw = decode_number((data_raw >> 16) & 0xFFFFFFFF, 32)
    id = id_raw * 1
    publish_field(hass, instance_name, 'id', 'ID', id, 'Library Data File', '', '130570')

    # type | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    type_raw = (data_raw >> 48) & 0xFF
    type = type_raw * 1
    publish_field(hass, instance_name, 'type', 'Type', type, 'Library Data File', '', '130570')

def process_pgn_130571(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130571."""
    # source | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 0) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Library Data Group', '', '130571')

    # number | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    number_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    number = number_raw * 1
    publish_field(hass, instance_name, 'number', 'Number', number, 'Library Data Group', '', '130571')

    # type | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    type_raw = (data_raw >> 16) & 0xFF
    type = type_raw * 1
    publish_field(hass, instance_name, 'type', 'Type', type, 'Library Data Group', '', '130571')

    # zone | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    zone_raw = (data_raw >> 24) & 0xFF
    zone = zone_raw * 1
    publish_field(hass, instance_name, 'zone', 'Zone', zone, 'Library Data Group', '', '130571')

    # group_id | Offset: 32, Length: 32, Resolution: 1, Field Type: NUMBER
    group_id_raw = decode_number((data_raw >> 32) & 0xFFFFFFFF, 32)
    group_id = group_id_raw * 1
    publish_field(hass, instance_name, 'group_id', 'Group ID', group_id, 'Library Data Group', '', '130571')

    # id_offset | Offset: 64, Length: 16, Resolution: 1, Field Type: NUMBER
    id_offset_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    id_offset = id_offset_raw * 1
    publish_field(hass, instance_name, 'id_offset', 'ID offset', id_offset, 'Library Data Group', '', '130571')

    # id_count | Offset: 80, Length: 16, Resolution: 1, Field Type: NUMBER
    id_count_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    id_count = id_count_raw * 1
    publish_field(hass, instance_name, 'id_count', 'ID count', id_count, 'Library Data Group', '', '130571')

    # total_id_count | Offset: 96, Length: 16, Resolution: 1, Field Type: NUMBER
    total_id_count_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    total_id_count = total_id_count_raw * 1
    publish_field(hass, instance_name, 'total_id_count', 'Total ID count', total_id_count, 'Library Data Group', '', '130571')

    # id_type | Offset: 112, Length: 8, Resolution: 1, Field Type: LOOKUP
    id_type_raw = (data_raw >> 112) & 0xFF
    id_type = id_type_raw * 1
    publish_field(hass, instance_name, 'id_type', 'ID type', id_type, 'Library Data Group', '', '130571')

    # id | Offset: 120, Length: 32, Resolution: 1, Field Type: NUMBER
    id_raw = decode_number((data_raw >> 120) & 0xFFFFFFFF, 32)
    id = id_raw * 1
    publish_field(hass, instance_name, 'id', 'ID', id, 'Library Data Group', '', '130571')

def process_pgn_130572(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130572."""
    # source | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 0) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Library Data Search', '', '130572')

    # number | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    number_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    number = number_raw * 1
    publish_field(hass, instance_name, 'number', 'Number', number, 'Library Data Search', '', '130572')

    # group_id | Offset: 16, Length: 32, Resolution: 1, Field Type: NUMBER
    group_id_raw = decode_number((data_raw >> 16) & 0xFFFFFFFF, 32)
    group_id = group_id_raw * 1
    publish_field(hass, instance_name, 'group_id', 'Group ID', group_id, 'Library Data Search', '', '130572')

    # group_type_1 | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    group_type_1_raw = (data_raw >> 48) & 0xFF
    group_type_1 = group_type_1_raw * 1
    publish_field(hass, instance_name, 'group_type_1', 'Group type 1', group_type_1, 'Library Data Search', '', '130572')

def process_pgn_130573(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130573."""
    # id_offset | Offset: 0, Length: 16, Resolution: 1, Field Type: NUMBER
    id_offset_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    id_offset = id_offset_raw * 1
    publish_field(hass, instance_name, 'id_offset', 'ID offset', id_offset, 'Supported Source Data', '', '130573')

    # id_count | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    id_count_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    id_count = id_count_raw * 1
    publish_field(hass, instance_name, 'id_count', 'ID count', id_count, 'Supported Source Data', '', '130573')

    # total_id_count | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    total_id_count_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    total_id_count = total_id_count_raw * 1
    publish_field(hass, instance_name, 'total_id_count', 'Total ID count', total_id_count, 'Supported Source Data', '', '130573')

    # id | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    id_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    id = id_raw * 1
    publish_field(hass, instance_name, 'id', 'ID', id, 'Supported Source Data', '', '130573')

    # source | Offset: 56, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 56) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Supported Source Data', '', '130573')

    # number | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    number_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    number = number_raw * 1
    publish_field(hass, instance_name, 'number', 'Number', number, 'Supported Source Data', '', '130573')

def process_pgn_130574(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130574."""
    # first_zone_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    first_zone_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    first_zone_id = first_zone_id_raw * 1
    publish_field(hass, instance_name, 'first_zone_id', 'First zone ID', first_zone_id, 'Supported Zone Data', '', '130574')

    # zone_count | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_count_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    zone_count = zone_count_raw * 1
    publish_field(hass, instance_name, 'zone_count', 'Zone count', zone_count, 'Supported Zone Data', '', '130574')

    # total_zone_count | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    total_zone_count_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    total_zone_count = total_zone_count_raw * 1
    publish_field(hass, instance_name, 'total_zone_count', 'Total zone count', total_zone_count, 'Supported Zone Data', '', '130574')

    # zone_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    zone_id_raw = (data_raw >> 24) & 0xFF
    zone_id = zone_id_raw * 1
    publish_field(hass, instance_name, 'zone_id', 'Zone ID', zone_id, 'Supported Zone Data', '', '130574')

def process_pgn_130576(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130576."""
    # port_trim_tab | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    port_trim_tab_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    if port_trim_tab_raw & (1 << (8 - 1)):
        port_trim_tab_raw -= (1 << 8)
    port_trim_tab = port_trim_tab_raw * 1
    publish_field(hass, instance_name, 'port_trim_tab', 'Port trim tab', port_trim_tab, 'Small Craft Status', '%', '130576')

    # starboard_trim_tab | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    starboard_trim_tab_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    if starboard_trim_tab_raw & (1 << (8 - 1)):
        starboard_trim_tab_raw -= (1 << 8)
    starboard_trim_tab = starboard_trim_tab_raw * 1
    publish_field(hass, instance_name, 'starboard_trim_tab', 'Starboard trim tab', starboard_trim_tab, 'Small Craft Status', '%', '130576')

    # reserved | Offset: 16, Length: 48, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Small Craft Status', '', '130576')

def process_pgn_130577(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130577."""
    # data_mode | Offset: 0, Length: 4, Resolution: 1, Field Type: LOOKUP
    data_mode_raw = (data_raw >> 0) & 0xF
    data_mode = data_mode_raw * 1
    publish_field(hass, instance_name, 'data_mode', 'Data Mode', data_mode, 'Direction Data', '', '130577')

    # cog_reference | Offset: 4, Length: 2, Resolution: 1, Field Type: LOOKUP
    cog_reference_raw = (data_raw >> 4) & 0x3
    cog_reference = cog_reference_raw * 1
    publish_field(hass, instance_name, 'cog_reference', 'COG Reference', cog_reference, 'Direction Data', '', '130577')

    # reserved | Offset: 6, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 6) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Direction Data', '', '130577')

    # sid | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Direction Data', '', '130577')

    # cog | Offset: 16, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    cog_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    cog = cog_raw * 0.0001
    publish_field(hass, instance_name, 'cog', 'COG', cog, 'Direction Data', 'rad', '130577')
    publish_field(hass, instance_name, 'cog_degrees', 'COG Degrees', radians_to_degrees(cog), 'Direction Data', 'Deg', '130577')

    # sog | Offset: 32, Length: 16, Resolution: 0.01, Field Type: NUMBER
    sog_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    sog = sog_raw * 0.01
    publish_field(hass, instance_name, 'sog', 'SOG', sog, 'Direction Data', 'm/s', '130577')
    publish_field(hass, instance_name, 'sog_knots', 'SOG Knots', mps_to_knots(sog), 'Direction Data', 'Kn', '130577')

    # heading | Offset: 48, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    heading_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    heading = heading_raw * 0.0001
    publish_field(hass, instance_name, 'heading', 'Heading', heading, 'Direction Data', 'rad', '130577')
    publish_field(hass, instance_name, 'heading_degrees', 'Heading Degrees', radians_to_degrees(heading), 'Direction Data', 'Deg', '130577')

    # speed_through_water | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    speed_through_water_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    speed_through_water = speed_through_water_raw * 0.01
    publish_field(hass, instance_name, 'speed_through_water', 'Speed through Water', speed_through_water, 'Direction Data', 'm/s', '130577')
    publish_field(hass, instance_name, 'speed_through_water_knots', 'Speed through Water Knots', mps_to_knots(speed_through_water), 'Direction Data', 'Kn', '130577')

    # set | Offset: 80, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    set_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    set = set_raw * 0.0001
    publish_field(hass, instance_name, 'set', 'Set', set, 'Direction Data', 'rad', '130577')
    publish_field(hass, instance_name, 'set_degrees', 'Set Degrees', radians_to_degrees(set), 'Direction Data', 'Deg', '130577')

    # drift | Offset: 96, Length: 16, Resolution: 0.01, Field Type: NUMBER
    drift_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    drift = drift_raw * 0.01
    publish_field(hass, instance_name, 'drift', 'Drift', drift, 'Direction Data', 'm/s', '130577')
    publish_field(hass, instance_name, 'drift_knots', 'Drift Knots', mps_to_knots(drift), 'Direction Data', 'Kn', '130577')

def process_pgn_130578(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130578."""
    # longitudinal_speed__water_referenced | Offset: 0, Length: 16, Resolution: 0.001, Field Type: NUMBER
    longitudinal_speed__water_referenced_raw = decode_number((data_raw >> 0) & 0xFFFF, 16)
    if longitudinal_speed__water_referenced_raw & (1 << (16 - 1)):
        longitudinal_speed__water_referenced_raw -= (1 << 16)
    longitudinal_speed__water_referenced = longitudinal_speed__water_referenced_raw * 0.001
    publish_field(hass, instance_name, 'longitudinal_speed__water_referenced', 'Longitudinal Speed, Water-referenced', longitudinal_speed__water_referenced, 'Vessel Speed Components', 'm/s', '130578')
    publish_field(hass, instance_name, 'longitudinal_speed__water_referenced_knots', 'Longitudinal Speed, Water-referenced Knots', mps_to_knots(longitudinal_speed__water_referenced), 'Vessel Speed Components', 'Kn', '130578')

    # transverse_speed__water_referenced | Offset: 16, Length: 16, Resolution: 0.001, Field Type: NUMBER
    transverse_speed__water_referenced_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    if transverse_speed__water_referenced_raw & (1 << (16 - 1)):
        transverse_speed__water_referenced_raw -= (1 << 16)
    transverse_speed__water_referenced = transverse_speed__water_referenced_raw * 0.001
    publish_field(hass, instance_name, 'transverse_speed__water_referenced', 'Transverse Speed, Water-referenced', transverse_speed__water_referenced, 'Vessel Speed Components', 'm/s', '130578')
    publish_field(hass, instance_name, 'transverse_speed__water_referenced_knots', 'Transverse Speed, Water-referenced Knots', mps_to_knots(transverse_speed__water_referenced), 'Vessel Speed Components', 'Kn', '130578')

    # longitudinal_speed__ground_referenced | Offset: 32, Length: 16, Resolution: 0.001, Field Type: NUMBER
    longitudinal_speed__ground_referenced_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if longitudinal_speed__ground_referenced_raw & (1 << (16 - 1)):
        longitudinal_speed__ground_referenced_raw -= (1 << 16)
    longitudinal_speed__ground_referenced = longitudinal_speed__ground_referenced_raw * 0.001
    publish_field(hass, instance_name, 'longitudinal_speed__ground_referenced', 'Longitudinal Speed, Ground-referenced', longitudinal_speed__ground_referenced, 'Vessel Speed Components', 'm/s', '130578')
    publish_field(hass, instance_name, 'longitudinal_speed__ground_referenced_knots', 'Longitudinal Speed, Ground-referenced Knots', mps_to_knots(longitudinal_speed__ground_referenced), 'Vessel Speed Components', 'Kn', '130578')

    # transverse_speed__ground_referenced | Offset: 48, Length: 16, Resolution: 0.001, Field Type: NUMBER
    transverse_speed__ground_referenced_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    if transverse_speed__ground_referenced_raw & (1 << (16 - 1)):
        transverse_speed__ground_referenced_raw -= (1 << 16)
    transverse_speed__ground_referenced = transverse_speed__ground_referenced_raw * 0.001
    publish_field(hass, instance_name, 'transverse_speed__ground_referenced', 'Transverse Speed, Ground-referenced', transverse_speed__ground_referenced, 'Vessel Speed Components', 'm/s', '130578')
    publish_field(hass, instance_name, 'transverse_speed__ground_referenced_knots', 'Transverse Speed, Ground-referenced Knots', mps_to_knots(transverse_speed__ground_referenced), 'Vessel Speed Components', 'Kn', '130578')

    # stern_speed__water_referenced | Offset: 64, Length: 16, Resolution: 0.001, Field Type: NUMBER
    stern_speed__water_referenced_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    if stern_speed__water_referenced_raw & (1 << (16 - 1)):
        stern_speed__water_referenced_raw -= (1 << 16)
    stern_speed__water_referenced = stern_speed__water_referenced_raw * 0.001
    publish_field(hass, instance_name, 'stern_speed__water_referenced', 'Stern Speed, Water-referenced', stern_speed__water_referenced, 'Vessel Speed Components', 'm/s', '130578')
    publish_field(hass, instance_name, 'stern_speed__water_referenced_knots', 'Stern Speed, Water-referenced Knots', mps_to_knots(stern_speed__water_referenced), 'Vessel Speed Components', 'Kn', '130578')

    # stern_speed__ground_referenced | Offset: 80, Length: 16, Resolution: 0.001, Field Type: NUMBER
    stern_speed__ground_referenced_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    if stern_speed__ground_referenced_raw & (1 << (16 - 1)):
        stern_speed__ground_referenced_raw -= (1 << 16)
    stern_speed__ground_referenced = stern_speed__ground_referenced_raw * 0.001
    publish_field(hass, instance_name, 'stern_speed__ground_referenced', 'Stern Speed, Ground-referenced', stern_speed__ground_referenced, 'Vessel Speed Components', 'm/s', '130578')
    publish_field(hass, instance_name, 'stern_speed__ground_referenced_knots', 'Stern Speed, Ground-referenced Knots', mps_to_knots(stern_speed__ground_referenced), 'Vessel Speed Components', 'Kn', '130578')

def process_pgn_130579(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130579."""
    # power | Offset: 0, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_raw = (data_raw >> 0) & 0x3
    power = power_raw * 1
    publish_field(hass, instance_name, 'power', 'Power', power, 'System Configuration', '', '130579')

    # default_settings | Offset: 2, Length: 2, Resolution: 1, Field Type: LOOKUP
    default_settings_raw = (data_raw >> 2) & 0x3
    default_settings = default_settings_raw * 1
    publish_field(hass, instance_name, 'default_settings', 'Default Settings', default_settings, 'System Configuration', '', '130579')

    # tuner_regions | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    tuner_regions_raw = (data_raw >> 4) & 0xF
    tuner_regions = tuner_regions_raw * 1
    publish_field(hass, instance_name, 'tuner_regions', 'Tuner regions', tuner_regions, 'System Configuration', '', '130579')

    # max_favorites | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    max_favorites_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    max_favorites = max_favorites_raw * 1
    publish_field(hass, instance_name, 'max_favorites', 'Max favorites', max_favorites, 'System Configuration', '', '130579')

    # video_protocols | Offset: 16, Length: 4, Resolution: 1, Field Type: LOOKUP
    video_protocols_raw = (data_raw >> 16) & 0xF
    video_protocols = video_protocols_raw * 1
    publish_field(hass, instance_name, 'video_protocols', 'Video protocols', video_protocols, 'System Configuration', '', '130579')

    # reserved | Offset: 20, Length: 44, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 20) & 0xFFFFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'System Configuration', '', '130579')

def process_pgn_130580(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130580."""
    # power | Offset: 0, Length: 2, Resolution: 1, Field Type: LOOKUP
    power_raw = (data_raw >> 0) & 0x3
    power = power_raw * 1
    publish_field(hass, instance_name, 'power', 'Power', power, 'System Configuration (deprecated)', '', '130580')

    # default_settings | Offset: 2, Length: 2, Resolution: 1, Field Type: LOOKUP
    default_settings_raw = (data_raw >> 2) & 0x3
    default_settings = default_settings_raw * 1
    publish_field(hass, instance_name, 'default_settings', 'Default Settings', default_settings, 'System Configuration (deprecated)', '', '130580')

    # tuner_regions | Offset: 4, Length: 4, Resolution: 1, Field Type: LOOKUP
    tuner_regions_raw = (data_raw >> 4) & 0xF
    tuner_regions = tuner_regions_raw * 1
    publish_field(hass, instance_name, 'tuner_regions', 'Tuner regions', tuner_regions, 'System Configuration (deprecated)', '', '130580')

    # max_favorites | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    max_favorites_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    max_favorites = max_favorites_raw * 1
    publish_field(hass, instance_name, 'max_favorites', 'Max favorites', max_favorites, 'System Configuration (deprecated)', '', '130580')

def process_pgn_130581(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130581."""
    # first_zone_id | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    first_zone_id_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    first_zone_id = first_zone_id_raw * 1
    publish_field(hass, instance_name, 'first_zone_id', 'First zone ID', first_zone_id, 'Zone Configuration (deprecated)', '', '130581')

    # zone_count | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_count_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    zone_count = zone_count_raw * 1
    publish_field(hass, instance_name, 'zone_count', 'Zone count', zone_count, 'Zone Configuration (deprecated)', '', '130581')

    # total_zone_count | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    total_zone_count_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    total_zone_count = total_zone_count_raw * 1
    publish_field(hass, instance_name, 'total_zone_count', 'Total zone count', total_zone_count, 'Zone Configuration (deprecated)', '', '130581')

    # zone_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    zone_id_raw = (data_raw >> 24) & 0xFF
    zone_id = zone_id_raw * 1
    publish_field(hass, instance_name, 'zone_id', 'Zone ID', zone_id, 'Zone Configuration (deprecated)', '', '130581')

def process_pgn_130582(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130582."""
    # zone_id | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    zone_id_raw = (data_raw >> 0) & 0xFF
    zone_id = zone_id_raw * 1
    publish_field(hass, instance_name, 'zone_id', 'Zone ID', zone_id, 'Zone Volume', '', '130582')

    # volume | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    volume_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    volume = volume_raw * 1
    publish_field(hass, instance_name, 'volume', 'Volume', volume, 'Zone Volume', '%', '130582')

    # volume_change | Offset: 16, Length: 2, Resolution: 1, Field Type: LOOKUP
    volume_change_raw = (data_raw >> 16) & 0x3
    volume_change = volume_change_raw * 1
    publish_field(hass, instance_name, 'volume_change', 'Volume change', volume_change, 'Zone Volume', '', '130582')

    # mute | Offset: 18, Length: 2, Resolution: 1, Field Type: LOOKUP
    mute_raw = (data_raw >> 18) & 0x3
    mute = mute_raw * 1
    publish_field(hass, instance_name, 'mute', 'Mute', mute, 'Zone Volume', '', '130582')

    # reserved | Offset: 20, Length: 4, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 20) & 0xF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Zone Volume', '', '130582')

    # channel | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    channel_raw = (data_raw >> 24) & 0xFF
    channel = channel_raw * 1
    publish_field(hass, instance_name, 'channel', 'Channel', channel, 'Zone Volume', '', '130582')

    # reserved | Offset: 32, Length: 32, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFFFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Zone Volume', '', '130582')

def process_pgn_130583(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130583."""
    # first_preset | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    first_preset_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    first_preset = first_preset_raw * 1
    publish_field(hass, instance_name, 'first_preset', 'First preset', first_preset, 'Available Audio EQ presets', '', '130583')

    # preset_count | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    preset_count_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    preset_count = preset_count_raw * 1
    publish_field(hass, instance_name, 'preset_count', 'Preset count', preset_count, 'Available Audio EQ presets', '', '130583')

    # total_preset_count | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    total_preset_count_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    total_preset_count = total_preset_count_raw * 1
    publish_field(hass, instance_name, 'total_preset_count', 'Total preset count', total_preset_count, 'Available Audio EQ presets', '', '130583')

    # preset_type | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    preset_type_raw = (data_raw >> 24) & 0xFF
    preset_type = preset_type_raw * 1
    publish_field(hass, instance_name, 'preset_type', 'Preset type', preset_type, 'Available Audio EQ presets', '', '130583')

def process_pgn_130584(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130584."""
    # first_address | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    first_address_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    first_address = first_address_raw * 1
    publish_field(hass, instance_name, 'first_address', 'First address', first_address, 'Available Bluetooth addresses', '', '130584')

    # address_count | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    address_count_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    address_count = address_count_raw * 1
    publish_field(hass, instance_name, 'address_count', 'Address count', address_count, 'Available Bluetooth addresses', '', '130584')

    # total_address_count | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    total_address_count_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    total_address_count = total_address_count_raw * 1
    publish_field(hass, instance_name, 'total_address_count', 'Total address count', total_address_count, 'Available Bluetooth addresses', '', '130584')

    # bluetooth_address | Offset: 24, Length: 48, Resolution: 1, Field Type: BINARY
    bluetooth_address_raw = (data_raw >> 24) & 0xFFFFFFFFFFFF
    bluetooth_address = bluetooth_address_raw * 1
    publish_field(hass, instance_name, 'bluetooth_address', 'Bluetooth address', bluetooth_address, 'Available Bluetooth addresses', '', '130584')

    # status | Offset: 72, Length: 8, Resolution: 1, Field Type: LOOKUP
    status_raw = (data_raw >> 72) & 0xFF
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Available Bluetooth addresses', '', '130584')

def process_pgn_130585(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130585."""
    # source_number | Offset: 0, Length: 8, Resolution: 1, Field Type: NUMBER
    source_number_raw = decode_number((data_raw >> 0) & 0xFF, 8)
    source_number = source_number_raw * 1
    publish_field(hass, instance_name, 'source_number', 'Source number', source_number, 'Bluetooth source status', '', '130585')

    # status | Offset: 8, Length: 4, Resolution: 1, Field Type: LOOKUP
    status_raw = (data_raw >> 8) & 0xF
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Bluetooth source status', '', '130585')

    # forget_device | Offset: 12, Length: 2, Resolution: 1, Field Type: LOOKUP
    forget_device_raw = (data_raw >> 12) & 0x3
    forget_device = forget_device_raw * 1
    publish_field(hass, instance_name, 'forget_device', 'Forget device', forget_device, 'Bluetooth source status', '', '130585')

    # discovering | Offset: 14, Length: 2, Resolution: 1, Field Type: LOOKUP
    discovering_raw = (data_raw >> 14) & 0x3
    discovering = discovering_raw * 1
    publish_field(hass, instance_name, 'discovering', 'Discovering', discovering, 'Bluetooth source status', '', '130585')

    # bluetooth_address | Offset: 16, Length: 48, Resolution: 1, Field Type: BINARY
    bluetooth_address_raw = (data_raw >> 16) & 0xFFFFFFFFFFFF
    bluetooth_address = bluetooth_address_raw * 1
    publish_field(hass, instance_name, 'bluetooth_address', 'Bluetooth address', bluetooth_address, 'Bluetooth source status', '', '130585')

def process_pgn_130586(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130586."""
    # zone_id | Offset: 0, Length: 8, Resolution: 1, Field Type: LOOKUP
    zone_id_raw = (data_raw >> 0) & 0xFF
    zone_id = zone_id_raw * 1
    publish_field(hass, instance_name, 'zone_id', 'Zone ID', zone_id, 'Zone Configuration', '', '130586')

    # volume_limit | Offset: 8, Length: 8, Resolution: 1, Field Type: NUMBER
    volume_limit_raw = decode_number((data_raw >> 8) & 0xFF, 8)
    volume_limit = volume_limit_raw * 1
    publish_field(hass, instance_name, 'volume_limit', 'Volume limit', volume_limit, 'Zone Configuration', '%', '130586')

    # fade | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    fade_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    if fade_raw & (1 << (8 - 1)):
        fade_raw -= (1 << 8)
    fade = fade_raw * 1
    publish_field(hass, instance_name, 'fade', 'Fade', fade, 'Zone Configuration', '%', '130586')

    # balance | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    balance_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    if balance_raw & (1 << (8 - 1)):
        balance_raw -= (1 << 8)
    balance = balance_raw * 1
    publish_field(hass, instance_name, 'balance', 'Balance', balance, 'Zone Configuration', '%', '130586')

    # sub_volume | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    sub_volume_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    sub_volume = sub_volume_raw * 1
    publish_field(hass, instance_name, 'sub_volume', 'Sub volume', sub_volume, 'Zone Configuration', '%', '130586')

    # eq___treble | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    eq___treble_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    if eq___treble_raw & (1 << (8 - 1)):
        eq___treble_raw -= (1 << 8)
    eq___treble = eq___treble_raw * 1
    publish_field(hass, instance_name, 'eq___treble', 'EQ - Treble', eq___treble, 'Zone Configuration', '%', '130586')

    # eq___mid_range | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    eq___mid_range_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    if eq___mid_range_raw & (1 << (8 - 1)):
        eq___mid_range_raw -= (1 << 8)
    eq___mid_range = eq___mid_range_raw * 1
    publish_field(hass, instance_name, 'eq___mid_range', 'EQ - Mid range', eq___mid_range, 'Zone Configuration', '%', '130586')

    # eq___bass | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    eq___bass_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    if eq___bass_raw & (1 << (8 - 1)):
        eq___bass_raw -= (1 << 8)
    eq___bass = eq___bass_raw * 1
    publish_field(hass, instance_name, 'eq___bass', 'EQ - Bass', eq___bass, 'Zone Configuration', '%', '130586')

    # preset_type | Offset: 64, Length: 8, Resolution: 1, Field Type: LOOKUP
    preset_type_raw = (data_raw >> 64) & 0xFF
    preset_type = preset_type_raw * 1
    publish_field(hass, instance_name, 'preset_type', 'Preset type', preset_type, 'Zone Configuration', '', '130586')

    # audio_filter | Offset: 72, Length: 8, Resolution: 1, Field Type: LOOKUP
    audio_filter_raw = (data_raw >> 72) & 0xFF
    audio_filter = audio_filter_raw * 1
    publish_field(hass, instance_name, 'audio_filter', 'Audio filter', audio_filter, 'Zone Configuration', '', '130586')

    # high_pass_filter_frequency | Offset: 80, Length: 16, Resolution: 1, Field Type: NUMBER
    high_pass_filter_frequency_raw = decode_number((data_raw >> 80) & 0xFFFF, 16)
    high_pass_filter_frequency = high_pass_filter_frequency_raw * 1
    publish_field(hass, instance_name, 'high_pass_filter_frequency', 'High pass filter frequency', high_pass_filter_frequency, 'Zone Configuration', 'Hz', '130586')

    # low_pass_filter_frequency | Offset: 96, Length: 16, Resolution: 1, Field Type: NUMBER
    low_pass_filter_frequency_raw = decode_number((data_raw >> 96) & 0xFFFF, 16)
    low_pass_filter_frequency = low_pass_filter_frequency_raw * 1
    publish_field(hass, instance_name, 'low_pass_filter_frequency', 'Low pass filter frequency', low_pass_filter_frequency, 'Zone Configuration', 'Hz', '130586')

    # channel | Offset: 112, Length: 8, Resolution: 1, Field Type: LOOKUP
    channel_raw = (data_raw >> 112) & 0xFF
    channel = channel_raw * 1
    publish_field(hass, instance_name, 'channel', 'Channel', channel, 'Zone Configuration', '', '130586')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Init #2', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Init #2', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Init #2', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Init #2', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Init #2', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Init #2', '', '130816')

    # a | Offset: 40, Length: 16, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'SonicHub: Init #2', '', '130816')

    # b | Offset: 56, Length: 16, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'SonicHub: Init #2', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: AM Radio', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: AM Radio', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: AM Radio', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: AM Radio', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: AM Radio', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: AM Radio', '', '130816')

    # item | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    item_raw = (data_raw >> 40) & 0xFF
    item = item_raw * 1
    publish_field(hass, instance_name, 'item', 'Item', item, 'SonicHub: AM Radio', '', '130816')

    # frequency | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    frequency_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    frequency = frequency_raw * 1
    publish_field(hass, instance_name, 'frequency', 'Frequency', frequency, 'SonicHub: AM Radio', 'Hz', '130816')

    # noise_level | Offset: 80, Length: 2, Resolution: 1, Field Type: NUMBER
    noise_level_raw = decode_number((data_raw >> 80) & 0x3, 2)
    noise_level = noise_level_raw * 1
    publish_field(hass, instance_name, 'noise_level', 'Noise level', noise_level, 'SonicHub: AM Radio', '', '130816')

    # signal_level | Offset: 82, Length: 4, Resolution: 1, Field Type: NUMBER
    signal_level_raw = decode_number((data_raw >> 82) & 0xF, 4)
    signal_level = signal_level_raw * 1
    publish_field(hass, instance_name, 'signal_level', 'Signal level', signal_level, 'SonicHub: AM Radio', '', '130816')

    # reserved | Offset: 86, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 86) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: AM Radio', '', '130816')

    # text | Offset: 88, Length: 256, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Zone info', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Zone info', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Zone info', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Zone info', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Zone info', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Zone info', '', '130816')

    # zone | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone = zone_raw * 1
    publish_field(hass, instance_name, 'zone', 'Zone', zone, 'SonicHub: Zone info', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Source', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Source', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Source', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Source', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Source', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Source', '', '130816')

    # source | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 40) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'SonicHub: Source', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Source List', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Source List', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Source List', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Source List', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Source List', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Source List', '', '130816')

    # source_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'SonicHub: Source List', '', '130816')

    # a | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'SonicHub: Source List', '', '130816')

    # text | Offset: 56, Length: 256, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Control', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Control', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Control', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Control', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Control', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Control', '', '130816')

    # item | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    item_raw = (data_raw >> 40) & 0xFF
    item = item_raw * 1
    publish_field(hass, instance_name, 'item', 'Item', item, 'SonicHub: Control', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: FM Radio', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: FM Radio', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: FM Radio', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: FM Radio', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: FM Radio', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: FM Radio', '', '130816')

    # item | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    item_raw = (data_raw >> 40) & 0xFF
    item = item_raw * 1
    publish_field(hass, instance_name, 'item', 'Item', item, 'SonicHub: FM Radio', '', '130816')

    # frequency | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    frequency_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    frequency = frequency_raw * 1
    publish_field(hass, instance_name, 'frequency', 'Frequency', frequency, 'SonicHub: FM Radio', 'Hz', '130816')

    # noise_level | Offset: 80, Length: 2, Resolution: 1, Field Type: NUMBER
    noise_level_raw = decode_number((data_raw >> 80) & 0x3, 2)
    noise_level = noise_level_raw * 1
    publish_field(hass, instance_name, 'noise_level', 'Noise level', noise_level, 'SonicHub: FM Radio', '', '130816')

    # signal_level | Offset: 82, Length: 4, Resolution: 1, Field Type: NUMBER
    signal_level_raw = decode_number((data_raw >> 82) & 0xF, 4)
    signal_level = signal_level_raw * 1
    publish_field(hass, instance_name, 'signal_level', 'Signal level', signal_level, 'SonicHub: FM Radio', '', '130816')

    # reserved | Offset: 86, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 86) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: FM Radio', '', '130816')

    # text | Offset: 88, Length: 256, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Playlist', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Playlist', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Playlist', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Playlist', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Playlist', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Playlist', '', '130816')

    # item | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    item_raw = (data_raw >> 40) & 0xFF
    item = item_raw * 1
    publish_field(hass, instance_name, 'item', 'Item', item, 'SonicHub: Playlist', '', '130816')

    # a | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'SonicHub: Playlist', '', '130816')

    # current_track | Offset: 56, Length: 32, Resolution: 1, Field Type: NUMBER
    current_track_raw = decode_number((data_raw >> 56) & 0xFFFFFFFF, 32)
    current_track = current_track_raw * 1
    publish_field(hass, instance_name, 'current_track', 'Current Track', current_track, 'SonicHub: Playlist', '', '130816')

    # tracks | Offset: 88, Length: 32, Resolution: 1, Field Type: NUMBER
    tracks_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    tracks = tracks_raw * 1
    publish_field(hass, instance_name, 'tracks', 'Tracks', tracks, 'SonicHub: Playlist', '', '130816')

    # length | Offset: 120, Length: 32, Resolution: 0.001, Field Type: TIME
    length_raw = (data_raw >> 120) & 0xFFFFFFFF
    length = decode_time(length_raw * 0.001)
    publish_field(hass, instance_name, 'length', 'Length', length, 'SonicHub: Playlist', 's', '130816')

    # position_in_track | Offset: 152, Length: 32, Resolution: 0.001, Field Type: TIME
    position_in_track_raw = (data_raw >> 152) & 0xFFFFFFFF
    position_in_track = decode_time(position_in_track_raw * 0.001)
    publish_field(hass, instance_name, 'position_in_track', 'Position in track', position_in_track, 'SonicHub: Playlist', 's', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Track', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Track', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Track', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Track', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Track', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Track', '', '130816')

    # item | Offset: 40, Length: 32, Resolution: 1, Field Type: NUMBER
    item_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    item = item_raw * 1
    publish_field(hass, instance_name, 'item', 'Item', item, 'SonicHub: Track', '', '130816')

    # text | Offset: 72, Length: 256, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Artist', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Artist', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Artist', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Artist', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Artist', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Artist', '', '130816')

    # item | Offset: 40, Length: 32, Resolution: 1, Field Type: NUMBER
    item_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    item = item_raw * 1
    publish_field(hass, instance_name, 'item', 'Item', item, 'SonicHub: Artist', '', '130816')

    # text | Offset: 72, Length: 256, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Album', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Album', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Album', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Album', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Album', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Album', '', '130816')

    # item | Offset: 40, Length: 32, Resolution: 1, Field Type: NUMBER
    item_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    item = item_raw * 1
    publish_field(hass, instance_name, 'item', 'Item', item, 'SonicHub: Album', '', '130816')

    # text | Offset: 72, Length: 256, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Menu Item', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Menu Item', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Menu Item', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Menu Item', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Menu Item', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Menu Item', '', '130816')

    # item | Offset: 40, Length: 32, Resolution: 1, Field Type: NUMBER
    item_raw = decode_number((data_raw >> 40) & 0xFFFFFFFF, 32)
    item = item_raw * 1
    publish_field(hass, instance_name, 'item', 'Item', item, 'SonicHub: Menu Item', '', '130816')

    # c | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'SonicHub: Menu Item', '', '130816')

    # d | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'SonicHub: Menu Item', '', '130816')

    # e | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'SonicHub: Menu Item', '', '130816')

    # text | Offset: 96, Length: 256, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Zones', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Zones', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Zones', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Zones', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Zones', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Zones', '', '130816')

    # zones | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zones_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zones = zones_raw * 1
    publish_field(hass, instance_name, 'zones', 'Zones', zones, 'SonicHub: Zones', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Max Volume', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Max Volume', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Max Volume', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Max Volume', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Max Volume', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Max Volume', '', '130816')

    # zone | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone = zone_raw * 1
    publish_field(hass, instance_name, 'zone', 'Zone', zone, 'SonicHub: Max Volume', '', '130816')

    # level | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    level_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    level = level_raw * 1
    publish_field(hass, instance_name, 'level', 'Level', level, 'SonicHub: Max Volume', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Volume', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Volume', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Volume', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Volume', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Volume', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Volume', '', '130816')

    # zone | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone = zone_raw * 1
    publish_field(hass, instance_name, 'zone', 'Zone', zone, 'SonicHub: Volume', '', '130816')

    # level | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    level_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    level = level_raw * 1
    publish_field(hass, instance_name, 'level', 'Level', level, 'SonicHub: Volume', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Init #1', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Init #1', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Init #1', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Init #1', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Init #1', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Init #1', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Position', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Position', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Position', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Position', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Position', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Position', '', '130816')

    # position | Offset: 40, Length: 32, Resolution: 0.001, Field Type: TIME
    position_raw = (data_raw >> 40) & 0xFFFFFFFF
    position = decode_time(position_raw * 0.001)
    publish_field(hass, instance_name, 'position', 'Position', position, 'SonicHub: Position', 's', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SonicHub: Init #3', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Init #3', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SonicHub: Init #3', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SonicHub: Init #3', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'SonicHub: Init #3', '', '130816')

    # control | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 32) & 0xFF
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'SonicHub: Init #3', '', '130816')

    # a | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'SonicHub: Init #3', '', '130816')

    # b | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'SonicHub: Init #3', '', '130816')

def process_pgn_130816(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130816."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simrad: Text Message', '', '130816')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simrad: Text Message', '', '130816')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simrad: Text Message', '', '130816')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simrad: Text Message', '', '130816')

    # proprietary_id | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 24) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Simrad: Text Message', '', '130816')

    # a | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Simrad: Text Message', '', '130816')

    # b | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simrad: Text Message', '', '130816')

    # c | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Simrad: Text Message', '', '130816')

    # sid | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Simrad: Text Message', '', '130816')

    # prio | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    prio_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    prio = prio_raw * 1
    publish_field(hass, instance_name, 'prio', 'Prio', prio, 'Simrad: Text Message', '', '130816')

    # text | Offset: 72, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_130817(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130817."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Navico: Product Information', '', '130817')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navico: Product Information', '', '130817')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Navico: Product Information', '', '130817')

    # product_code | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    product_code_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    product_code = product_code_raw * 1
    publish_field(hass, instance_name, 'product_code', 'Product Code', product_code, 'Navico: Product Information', '', '130817')

    # model | Offset: 32, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # a | Offset: 288, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 288) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Navico: Product Information', '', '130817')

    # b | Offset: 296, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 296) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Navico: Product Information', '', '130817')

    # c | Offset: 304, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 304) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Navico: Product Information', '', '130817')

    # firmware_version | Offset: 312, Length: 80, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # firmware_date | Offset: 392, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # firmware_time | Offset: 648, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_130817(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130817."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Lowrance: Product Information', '', '130817')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Lowrance: Product Information', '', '130817')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Lowrance: Product Information', '', '130817')

    # product_code | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    product_code_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    product_code = product_code_raw * 1
    publish_field(hass, instance_name, 'product_code', 'Product Code', product_code, 'Lowrance: Product Information', '', '130817')

    # model | Offset: 32, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # a | Offset: 288, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 288) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Lowrance: Product Information', '', '130817')

    # b | Offset: 296, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 296) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Lowrance: Product Information', '', '130817')

    # c | Offset: 304, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 304) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Lowrance: Product Information', '', '130817')

    # firmware_version | Offset: 312, Length: 80, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # firmware_date | Offset: 392, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # firmware_time | Offset: 648, Length: 256, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_130818(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130818."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Reprogram Data', '', '130818')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Reprogram Data', '', '130818')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Reprogram Data', '', '130818')

    # version | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    version_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    version = version_raw * 1
    publish_field(hass, instance_name, 'version', 'Version', version, 'Simnet: Reprogram Data', '', '130818')

    # sequence | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    sequence_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    sequence = sequence_raw * 1
    publish_field(hass, instance_name, 'sequence', 'Sequence', sequence, 'Simnet: Reprogram Data', '', '130818')

    # data | Offset: 48, Length: 1736, Resolution: 1, Field Type: BINARY
    # Skipping fields longer than 256
def process_pgn_130819(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130819."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Request Reprogram', '', '130819')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Request Reprogram', '', '130819')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Request Reprogram', '', '130819')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Reprogram Status', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Reprogram Status', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Reprogram Status', '', '130820')

    # reserved | Offset: 16, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 16) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Reprogram Status', '', '130820')

    # status | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    status_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Simnet: Reprogram Status', '', '130820')

    # reserved | Offset: 32, Length: 24, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFFFFFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Reprogram Status', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Unknown 130820', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Unknown 130820', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Unknown 130820', '', '130820')

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Furuno: Unknown 130820', '', '130820')

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Furuno: Unknown 130820', '', '130820')

    # c | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Furuno: Unknown 130820', '', '130820')

    # d | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Furuno: Unknown 130820', '', '130820')

    # e | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Furuno: Unknown 130820', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Source Name', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Source Name', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Source Name', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Source Name', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Source Name', '', '130820')

    # source_id | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    source_id_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    source_id = source_id_raw * 1
    publish_field(hass, instance_name, 'source_id', 'Source ID', source_id, 'Fusion: Source Name', '', '130820')

    # current_source_id | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    current_source_id_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    current_source_id = current_source_id_raw * 1
    publish_field(hass, instance_name, 'current_source_id', 'Current Source ID', current_source_id, 'Fusion: Source Name', '', '130820')

    # d | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Fusion: Source Name', '', '130820')

    # e | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Fusion: Source Name', '', '130820')

    # source | Offset: 64, Length: 40, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Track Info', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Track Info', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Track Info', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Track Info', '', '130820')

    # a | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Track Info', '', '130820')

    # transport | Offset: 40, Length: 4, Resolution: 1, Field Type: LOOKUP
    transport_raw = (data_raw >> 40) & 0xF
    transport = transport_raw * 1
    publish_field(hass, instance_name, 'transport', 'Transport', transport, 'Fusion: Track Info', '', '130820')

    # x | Offset: 44, Length: 4, Resolution: 1, Field Type: NUMBER
    x_raw = decode_number((data_raw >> 44) & 0xF, 4)
    x = x_raw * 1
    publish_field(hass, instance_name, 'x', 'X', x, 'Fusion: Track Info', '', '130820')

    # b | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Track Info', '', '130820')

    # track__ | Offset: 56, Length: 16, Resolution: 1, Field Type: NUMBER
    track___raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    track__ = track___raw * 1
    publish_field(hass, instance_name, 'track__', 'Track #', track__, 'Fusion: Track Info', '', '130820')

    # c | Offset: 72, Length: 16, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Fusion: Track Info', '', '130820')

    # track_count | Offset: 88, Length: 16, Resolution: 1, Field Type: NUMBER
    track_count_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    track_count = track_count_raw * 1
    publish_field(hass, instance_name, 'track_count', 'Track Count', track_count, 'Fusion: Track Info', '', '130820')

    # e | Offset: 104, Length: 16, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 104) & 0xFFFF, 16)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Fusion: Track Info', '', '130820')

    # length | Offset: 120, Length: 24, Resolution: 0.001, Field Type: TIME
    length_raw = (data_raw >> 120) & 0xFFFFFF
    length = decode_time(length_raw * 0.001)
    publish_field(hass, instance_name, 'length', 'Length', length, 'Fusion: Track Info', 's', '130820')

    # position_in_track | Offset: 144, Length: 24, Resolution: 0.001, Field Type: TIME
    position_in_track_raw = (data_raw >> 144) & 0xFFFFFF
    position_in_track = decode_time(position_in_track_raw * 0.001)
    publish_field(hass, instance_name, 'position_in_track', 'Position in track', position_in_track, 'Fusion: Track Info', 's', '130820')

    # h | Offset: 168, Length: 16, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 168) & 0xFFFF, 16)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Fusion: Track Info', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Track', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Track', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Track', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Track', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Track', '', '130820')

    # b | Offset: 32, Length: 40, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFFFFFFFFFF, 40)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Track', '', '130820')

    # track | Offset: 72, Length: 80, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Artist', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Artist', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Artist', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Artist', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Artist', '', '130820')

    # b | Offset: 32, Length: 40, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFFFFFFFFFF, 40)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Artist', '', '130820')

    # artist | Offset: 72, Length: 80, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Album', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Album', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Album', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Album', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Album', '', '130820')

    # b | Offset: 32, Length: 40, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFFFFFFFFFF, 40)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Album', '', '130820')

    # album | Offset: 72, Length: 80, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Unit Name', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Unit Name', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Unit Name', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Unit Name', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Unit Name', '', '130820')

    # name | Offset: 32, Length: 112, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Zone Name', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Zone Name', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Zone Name', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Zone Name', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Zone Name', '', '130820')

    # number | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    number_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    number = number_raw * 1
    publish_field(hass, instance_name, 'number', 'Number', number, 'Fusion: Zone Name', '', '130820')

    # name | Offset: 40, Length: 104, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Play Progress', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Play Progress', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Play Progress', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Play Progress', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Play Progress', '', '130820')

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Play Progress', '', '130820')

    # progress | Offset: 40, Length: 24, Resolution: 0.001, Field Type: TIME
    progress_raw = (data_raw >> 40) & 0xFFFFFF
    progress = decode_time(progress_raw * 0.001)
    publish_field(hass, instance_name, 'progress', 'Progress', progress, 'Fusion: Play Progress', 's', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: AM/FM Station', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: AM/FM Station', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: AM/FM Station', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: AM/FM Station', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: AM/FM Station', '', '130820')

    # am_fm | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    am_fm_raw = (data_raw >> 32) & 0xFF
    am_fm = am_fm_raw * 1
    publish_field(hass, instance_name, 'am_fm', 'AM/FM', am_fm, 'Fusion: AM/FM Station', '', '130820')

    # b | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: AM/FM Station', '', '130820')

    # frequency | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    frequency_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    frequency = frequency_raw * 1
    publish_field(hass, instance_name, 'frequency', 'Frequency', frequency, 'Fusion: AM/FM Station', 'Hz', '130820')

    # c | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Fusion: AM/FM Station', '', '130820')

    # track | Offset: 88, Length: 80, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: VHF', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: VHF', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: VHF', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: VHF', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: VHF', '', '130820')

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: VHF', '', '130820')

    # channel | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    channel_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    channel = channel_raw * 1
    publish_field(hass, instance_name, 'channel', 'Channel', channel, 'Fusion: VHF', '', '130820')

    # d | Offset: 48, Length: 24, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 48) & 0xFFFFFF, 24)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Fusion: VHF', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Squelch', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Squelch', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Squelch', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Squelch', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Squelch', '', '130820')

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Squelch', '', '130820')

    # squelch | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    squelch_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    squelch = squelch_raw * 1
    publish_field(hass, instance_name, 'squelch', 'Squelch', squelch, 'Fusion: Squelch', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Scan', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Scan', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Scan', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Scan', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Scan', '', '130820')

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Scan', '', '130820')

    # scan | Offset: 40, Length: 2, Resolution: 1, Field Type: LOOKUP
    scan_raw = (data_raw >> 40) & 0x3
    scan = scan_raw * 1
    publish_field(hass, instance_name, 'scan', 'Scan', scan, 'Fusion: Scan', '', '130820')

    # c | Offset: 42, Length: 6, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 42) & 0x3F, 6)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Fusion: Scan', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Menu Item', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Menu Item', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Menu Item', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Menu Item', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Menu Item', '', '130820')

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Menu Item', '', '130820')

    # line | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    line_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    line = line_raw * 1
    publish_field(hass, instance_name, 'line', 'Line', line, 'Fusion: Menu Item', '', '130820')

    # e | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Fusion: Menu Item', '', '130820')

    # f | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    f_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    f = f_raw * 1
    publish_field(hass, instance_name, 'f', 'F', f, 'Fusion: Menu Item', '', '130820')

    # g | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    g_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    g = g_raw * 1
    publish_field(hass, instance_name, 'g', 'G', g, 'Fusion: Menu Item', '', '130820')

    # h | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Fusion: Menu Item', '', '130820')

    # i | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    i_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    i = i_raw * 1
    publish_field(hass, instance_name, 'i', 'I', i, 'Fusion: Menu Item', '', '130820')

    # text | Offset: 88, Length: 40, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Replay', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Replay', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Replay', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Replay', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Replay', '', '130820')

    # mode | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    mode_raw = (data_raw >> 32) & 0xFF
    mode = mode_raw * 1
    publish_field(hass, instance_name, 'mode', 'Mode', mode, 'Fusion: Replay', '', '130820')

    # c | Offset: 40, Length: 24, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 40) & 0xFFFFFF, 24)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Fusion: Replay', '', '130820')

    # d | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Fusion: Replay', '', '130820')

    # e | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Fusion: Replay', '', '130820')

    # status | Offset: 80, Length: 8, Resolution: 1, Field Type: LOOKUP
    status_raw = (data_raw >> 80) & 0xFF
    status = status_raw * 1
    publish_field(hass, instance_name, 'status', 'Status', status, 'Fusion: Replay', '', '130820')

    # h | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Fusion: Replay', '', '130820')

    # i | Offset: 96, Length: 8, Resolution: 1, Field Type: NUMBER
    i_raw = decode_number((data_raw >> 96) & 0xFF, 8)
    i = i_raw * 1
    publish_field(hass, instance_name, 'i', 'I', i, 'Fusion: Replay', '', '130820')

    # j | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    j_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    j = j_raw * 1
    publish_field(hass, instance_name, 'j', 'J', j, 'Fusion: Replay', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Mute', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Mute', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Mute', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Mute', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Mute', '', '130820')

    # mute | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    mute_raw = (data_raw >> 32) & 0xFF
    mute = mute_raw * 1
    publish_field(hass, instance_name, 'mute', 'Mute', mute, 'Fusion: Mute', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Sub Volume', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Sub Volume', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Sub Volume', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Sub Volume', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Sub Volume', '', '130820')

    # zone_1 | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_1_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    zone_1 = zone_1_raw * 1
    publish_field(hass, instance_name, 'zone_1', 'Zone 1', zone_1, 'Fusion: Sub Volume', '', '130820')

    # zone_2 | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_2_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone_2 = zone_2_raw * 1
    publish_field(hass, instance_name, 'zone_2', 'Zone 2', zone_2, 'Fusion: Sub Volume', '', '130820')

    # zone_3 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_3_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    zone_3 = zone_3_raw * 1
    publish_field(hass, instance_name, 'zone_3', 'Zone 3', zone_3, 'Fusion: Sub Volume', '', '130820')

    # zone_4 | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_4_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    zone_4 = zone_4_raw * 1
    publish_field(hass, instance_name, 'zone_4', 'Zone 4', zone_4, 'Fusion: Sub Volume', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Tone', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Tone', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Tone', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Tone', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Tone', '', '130820')

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Fusion: Tone', '', '130820')

    # bass | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    bass_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    if bass_raw & (1 << (8 - 1)):
        bass_raw -= (1 << 8)
    bass = bass_raw * 1
    publish_field(hass, instance_name, 'bass', 'Bass', bass, 'Fusion: Tone', '', '130820')

    # mid | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    mid_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    if mid_raw & (1 << (8 - 1)):
        mid_raw -= (1 << 8)
    mid = mid_raw * 1
    publish_field(hass, instance_name, 'mid', 'Mid', mid, 'Fusion: Tone', '', '130820')

    # treble | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    treble_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    if treble_raw & (1 << (8 - 1)):
        treble_raw -= (1 << 8)
    treble = treble_raw * 1
    publish_field(hass, instance_name, 'treble', 'Treble', treble, 'Fusion: Tone', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Volume', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Volume', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Volume', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Volume', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Volume', '', '130820')

    # zone_1 | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_1_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    zone_1 = zone_1_raw * 1
    publish_field(hass, instance_name, 'zone_1', 'Zone 1', zone_1, 'Fusion: Volume', '', '130820')

    # zone_2 | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_2_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    zone_2 = zone_2_raw * 1
    publish_field(hass, instance_name, 'zone_2', 'Zone 2', zone_2, 'Fusion: Volume', '', '130820')

    # zone_3 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_3_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    zone_3 = zone_3_raw * 1
    publish_field(hass, instance_name, 'zone_3', 'Zone 3', zone_3, 'Fusion: Volume', '', '130820')

    # zone_4 | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    zone_4_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    zone_4 = zone_4_raw * 1
    publish_field(hass, instance_name, 'zone_4', 'Zone 4', zone_4, 'Fusion: Volume', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: Power State', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: Power State', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: Power State', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: Power State', '', '130820')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: Power State', '', '130820')

    # state | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    state_raw = (data_raw >> 32) & 0xFF
    state = state_raw * 1
    publish_field(hass, instance_name, 'state', 'State', state, 'Fusion: Power State', '', '130820')

def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: SiriusXM Channel', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: SiriusXM Channel', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: SiriusXM Channel', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: SiriusXM Channel', '', '130820')

    # a | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: SiriusXM Channel', '', '130820')

    # channel | Offset: 56, Length: 96, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: SiriusXM Title', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: SiriusXM Title', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: SiriusXM Title', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: SiriusXM Title', '', '130820')

    # a | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: SiriusXM Title', '', '130820')

    # title | Offset: 56, Length: 96, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: SiriusXM Artist', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: SiriusXM Artist', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: SiriusXM Artist', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: SiriusXM Artist', '', '130820')

    # a | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: SiriusXM Artist', '', '130820')

    # artist | Offset: 56, Length: 96, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130820(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130820."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Fusion: SiriusXM Genre', '', '130820')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Fusion: SiriusXM Genre', '', '130820')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Fusion: SiriusXM Genre', '', '130820')

    # message_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    message_id_raw = (data_raw >> 16) & 0xFF
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Fusion: SiriusXM Genre', '', '130820')

    # a | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Fusion: SiriusXM Genre', '', '130820')

    # genre | Offset: 56, Length: 96, Resolution: 1, Field Type: STRING_LZ
    # Skipping STRING field types
def process_pgn_130821(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130821."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Navico: ASCII Data', '', '130821')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navico: ASCII Data', '', '130821')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Navico: ASCII Data', '', '130821')

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Navico: ASCII Data', '', '130821')

    # message | Offset: 24, Length: 2048, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_130821(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130821."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Unknown 130821', '', '130821')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Unknown 130821', '', '130821')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Unknown 130821', '', '130821')

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Furuno: Unknown 130821', '', '130821')

    # a | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Furuno: Unknown 130821', '', '130821')

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Furuno: Unknown 130821', '', '130821')

    # c | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Furuno: Unknown 130821', '', '130821')

    # d | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Furuno: Unknown 130821', '', '130821')

    # e | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Furuno: Unknown 130821', '', '130821')

    # f | Offset: 64, Length: 8, Resolution: 1, Field Type: NUMBER
    f_raw = decode_number((data_raw >> 64) & 0xFF, 8)
    f = f_raw * 1
    publish_field(hass, instance_name, 'f', 'F', f, 'Furuno: Unknown 130821', '', '130821')

    # g | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    g_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    g = g_raw * 1
    publish_field(hass, instance_name, 'g', 'G', g, 'Furuno: Unknown 130821', '', '130821')

    # h | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Furuno: Unknown 130821', '', '130821')

    # i | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    i_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    i = i_raw * 1
    publish_field(hass, instance_name, 'i', 'I', i, 'Furuno: Unknown 130821', '', '130821')

def process_pgn_130822(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130822."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Navico: Unknown 1', '', '130822')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navico: Unknown 1', '', '130822')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Navico: Unknown 1', '', '130822')

    # data | Offset: 16, Length: 1848, Resolution: 1, Field Type: BINARY
    # Skipping fields longer than 256
def process_pgn_130823(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130823."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Maretron: Proprietary Temperature High Range', '', '130823')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Proprietary Temperature High Range', '', '130823')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Maretron: Proprietary Temperature High Range', '', '130823')

    # sid | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    sid_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    sid = sid_raw * 1
    publish_field(hass, instance_name, 'sid', 'SID', sid, 'Maretron: Proprietary Temperature High Range', '', '130823')

    # instance | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Maretron: Proprietary Temperature High Range', '', '130823')

    # source | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    source_raw = (data_raw >> 32) & 0xFF
    source = source_raw * 1
    publish_field(hass, instance_name, 'source', 'Source', source, 'Maretron: Proprietary Temperature High Range', '', '130823')

    # actual_temperature | Offset: 40, Length: 16, Resolution: 0.1, Field Type: NUMBER
    actual_temperature_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    actual_temperature = actual_temperature_raw * 0.1
    publish_field(hass, instance_name, 'actual_temperature', 'Actual Temperature', actual_temperature, 'Maretron: Proprietary Temperature High Range', 'K', '130823')
    publish_field(hass, instance_name, 'actual_temperature_celsius', 'Actual Temperature Celsius', kelvin_to_celsius(actual_temperature), 'Maretron: Proprietary Temperature High Range', 'C', '130823')
    publish_field(hass, instance_name, 'actual_temperature_fahrenheit', 'Actual Temperature Fahrenheit', kelvin_to_fahrenheit(actual_temperature), 'Maretron: Proprietary Temperature High Range', 'F', '130823')

    # set_temperature | Offset: 56, Length: 16, Resolution: 0.1, Field Type: NUMBER
    set_temperature_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    set_temperature = set_temperature_raw * 0.1
    publish_field(hass, instance_name, 'set_temperature', 'Set Temperature', set_temperature, 'Maretron: Proprietary Temperature High Range', 'K', '130823')
    publish_field(hass, instance_name, 'set_temperature_celsius', 'Set Temperature Celsius', kelvin_to_celsius(set_temperature), 'Maretron: Proprietary Temperature High Range', 'C', '130823')
    publish_field(hass, instance_name, 'set_temperature_fahrenheit', 'Set Temperature Fahrenheit', kelvin_to_fahrenheit(set_temperature), 'Maretron: Proprietary Temperature High Range', 'F', '130823')

def process_pgn_130824(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130824."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'B&G: key-value data', '', '130824')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'B&G: key-value data', '', '130824')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'B&G: key-value data', '', '130824')

    # key | Offset: 16, Length: 12, Resolution: 1, Field Type: FIELDTYPE_LOOKUP
    key_raw = (data_raw >> 16) & 0xFFF
    key = key_raw * 1
    publish_field(hass, instance_name, 'key', 'Key', key, 'B&G: key-value data', '', '130824')

    # length | Offset: 28, Length: 4, Resolution: 1, Field Type: NUMBER
    length_raw = decode_number((data_raw >> 28) & 0xF, 4)
    length = length_raw * 1
    publish_field(hass, instance_name, 'length', 'Length', length, 'B&G: key-value data', '', '130824')

def process_pgn_130824(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130824."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Maretron: Annunciator', '', '130824')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Annunciator', '', '130824')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Maretron: Annunciator', '', '130824')

    # field_4 | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    field_4_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    field_4 = field_4_raw * 1
    publish_field(hass, instance_name, 'field_4', 'Field 4', field_4, 'Maretron: Annunciator', '', '130824')

    # field_5 | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    field_5_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    field_5 = field_5_raw * 1
    publish_field(hass, instance_name, 'field_5', 'Field 5', field_5, 'Maretron: Annunciator', '', '130824')

    # field_6 | Offset: 32, Length: 16, Resolution: 1, Field Type: NUMBER
    field_6_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    field_6 = field_6_raw * 1
    publish_field(hass, instance_name, 'field_6', 'Field 6', field_6, 'Maretron: Annunciator', '', '130824')

    # field_7 | Offset: 48, Length: 8, Resolution: 1, Field Type: NUMBER
    field_7_raw = decode_number((data_raw >> 48) & 0xFF, 8)
    field_7 = field_7_raw * 1
    publish_field(hass, instance_name, 'field_7', 'Field 7', field_7, 'Maretron: Annunciator', '', '130824')

    # field_8 | Offset: 56, Length: 16, Resolution: 1, Field Type: NUMBER
    field_8_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    field_8 = field_8_raw * 1
    publish_field(hass, instance_name, 'field_8', 'Field 8', field_8, 'Maretron: Annunciator', '', '130824')

def process_pgn_130825(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130825."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Navico: Unknown 2', '', '130825')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Navico: Unknown 2', '', '130825')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Navico: Unknown 2', '', '130825')

    # data | Offset: 16, Length: 80, Resolution: 1, Field Type: BINARY
    data_raw = (data_raw >> 16) & 0xFFFFFFFFFFFFFFFFFFFF
    data = data_raw * 1
    publish_field(hass, instance_name, 'data', 'Data', data, 'Navico: Unknown 2', '', '130825')

def process_pgn_130827(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130827."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Lowrance: unknown', '', '130827')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Lowrance: unknown', '', '130827')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Lowrance: unknown', '', '130827')

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Lowrance: unknown', '', '130827')

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Lowrance: unknown', '', '130827')

    # c | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Lowrance: unknown', '', '130827')

    # d | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Lowrance: unknown', '', '130827')

    # e | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Lowrance: unknown', '', '130827')

    # f | Offset: 64, Length: 16, Resolution: 1, Field Type: NUMBER
    f_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    f = f_raw * 1
    publish_field(hass, instance_name, 'f', 'F', f, 'Lowrance: unknown', '', '130827')

def process_pgn_130828(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130828."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Set Serial Number', '', '130828')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Set Serial Number', '', '130828')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Set Serial Number', '', '130828')

def process_pgn_130831(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130831."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Suzuki: Engine and Storage Device Config', '', '130831')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Suzuki: Engine and Storage Device Config', '', '130831')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Suzuki: Engine and Storage Device Config', '', '130831')

def process_pgn_130832(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130832."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Fuel Used - High Resolution', '', '130832')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Fuel Used - High Resolution', '', '130832')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Fuel Used - High Resolution', '', '130832')

def process_pgn_130833(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130833."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'B&G: User and Remote rename', '', '130833')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'B&G: User and Remote rename', '', '130833')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'B&G: User and Remote rename', '', '130833')

    # data_type | Offset: 16, Length: 12, Resolution: 1, Field Type: FIELDTYPE_LOOKUP
    data_type_raw = (data_raw >> 16) & 0xFFF
    data_type = data_type_raw * 1
    publish_field(hass, instance_name, 'data_type', 'Data Type', data_type, 'B&G: User and Remote rename', '', '130833')

    # length | Offset: 28, Length: 4, Resolution: 1, Field Type: NUMBER
    length_raw = decode_number((data_raw >> 28) & 0xF, 4)
    length = length_raw * 1
    publish_field(hass, instance_name, 'length', 'Length', length, 'B&G: User and Remote rename', '', '130833')

    # reserved | Offset: 32, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 32) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'B&G: User and Remote rename', '', '130833')

    # decimals | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    decimals_raw = (data_raw >> 40) & 0xFF
    decimals = decimals_raw * 1
    publish_field(hass, instance_name, 'decimals', 'Decimals', decimals, 'B&G: User and Remote rename', '', '130833')

    # short_name | Offset: 48, Length: 64, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # long_name | Offset: 112, Length: 128, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_130834(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130834."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Engine and Tank Configuration', '', '130834')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Engine and Tank Configuration', '', '130834')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Engine and Tank Configuration', '', '130834')

def process_pgn_130835(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130835."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Set Engine and Tank Configuration', '', '130835')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Set Engine and Tank Configuration', '', '130835')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Set Engine and Tank Configuration', '', '130835')

def process_pgn_130836(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130836."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # c | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # device | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    device_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    device = device_raw * 1
    publish_field(hass, instance_name, 'device', 'Device', device, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # instance | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # f | Offset: 40, Length: 4, Resolution: 1, Field Type: NUMBER
    f_raw = decode_number((data_raw >> 40) & 0xF, 4)
    f = f_raw * 1
    publish_field(hass, instance_name, 'f', 'F', f, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # tank_type | Offset: 44, Length: 4, Resolution: 1, Field Type: LOOKUP
    tank_type_raw = (data_raw >> 44) & 0xF
    tank_type = tank_type_raw * 1
    publish_field(hass, instance_name, 'tank_type', 'Tank type', tank_type, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # capacity | Offset: 48, Length: 32, Resolution: 0.1, Field Type: NUMBER
    capacity_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    capacity = capacity_raw * 0.1
    publish_field(hass, instance_name, 'capacity', 'Capacity', capacity, 'Simnet: Fluid Level Sensor Configuration', 'L', '130836')

    # g | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    g_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    g = g_raw * 1
    publish_field(hass, instance_name, 'g', 'G', g, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # h | Offset: 88, Length: 16, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 88) & 0xFFFF, 16)
    if h_raw & (1 << (16 - 1)):
        h_raw -= (1 << 16)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

    # i | Offset: 104, Length: 8, Resolution: 1, Field Type: NUMBER
    i_raw = decode_number((data_raw >> 104) & 0xFF, 8)
    if i_raw & (1 << (8 - 1)):
        i_raw -= (1 << 8)
    i = i_raw * 1
    publish_field(hass, instance_name, 'i', 'I', i, 'Simnet: Fluid Level Sensor Configuration', '', '130836')

def process_pgn_130836(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130836."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Maretron: Switch Status Counter', '', '130836')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Switch Status Counter', '', '130836')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Maretron: Switch Status Counter', '', '130836')

    # instance | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Maretron: Switch Status Counter', '', '130836')

    # indicator_number | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    indicator_number_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    indicator_number = indicator_number_raw * 1
    publish_field(hass, instance_name, 'indicator_number', 'Indicator Number', indicator_number, 'Maretron: Switch Status Counter', '', '130836')

    # start_date | Offset: 32, Length: 16, Resolution: 1, Field Type: DATE
    start_date_raw = (data_raw >> 32) & 0xFFFF
    start_date = decode_date(start_date_raw * 1)
    publish_field(hass, instance_name, 'start_date', 'Start Date', start_date, 'Maretron: Switch Status Counter', 'd', '130836')

    # start_time | Offset: 48, Length: 32, Resolution: 0.0001, Field Type: TIME
    start_time_raw = (data_raw >> 48) & 0xFFFFFFFF
    start_time = decode_time(start_time_raw * 0.0001)
    publish_field(hass, instance_name, 'start_time', 'Start Time', start_time, 'Maretron: Switch Status Counter', 's', '130836')

    # off_counter | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    off_counter_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    off_counter = off_counter_raw * 1
    publish_field(hass, instance_name, 'off_counter', 'OFF Counter', off_counter, 'Maretron: Switch Status Counter', '', '130836')

    # on_counter | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    on_counter_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    on_counter = on_counter_raw * 1
    publish_field(hass, instance_name, 'on_counter', 'ON Counter', on_counter, 'Maretron: Switch Status Counter', '', '130836')

    # error_counter | Offset: 96, Length: 8, Resolution: 1, Field Type: NUMBER
    error_counter_raw = decode_number((data_raw >> 96) & 0xFF, 8)
    error_counter = error_counter_raw * 1
    publish_field(hass, instance_name, 'error_counter', 'ERROR Counter', error_counter, 'Maretron: Switch Status Counter', '', '130836')

    # switch_status | Offset: 104, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch_status_raw = (data_raw >> 104) & 0x3
    switch_status = switch_status_raw * 1
    publish_field(hass, instance_name, 'switch_status', 'Switch Status', switch_status, 'Maretron: Switch Status Counter', '', '130836')

    # reserved | Offset: 106, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 106) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Switch Status Counter', '', '130836')

def process_pgn_130837(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130837."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Fuel Flow Turbine Configuration', '', '130837')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Fuel Flow Turbine Configuration', '', '130837')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Fuel Flow Turbine Configuration', '', '130837')

def process_pgn_130837(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130837."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Maretron: Switch Status Timer', '', '130837')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Switch Status Timer', '', '130837')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Maretron: Switch Status Timer', '', '130837')

    # instance | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    instance_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    instance = instance_raw * 1
    publish_field(hass, instance_name, 'instance', 'Instance', instance, 'Maretron: Switch Status Timer', '', '130837')

    # indicator_number | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    indicator_number_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    indicator_number = indicator_number_raw * 1
    publish_field(hass, instance_name, 'indicator_number', 'Indicator Number', indicator_number, 'Maretron: Switch Status Timer', '', '130837')

    # start_date | Offset: 32, Length: 16, Resolution: 1, Field Type: DATE
    start_date_raw = (data_raw >> 32) & 0xFFFF
    start_date = decode_date(start_date_raw * 1)
    publish_field(hass, instance_name, 'start_date', 'Start Date', start_date, 'Maretron: Switch Status Timer', 'd', '130837')

    # start_time | Offset: 48, Length: 32, Resolution: 0.0001, Field Type: TIME
    start_time_raw = (data_raw >> 48) & 0xFFFFFFFF
    start_time = decode_time(start_time_raw * 0.0001)
    publish_field(hass, instance_name, 'start_time', 'Start Time', start_time, 'Maretron: Switch Status Timer', 's', '130837')

    # accumulated_off_period | Offset: 80, Length: 32, Resolution: 1, Field Type: TIME
    accumulated_off_period_raw = (data_raw >> 80) & 0xFFFFFFFF
    accumulated_off_period = decode_time(accumulated_off_period_raw * 1)
    publish_field(hass, instance_name, 'accumulated_off_period', 'Accumulated OFF Period', accumulated_off_period, 'Maretron: Switch Status Timer', 's', '130837')

    # accumulated_on_period | Offset: 112, Length: 32, Resolution: 1, Field Type: TIME
    accumulated_on_period_raw = (data_raw >> 112) & 0xFFFFFFFF
    accumulated_on_period = decode_time(accumulated_on_period_raw * 1)
    publish_field(hass, instance_name, 'accumulated_on_period', 'Accumulated ON Period', accumulated_on_period, 'Maretron: Switch Status Timer', 's', '130837')

    # accumulated_error_period | Offset: 144, Length: 32, Resolution: 1, Field Type: TIME
    accumulated_error_period_raw = (data_raw >> 144) & 0xFFFFFFFF
    accumulated_error_period = decode_time(accumulated_error_period_raw * 1)
    publish_field(hass, instance_name, 'accumulated_error_period', 'Accumulated ERROR Period', accumulated_error_period, 'Maretron: Switch Status Timer', 's', '130837')

    # switch_status | Offset: 176, Length: 2, Resolution: 1, Field Type: LOOKUP
    switch_status_raw = (data_raw >> 176) & 0x3
    switch_status = switch_status_raw * 1
    publish_field(hass, instance_name, 'switch_status', 'Switch Status', switch_status, 'Maretron: Switch Status Timer', '', '130837')

    # reserved | Offset: 178, Length: 6, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 178) & 0x3F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Maretron: Switch Status Timer', '', '130837')

def process_pgn_130838(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130838."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Fluid Level Warning', '', '130838')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Fluid Level Warning', '', '130838')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Fluid Level Warning', '', '130838')

def process_pgn_130839(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130839."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Pressure Sensor Configuration', '', '130839')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Pressure Sensor Configuration', '', '130839')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Pressure Sensor Configuration', '', '130839')

def process_pgn_130840(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130840."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Data User Group Configuration', '', '130840')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Data User Group Configuration', '', '130840')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Data User Group Configuration', '', '130840')

def process_pgn_130842(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130842."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: AIS Class B static data (msg 24 Part A)', '', '130842')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AIS Class B static data (msg 24 Part A)', '', '130842')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: AIS Class B static data (msg 24 Part A)', '', '130842')

    # message_id | Offset: 16, Length: 6, Resolution: 1, Field Type: NUMBER
    message_id_raw = decode_number((data_raw >> 16) & 0x3F, 6)
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Simnet: AIS Class B static data (msg 24 Part A)', '', '130842')

    # repeat_indicator | Offset: 22, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 22) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'Simnet: AIS Class B static data (msg 24 Part A)', '', '130842')

    # d | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: AIS Class B static data (msg 24 Part A)', '', '130842')

    # e | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Simnet: AIS Class B static data (msg 24 Part A)', '', '130842')

    # user_id | Offset: 40, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 40) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'Simnet: AIS Class B static data (msg 24 Part A)', '', '130842')

    # name | Offset: 72, Length: 160, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_130842(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130842."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # a | Offset: 16, Length: 32, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFFFFFFFF, 32)
    if a_raw & (1 << (32 - 1)):
        a_raw -= (1 << 32)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # b | Offset: 48, Length: 32, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 48) & 0xFFFFFFFF, 32)
    if b_raw & (1 << (32 - 1)):
        b_raw -= (1 << 32)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # c | Offset: 80, Length: 32, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 80) & 0xFFFFFFFF, 32)
    if c_raw & (1 << (32 - 1)):
        c_raw -= (1 << 32)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # d | Offset: 112, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 112) & 0xFF, 8)
    if d_raw & (1 << (8 - 1)):
        d_raw -= (1 << 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # e | Offset: 120, Length: 32, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 120) & 0xFFFFFFFF, 32)
    if e_raw & (1 << (32 - 1)):
        e_raw -= (1 << 32)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # f | Offset: 152, Length: 32, Resolution: 1, Field Type: NUMBER
    f_raw = decode_number((data_raw >> 152) & 0xFFFFFFFF, 32)
    if f_raw & (1 << (32 - 1)):
        f_raw -= (1 << 32)
    f = f_raw * 1
    publish_field(hass, instance_name, 'f', 'F', f, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # g | Offset: 184, Length: 16, Resolution: 1, Field Type: NUMBER
    g_raw = decode_number((data_raw >> 184) & 0xFFFF, 16)
    if g_raw & (1 << (16 - 1)):
        g_raw -= (1 << 16)
    g = g_raw * 1
    publish_field(hass, instance_name, 'g', 'G', g, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # h | Offset: 200, Length: 16, Resolution: 1, Field Type: NUMBER
    h_raw = decode_number((data_raw >> 200) & 0xFFFF, 16)
    if h_raw & (1 << (16 - 1)):
        h_raw -= (1 << 16)
    h = h_raw * 1
    publish_field(hass, instance_name, 'h', 'H', h, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

    # i | Offset: 216, Length: 16, Resolution: 1, Field Type: NUMBER
    i_raw = decode_number((data_raw >> 216) & 0xFFFF, 16)
    if i_raw & (1 << (16 - 1)):
        i_raw -= (1 << 16)
    i = i_raw * 1
    publish_field(hass, instance_name, 'i', 'I', i, 'Furuno: Six Degrees Of Freedom Movement', '', '130842')

def process_pgn_130842(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130842."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # message_id | Offset: 16, Length: 6, Resolution: 1, Field Type: NUMBER
    message_id_raw = decode_number((data_raw >> 16) & 0x3F, 6)
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # repeat_indicator | Offset: 22, Length: 2, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 22) & 0x3
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # d | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # e | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # user_id | Offset: 40, Length: 32, Resolution: 1, Field Type: MMSI
    user_id_raw = (data_raw >> 40) & 0xFFFFFFFF
    user_id = user_id_raw * 1
    publish_field(hass, instance_name, 'user_id', 'User ID', user_id, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # type_of_ship | Offset: 72, Length: 8, Resolution: 1, Field Type: LOOKUP
    type_of_ship_raw = (data_raw >> 72) & 0xFF
    type_of_ship = type_of_ship_raw * 1
    publish_field(hass, instance_name, 'type_of_ship', 'Type of ship', type_of_ship, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # vendor_id | Offset: 80, Length: 56, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # callsign | Offset: 136, Length: 56, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
    # length | Offset: 192, Length: 16, Resolution: 0.1, Field Type: NUMBER
    length_raw = decode_number((data_raw >> 192) & 0xFFFF, 16)
    length = length_raw * 0.1
    publish_field(hass, instance_name, 'length', 'Length', length, 'Simnet: AIS Class B static data (msg 24 Part B)', 'm', '130842')

    # beam | Offset: 208, Length: 16, Resolution: 0.1, Field Type: NUMBER
    beam_raw = decode_number((data_raw >> 208) & 0xFFFF, 16)
    beam = beam_raw * 0.1
    publish_field(hass, instance_name, 'beam', 'Beam', beam, 'Simnet: AIS Class B static data (msg 24 Part B)', 'm', '130842')

    # position_reference_from_starboard | Offset: 224, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_starboard_raw = decode_number((data_raw >> 224) & 0xFFFF, 16)
    position_reference_from_starboard = position_reference_from_starboard_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_starboard', 'Position reference from Starboard', position_reference_from_starboard, 'Simnet: AIS Class B static data (msg 24 Part B)', 'm', '130842')

    # position_reference_from_bow | Offset: 240, Length: 16, Resolution: 0.1, Field Type: NUMBER
    position_reference_from_bow_raw = decode_number((data_raw >> 240) & 0xFFFF, 16)
    position_reference_from_bow = position_reference_from_bow_raw * 0.1
    publish_field(hass, instance_name, 'position_reference_from_bow', 'Position reference from Bow', position_reference_from_bow, 'Simnet: AIS Class B static data (msg 24 Part B)', 'm', '130842')

    # mothership_user_id | Offset: 256, Length: 32, Resolution: 1, Field Type: MMSI
    mothership_user_id_raw = (data_raw >> 256) & 0xFFFFFFFF
    mothership_user_id = mothership_user_id_raw * 1
    publish_field(hass, instance_name, 'mothership_user_id', 'Mothership User ID', mothership_user_id, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # spare | Offset: 288, Length: 6, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 288) & 0x3F
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

    # reserved | Offset: 294, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 294) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AIS Class B static data (msg 24 Part B)', '', '130842')

def process_pgn_130843(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130843."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Heel Angle, Roll Information', '', '130843')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Heel Angle, Roll Information', '', '130843')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Heel Angle, Roll Information', '', '130843')

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Furuno: Heel Angle, Roll Information', '', '130843')

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Furuno: Heel Angle, Roll Information', '', '130843')

    # yaw | Offset: 32, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    yaw_raw = decode_number((data_raw >> 32) & 0xFFFF, 16)
    if yaw_raw & (1 << (16 - 1)):
        yaw_raw -= (1 << 16)
    yaw = yaw_raw * 0.0001
    publish_field(hass, instance_name, 'yaw', 'Yaw', yaw, 'Furuno: Heel Angle, Roll Information', 'rad', '130843')
    publish_field(hass, instance_name, 'yaw_degrees', 'Yaw Degrees', radians_to_degrees(yaw), 'Furuno: Heel Angle, Roll Information', 'Deg', '130843')

    # pitch | Offset: 48, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    pitch_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    if pitch_raw & (1 << (16 - 1)):
        pitch_raw -= (1 << 16)
    pitch = pitch_raw * 0.0001
    publish_field(hass, instance_name, 'pitch', 'Pitch', pitch, 'Furuno: Heel Angle, Roll Information', 'rad', '130843')
    publish_field(hass, instance_name, 'pitch_degrees', 'Pitch Degrees', radians_to_degrees(pitch), 'Furuno: Heel Angle, Roll Information', 'Deg', '130843')

    # roll | Offset: 64, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    roll_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    if roll_raw & (1 << (16 - 1)):
        roll_raw -= (1 << 16)
    roll = roll_raw * 0.0001
    publish_field(hass, instance_name, 'roll', 'Roll', roll, 'Furuno: Heel Angle, Roll Information', 'rad', '130843')
    publish_field(hass, instance_name, 'roll_degrees', 'Roll Degrees', radians_to_degrees(roll), 'Furuno: Heel Angle, Roll Information', 'Deg', '130843')

def process_pgn_130843(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130843."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Sonar Status, Frequency and DSP Voltage', '', '130843')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Sonar Status, Frequency and DSP Voltage', '', '130843')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Sonar Status, Frequency and DSP Voltage', '', '130843')

def process_pgn_130845(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130845."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Multi Sats In View Extended', '', '130845')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Multi Sats In View Extended', '', '130845')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Multi Sats In View Extended', '', '130845')

def process_pgn_130845(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130845."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Key Value', '', '130845')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Key Value', '', '130845')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Key Value', '', '130845')

    # address | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    address_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    address = address_raw * 1
    publish_field(hass, instance_name, 'address', 'Address', address, 'Simnet: Key Value', '', '130845')

    # repeat_indicator | Offset: 24, Length: 8, Resolution: 1, Field Type: LOOKUP
    repeat_indicator_raw = (data_raw >> 24) & 0xFF
    repeat_indicator = repeat_indicator_raw * 1
    publish_field(hass, instance_name, 'repeat_indicator', 'Repeat Indicator', repeat_indicator, 'Simnet: Key Value', '', '130845')

    # display_group | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    display_group_raw = (data_raw >> 32) & 0xFF
    display_group = display_group_raw * 1
    publish_field(hass, instance_name, 'display_group', 'Display Group', display_group, 'Simnet: Key Value', '', '130845')

    # reserved | Offset: 40, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Key Value', '', '130845')

    # key | Offset: 48, Length: 16, Resolution: 1, Field Type: FIELDTYPE_LOOKUP
    key_raw = (data_raw >> 48) & 0xFFFF
    key = key_raw * 1
    publish_field(hass, instance_name, 'key', 'Key', key, 'Simnet: Key Value', '', '130845')

    # spare | Offset: 64, Length: 8, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 64) & 0xFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: Key Value', '', '130845')

    # minlength | Offset: 72, Length: 8, Resolution: 1, Field Type: NUMBER
    minlength_raw = decode_number((data_raw >> 72) & 0xFF, 8)
    minlength = minlength_raw * 1
    publish_field(hass, instance_name, 'minlength', 'MinLength', minlength, 'Simnet: Key Value', '', '130845')

def process_pgn_130846(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130846."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Parameter Set', '', '130846')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Parameter Set', '', '130846')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Parameter Set', '', '130846')

    # address | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    address_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    address = address_raw * 1
    publish_field(hass, instance_name, 'address', 'Address', address, 'Simnet: Parameter Set', '', '130846')

    # b | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: Parameter Set', '', '130846')

    # display_group | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    display_group_raw = (data_raw >> 32) & 0xFF
    display_group = display_group_raw * 1
    publish_field(hass, instance_name, 'display_group', 'Display Group', display_group, 'Simnet: Parameter Set', '', '130846')

    # d | Offset: 40, Length: 16, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: Parameter Set', '', '130846')

    # key | Offset: 56, Length: 16, Resolution: 1, Field Type: FIELDTYPE_LOOKUP
    key_raw = (data_raw >> 56) & 0xFFFF
    key = key_raw * 1
    publish_field(hass, instance_name, 'key', 'Key', key, 'Simnet: Parameter Set', '', '130846')

    # spare | Offset: 72, Length: 8, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 72) & 0xFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: Parameter Set', '', '130846')

    # length | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    length_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    length = length_raw * 1
    publish_field(hass, instance_name, 'length', 'Length', length, 'Simnet: Parameter Set', '', '130846')

def process_pgn_130846(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130846."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Furuno: Motion Sensor Status Extended', '', '130846')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Furuno: Motion Sensor Status Extended', '', '130846')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Furuno: Motion Sensor Status Extended', '', '130846')

def process_pgn_130847(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130847."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'SeaTalk: Node Statistics', '', '130847')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'SeaTalk: Node Statistics', '', '130847')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'SeaTalk: Node Statistics', '', '130847')

    # product_code | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    product_code_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    product_code = product_code_raw * 1
    publish_field(hass, instance_name, 'product_code', 'Product Code', product_code, 'SeaTalk: Node Statistics', '', '130847')

    # year | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    year_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    year = year_raw * 1
    publish_field(hass, instance_name, 'year', 'Year', year, 'SeaTalk: Node Statistics', '', '130847')

    # month | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    month_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    month = month_raw * 1
    publish_field(hass, instance_name, 'month', 'Month', month, 'SeaTalk: Node Statistics', '', '130847')

    # device_number | Offset: 48, Length: 16, Resolution: 1, Field Type: NUMBER
    device_number_raw = decode_number((data_raw >> 48) & 0xFFFF, 16)
    device_number = device_number_raw * 1
    publish_field(hass, instance_name, 'device_number', 'Device Number', device_number, 'SeaTalk: Node Statistics', '', '130847')

    # node_voltage | Offset: 64, Length: 16, Resolution: 0.01, Field Type: NUMBER
    node_voltage_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    node_voltage = node_voltage_raw * 0.01
    publish_field(hass, instance_name, 'node_voltage', 'Node Voltage', node_voltage, 'SeaTalk: Node Statistics', 'V', '130847')

def process_pgn_130850(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130850."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: AP Command', '', '130850')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Command', '', '130850')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: AP Command', '', '130850')

    # address | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    address_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    address = address_raw * 1
    publish_field(hass, instance_name, 'address', 'Address', address, 'Simnet: AP Command', '', '130850')

    # reserved | Offset: 24, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 24) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Command', '', '130850')

    # proprietary_id | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 32) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Simnet: AP Command', '', '130850')

    # ap_status | Offset: 40, Length: 8, Resolution: 1, Field Type: LOOKUP
    ap_status_raw = (data_raw >> 40) & 0xFF
    ap_status = ap_status_raw * 1
    publish_field(hass, instance_name, 'ap_status', 'AP status', ap_status, 'Simnet: AP Command', '', '130850')

    # ap_command | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    ap_command_raw = (data_raw >> 48) & 0xFF
    ap_command = ap_command_raw * 1
    publish_field(hass, instance_name, 'ap_command', 'AP Command', ap_command, 'Simnet: AP Command', '', '130850')

    # spare | Offset: 56, Length: 8, Resolution: 1, Field Type: SPARE
    spare_raw = (data_raw >> 56) & 0xFF
    spare = spare_raw * 1
    publish_field(hass, instance_name, 'spare', 'Spare', spare, 'Simnet: AP Command', '', '130850')

    # direction | Offset: 64, Length: 8, Resolution: 1, Field Type: LOOKUP
    direction_raw = (data_raw >> 64) & 0xFF
    direction = direction_raw * 1
    publish_field(hass, instance_name, 'direction', 'Direction', direction, 'Simnet: AP Command', '', '130850')

    # angle | Offset: 72, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    angle_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    angle = angle_raw * 0.0001
    publish_field(hass, instance_name, 'angle', 'Angle', angle, 'Simnet: AP Command', 'rad', '130850')
    publish_field(hass, instance_name, 'angle_degrees', 'Angle Degrees', radians_to_degrees(angle), 'Simnet: AP Command', 'Deg', '130850')

def process_pgn_130850(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130850."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Event Command: AP command', '', '130850')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Event Command: AP command', '', '130850')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Event Command: AP command', '', '130850')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Simnet: Event Command: AP command', '', '130850')

    # unused_a | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    unused_a_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    unused_a = unused_a_raw * 1
    publish_field(hass, instance_name, 'unused_a', 'Unused A', unused_a, 'Simnet: Event Command: AP command', '', '130850')

    # controlling_device | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    controlling_device_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    controlling_device = controlling_device_raw * 1
    publish_field(hass, instance_name, 'controlling_device', 'Controlling Device', controlling_device, 'Simnet: Event Command: AP command', '', '130850')

    # event | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    event_raw = (data_raw >> 48) & 0xFF
    event = event_raw * 1
    publish_field(hass, instance_name, 'event', 'Event', event, 'Simnet: Event Command: AP command', '', '130850')

    # unused_b | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    unused_b_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    unused_b = unused_b_raw * 1
    publish_field(hass, instance_name, 'unused_b', 'Unused B', unused_b, 'Simnet: Event Command: AP command', '', '130850')

    # direction | Offset: 64, Length: 8, Resolution: 1, Field Type: LOOKUP
    direction_raw = (data_raw >> 64) & 0xFF
    direction = direction_raw * 1
    publish_field(hass, instance_name, 'direction', 'Direction', direction, 'Simnet: Event Command: AP command', '', '130850')

    # angle | Offset: 72, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    angle_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    angle = angle_raw * 0.0001
    publish_field(hass, instance_name, 'angle', 'Angle', angle, 'Simnet: Event Command: AP command', 'rad', '130850')
    publish_field(hass, instance_name, 'angle_degrees', 'Angle Degrees', radians_to_degrees(angle), 'Simnet: Event Command: AP command', 'Deg', '130850')

    # unused_c | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    unused_c_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    unused_c = unused_c_raw * 1
    publish_field(hass, instance_name, 'unused_c', 'Unused C', unused_c, 'Simnet: Event Command: AP command', '', '130850')

def process_pgn_130850(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130850."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Alarm', '', '130850')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Alarm', '', '130850')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Alarm', '', '130850')

    # address | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    address_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    address = address_raw * 1
    publish_field(hass, instance_name, 'address', 'Address', address, 'Simnet: Alarm', '', '130850')

    # reserved | Offset: 24, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 24) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Alarm', '', '130850')

    # proprietary_id | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 32) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Simnet: Alarm', '', '130850')

    # reserved | Offset: 40, Length: 8, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 40) & 0xFF
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Alarm', '', '130850')

    # alarm | Offset: 48, Length: 16, Resolution: 1, Field Type: LOOKUP
    alarm_raw = (data_raw >> 48) & 0xFFFF
    alarm = alarm_raw * 1
    publish_field(hass, instance_name, 'alarm', 'Alarm', alarm, 'Simnet: Alarm', '', '130850')

    # message_id | Offset: 64, Length: 16, Resolution: 1, Field Type: NUMBER
    message_id_raw = decode_number((data_raw >> 64) & 0xFFFF, 16)
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Simnet: Alarm', '', '130850')

    # f | Offset: 80, Length: 8, Resolution: 1, Field Type: NUMBER
    f_raw = decode_number((data_raw >> 80) & 0xFF, 8)
    f = f_raw * 1
    publish_field(hass, instance_name, 'f', 'F', f, 'Simnet: Alarm', '', '130850')

    # g | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    g_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    g = g_raw * 1
    publish_field(hass, instance_name, 'g', 'G', g, 'Simnet: Alarm', '', '130850')

def process_pgn_130851(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130851."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Event Reply: AP command', '', '130851')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Event Reply: AP command', '', '130851')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Event Reply: AP command', '', '130851')

    # proprietary_id | Offset: 16, Length: 8, Resolution: 1, Field Type: LOOKUP
    proprietary_id_raw = (data_raw >> 16) & 0xFF
    proprietary_id = proprietary_id_raw * 1
    publish_field(hass, instance_name, 'proprietary_id', 'Proprietary ID', proprietary_id, 'Simnet: Event Reply: AP command', '', '130851')

    # b | Offset: 24, Length: 16, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: Event Reply: AP command', '', '130851')

    # address | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    address_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    address = address_raw * 1
    publish_field(hass, instance_name, 'address', 'Address', address, 'Simnet: Event Reply: AP command', '', '130851')

    # event | Offset: 48, Length: 8, Resolution: 1, Field Type: LOOKUP
    event_raw = (data_raw >> 48) & 0xFF
    event = event_raw * 1
    publish_field(hass, instance_name, 'event', 'Event', event, 'Simnet: Event Reply: AP command', '', '130851')

    # c | Offset: 56, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 56) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Simnet: Event Reply: AP command', '', '130851')

    # direction | Offset: 64, Length: 8, Resolution: 1, Field Type: LOOKUP
    direction_raw = (data_raw >> 64) & 0xFF
    direction = direction_raw * 1
    publish_field(hass, instance_name, 'direction', 'Direction', direction, 'Simnet: Event Reply: AP command', '', '130851')

    # angle | Offset: 72, Length: 16, Resolution: 0.0001, Field Type: NUMBER
    angle_raw = decode_number((data_raw >> 72) & 0xFFFF, 16)
    angle = angle_raw * 0.0001
    publish_field(hass, instance_name, 'angle', 'Angle', angle, 'Simnet: Event Reply: AP command', 'rad', '130851')
    publish_field(hass, instance_name, 'angle_degrees', 'Angle Degrees', radians_to_degrees(angle), 'Simnet: Event Reply: AP command', 'Deg', '130851')

    # g | Offset: 88, Length: 8, Resolution: 1, Field Type: NUMBER
    g_raw = decode_number((data_raw >> 88) & 0xFF, 8)
    g = g_raw * 1
    publish_field(hass, instance_name, 'g', 'G', g, 'Simnet: Event Reply: AP command', '', '130851')

def process_pgn_130856(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130856."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: Alarm Message', '', '130856')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: Alarm Message', '', '130856')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: Alarm Message', '', '130856')

    # message_id | Offset: 16, Length: 16, Resolution: 1, Field Type: NUMBER
    message_id_raw = decode_number((data_raw >> 16) & 0xFFFF, 16)
    message_id = message_id_raw * 1
    publish_field(hass, instance_name, 'message_id', 'Message ID', message_id, 'Simnet: Alarm Message', '', '130856')

    # b | Offset: 32, Length: 8, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 32) & 0xFF, 8)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: Alarm Message', '', '130856')

    # c | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Simnet: Alarm Message', '', '130856')

    # text | Offset: 48, Length: 1784, Resolution: 1, Field Type: STRING_FIX
    # Skipping STRING field types
def process_pgn_130860(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130860."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Simnet: AP Unknown 4', '', '130860')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Simnet: AP Unknown 4', '', '130860')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Simnet: AP Unknown 4', '', '130860')

    # a | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    a_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    a = a_raw * 1
    publish_field(hass, instance_name, 'a', 'A', a, 'Simnet: AP Unknown 4', '', '130860')

    # b | Offset: 24, Length: 32, Resolution: 1, Field Type: NUMBER
    b_raw = decode_number((data_raw >> 24) & 0xFFFFFFFF, 32)
    if b_raw & (1 << (32 - 1)):
        b_raw -= (1 << 32)
    b = b_raw * 1
    publish_field(hass, instance_name, 'b', 'B', b, 'Simnet: AP Unknown 4', '', '130860')

    # c | Offset: 56, Length: 32, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 56) & 0xFFFFFFFF, 32)
    if c_raw & (1 << (32 - 1)):
        c_raw -= (1 << 32)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Simnet: AP Unknown 4', '', '130860')

    # d | Offset: 88, Length: 32, Resolution: 1, Field Type: NUMBER
    d_raw = decode_number((data_raw >> 88) & 0xFFFFFFFF, 32)
    d = d_raw * 1
    publish_field(hass, instance_name, 'd', 'D', d, 'Simnet: AP Unknown 4', '', '130860')

    # e | Offset: 120, Length: 32, Resolution: 1, Field Type: NUMBER
    e_raw = decode_number((data_raw >> 120) & 0xFFFFFFFF, 32)
    if e_raw & (1 << (32 - 1)):
        e_raw -= (1 << 32)
    e = e_raw * 1
    publish_field(hass, instance_name, 'e', 'E', e, 'Simnet: AP Unknown 4', '', '130860')

    # f | Offset: 152, Length: 32, Resolution: 1, Field Type: NUMBER
    f_raw = decode_number((data_raw >> 152) & 0xFFFFFFFF, 32)
    f = f_raw * 1
    publish_field(hass, instance_name, 'f', 'F', f, 'Simnet: AP Unknown 4', '', '130860')

def process_pgn_130880(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130880."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Additional Weather Data', '', '130880')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Additional Weather Data', '', '130880')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Additional Weather Data', '', '130880')

    # c | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Airmar: Additional Weather Data', '', '130880')

    # apparent_windchill_temperature | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    apparent_windchill_temperature_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    apparent_windchill_temperature = apparent_windchill_temperature_raw * 0.01
    publish_field(hass, instance_name, 'apparent_windchill_temperature', 'Apparent Windchill Temperature', apparent_windchill_temperature, 'Airmar: Additional Weather Data', 'K', '130880')
    publish_field(hass, instance_name, 'apparent_windchill_temperature_celsius', 'Apparent Windchill Temperature Celsius', kelvin_to_celsius(apparent_windchill_temperature), 'Airmar: Additional Weather Data', 'C', '130880')
    publish_field(hass, instance_name, 'apparent_windchill_temperature_fahrenheit', 'Apparent Windchill Temperature Fahrenheit', kelvin_to_fahrenheit(apparent_windchill_temperature), 'Airmar: Additional Weather Data', 'F', '130880')

    # true_windchill_temperature | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    true_windchill_temperature_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    true_windchill_temperature = true_windchill_temperature_raw * 0.01
    publish_field(hass, instance_name, 'true_windchill_temperature', 'True Windchill Temperature', true_windchill_temperature, 'Airmar: Additional Weather Data', 'K', '130880')
    publish_field(hass, instance_name, 'true_windchill_temperature_celsius', 'True Windchill Temperature Celsius', kelvin_to_celsius(true_windchill_temperature), 'Airmar: Additional Weather Data', 'C', '130880')
    publish_field(hass, instance_name, 'true_windchill_temperature_fahrenheit', 'True Windchill Temperature Fahrenheit', kelvin_to_fahrenheit(true_windchill_temperature), 'Airmar: Additional Weather Data', 'F', '130880')

    # dewpoint | Offset: 56, Length: 16, Resolution: 0.01, Field Type: NUMBER
    dewpoint_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    dewpoint = dewpoint_raw * 0.01
    publish_field(hass, instance_name, 'dewpoint', 'Dewpoint', dewpoint, 'Airmar: Additional Weather Data', 'K', '130880')
    publish_field(hass, instance_name, 'dewpoint_celsius', 'Dewpoint Celsius', kelvin_to_celsius(dewpoint), 'Airmar: Additional Weather Data', 'C', '130880')
    publish_field(hass, instance_name, 'dewpoint_fahrenheit', 'Dewpoint Fahrenheit', kelvin_to_fahrenheit(dewpoint), 'Airmar: Additional Weather Data', 'F', '130880')

def process_pgn_130881(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130881."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: Heater Control', '', '130881')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: Heater Control', '', '130881')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: Heater Control', '', '130881')

    # c | Offset: 16, Length: 8, Resolution: 1, Field Type: NUMBER
    c_raw = decode_number((data_raw >> 16) & 0xFF, 8)
    c = c_raw * 1
    publish_field(hass, instance_name, 'c', 'C', c, 'Airmar: Heater Control', '', '130881')

    # plate_temperature | Offset: 24, Length: 16, Resolution: 0.01, Field Type: NUMBER
    plate_temperature_raw = decode_number((data_raw >> 24) & 0xFFFF, 16)
    plate_temperature = plate_temperature_raw * 0.01
    publish_field(hass, instance_name, 'plate_temperature', 'Plate Temperature', plate_temperature, 'Airmar: Heater Control', 'K', '130881')
    publish_field(hass, instance_name, 'plate_temperature_celsius', 'Plate Temperature Celsius', kelvin_to_celsius(plate_temperature), 'Airmar: Heater Control', 'C', '130881')
    publish_field(hass, instance_name, 'plate_temperature_fahrenheit', 'Plate Temperature Fahrenheit', kelvin_to_fahrenheit(plate_temperature), 'Airmar: Heater Control', 'F', '130881')

    # air_temperature | Offset: 40, Length: 16, Resolution: 0.01, Field Type: NUMBER
    air_temperature_raw = decode_number((data_raw >> 40) & 0xFFFF, 16)
    air_temperature = air_temperature_raw * 0.01
    publish_field(hass, instance_name, 'air_temperature', 'Air Temperature', air_temperature, 'Airmar: Heater Control', 'K', '130881')
    publish_field(hass, instance_name, 'air_temperature_celsius', 'Air Temperature Celsius', kelvin_to_celsius(air_temperature), 'Airmar: Heater Control', 'C', '130881')
    publish_field(hass, instance_name, 'air_temperature_fahrenheit', 'Air Temperature Fahrenheit', kelvin_to_fahrenheit(air_temperature), 'Airmar: Heater Control', 'F', '130881')

    # dewpoint | Offset: 56, Length: 16, Resolution: 0.01, Field Type: NUMBER
    dewpoint_raw = decode_number((data_raw >> 56) & 0xFFFF, 16)
    dewpoint = dewpoint_raw * 0.01
    publish_field(hass, instance_name, 'dewpoint', 'Dewpoint', dewpoint, 'Airmar: Heater Control', 'K', '130881')
    publish_field(hass, instance_name, 'dewpoint_celsius', 'Dewpoint Celsius', kelvin_to_celsius(dewpoint), 'Airmar: Heater Control', 'C', '130881')
    publish_field(hass, instance_name, 'dewpoint_fahrenheit', 'Dewpoint Fahrenheit', kelvin_to_fahrenheit(dewpoint), 'Airmar: Heater Control', 'F', '130881')

def process_pgn_130944(hass, instance_name, entity_id, data_raw):
    from .sensor import publish_field
    """Process and log data for PGN 130944."""
    # manufacturer_code | Offset: 0, Length: 11, Resolution: 1, Field Type: LOOKUP
    manufacturer_code_raw = (data_raw >> 0) & 0x7FF
    manufacturer_code = manufacturer_code_raw * 1
    publish_field(hass, instance_name, 'manufacturer_code', 'Manufacturer Code', manufacturer_code, 'Airmar: POST', '', '130944')

    # reserved | Offset: 11, Length: 2, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 11) & 0x3
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: POST', '', '130944')

    # industry_code | Offset: 13, Length: 3, Resolution: 1, Field Type: LOOKUP
    industry_code_raw = (data_raw >> 13) & 0x7
    industry_code = industry_code_raw * 1
    publish_field(hass, instance_name, 'industry_code', 'Industry Code', industry_code, 'Airmar: POST', '', '130944')

    # control | Offset: 16, Length: 1, Resolution: 1, Field Type: LOOKUP
    control_raw = (data_raw >> 16) & 0x1
    control = control_raw * 1
    publish_field(hass, instance_name, 'control', 'Control', control, 'Airmar: POST', '', '130944')

    # reserved | Offset: 17, Length: 7, Resolution: 1, Field Type: RESERVED
    reserved_raw = (data_raw >> 17) & 0x7F
    reserved = reserved_raw * 1
    publish_field(hass, instance_name, 'reserved', 'Reserved', reserved, 'Airmar: POST', '', '130944')

    # number_of_id_test_result_pairs_to_follow | Offset: 24, Length: 8, Resolution: 1, Field Type: NUMBER
    number_of_id_test_result_pairs_to_follow_raw = decode_number((data_raw >> 24) & 0xFF, 8)
    number_of_id_test_result_pairs_to_follow = number_of_id_test_result_pairs_to_follow_raw * 1
    publish_field(hass, instance_name, 'number_of_id_test_result_pairs_to_follow', 'Number of ID/test result pairs to follow', number_of_id_test_result_pairs_to_follow, 'Airmar: POST', '', '130944')

    # test_id | Offset: 32, Length: 8, Resolution: 1, Field Type: LOOKUP
    test_id_raw = (data_raw >> 32) & 0xFF
    test_id = test_id_raw * 1
    publish_field(hass, instance_name, 'test_id', 'Test ID', test_id, 'Airmar: POST', '', '130944')

    # test_result | Offset: 40, Length: 8, Resolution: 1, Field Type: NUMBER
    test_result_raw = decode_number((data_raw >> 40) & 0xFF, 8)
    test_result = test_result_raw * 1
    publish_field(hass, instance_name, 'test_result', 'Test result', test_result, 'Airmar: POST', '', '130944')

