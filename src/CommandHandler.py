import PacketBuilder

def handle_help():
    return ""

def handle_device_get_service(options):
    available_options = {
        "-help": "provides help document"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_service_packet()
    return ""
    
def handle_device_get_host_info(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_host_info_packet(target)
    return ""

def handle_device_get_host_firmware(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_host_firmware_packet(target)
    return ""

def handle_device_get_wifi_info(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_wifi_info_packet(target)
    return ""

def handle_device_get_wifi_firmware(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_wifi_firmware_packet(target)
    return ""

def handle_device_get_power(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_power_packet(target)
    return ""

def handle_device_set_power(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-l:Level": "power level, must be 0 or 1"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_set_power_packet(target, level_value)
    return ""

def handle_device_get_label(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_label_packet(target)
    return ""

def handle_device_set_label(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-l:Label": "new device text"
        }
    print("not yet implemented")
    
    #create source
    #PacketBuilder.build_device_set_label_packet(target, label_value)
    return ""

def handle_device_get_version(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_version_packet(target)
    return ""

def handle_device_get_info(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_info_packet(target)
    return ""

def handle_device_get_location(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices"
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_location_packet(target)
    return ""

def handle_device_set_location(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        "-l:Label": "new location text" 
        }
    print("not yet implemented")
    
    #create guid
    #created updated_at
    #PacketBuilder.build_device_set_location_packet(target, location_value, label_value, updated_at_value)
    return ""

def handle_device_get_group(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_get_group_packet(target):
    return ""

def handle_device_set_group(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #create source
    #PacketBuilder.build_device_set_group_packet(target, group_value, label_value, update_at_value)
    return ""

def handle_device_echo_request(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_device_echo_request_packet(payload)
    return ""

def handle_light_get_state(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_light_get_state_packet()
    return ""

def handle_light_set_color(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-h:Hue": "hue (0-65535)",
        "-s:Saturation": "saturation (0-65535)",
        "-b:Brightness": "brightness (0-65535)",
        "-k:Kelvin": "kelvin (2500-9000)"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_light_set_color_packet(target, hue_value, sat_value, brightness_value, kelvin_value, duration_value)
    return ""

def handle_light_set_waveform(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    #PacketBuilder.build_ligth_set_waveform_packet(target, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value)
    return ""

def handle_light_get_power(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_light_get_power_packet(target)
    return ""

def handle_light_set_power(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-l:Level": "power level, must be 0 or 1",
        "-d:Duration": "transition time in milliseconds"
        }
    print("not yet implemented")
    
    #PacketBuilder.build_light_set_power_packet(target, level_value, duration_value)
    return ""

def handle_light_set_waveform_optional(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    #PacketBuilder.build_light_set_waveform_optional_packet(target, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value, set_hue_value, set_sat_value, set_brightness_value, set_kelvin_value)build_light_set_power_packet(source, target, level_value, duration_value)
    return ""

def handle_light_get_infrared(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    #PacketBuilder.build_light_get_infrared_packet(target)
    return ""

def handle_light_set_infrared(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    #PacketBuilder.build_light_set_infrared_packet(target, brightness_value)
    return ""