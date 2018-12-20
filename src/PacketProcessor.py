import EndianConverter

def conver_bin_to_int(binary):
    return int(binary, 2)

def parse_device_state_service(payload):
    #result = {"service": "u8-bit int", "port": "u32-bit int", "bits": payload}
    result = {"service": conver_bin_to_int(payload[0:8]), "port": conver_bin_to_int(EndianConverter.convert(payload[8:24]))}
    return result

def parse_device_state_host_info(payload):
    result = {"signal": "32-bit float", "tx": "u32-bit int", "rx": "u32-bit int", "reserved": "16-bit int", "bits": payload}
    return result

def parse_device_state_host_firmware(payload):
    result = {"build": "u64-bit int", "reserved": "u64-bit int", "version": "u32-bit int", "bits": payload}
    return result

def parse_device_state_wifi_info(payload):
    result = {"signal": "32-bit float", "tx": "u32-bit int", "rx": "u32-bit int", "reserved": "16-bit int", "bits": payload}

def parse_device_state_wifi_firmware(payload):
    result = {"build": "u64-bit int", "reserved": "u64-bit int", "version": "u32-bit int", "bits": payload}
    return result

def parse_device_set_power(payload):
    level = conver_bin_to_int(payload)
    result = {"level": level}
    return result;

def parse_device_state_power(payload):
    #result = {"level": "u16-bit int", "bits": payload}
    result = {"level": conver_bin_to_int(payload[0:16])}
    return result

def parse_device_state_label(payload):
    label = ""
    tempPayload = payload
    while(len(tempPayload) > 0):
        label += chr(conver_bin_to_int(tempPayload[0:8]))
        tempPayload = tempPayload[8:]
    result = {"label": label}
    return result

def parse_device_state_version(payload):
    result = {"vendor": "u32-bit int", "product": "u32-bit int", "version": "u32-bit int", "bits": payload}
    return result

def parse_device_state_info(payload):
    result = {"time": "u64-bit int", "uptime": "u64-bit int", "downtime": "u64-bit int", "bits": payload}
    return result

def parse_device_acknowledgement(payload):
    result = {"acknowledged": "true"}
    return result

def parse_device_state_location(payload):
    result = {"location": "16 bytes byte array", "label": "32 bytes string", "updatedAt": "u64-bit int", "bits": payload}
    return result
 
def parse_device_state_group(payload):
    result = {"group": "16 bytes byte array", "label": "32 bytes string", "updatedAt": "u64-bit int", "bits": payload}
    return result

def parse_device_echo_response(payload):
    result = {"payload": "64 bytes byte array", "bits": payload}
    return result
              
def parse_light_state(payload):
    result = {"color": "HSBK", "reserved": "16-bit int", "power": "u16-bit int", "label": "32 byte string", "reserved2": "u64-bit int", "bits": payload}
    return result

def parse_light_state_power(payload):
    result = {"level": "u16-bit int", "bits": payload}
    return result

def parse_light_state_infrared(payload):
    result = {"brightness": "u16-bit int", "bits": payload}
    return result

def process_payload(type, payload):
    empty_result = {"": ""}
    if(type == 3):
        return parse_device_state_service(payload)
    if(type == 13):
        return parse_device_state_host_info(payload)
    if(type == 15):
        return parse_device_state_host_firmware(payload)
    if(type == 17):
        return parse_device_state_wifi_info(payload)
    if(type == 19):
        return parse_device_state_wifi_firmware(payload)
    if(type == 21):
        return parse_device_set_power(payload)
    if(type == 22):
        return parse_device_state_power(payload)
    if(type == 24):
        #return parse_device_set_label(payload)
        return empty_result
    if(type == 25):
        return parse_device_state_label(payload)      
    if(type == 33):
        return parse_device_state_version(payload)
    if(type == 35):
        return parse_device_state_info(payload)
    if(type == 45):
        return parse_device_acknowledgement(payload)
    if(type == 49):
        #return parse_device_set_location(payload)
        return empty_result
    if(type == 50):
        return parse_device_state_location(payload)
    if(type == 52):
        #return parse_device_set_group(payload)
        return empty_result
    if(type == 53):
        return parse_device_state_group(payload)
    if(type == 58):
        #return parse_device_echo_request(payload)
        return empty_result
    if(type == 59):
        return parse_device_echo_response(payload)
    if(type == 102):
        #return parse_light_set_color(payload)
        return empty_result
    if(type == 103):
        #return parse_light_set_waveform(payload)
        return empty_result
    if(type == 107):
        return parse_light_state(payload)
    if(type == 117):
        #return parse_light_set_power(payload)
        return empty_result
    if(type == 118):
        return parse_light_state_power(payload)
    if(type == 119):
        #return parse_light_set_waveform_optional(payload)
        return empty_result
    if(type == 121):
        return parse_light_state_infrared(payload)
    if(type == 122):
        #return pase_light_set_infrared(payload)
        return empty_result

    return empty_result


def process_header(header_bits):
    bits = EndianConverter.convert(header_bits)
    
    frame_size = conver_bin_to_int(bits[0:16])
    frame_origin = conver_bin_to_int(bits[16:18])
    frame_tagged = conver_bin_to_int(bits[18:19])
    frame_addressable = conver_bin_to_int(bits[19:20])
    frame_protocol = conver_bin_to_int(bits[20:32])
    frame_source = conver_bin_to_int(bits[32:64])
    frame_address_target = conver_bin_to_int(bits[64:128])
    frame_address_reserved1 = conver_bin_to_int(bits[128:176])
    frame_address_reserved2 = conver_bin_to_int(bits[176:182])
    frame_address_ackRequired = conver_bin_to_int(bits[182:183])
    frame_address_resRequired = conver_bin_to_int(bits[183:184])
    frame_address_sequence = conver_bin_to_int(bits[184:192])
    protocol_header_reserved1 = conver_bin_to_int(bits[192:256])
    protocol_header_type = conver_bin_to_int(bits[256:272])
    protocol_header_reserved2 = conver_bin_to_int(bits[272:288])
    
    target_bits = bits[64:128]
    if(target_bits[-16:] == "0000000000000000"):
        frame_address_target = conver_bin_to_int(target_bits[0:48])
    
    header = {"size": frame_size, "origin": frame_origin, "tagged": frame_tagged, "addressable": frame_addressable, "protocol": frame_protocol, "source": frame_source,
              "target": frame_address_target, "ackReq": frame_address_ackRequired, "resReq": frame_address_resRequired, "sequence": frame_address_sequence, "type": protocol_header_type}
    
    #header = {"size": frame_size, "origin": frame_origin, "tagged": frame_tagged, "addressable": frame_addressable, "protocol": frame_protocol, "source": frame_source,
    #          "target": frame_address_target, "far1": frame_address_reserved1, "far2": frame_address_reserved2, "ackReq": frame_address_ackRequired, "resReq": frame_address_resRequired,
    #          "sequence": frame_address_sequence, "phr1": protocol_header_reserved1, "type": protocol_header_type, "phr2": protocol_header_reserved2}
    
    return header


def convert_hex_string_to_binary(hex_string):
    packet = ""
    temp_string = hex_string
    
    while(len(temp_string) > 0):
        hexed = "0x" + temp_string[0:2]
        hex_value = int(hexed, 16)
        packet += bin(hex_value).replace("0b", "").zfill(8)
        temp_string = temp_string[2:]
        
    return packet


def process_data(data):
    hex_string = data.hex()
    binary_string = convert_hex_string_to_binary(hex_string)
    header = process_header(binary_string[0:288])
    payload = process_payload(header["type"], binary_string[288:])
    
    print(header)
    print(payload)
    print("\n")