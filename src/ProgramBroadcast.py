import PacketBroadcaster
import PacketBuilder

def broadcast():
    
    packet_bytes = PacketBuilder.build_light_get_state_packet()
    
    PacketBroadcaster.broadcast_packet("172.16.10.255", 56700, packet_bytes)
    return

broadcast()