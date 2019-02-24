import sys
import PacketBroadcaster
import CommandHandler

def run():
    while True:
        user_input = input("Enter a command: ")
        
        split_user_input = user_input.split()
    
        #validate
        
        command = split_user_input[0]
        options = split_user_input[1:]
        
        option_dictionary = {}
        for option in options:
            split_option = option.split(":")
            if len(split_option) == 1:
                option_dictionary[split_option[0]] = ""
            else:
                option_dictionary[split_option[0]] = split_option[1]
        
        packet_bytes = ""
        
        if command == "help":
            CommandHandler.handle_help("")
        elif command == "exit":
            break
        elif command == "device-get-service":
            packet_bytes = CommandHandler.handle_device_get_service(option_dictionary)
        elif command == "device-get-host-info":
            packet_bytes = CommandHandler.handle_device_get_host_info(option_dictionary)
        elif command == "device-get-host-firmware":
            packet_bytes = CommandHandler.handle_device_get_host_firmware(option_dictionary)
        elif command == "device-get-wifi-info":
            packet_bytes = CommandHandler.handle_device_get_wifi_info(option_dictionary)
        elif command == "device-get-wifi-firmware":
            packet_bytes = CommandHandler.handle_device_get_wifi_firmware(option_dictionary)
        elif command == "device-get-power":
            packet_bytes = CommandHandler.handle_device_get_power(option_dictionary)
        elif command == "device-set-power":
            packet_bytes = CommandHandler.handle_device_set_power(option_dictionary)
        elif command == "device-get-label":
            packet_bytes = CommandHandler.handle_device_get_label(option_dictionary)
        elif command == "device-set-label":
            packet_bytes = CommandHandler.handle_device_set_label(option_dictionary)
        elif command == "device-get-version":
            packet_bytes = CommandHandler.handle_device_get_version(option_dictionary)
        elif command == "device-get-info":
            packet_bytes = CommandHandler.handle_device_get_info(option_dictionary)
        elif command == "device-get-location":
            packet_bytes = CommandHandler.handle_device_get_location(option_dictionary)
        elif command == "device-set-location":
            packet_bytes = CommandHandler.handle_device_set_location(option_dictionary)
        elif command == "device-get-group":
            packet_bytes = CommandHandler.handle_device_get_group(option_dictionary)
        elif command == "device-set-group":
            packet_bytes = CommandHandler.handle_device_set_group(option_dictionary)
        elif command == "device-echo-request":
            packet_bytes = CommandHandler.handle_device_echo_request(option_dictionary)
        elif command == "light-get-state":
            packet_bytes = CommandHandler.handle_light_get_state(option_dictionary)
        elif command == "light-set-color":
            packet_bytes = CommandHandler.handle_light_set_color(option_dictionary)
        elif command == "light-set-waveform":
            packet_bytes = CommandHandler.handle_light_set_waveform(option_dictionary)
        elif command == "light-get-power":
            packet_bytes = CommandHandler.handle_light_get_power(option_dictionary)
        elif command == "light-set-power":
            packet_bytes = CommandHandler.handle_light_set_power(option_dictionary)
        elif command == "light-set-waveform-optional":
            packet_bytes = CommandHandler.handle_light_set_waveform_optional(option_dictionary)
        elif command == "light-get-infrared":
            packet_bytes = CommandHandler.handle_light_get_infrared(option_dictionary)
        elif command == "light-set-infrared":
            packet_bytes = CommandHandler.handle_light_set_infrared(option_dictionary)
        else:
            print("invalid command. type help for availble commands")
        
        print();

        if packet_bytes == "":
            continue
        else:
            PacketBroadcaster.broadcast_packet("172.16.10.255", 56700, packet_bytes)
            
run()