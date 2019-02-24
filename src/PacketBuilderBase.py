import EndianConverter

def int_to_bin(integer, bits_to_occupy):
    binary_string = bin(integer).replace("0b","").zfill(bits_to_occupy)
    return binary_string


def build_frame(size, tagged, source):
    frame_size = int_to_bin(size, 16) #size in bytes
    frame_origin = int_to_bin(0, 2)
    frame_tagged = int_to_bin(tagged, 1)
    frame_addressable = int_to_bin(1, 1)
    frame_protocol = int_to_bin(1024, 12)
    frame_source = int_to_bin(source, 32)
    frame = frame_size + frame_origin + frame_tagged + frame_addressable + frame_protocol + frame_source
    return frame


def build_frame_address(target, ack, res, sequence):
    #frame_address_target = int_to_bin(target, 64)
    frame_address_target = int_to_bin(target, 48) + "".zfill(16)
    frame_address_reserved1 = int_to_bin(0, 48)
    frame_address_reserved2 = int_to_bin(0, 6)
    frame_address_ackRequired = int_to_bin(ack, 1)
    frame_address_resRequired = int_to_bin(res, 1)
    frame_address_sequence = int_to_bin(sequence, 8)
    frame_address = frame_address_target + frame_address_reserved1 + frame_address_reserved2 + frame_address_ackRequired + frame_address_resRequired + frame_address_sequence
    return frame_address


def build_protocol_header(type):
    protocol_header_reserved1 = int_to_bin(0, 64)
    protocol_header_type = int_to_bin(type, 16)
    protocol_header_reserved2 = int_to_bin(0, 16)
    protocol_header = protocol_header_reserved1 + protocol_header_type + protocol_header_reserved2
    return protocol_header


def convert_binary_packet_to_hex_string(binary_packet):
    hex_string = ""
    temp_packet = binary_packet
    
    while(len(temp_packet) > 0):
        hex_string += hex(int(temp_packet[0:8], 2)).replace("0x", "").zfill(2)
        temp_packet = temp_packet[8:]
        
    return hex_string


def buildPacket(field_dictionary, payload):
    header_size = 288
    payload_size = len(payload)
    packet_size = int((header_size + payload_size) / 8) #8 bits per byte
    
    tagged = field_dictionary["tagged"]
    source = field_dictionary["source"]
    target = field_dictionary["target"]
    ack = field_dictionary["ack"]
    res = field_dictionary["res"]
    sequence = field_dictionary["sequence"]
    type = field_dictionary["type"]
    
    frame = build_frame(packet_size, tagged, source)
    frame_address = build_frame_address(target, ack, res, sequence)
    protocol_header = build_protocol_header(type)
    
    binary_packet_header = frame + frame_address + protocol_header
    little_endian_packet = EndianConverter.convert(binary_packet_header) + payload #the payload is not always little endian
    hexString = convert_binary_packet_to_hex_string(little_endian_packet)
    packet_bytes = bytes.fromhex(hexString)
    
    return packet_bytes