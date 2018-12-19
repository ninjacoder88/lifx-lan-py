import PacketBroadcaster
import PacketBuilder

def broadcast():
    #packetBytes = buildDeviceGetServicePacket() #DEVICE_GetService #1227133513
    #packetBytes = buildDeviceEchoRequestPacket("00110011001100110011") #DEVICE_EchoRequest (payload byte array; 64 bytes)
    #packetBytes = buildGetPacket(12) #DEVICE_GetHostInfo
    #packetBytes = buildGetPacket(14) #DEVICE_GetHostFirmware
    #packetBytes = buildGetPacket(16) #DEVICE_GetWifiInfo
    #packetBytes = buildGetPacket(20) #DEVICE_GetPower
    #packetBytes = buildGetPacket(23) #DEVICE_GetLabel
    #packetBytes = buildGetPacket(32) #DEVICE_GetVersion
    #packetBytes = buildGetPacket(34) #DEVICE_GetInfo
    #packetBytes = buildGetPacket(48) #DEVICE_GetLocation
    #packetBytes = buildGetPacket(51) #DEVICE_GetGroup
    #packetBytes = buildGetPacket(101) #LIGHT_GetState
    #packetBytes = buildGetPacket(116) #LIGHT_GetPower
    #packetBytes = buildGetPacket(120) #LIGHT_GetInfrared
    packetBytes = PacketBuilder.buildDeviceGetServicePacket()
    PacketBroadcaster.broadcastPacket("172.16.10.255", 56700, packetBytes)
    return

broadcast()