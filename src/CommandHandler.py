import PacketBuilder
import CommandHandlerHelp

def handle_help(command):
    CommandHandlerHelp.handle_help(command)
    return ""

def handle_device_get_service(options):
    if "-help" in options:
        handle_help("device-get-service")
        return ""
    else:
        return PacketBuilder.build_device_get_service_packet()
    
def handle_device_get_host_info(options):
    if "-help" in options:
        handle_help("device-get-host")
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
    if "-help" in options:
        handle_help("device-get-host-firmware")
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
    if "-help" in options:
        handle_help("device-get-wifi-info")
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
    if "-help" in options:
        handle_help("device-get-wifi-firmware")
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
    if "-help" in options:
        handle_help("device-get-power")
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
    if "-help" in options:
        handle_help("device-set-power")
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
    if "-help" in options:
        handle_help("device-get-label")
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
    if "-help" in options:
        handle_help("device-set-label")
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
    if "-help" in options:
        handle_help("device-get-version")
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
    if "-help" in options:
        handle_help("device-get-info")
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
    if "-help" in options:
        handle_help("device-get-location")
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
    print("not yet implemented")
    return ""
    #if "-help" in options:
    #    handle_help("device-set-location")
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
    if "-help" in options:
        handle_help("device-get-group")
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
    print("not yet implemented")
    return ""
    
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
    if "-help" in options:
        handle_help("device-echo-request")
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
    if "-help" in options:
        handle_help("light-get-state")
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
    if "-help" in options:
        handle_help("light-set-color")
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
    print("not yet implemented")
    return ""
    #if "-help" in options:
    #    handle_help("light-set-waveform")
    #    return ""
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #PacketBuilder.build_ligth_set_waveform_packet(target, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value)

def handle_light_get_power(options):
    if "-help" in options:
        handle_help("light-get-power")
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
    if "-help" in options:
        handle_help("light-set-power")
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
    print("not yet implemented")
    return ""
    #if "-help" in options:
    #    handle_help("light-set-waveform-optional")
    #    return ""
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #PacketBuilder.build_light_set_waveform_optional_packet(target, transient_value, hue_value, sat_value, brightness_value, kelvin_value, period_value, cycles_value, skew_ration_value, waveform_value, set_hue_value, set_sat_value, set_brightness_value, set_kelvin_value)build_light_set_power_packet(source, target, level_value, duration_value)

def handle_light_get_infrared(options):
    print("not yet implemented")
    return ""
    #if "-help" in options:
    #    handle_help("light-get-infrared")
    #    return ""
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #PacketBuilder.build_light_get_infrared_packet(target)

def handle_light_set_infrared(options):
    print("not yet implemented")
    return ""
    #if "-help" in options:
    #    handle_help("light-set-infrared")
    #    return ""
    #else:
    #    print("invalid options. use -help to see usage")
    #    return ""
    
    #PacketBuilder.build_light_set_infrared_packet(target, brightness_value)