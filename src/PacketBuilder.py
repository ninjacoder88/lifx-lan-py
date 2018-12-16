def numberToBin(n, size):
    binary = bin(n).replace("0b","").zfill(size)
    return binary

def buildPacket(tagged, addressable, source, target, ack, res, sequence, type, payload):
    frame_origin = numberToBin(0, 2)
    frame_tagged = numberToBin(tagged, 1)
    frame_addressable = numberToBin(addressable, 1)
    frame_protocol = numberToBin(1024, 12)
    frame_source = numberToBin(source, 32) #1227133513
    frameAddress_target = numberToBin(target, 64)
    frameAddress_reserved1 = numberToBin(0, 48)
    frameAddress_reserved2 = numberToBin(0, 6)
    frameAddress_ackRequired = numberToBin(ack, 1)
    frameAddress_resRequired = numberToBin(res, 1)
    frameAddress_sequence = numberToBin(sequence, 8)
    protocolHeader_reserved1 = numberToBin(0, 64)
    protocolHeader_type = numberToBin(type, 16)
    protocolHeader_reserved2 = numberToBin(0, 16)
    payload_payload = payload
    
    packetSize = int((288 + len(payload_payload)) / 8)
    frame_size = numberToBin(packetSize, 16)
    
    frame = frame_size + frame_origin + frame_tagged + frame_addressable + frame_protocol + frame_source
    frameAddress = frameAddress_target + frameAddress_reserved1 + frameAddress_reserved2 + frameAddress_ackRequired + frameAddress_resRequired + frameAddress_sequence
    protocolHeader = protocolHeader_reserved1 + protocolHeader_type + protocolHeader_reserved2
    
    binaryPacket = frame + frameAddress + protocolHeader + payload_payload
    
    return binaryPacket

def convertRawPacketToLittleEndian(rawPacket):
    littleEndianPacket = ""
    tempPacket = rawPacket
    
    while(len(tempPacket) > 0):
        firstByte = tempPacket[0:8]
        secondByte = tempPacket[8:16]
        
        littleEndianPacket += secondByte
        littleEndianPacket += firstByte
        
        tempPacket = tempPacket[16:]
        
    return littleEndianPacket

def convertPacketToHexString(packet):
    hexString = ""
    tempPacket = packet
    
    while(len(tempPacket) > 0):
        hexString += hex(int(tempPacket[0:8], 2)).replace("0x", "").zfill(2)
        tempPacket = tempPacket[8:]
        
    return hexString