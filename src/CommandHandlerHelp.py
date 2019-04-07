def handle_help(command):
    available_commands = {
        "device-get-service": {
            "-help": "provides help document"
            },
        "device-get-host-info": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-get-host-firmware": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-get-wifi-info": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-get-wifi-firmware": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-get-power": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-set-power": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            "-l:Level": "power level, must be 0 or 1"
            },
        "device-get-label": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-set-label": {
            "-help": "provides help document",
            #"-a": "all devices", probably dont support changing all labels to same
            "-t:Target": "target device mac address",
            "-l:Label": "new device text"
            },
        "device-get-version": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-get-info": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-get-location": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-set-location": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            "-l:Label": "new location text" 
            },
        "device-get-group": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "device-set-group": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            "-l:Label": "new group text"
            },
        "device-echo-request": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            },
        "light-get-state": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "light-set-color": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            "-h:Hue": "hue (0-360)",
            "-s:Saturation": "saturation (0-100)",
            "-b:Brightness": "brightness (0-100)",
            "-k:Kelvin": "kelvin (2500-9000)"
            },
        "light-set-waveform": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            },
        "light-get-power": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address"
            },
        "light-set-power": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            "-l:Level": "power level, must be 0 or 1"
            },
        "light-set-waveform-optional": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            },
        "light-get-infrared": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            },
        "light-set-infrared": {
            "-help": "provides help document",
            "-a": "all devices",
            "-t:Target": "target device mac address",
            "-b:Brightness": "brightness"
            }
        }
    
    if command == "":
        for key, value in available_commands.items():
            print(key)
            print(value)
            print()
    elif command in available_commands:
        print(available_commands[command])
    else:
        print("command not found")