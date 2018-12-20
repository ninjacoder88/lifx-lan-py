import socket

def broadcast_packet(host, port, packet_bytes):
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(packet_bytes, (host, port))
        
    return
