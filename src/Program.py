import PacketBroadcaster
import PacketReceiver

def broadcast():
    PacketBroadast.broadcastPacket("172.16.10.255", 56700, packetBytes)
    return

def receive():
    PacketReceiver.receivePackets('', 56700)
    return

