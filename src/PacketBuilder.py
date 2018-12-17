def integerToBinary(integer, bitsToOccupy):
    binaryString = bin(integer).replace("0b","").zfill(bitsToOccupy)
    return binaryString


def buildFrame(size, tagged, source):
    frame_size = integerToBinary(size, 16)
    frame_origin = integerToBinary(0, 2)
    frame_tagged = integerToBinary(tagged, 1)
    frame_addressable = integerToBinary(1, 1)
    frame_protocol = integerToBinary(1024, 12)
    frame_source = integerToBinary(source, 32)
    frame = frame_size + frame_origin + frame_tagged + frame_addressable + frame_protocol + frame_source
    return frame


def buildFrameAddress(target, ack, res, sequence):
    frameAddress_target = integerToBinary(target, 64)
    frameAddress_reserved1 = integerToBinary(0, 48)
    frameAddress_reserved2 = integerToBinary(0, 6)
    frameAddress_ackRequired = integerToBinary(ack, 1)
    frameAddress_resRequired = integerToBinary(res, 1)
    frameAddress_sequence = integerToBinary(sequence, 8)
    frameAddress = frameAddress_target + frameAddress_reserved1 + frameAddress_reserved2 + frameAddress_ackRequired + frameAddress_resRequired + frameAddress_sequence
    return frameAddress


def buildProtocolHeader(type):
    protocolHeader_reserved1 = integerToBinary(0, 64)
    protocolHeader_type = integerToBinary(type, 16)
    protocolHeader_reserved2 = integerToBinary(0, 16)
    protocolHeader = protocolHeader_reserved1 + protocolHeader_type + protocolHeader_reserved2
    return protocolHeader


def buildPayload():
    
    return


def convertBinaryPacketToLittleEndian(binaryPacket):
    littleEndianPacket = ""
    tempPacket = binaryPacket
    
    while(len(tempPacket) > 0):
        firstByte = tempPacket[0:8]
        secondByte = tempPacket[8:16]
        
        littleEndianPacket += secondByte
        littleEndianPacket += firstByte
        
        tempPacket = tempPacket[16:]
        
    return littleEndianPacket


def convertBinaryPacketToHexString(binaryPacket):
    hexString = ""
    tempPacket = binaryPacket
    
    while(len(tempPacket) > 0):
        hexString += hex(int(tempPacket[0:8], 2)).replace("0x", "").zfill(2)
        tempPacket = tempPacket[8:]
        
    return hexString


def buildPacket(dictionary, payload):
    headerSize = 288
    payloadSize = len(payload)
    packetSize = int((headerSize + payloadSize) / 8)
    
    tagged = dictionary["tagged"]
    source = dictionary["source"]
    target = dictionary["target"]
    ack = dictionary["ack"]
    res = dictionary["res"]
    sequence = dictionary["sequence"]
    type = dictionary["type"]
    
    frame = buildFrame(packetSize, tagged, source)
    frameAddress = buildFrameAddress(target, ack, res, sequence)
    protocolHeader = buildProtocolHeader(type)
    
    binaryPacket = frame + frameAddress + protocolHeader
    littleEndianPacket = convertBinaryPacketToLittleEndian(binaryPacket) + payload #the payload is not always little endian
    hexString = convertBinaryPacketToHexString(littleEndianPacket)
    packetBytes = bytes.fromhex(hexString)
    
    return packetBytes