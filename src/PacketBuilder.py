import PacketBuilderBase
import EndianConverter

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

def build_device_get_poower_packet():
    return build_device_get_packet(20)

def build_device_set_power_packet(source, level_value):
    #validate 0 or 100
    field_dictionary = {"tagged": 0, "source": source, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 21}
    level = int(float(level_value) / 100 * 65535)
    payload = bin(level).replace("0b","").zfill(16)
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_device_get_label_packet():
    return build_device_get_packet(23)

def build_device_set_label_packet(label_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 24}
    label = label_value #32 byte string
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_device_get_version_packet():
    return build_device_get_packet(32)

def build_device_get_info_packet():
    return build_device_get_packet(34)

def build_device_get_location_packet():
    return build_device_get_packet(48)

def build_device_set_location_packet(location_value, label_value, updated_at_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 49}
    location = location_value #byte array 16
    label = label_value #32 byte string
    updatedAt = updated_at_value #64 bit int
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_device_get_group_packet():
    return build_device_get_packet(51)

def build_device_set_group_packet(group_value, label_value, update_at_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 52}
    group = group_value #byte array 16
    label = label_value #32 byte string
    updatedAt = update_at_value #64 bit int
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_device_echo_request_packet(payload):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 58}
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_light_get_packet(type):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": type}
    return PacketBuilderBase.buildPacket(field_dictionary, "")

def build_light_get_state_packet():
    return build_light_get_packet(101)

def build_light_set_color_packet(color_value, duration_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 102}
    reserved = "00000000" #u8bit-int
    color = color_value #HSBK
    duration = duration_value #u32-bit int
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_ligth_set_waveform_packet(transient_value, color_value, period_value, cycles_value, skew_ration_value, waveform_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 103}
    reserved = "00000000" #u8bit-int
    transient = transient_value
    color = color_value
    period = period_value
    cycles = cycles_value
    skewRatio = skew_ration_value
    waveform = waveform_value
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(field_dictionary, payload)
    
def build_light_get_power_packet():
    return build_light_get_packet(116)

def build_light_set_power_packet(level_value, duration_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 117}
    level = level_value
    duration = duration_value
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_light_set_waveform_optional_packet():
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 119}
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(field_dictionary, payload)

def build_light_get_infrared_packet():
    return build_light_get_packet(120)

def build_light_set_infrared_packet(brightness_value):
    field_dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 122}
    brightness = brightness_value
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(field_dictionary, payload)