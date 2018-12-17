def convertBinToInt(binary):
    return int(binary, 2)

def destroyPayload(type, payload):
    #print("destroyPayload")
    #print(payload)
    
    if(payload == ""):
        return ""
    
    if(type == 3):
        print(payload)
        tempPayload = payload + "00000000"
        service = convertBinToInt(tempPayload[0:8])
        port = convertBinToInt(tempPayload[8:40])
        print( {"service": service, "port": port} )
    if(type == 25):
        label = ""
        tempPayload = convertBinaryToLittleEndian(payload)
        while(len(tempPayload) > 0):
            label += chr(convertBinToInt(tempPayload[0:8]))
            tempPayload = tempPayload[8:]
        print( {"label": label} )
    return

def destroyPacket(packet):
    frame_size = convertBinToInt(packet[0:16])
    frame_origin = convertBinToInt(packet[16:18])
    frame_tagged = convertBinToInt(packet[18:19])
    frame_addressable = convertBinToInt(packet[19:20])
    frame_protocol = convertBinToInt(packet[20:32])
    frame_source = convertBinToInt(packet[32:64])
    frameAddress_target = convertBinToInt(packet[64:128])
    frameAddress_reserved1 = convertBinToInt(packet[128:176])
    frameAddress_reserved2 = convertBinToInt(packet[176:182])
    frameAddress_ackRequired = convertBinToInt(packet[182:183])
    frameAddress_resRequired = convertBinToInt(packet[183:184])
    frameAddress_sequence = convertBinToInt(packet[184:192])
    protocolHeader_reserved1 = convertBinToInt(packet[192:256])
    protocolHeader_type = convertBinToInt(packet[256:272])
    protocolHeader_reserved2 = convertBinToInt(packet[272:288])

    payload = destroyPayload(protocolHeader_type, packet[288:])
    
    packet = {"size": frame_size, "origin": frame_origin, "tagged": frame_tagged, "addressable": frame_addressable, "protocol": frame_protocol, "source": frame_source,
              "target": frameAddress_target, "far1": frameAddress_reserved1, "far2": frameAddress_reserved2, "ackReq": frameAddress_ackRequired, "resReq": frameAddress_resRequired,
              "sequence": frameAddress_sequence, "phr1": protocolHeader_reserved1, "type": protocolHeader_type, "phr2": protocolHeader_reserved2}
    
    
    return packet

def convertBinaryToLittleEndian(binaryPacket):
    littleEndianPacket = ""
    tempPacket = binaryPacket
    
    while(len(tempPacket) > 0):
        firstByte = tempPacket[0:8]
        secondByte = tempPacket[8:16]
        
        littleEndianPacket += secondByte
        littleEndianPacket += firstByte
        
        tempPacket = tempPacket[16:]
        
    return littleEndianPacket


def convertLittleEndianToBigEndian(binaryString):
    bigEndianPacket = ""
    
    tempPacket = binaryString
    
    while(len(tempPacket) > 0):
        firstByte = tempPacket[0:8]
        secondByte = tempPacket[8:16]
        
        bigEndianPacket += secondByte
        bigEndianPacket += firstByte
        
        tempPacket = tempPacket[16:]
        
    return bigEndianPacket

def convertHexStringToBinary(hexString):
    packet = ""
    tempString = hexString
    
    while(len(tempString) > 0):
        hexed = "0x" + tempString[0:2]
        hexValue = int(hexed, 16)
        packet += bin(hexValue).replace("0b", "").zfill(8)
        
        tempString = tempString[2:]
        
    return packet

def processData(data):
    #print(data)
    #print("\n")
    
    hexString = data.hex()
    #print(data.hex())
    #print("\n")
    
    binaryString = convertHexStringToBinary(hexString)
    #print(packet)
    #print("\n")
    
    rawPacket = convertLittleEndianToBigEndian(binaryString)
    #print(rawPacket)
    #print("\n")
    
    rawData = destroyPacket(rawPacket)
    print(rawData)
    print("\n")