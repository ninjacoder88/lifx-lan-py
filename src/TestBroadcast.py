import PacketBroadcaster
import PacketBuilder

def broadcast():
    
    #packet_bytes = PacketBuilder.build_light_get_state_packet()
    #packet_bytes = PacketBuilder.build_device_set_power_packet(1001, 127337741231970, 0)
    #packet_bytes = PacketBuilder.build_light_set_color_packet(127337741231970, 23040, 65535, 32766, 2999, 0)
    #packet_bytes = PacketBuilder.build_light_set_power_packet(1001, 127337741231970, 65535, 0)
    packet_bytes = PacketBuilder.build_device_get_host_info_packet();
    
    PacketBroadcaster.broadcast_packet("172.16.10.255", 56700, packet_bytes)
    return

broadcast()