import PacketBuilder
import PacketSender

def buildGetServicePacket():
    return PacketBuilder.buildPacket(1, 1, 0, 0, 0, 0, 0, 2, "")

rawPacket = buildGetServicePacket()
littleEndianPacket = PacketBuilder.convertRawPacketToLittleEndian(rawPacket)
hexString = PacketBuilder.convertPacketToHexString(littleEndianPacket)
packetBytes = bytes.fromhex(hexString)
PacketSender.broadcastPacket(packetBytes)