import socket

def broadcastPacket(packetBytes):
    HOST = "172.16.10.255"
    PORT = 56700
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(packetBytes, (HOST, PORT))
        
    return