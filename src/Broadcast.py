import PacketBuilder
import PacketSender

#1227133513

def buildEchoRequestPacket(payload):
    fieldDictionary = {"tagged": 1, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 58}
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildGetServicePacket(type):
    fieldDictionary = {"tagged": 1, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 2}
    return PacketBuilder.buildPacket(fieldDictionary, "")

def buildGetPacket(type):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": type}
    return PacketBuilder.buildPacket(fieldDictionary, "")


#packetBytes = buildGetServicePacket(2) #DEVICE_GetService
#packetBytes = buildEchoRequestPacket("00110011001100110011") #DEVICE_EchoRequest (payload byte array; 64 bytes)
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

HOST = "172.16.10.255"
PORT = 56700

PacketSender.broadcastPacket(HOST, PORT, packetBytes)