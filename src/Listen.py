import socket
import PacketProcessor

def listenForPackets():
    HOST = ''
    PORT = 56700

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        data_buffer = []
        while True:
            data = s.recvfrom(512)[0]
            PacketProcessor.processData(data)
            
    return