import PacketBuilderBase
import EndianConverter

#####COMMON FUNCTIONS#####
def int_to_bin(integer_value, bits_to_occupy):
    binary_string = EndianConverter.convert(bin(integer_value).replace("0b","").zfill(bits_to_occupy))
    return binary_string

def string_to_bin(string_value, bits_to_occupy):
    binary_string = "".join(format(ord(x), 'b') for x in string_value)
    return binary_string

def float_to_bin(float_value, bits_to_occupy):
    binary_string = ""
    return binary_string

def time_to_bin(time_value, bits_to_occupy):
    binary_string = ""
    return binary_string

def build_standard_get_packet(target, type, payload):
    field_dictionary = {"tagged": 0, "source": 0, "target": target, "ack": 0, "res": 1, "sequence": 0, "type": type}
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

#####DEVICE MESSAGES#####
def build_device_get_service_packet():
    field_dictionary = {"tagged": 1, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 2}
    return PacketBuilderBase.buildPacket(field_dictionary, "")

def build_device_get_host_info_packet(target):
    return build_standard_get_packet(target, 12, "")

def build_device_get_host_firmware_packet(target):
    return build_standard_get_packet(target, 14, "")

def build_device_get_wifi_info_packet(target):
    return build_standard_get_packet(target, 16, "")

def build_device_get_wifi_firmware_packet(target):
    return build_standard_get_packet(target, 18, "")

def build_device_get_power_packet(target):
    return build_standard_get_packet(target, 20, "")

def build_device_set_power_packet(target, level_value):
    #validate 0 or 65535
    level = int_to_bin(level_value, 16)#unsigned 16 bit integer (0 or 65535)
    payload = level
    return build_standard_get_packet(target, 21, payload)

def build_device_get_label_packet(target):
    return build_standard_get_packet(target, 23, "")

def build_device_set_label_packet(target, label_value):
    #validate not empty
    label = string_to_bin(label_value, 256)#32 byte string
    payload = label
    return build_standard_get_packet(target, 24, payload)

def build_device_get_version_packet(target):
    return build_standard_get_packet(target, 32, "")

def build_device_get_info_packet(target):
    return build_standard_get_packet(target, 34, "")

def build_device_get_location_packet(target):
    return build_standard_get_packet(target, 48, "")

def build_device_set_location_packet(target, location_value, label_value, updated_at_value):
    #validate
    location = location_value #byte array of 16 bytes
    label = string_to_bin(label_value, 256)#32 byte string
    updated_at = time_to_bin(updated_at_value, 64)#unsigned 64 bit integer
    payload = location + label + updated_at
    return build_standard_get_packet(target, 49, payload)

def build_device_get_group_packet(target):
    return build_device_get_packet(target, 51, "")

def build_device_set_group_packet(target, group_value, label_value, update_at_value):
    #validate
    group = group_value #byte array of 16 bytes
    label = string_to_bin(label_value, 256)#32 byte string
    updated_at = time_to_bin(update_at_value, 64)#unsigned 64 bit integer
    payload = group + label + updated_at
    return build_standard_get_packet(target, 52, payload)

def build_device_echo_request_packet(target, payload):
    return build_standard_get_packet(target, 58, payload)

#####LIGHT MESSAGES#####
def build_light_get_state_packet(target):
    return build_standard_get_packet(target, 101, "")

def build_light_set_color_packet(target, hue_value, sat_value, brightness_value, kelvin_value, duration_value):
    #int(float(level_value) / 100 * 65535)
    reserved = "".zfill(8) #unsigned 8 bit integer 
    hue = int_to_bin(hue_value, 16)#unsigned 16 bit integer (0-65535)
    saturation = int_to_bin(sat_value, 16)#unsigned 16 bit integer (0-65535)
    brightness = int_to_bin(brightness_value, 16)#unsigned 16 bit integer (0-65535)
    kelvin = int_to_bin(kelvin_value, 16)#unsigned 16 bit integer (2500-9000)
    duration = int_to_bin(duration_value, 32)#unsigned 32 bit integer (transition in milliseconds)
    payload = reserved + hue + saturation + brightness + kelvin + duration
    return build_standard_get_packet(target, 102, payload)

def build_ligth_set_waveform_packet(target, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value):
    #int(float(level_value) / 100 * 65535)
    reserved = "".zfill(8)#unsigned 8 bit integer
    transient = transient_value#8 bit integer (0 or 1)
    hue = int_to_bin(hue_value, 16)#unsigned 16 bit integer (0-65535)
    saturation = int_to_bin(sat_value, 16)#unsigned 16 bit integer (0-65535)
    brightness = int_to_bin(brightness_value, 16)#unsigned 16 bit integer (0-65535)
    kelvin = int_to_bin(kelvin_value, 16)#unsigned 16 bit integer (2500-9000)
    period = period_value#unsigned 32 bit integer (cycle duration in milliseconds)
    cycles = cycles_value#32 bit float (number of cycles)
    skew_ratio = skew_ration_value#16 bit integer
    waveform = waveform_value#unsinged 8 bit integer
    payload = reserved + transient + hue + saturation + brightness + kelvin + period + cycles + skew_ratio + waveform
    return build_standard_get_packet(target, 103, payload)
    
def build_light_get_power_packet(target):
    return build_standard_get_packet(target, 116, "")

def build_light_set_power_packet(target, level_value, duration_value):
    level = int_to_bin(level_value * 65535, 16)#unsigned 16 bit integer (0 or 65535)
    duration = int_to_bin(duration_value, 32)#unsigned 32 bit integer (transition in milliseconds)
    payload = level + duration
    return build_standard_get_packet(taget, 117, payload)

def build_light_set_waveform_optional_packet(target, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value, set_hue_value, set_sat_value, set_brightness_value, set_kelvin_value):
    #int(float(level_value) / 100 * 65535)
    reserved = "".zfill(8)#unsigned 8 bit integer
    transient = transient_value#8 bit integer (0 or 1)
    hue = int_to_bin(hue_value, 16)#unsigned 16 bit integer (0-65535)
    saturation = int_to_bin(sat_value, 16)#unsigned 16 bit integer (0-65535)
    brightness = int_to_bin(brightness_value, 16)#unsigned 16 bit integer (0-65535)
    kelvin = int_to_bin(kelvin_value, 16)#unsigned 16 bit integer (2500-9000)
    period = period_value#unsigned 32 bit integer (cycle duration in milliseconds)
    cycles = cycles_value#32 bit float (number of cycles)
    skew_ratio = skew_ration_value#16 bit integer
    waveform = waveform_value#unsinged 8 bit integer
    set_hue = set_hue_value#8 bit integer (0 or 1)
    set_saturation = set_sat_value#8 bit integer (0 or 1)
    set_brightness = set_brightness_value#8 bit integer (0 or 1)
    set_kelvin = set_kelvin_value#8 bit integer (0 or 1)
    payload = reserved + transient + hue + saturation + brightness + kelvin + period + cycles + skew_ratio + waveform + set_hue + set_saturation + set_brightness + set_kelvin
    return build_standard_get_packet(target, 119, payload)

def build_light_get_infrared_packet(target):
    return build_standard_get_packet(target, 120, "")

def build_light_set_infrared_packet(target, brightness_value):
    #int(float(level_value) / 100 * 65535)
    brightness = int_to_bin(brightness_value, 16)#unsigned 16 bit integer
    payload = brightness
    return build_standard_get_packet(target, 122, payload)