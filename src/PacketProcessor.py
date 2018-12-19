import EndianConverter

def convertBinToInt(binary):
    return int(binary, 2)

def parseDeviceStateService(payload):
    result = {"service": "u8-bit int", "port": "u 2-bit int"} 
    return result

def parseDeviceStateHostInfo(payload):
    result = {"signal": "32-bit float", "tx": "u32-bit int", "rx": "u32-bit int", "reserved": "16-bit int"}
    return result

def parseDeviceStateHostFirmware(payload):
    result = {"build": "u64-bit int", "reserved": "u64-bit int", "version": "u32-bit int"}
    return result

def parseDeviceStateWifiInfo(payload):
    result = {"signal": "32-bit float", "tx": "u32-bit int", "rx": "u32-bit int", "reserved": "16-bit int"}

def parseDeviceStateWifiFirmware(payload):
    result = {"build": "u64-bit int", "reserved": "u64-bit int", "version": "u32-bit int"}
    return result

def parseDeviceStatePower(payload):
    result = {"level": "u16-bit int"}
    return result

def parseDeviceStateLabel(payload):
    label = ""
    tempPayload = convertBinaryToLittleEndian(payload)
    while(len(tempPayload) > 0):
        label += chr(convertBinToInt(tempPayload[0:8]))
        tempPayload = tempPayload[8:]
    result = {"label": label}
    return result

def parseDeviceStateVersion(payload):
    result = {"vendor": "u32-bit int", "product": "u32-bit int", "version": "u32-bit int"}
    return result

def parseDeviceStateInfo(payload):
    result = {"time": "u64-bit int", "uptime": "u64-bit int", "downtime": "u64-bit int"}
    return result

def parseDeviceAcknowledgement(payload):
    result = {"acknowledged": "true"}
    return result

def parseDeviceStateLocation(payload):
    result = {"location": "16 bytes byte array", "label": "32 bytes string", "updatedAt": "u64-bit int"}
    return result
 
def parseDeviceStateGroup(payload):
    result = {"group": "16 bytes byte array", "label": "32 bytes string", "updatedAt": "u64-bit int"}
    return result

def parseDeviceEchoResponse(payload):
    result = {"payload": "64 bytes byte array"}
    return result
              
def parseLightState(payload):
    result = {"color": "HSBK", "reserved": "16-bit int", "power": "u16-bit int", "label": "32 byte string", "reserved2": "u64-bit int"}
    return result

def parseLightStatePower(payload):
    result = {"level": "u16-bit int"}
    return result

def parseLightStateInfrared(payload):
    result = {"brightness": "u16-bit int"}
    return result

def parsePayload(type, payload):
    result = {"": ""}
    if(payload == ""):
        result = {"": ""}
    if(type == 3):
        result = parseDeviceStateService(payload)
    if(type == 13):
        result = parseDeviceStateHostInfo(payload)
    if(type == 15):
        result = parseDeviceStateHostFirmware(payload)
    if(type == 17):
        result = parseDeviceStateWifiInfo(payload)
    if(type == 19):
        result = parseDeviceStateWifiFirmware(payload)
    if(type == 22):
        result = parseDeviceStatePower(payload)
    if(type == 25):
        result = parseDeviceStateLabel(payload)      
    if(type == 33):
        result = parseDeviceStateVersion(payload)
    if(type == 35):
        result = parseDeviceStateInfo(payload)
    if(type == 45):
        result = parseDeviceAcknowledgement(payload)
    if(type == 50):
        result = parseDeviceStateLocation(payload)
    if(type == 52):
        result = parseDeviceStateGroup(payload)
    if(type == 59):
        result = parseDeviceEchoResponse(payload)
    if(type == 107):
        result = parseLightState(payload)
    if(type == 118):
        result = parseLightStatePower(payload)
    if(type == 121):
        result = parseLightStateInfrared(payload)
    #print(result)
    return result

def parsePacket(packet):
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

    payload = parsePayload(protocolHeader_type, packet[288:])
    
    packet = {"size": frame_size, "origin": frame_origin, "tagged": frame_tagged, "addressable": frame_addressable, "protocol": frame_protocol, "source": frame_source,
              "target": frameAddress_target, "far1": frameAddress_reserved1, "far2": frameAddress_reserved2, "ackReq": frameAddress_ackRequired, "resReq": frameAddress_resRequired,
              "sequence": frameAddress_sequence, "phr1": protocolHeader_reserved1, "type": protocolHeader_type, "phr2": protocolHeader_reserved2, "payload": payload}
    
    return packet


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
    hexString = data.hex()
    binaryString = convertHexStringToBinary(hexString)
    rawPacket = EndianConverter.convert(binaryString)
    packetData = parsePacket(rawPacket)
    
    #for k, v in packetData.items():
    #    print(k, v)
    
    print(packetData)
    print("\n")