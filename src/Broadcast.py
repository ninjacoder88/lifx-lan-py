import PacketBuilder
import PacketSender

#1227133513

def buildDeviceEchoRequestPacket(payload):
    fieldDictionary = {"tagged": 1, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 58}
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildDeviceGetServicePacket():
    fieldDictionary = {"tagged": 1, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 2}
    return PacketBuilder.buildPacket(fieldDictionary, "")

def buildGetPacket(type):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": type}
    return PacketBuilder.buildPacket(fieldDictionary, "")

def buildDeviceSetPowerPacket(levelValue):
    #validate between 0 and 100
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 21}
    level = int(float(levelValue) / 100) * 65535)
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildDeviceSetLabelPacket(labelValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 24}
    label = labelValue #32 byte string
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildDeviceSetLocationPacket(locationValue, labelValue, updatedAtValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 49}
    location = locationValue #byte array 16
    label = labelValue #32 byte string
    updatedAt = updatedAtValue #64 bit int
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildDeviceSetGroupPacket(groupValue, labelValue, updatedAtValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 52}
    group = groupValue #byte array 16
    label = labelValue #32 byte string
    updatedAt = updatedAtValue #64 bit int
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildLightSetColorPacket(colorValue, durationValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 102}
    reserved = "00000000" #u8bit-int
    color = colorValue #HSBK
    duration = durationValue #u32-bit int
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildLightSetWaveformPacket(transientValue, colorValue, periodValue, cyclesValue, skewRationValue, waveformValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 103}
    reserved = "00000000" #u8bit-int
    transient = transientValue
    color = colorValue
    period = periodValue
    cycles = cyclesValue
    skewRatio = skewRatioValue
    waveform = waveformValue
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)
    
def buildLightSetWaveformOptionPacket():
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 119}
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildLightSetPowerPacket(levelValue, durationValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 117}
    level = levelValue
    duration = durationValue
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)

def buildLightSetInfraredPacket(brightnessValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 122}
    brightness = brightnessValue
    payload = "" # need to build payload
    return PacketBuilder.buildPacket(fieldDictionary, payload)
    

#packetBytes = buildDeviceGetServicePacket() #DEVICE_GetService
#packetBytes = buildDeviceEchoRequestPacket("00110011001100110011") #DEVICE_EchoRequest (payload byte array; 64 bytes)
#packetBytes = buildGetPacket(12) #DEVICE_GetHostInfo
#packetBytes = buildGetPacket(14) #DEVICE_GetHostFirmware
#packetBytes = buildGetPacket(16) #DEVICE_GetWifiInfo
#packetBytes = buildGetPacket(20) #DEVICE_GetPower
#packetBytes = buildGetPacket(23) #DEVICE_GetLabel
#packetBytes = buildGetPacket(32) #DEVICE_GetVersion
#packetBytes = buildGetPacket(34) #DEVICE_GetInfo
#packetBytes = buildGetPacket(48) #DEVICE_GetLocation
#packetBytes = buildGetPacket(51) #DEVICE_GetGroup
#packetBytes = buildGetPacket(101) #LIGHT_GetState
#packetBytes = buildGetPacket(116) #LIGHT_GetPower
#packetBytes = buildGetPacket(120) #LIGHT_GetInfrared

HOST = "172.16.10.255"
PORT = 56700

PacketSender.broadcastPacket(HOST, PORT, packetBytes)