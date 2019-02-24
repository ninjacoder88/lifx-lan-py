# lifx-lan-py
Python project for controlling lifx lights via LAN

LIFX protocol documentation can be found at: https://lan.developer.lifx.com/docs/introduction

This project exists to demonstrate how to manage LIFX lights with the LAN protocol using Python.

### How To Run
- Install Python 3
- Clone Repository
- Open Shell #1 (to listen for packets)
- python3 ProgramReceive.py
- Open Shell #2 (to send packets)
- python3 Program.py

*Note: At some point only 1 shell will be needed, but for now you have to work with 2

### Available Commands:
- help
- exit
- device-get-service
- device-get-host-info
- device-get-host-firmware
- device-get-wifi-info
- device-get-wifi-firmware
- device-get-power
- device-set-power
- device-get-label
- device-set-label
- device-get-version
- device-get-info
- device-get-location
- device-set-location
- device-get-group
- device-set-group
- device-echo-request
- light-get-state
- light-set-color
- light-set-waveform
- light-get-power
- light-set-power
- light-set-waveform-optional
- light-get-infrared
- light-set-infrared

*Note: All 'device-' and 'light-' commands support -help

### How to Contribute
- Request contributor
- Submit issue
- Clone the repository
- Create branch
- Make changes on branch
- Pull Request
