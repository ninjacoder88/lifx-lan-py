import socket
import PacketProcessor

def receive_packets(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        data_buffer = []
        while True:
            data = s.recvfrom(512)[0]
            result = PacketProcessor.process_data(data)
            print(result)
            print("\n")
            
    return
