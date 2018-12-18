import socket

def broadcastPacket(host, port, packetBytes):
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(packetBytes, (host, port))
        
    return
