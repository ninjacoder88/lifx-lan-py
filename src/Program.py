import PacketBuilder
import PacketSender

#1227133513

def buildGetServicePacket():
    dictionary = {"tagged": 1, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 2}
    return PacketBuilder.buildPacket(dictionary, "")

def buildSetPowerPacket():
    dictionary = {"tagged": 0, "source": 0, "target": 8345188618731978752, "ack": 0, "res": 0, "sequence": 0, "type": 21} 
    level = int((float(50) / 100) * 65535) 
    payload = PacketBuilder.integerToBinary(level, 16)
    return PacketBuilder.buildPacket(dictionary, payload)

def buildGetLabelPacket():
    dictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 23}
    return PacketBuilder.buildPacket(dictionary, "")

HOST = "172.16.10.255"
PORT = 56700

#packetBytes = buildGetServicePacket()
#packetBytes = buildSetPowerPacket()
packetBytes = buildGetLabelPacket()
PacketSender.broadcastPacket(HOST, PORT, packetBytes)