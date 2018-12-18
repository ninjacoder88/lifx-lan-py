import socket
import PacketProcessor

def receivePackets(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        data_buffer = []
        while True:
            data = s.recvfrom(512)[0]
            PacketProcessor.processData(data)
            
    return
