import sys
import PacketBroadcaster
import CommandHandler

def run():
    while True:
        user_input = input("Enter a command: ")
        
        packet_bytes = "";
        
        if user_input == "help":
            CommandHandler.handle_help()
        elif user_input == "exit":
            break
        elif user_input.startswith("device-get-service"):
            packet_bytes = CommandHandler.handle_device_get_service(user_input)
        elif user_input.startswith("device-get-host-info"):
            packet_bytes = CommandHandler.handle_device_get_info(user_input)
        elif user_input.startswith("device-get-host-firmware"):
            packet_bytes = CommandHandler.handle_device_get_host_firmware(user_input)
        elif user_input.startswith("device-get-wifi-info"):
            packet_bytes = CommandHandler.handle_device_get_wifi_info(user_input)
        elif user_input.startswith("device-get-wifi-firmware"):
            packet_bytes = CommandHandler.handle_device_get_wifi_firmware(user_input)
        elif user_input.startswith("device-get-power"):
            packet_bytes = CommandHandler.handle_device_get_power(user_input)
        elif user_input.startswith("device-set-power"):
            packet_bytes = CommandHandler.handle_device_set_power(user_input)
        elif user_input.startswith("device-get-label"):
            packet_bytes = CommandHandler.handle_device_get_label(user_input)
        elif user_input.startswith("device-set-label"):
            packet_bytes = CommandHandler.handle_device_set_label(user_input)
        elif user_input.startswith("device-get-version"):
            packet_bytes = CommandHandler.handle_device_get_version(user_input)
        elif user_input.startswith("device-get-info"):
            packet_bytes = CommandHandler.handle_device_get_info(user_input)
        elif user_input.startswith("device-set-location"):
            packet_bytes = CommandHandler.handle_device_set_location(user_input)
        elif user_input.startswith("device-get-group"):
            packet_bytes = CommandHandler.handle_device_get_group(user_input)
        elif user_input.startswith("device-set-group"):
            packet_bytes = CommandHandler.handle_device_set_group(user_input)
        elif user_input.startswith("device-echo-request"):
            packet_bytes = CommandHandler.handle_device_echo_request(user_input)
        elif user_input.startswith("light-get-state"):
            packet_bytes = CommandHandler.handle_light_get_state(user_input)
        elif user_input.startswith("light-set-color"):
            packet_bytes = CommandHandler.handle_light_set_color(user_input)
        elif user_input.startswith("light-set-waveform"):
            packet_bytes = CommandHandler.handle_light_set_waveform(user_input)
        elif user_input.startswith("light-get-power"):
            packet_bytes = CommandHandler.handle_light_get_power(user_input)
        elif user_input.startswith("light-set-power"):
            packet_bytes = CommandHandler.handle_light_set_power(user_input)
        elif user_input.startswith("light-set-waveform-optional"):
            packet_bytes = CommandHandler.handle_light_set_waveform_optional(user_input)
        elif user_input.startswith("light-get-infrared"):
            packet_bytes = CommandHandler.handle_light_get_infrared(user_input)
        elif user_input.startswith("light-set-infrared"):
            packet_bytes = CommandHandler.handle_light_set_infrared(user_input)
        else:
            print("invalid command. type help for availble commands")
        
        print();

        if packet_bytes == "":
            continue
        else:
            PacketBroadcaster.broadcast_packet("172.16.10.255", 56700, packet_bytes)
            
run()