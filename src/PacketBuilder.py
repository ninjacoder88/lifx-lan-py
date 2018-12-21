import PacketBuilderBase
import EndianConverter

def int_to_bin(integer_value, bits_to_occupy):
    binary_string = EndianConverter.convert(bin(integer_value).replace("0b","").zfill(bits_to_occupy))
    return binary_string

def string_to_bin(string_value, bits_to_occupy):
    binary_string = ""
    return binary_string

def float_to_bin(float_value, bits_to_occupy):
    binary_string = ""
    return binary_string

def time_to_bin(time_value, bits_to_occupy):
    binary_string = ""
    return binary_string


def build_device_get_packet(type):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": type}
    return PacketBuilderBase.buildPacket(field_dictionary, "")

def build_device_get_service_packet():
    field_dictionary = {"tagged": 1, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 2}
    return PacketBuilderBase.buildPacket(field_dictionary, "")

def build_device_get_host_info_packet():
    return build_device_get_packet(12)

def build_device_get_host_firmware_packet():
    return build_device_get_packet(14)

def build_device_get_wifi_info_packet():
    return build_device_get_packet(16)

def build_device_get_wifi_firmware_packet():
    return build_device_get_packet(18)

def build_device_get_power_packet():
    return build_device_get_packet(20)

def build_device_set_power_packet(source, level_value):
    #validate 0 or 100
    field_dictionary = {"tagged": 0, "source": source, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 21}
    level = int_to_bin(int(float(level_value) / 100 * 65535), 16)#unsigned 16 bit integer (0 or 65535)
    payload = level
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_device_get_label_packet():
    return build_device_get_packet(23)

def build_device_set_label_packet(source, label_value):
    field_dictionary = {"tagged": 0, "source": source, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 24}
    label = string_to_bin(label_value, 256)#32 byte string
    payload = label
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_device_get_version_packet():
    return build_device_get_packet(32)

def build_device_get_info_packet():
    return build_device_get_packet(34)

def build_device_get_location_packet():
    return build_device_get_packet(48)

def build_device_set_location_packet(source, location_value, label_value, updated_at_value):
    field_dictionary = {"tagged": 0, "source": source, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 49}
    location = location_value #byte array of 16 bytes
    label = string_to_bin(label_value, 256)#32 byte string
    updated_at = time_to_bin(updated_at_value, 64)#unsigned 64 bit integer
    payload = location + label + updated_at
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_device_get_group_packet():
    return build_device_get_packet(51)

def build_device_set_group_packet(source, group_value, label_value, update_at_value):
    field_dictionary = {"tagged": 0, "source": source, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 52}
    group = group_value #byte array of 16 bytes
    label = string_to_bin(label_value, 256)#32 byte string
    updated_at = time_to_bin(update_at_value, 64)#unsigned 64 bit integer
    payload = group + label + updated_at
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_device_echo_request_packet(payload):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 58}
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_light_get_packet(type):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": type}
    return PacketBuilderBase.buildPacket(field_dictionary, "")

def build_light_get_state_packet():
    return build_light_get_packet(101)

def build_light_set_color_packet(hue_value, sat_value, brightness_value, kelvin_value, duration_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 102}
    reserved = "".zfill(8) #unsigned 8 bit integer 
    hue = int_to_bin(hue_value, 16)#unsigned 16 bit integer (0-65535)
    saturation = int_to_bin(sat_value, 16)#unsigned 16 bit integer (0-65535)
    brightness = int_to_bin(brightness_value, 16)#unsigned 16 bit integer (0-65535)
    kelvin = int_to_bin(kelvin_value, 16)#unsigned 16 bit integer (2500-9000)
    duration = int_to_bin(duration_value, 32)#unsigned 32 bit integer (transition in milliseconds)
    payload = reserved + hue + saturation + brightness + kelving + duration
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_ligth_set_waveform_packet(source, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value):
    field_dictionary = {"tagged": 0, "source": source, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 103}
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
    return PacketBuilderBase.buildPacket(field_dictionary, payload)
    
def build_light_get_power_packet():
    return build_light_get_packet(116)

def build_light_set_power_packet(source, level_value, duration_value):
    field_dictionary = {"tagged": 0, "source": source, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 117}
    level = int_to_bin(level_value, 16)#unsigned 16 bit integer (0 or 65535)
    duration = int_to_bin(duration_value, 32)#unsigned 32 bit integer (transition in milliseconds)
    payload = level + duration
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_light_set_waveform_optional_packet(source, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value, set_hue_value, set_sat_value, set_brightness_value, set_kelvin_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 119}
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
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_light_get_infrared_packet():
    return build_light_get_packet(120)

def build_light_set_infrared_packet(brightness_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 122}
    brightness = int_to_bin(brightness_value, 16)#unsigned 16 bit integer
    payload = brightness
    return PacketBuilderBase.buildPacket(field_dictionary, payload)