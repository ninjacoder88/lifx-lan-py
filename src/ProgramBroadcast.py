import PacketBroadcaster
import PacketBuilder

def broadcast():
    
    #packetBytes = PacketBuilder.buildDeviceEchoRequestPacket("00110011001100110011") #DEVICE_EchoRequest (payload byte array; 64 bytes)
    #packetBytes = PacketBuilder.buildDeviceGetPacket(12) #DEVICE_GetHostInfo
    #packetBytes = PacketBuilder.buildDeviceGetPacket(14) #DEVICE_GetHostFirmware
    #packetBytes = PacketBuilder.buildDeviceGetPacket(16) #DEVICE_GetWifiInfo
    #packetBytes = PacketBuilder.buildDeviceGetPacket(20) #DEVICE_GetPower
    #packetBytes = PacketBuilder.buildDeviceGetPacket(23) #DEVICE_GetLabel
    #packetBytes = PacketBuilder.buildDeviceGetPacket(32) #DEVICE_GetVersion
    #packetBytes = PacketBuilder.buildDeviceGetPacket(34) #DEVICE_GetInfo
    #packetBytes = PacketBuilder.buildDeviceGetPacket(48) #DEVICE_GetLocation
    #packetBytes = PacketBuilder.buildDeviceGetPacket(51) #DEVICE_GetGroup
    #packetBytes = PacketBuilder.buildLightGetPacket(101) #LIGHT_GetState
    #packetBytes = PacketBuilder.buildLightGetPacket(116) #LIGHT_GetPower
    #packetBytes = PacketBuilder.buildLightGetPacket(120) #LIGHT_GetInfrared
    #packetBytes = PacketBuilder.buildDeviceGetServicePacket()
    
    #packetBytes = PacketBuilder.buildDeviceSetPowerPacket(0, 50)
    packetBytes = PacketBuilder.buildDeviceGetServicePacket() #DEVICE_GetService #1227133513
    
    PacketBroadcaster.broadcastPacket("172.16.10.255", 56700, packetBytes)
    return

broadcast()