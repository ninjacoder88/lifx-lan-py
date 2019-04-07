import EndianConverter
import BitParser
    
def parse_device_state_service(payload):
    service = BitParser.parse_int("u8", payload[0:8])
    port = BitParser.parse_int("u32", payload[8:24])
    return {"service": service, "port": port}

def parse_device_state_host_info(payload):
    signal = BitParser.parse_float("f32", payload[0:32])
    tx = BitParser.parse_int("u32", payload[32:64])
    rx = BitParser.parse_int("u32", payload[64:96])
    reserved = BitParser.parse_int("s16", payload[96:112])
    return {"signal": signal, "tx": tx, "rx": rx}

def parse_device_state_host_firmware(payload):
    build = BitParser.parse_int("u64", payload[0:64])
    reserved = BitParser.parse_int("u64", payload[64:128])
    version = BitParser.parse_int("u32", payload[128:160])
    return {"build": build, "version": version}

def parse_device_state_wifi_info(payload):
    signal = BitParser.parse_float("f32", payload[0:32])
    tx = BitParser.parse_int("u32", payload[32:64])
    rx = BitParser.parse_int("u32", payload[64:96])
    reserved = BitParser.parse_int("s16", payload[96:112])
    return {"signal": signal, "tx": tx, "rx": rx}

def parse_device_state_wifi_firmware(payload):
    build = BitParser.parse_int("u64", payload[0:64])
    reserved = BitParser.parse_int("u64", payload[64:128])
    version = BitParser.parse_int("u32", payload[128:160])
    return {"build": build, "version": version}

def parse_device_set_power(payload):
    level = BitParser.parse_int("u16", payload[0:16])
    return {"level": level}

def parse_device_state_power(payload):
    level = BitParser.parse_int("u16", payload[0:16])
    return {"level": level}

def parse_device_set_label(payload):
    label = BitParser.parse_string(payload[0:256])#32 byte string
    return {"label": label}

def parse_device_state_label(payload):
    label = BitParser.parse_string(payload)#32 byte string
    return {"label": label}

def parse_device_state_version(payload):
    vendor = BitParser.parse_int("u32", payload[0:32])
    product = BitParser.parse_int("u32", payload[32:64])
    version = BitParser.parse_int("u32", payload[64:96])
    return {"vendor": vendor, "product": product, "version": version}

def parse_device_state_info(payload):
    #need to figure out lifx time
    time = BitParser.parse_time("u64", payload[0:64])
    uptime = BitParser.parse_int("u64", payload[64:128])
    downtime = BitParser.parse_int("u64", payload[128:196])
    return {"time": time, "uptime": uptime, "downtime": downtime}

def parse_device_acknowledgement(payload):
    #need to investigate if a payload exists
    return {"acknowledged": "true"}

def parse_device_set_location(payload):
    location = payload[0:128]#byte array of 16 bytes (guid)
    label = BitParser.parse_string(payload[128:384])#32 byte string
    updated_at = BitParser.parse_time("u64", payload[384:448])
    return {"location": "GUID", "label": label, "updatedAt": updated_at}

def parse_device_state_location(payload):
    #need to parse byte array
    location = payload[0:128]#byte array of 16 bytes (guid)
    label = BitParser.parse_string(payload[128:384])#32 byte string
    updated_at = BitParser.parse_time("u64", payload[384:448])
    return {"location": "GUID", "label": label, "updatedAt": updated_at}

def parse_device_set_group(payload):
    #need to parse byte array
    group = payload[0:128]#byte array of 16 bytes (guid)
    label = BitParser.parse_string(payload[128:384])#32 byte string
    updated_at = BitParser.parse_time("u64", payload[384:448])
    return {"group": "GUID", "label": label, "updatedAt": updated_at}
 
def parse_device_state_group(payload):
    #need to parse byte array
    group = payload[0:128]#byte array of 16 bytes (guid)
    label = BitParser.parse_string(payload[128:384])#32 byte string
    updated_at = BitParser.parse_time("u64", payload[384:448])
    return {"group": "GUID", "label": label, "updatedAt": updated_at}

def parse_device_echo_request(payload):
    payload = payload[0:512]#byte array of 64 bytes
    return {"payload": "64 bytes byte array"}

def parse_device_echo_response(payload):
    payload = payload[0:512]#byte array of 64 bytes
    return {"payload": "64 bytes byte array"}


def parse_light_set_color(payload):
    reserved = BitParser.parse_int("u8", payload[0:8])
    hue = BitParser.parse_int("u16", payload[8:24])
    saturation = BitParser.parse_int("u16", payload[24:40])
    brightness = BitParser.parse_int("u16", payload[40:56])
    kelvin = BitParser.parse_int("u16", payload[56:72])
    duration = BitParser.parse_int("u32", payload[72:104])
    return {"hue": hue, "saturation": saturation, "brightness": brightness, "kelvin": kelvin, "duration": duration}

def parse_light_set_waveform(payload):
    reserved = BitParser.parse_int("u8", payload[0:8])
    transient = BitParser.parse_int("s8", payload[8:16])
    hue = BitParser.parse_int("u16", payload[16:32])
    saturation = BitParser.parse_int("u16", payload[32:48])
    brightness = BitParser.parse_int("u16", payload[48:64])
    kelvin = BitParser.parse_int("u16", payload[64:80])
    period = BitParser.parse_int("u32", payload[80:112])
    cycles = BitParser.parse_float("f32", payload[112:144])
    skew_ratio = BitParser.parse_int("s16", payload[144:160])
    waveform = BitParser.parse_int("u8", payload[160:168])
    return {"transient": transient, "hue": hue, "saturation": saturation, "brightness": brightness, "kelvin": kelvin, "period": period, "cycles": cycles, "skew_ratio": skew_ratio, "waveform": waveform}
              
def parse_light_state(payload):
    hue = BitParser.parse_int("u16", payload[0:16])
    saturation = BitParser.parse_int("u16", payload[16:32])
    brightness = BitParser.parse_int("u16", payload[32:48])
    kelvin = BitParser.parse_int("u16", payload[48:64])
    reserved1 = BitParser.parse_int("s16", payload[64:80])
    power = BitParser.parse_int("u16", payload[80:96])
    label = BitParser.parse_string(payload[96:352])#32 byte string
    reserved2 = BitParser.parse_int("u64", payload[352:416])
    return {"color": {"hue": hue, "saturation": saturation, "brightness": brightness, "kelvin": kelvin}, "power": power, "label": label}

def parse_light_set_power(payload):
    level = BitParser.parse_int("u16", payload[0:16])
    duration = BitParser.parse_int("u32", payload[16:48])
    return {"level": level, "duration": duration}

def parse_light_state_power(payload):
    level = BitParser.parse_int("u16", payload[0:16])
    return {"level": level}

def parse_light_set_waveform_optional(payload):
    reserved = BitParser.parse_int("u8", payload[0:8])
    transient = BitParser.parse_int("s8", payload[8:16])
    hue = BitParser.parse_int("u16", payload[16:32])
    saturation = BitParser.parse_int("u16", payload[32:48])
    brightness = BitParser.parse_int("u16", payload[48:64])
    kelvin = BitParser.parse_int("u16", payload[64:80])
    period = BitParser.parse_int("u32", payload[80:112])
    cycles = BitParser.parse_float("f32", payload[112:144])
    skew_ratio = BitParser.parse_int("s16", payload[144:160])
    waveform = BitParser.parse_int("u8", payload[160:168])
    set_hue = BitParser.parse_int("s8", payload[168:176])
    set_saturation = BitParser.parse_int("s8", payload[176:184])
    set_brightness = BitParser.parse_int("s8", payload[184:192])
    set_kelvin = BitParser.parse_int("s8", payload[192:200])
    return {"transient": transient, "hue": hue, "saturation": saturation, "brightness": brightness, "kelvin": kelvin, "period": period, "cycles": cycles, "skew_ratio": skew_ratio, "waveform": waveform, "set_hue": set_hue, "set_saturation": set_saturation, "set_brightness": set_brightness, "set_kelvin": set_kelvin}

def parse_light_state_infrared(payload):
    brightness = BitParser.parse_int("u16", payload[0:16])
    return {"brightness": brightness}

def parse_light_set_infrared(payload):
    brightness = BitParser.parse_int("u16", payload[0:16])
    return {"brightness": brightness}


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
        return parse_device_set_label(payload)
    if(type == 25):
        return parse_device_state_label(payload)      
    if(type == 33):
        return parse_device_state_version(payload)
    if(type == 35):
        return parse_device_state_info(payload)
    if(type == 45):
        return parse_device_acknowledgement(payload)
    if(type == 49):
        return parse_device_set_location(payload)
    if(type == 50):
        return parse_device_state_location(payload)
    if(type == 52):
        return parse_device_set_group(payload)
    if(type == 53):
        return parse_device_state_group(payload)
    if(type == 58):
        return parse_device_echo_request(payload)
    if(type == 59):
        return parse_device_echo_response(payload)
    if(type == 102):
        return parse_light_set_color(payload)
    if(type == 103):
        return parse_light_set_waveform(payload)
    if(type == 107):
        return parse_light_state(payload)
    if(type == 117):
        return parse_light_set_power(payload)
    if(type == 118):
        return parse_light_state_power(payload)
    if(type == 119):
        return parse_light_set_waveform_optional(payload)
    if(type == 121):
        return parse_light_state_infrared(payload)
    if(type == 122):
        return parse_light_set_infrared(payload)
    return empty_result


def process_header(header_bits):
    bits = EndianConverter.convert(header_bits)

    frame_size = BitParser.bin_to_int(bits[0:16])
    frame_origin = BitParser.bin_to_int(bits[16:18])
    frame_tagged = BitParser.bin_to_int(bits[18:19])
    frame_addressable = BitParser.bin_to_int(bits[19:20])
    frame_protocol = BitParser.bin_to_int(bits[20:32])
    frame_source = BitParser.bin_to_int(bits[32:64])
    frame_address_target = BitParser.bin_to_int(bits[64:128])
    frame_address_reserved1 = BitParser.bin_to_int(bits[128:176])
    frame_address_reserved2 = BitParser.bin_to_int(bits[176:182])
    frame_address_ackRequired = BitParser.bin_to_int(bits[182:183])
    frame_address_resRequired = BitParser.bin_to_int(bits[183:184])
    frame_address_sequence = BitParser.bin_to_int(bits[184:192])
    protocol_header_reserved1 = BitParser.bin_to_int(bits[192:256])
    protocol_header_type = BitParser.bin_to_int(bits[256:272])
    protocol_header_reserved2 = BitParser.bin_to_int(bits[272:288])
    
    target_bits = bits[64:128]
    if(target_bits[-16:] == "".zfill(16)):
        frame_address_target = BitParser.bin_to_int(target_bits[0:48])
        #frame_address_target = BitParser.parse_string(target_bits[0:48])
    
    return {"size": frame_size, "origin": frame_origin, "tagged": frame_tagged, "addressable": frame_addressable,
              "protocol": frame_protocol, "source": frame_source, "target": frame_address_target, "ackReq": frame_address_ackRequired,
              "resReq": frame_address_resRequired, "sequence": frame_address_sequence, "type": protocol_header_type}


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
    
    return {"header": header, "payload": payload}