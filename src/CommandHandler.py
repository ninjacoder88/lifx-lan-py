import PacketBuilder

def handle_help():
    return ""

def handle_device_get_service(options):
    available_options = {
        "-help": "provides help document"
        }

    if "-help" in options:
        print(available_options)
        return ""
    else:
        return PacketBuilder.build_device_get_service_packet()
    
def handle_device_get_host_info(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_host_info_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_host_info_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_get_host_firmware(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_host_firmware_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_host_firmware_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_get_wifi_info(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_wifi_info_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_wifi_info_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_get_wifi_firmware(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_wifi_firmware_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_wifi_firmware_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_get_power(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_power_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_power_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_set_power(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-l:Level": "power level, must be 0 or 1"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    level = -1
    if "-l" in options:
        level = int(options["-l"]) * 65535
    else:
        print("invalid options. -l is required. use -help to see usage")
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_set_power_packet(0, level)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_set_power_packet(target, level)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_get_label(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_label_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_label_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_set_label(options):#need to validate
    available_options = {
        "-help": "provides help document",
        #"-a": "all devices", probably dont support changing all labels to same
        "-t:Target": "target device mac address",
        "-l:Label": "new device text"
        }

    if "-help" in options:
        print(available_options)
        return ""
    
    label = "N/A"
    if "-l" in options:
        label = options["-l"]
    else:
        print("invalid options. -l is required. use -help to see usage")
        return ""
    
    if "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_set_label_packet(target, label)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_get_version(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_version_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_version_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_get_info(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_info_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_info_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_get_location(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_location_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_location_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_set_location(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-l:Label": "new location text" 
        }
    print("not yet implemented")
    
    #if "-help" in options:
    #    print(available_options)
    #    return ""
    
    #if "-a" in options:
    #    return PacketBuilder.build_device_set_location_packet(0)
    #elif "-t" in options:
    #    target = int(options["-t"])
    #    return PacketBuilder.build_device_set_location_packet(target)
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #create guid
    #created updated_at
    #PacketBuilder.build_device_set_location_packet(target, location_value, label_value, updated_at_value)

def handle_device_get_group(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_device_get_group_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_get_group_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_device_set_group(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-l:Label": "new group text"
        }
    print("not yet implemented")
    
    #if "-help" in options:
    #    print(available_options)
    #    return ""
    
    #label = "N/A"
    #if "-l" in options:
    #    label = options["-l"]
    #else:
    #    print("invalid options. -l is required. use -help to see usage")
    #    return ""
    
    #if "-a" in options:
    #    return PacketBuilder.build_device_set_group_packet(0, )
    #elif "-t" in options:
    #    target = int(options["-t"])
    #    return PacketBuilder.build_device_set_group_packet(target)
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #create source
    #PacketBuilder.build_device_set_group_packet(target, group_value, label_value, update_at_value)

def handle_device_echo_request(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    if "-help" in options:
        print(available_options)
        return ""
    
    payload = "101010101010101"
    
    if "-a" in options:
        return PacketBuilder.build_device_echo_request_packet(0, payload)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_device_echo_request_packet(target, payload)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_light_get_state(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }
    print("not yet implemented")
    
    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_light_get_state_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_light_get_state_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_light_set_color(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-h:Hue": "hue (0-360)",
        "-s:Saturation": "saturation (0-100)",
        "-b:Brightness": "brightness (0-100)",
        "-k:Kelvin": "kelvin (2500-9000)"
        }
    #print("not yet implemented")
    
    if "-help" in options:
        print(available_options)
        return ""
    
    hue = -1
    saturation = -1
    brightness = -1
    kelvin = -1
    
    if "-h" in options:
        hue_value = int(options["-h"])
        hue = int(float(hue_value) / 360 * 65535)
    else:
        print("invalid options. -h is required. use -help to see usage")
        return ""
        
    if "-s" in options:
        saturation_value = int(options["-s"])
        saturation = int(float(saturation_value) / 100 * 65535)
    else:
        print("invalid options. -s is required. use -help to see usage")
        return ""
        
    if "-b" in options:
        brightness_value = int(options["-b"])
        brightness = int(float(brightness_value) / 100 * 65535)
    else:
        print("invalid options. -b is required. use -help to see usage")
        return ""
        
    if "-k" in options:
        kelvin = int(options["-k"])
    else:
        print("invalid options. -k is required. use -help to see usage")
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_light_set_color_packet(0, hue, saturation, brightness, kelvin, 0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_light_set_color_packet(target, hue, saturation, brightness, kelvin, 0)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_light_set_waveform(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    #if "-help" in options:
    #    print(available_options)
    #    return ""
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #PacketBuilder.build_ligth_set_waveform_packet(target, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value)

def handle_light_get_power(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address"
        }

    if "-help" in options:
        print(available_options)
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_light_get_power_packet(0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_light_get_power_packet(target)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_light_set_power(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        "-l:Level": "power level, must be 0 or 1"
        }
    print("not yet implemented")
    
    if "-help" in options:
        print(available_options)
        return ""
    
    level = -1
    if "-l" in options:
        level = int(options["-l"]) * 65535
    else:
        print("invalid options. -l is required. use -help to see usage")
        return ""
    
    if "-a" in options:
        return PacketBuilder.build_light_set_power_packet(0, level, 0)
    elif "-t" in options:
        target = int(options["-t"])
        return PacketBuilder.build_light_set_power_packet(target, level, 0)
    else:
        print("invalid options. use -help to see usage")
        return ""

def handle_light_set_waveform_optional(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    #if "-help" in options:
    #    print(available_options)
    #    return ""
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #PacketBuilder.build_light_set_waveform_optional_packet(target, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value, set_hue_value, set_sat_value, set_brightness_value, set_kelvin_value)build_light_set_power_packet(source, target, level_value, duration_value)

def handle_light_get_infrared(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    #if "-help" in options:
    #    print(available_options)
    #    return ""
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #PacketBuilder.build_light_get_infrared_packet(target)

def handle_light_set_infrared(options):
    available_options = {
        "-help": "provides help document",
        "-a": "all devices",
        "-t:Target": "target device mac address",
        }
    print("not yet implemented")
    
    #if "-help" in options:
    #    print(available_options)
    #    return ""
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #PacketBuilder.build_light_set_infrared_packet(target, brightness_value)