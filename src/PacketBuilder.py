import PacketBuilderBase
import EndianConverter

def buildDeviceGetPacket(type):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": type}
    return PacketBuilderBase.buildPacket(fieldDictionary, "")

def buildDeviceGetServicePacket():
    fieldDictionary = {"tagged": 1, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 2}
    return PacketBuilderBase.buildPacket(fieldDictionary, "")

def buildDeviceSetPowerPacket(source, levelValue):
    #validate between 0 and 100
    fieldDictionary = {"tagged": 0, "source": source, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 21}
    level = int(float(levelValue) / 100 * 65535)
    payload = EndianConverter.convert(bin(level).replace("0b","").zfill(16))
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)

def buildDeviceSetLabelPacket(labelValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 24}
    label = labelValue #32 byte string
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)

def buildDeviceSetLocationPacket(locationValue, labelValue, updatedAtValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 49}
    location = locationValue #byte array 16
    label = labelValue #32 byte string
    updatedAt = updatedAtValue #64 bit int
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)

def buildDeviceSetGroupPacket(groupValue, labelValue, updatedAtValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 52}
    group = groupValue #byte array 16
    label = labelValue #32 byte string
    updatedAt = updatedAtValue #64 bit int
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)

def buildDeviceEchoRequestPacket(payload):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 58}
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)

def buildLightGetPacket(type):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": type}
    return PacketBuilderBase.buildPacket(fieldDictionary, "")

def buildLightSetColorPacket(colorValue, durationValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 102}
    reserved = "00000000" #u8bit-int
    color = colorValue #HSBK
    duration = durationValue #u32-bit int
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)

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
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)
    
def buildLightSetWaveformOptionPacket():
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 119}
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)

def buildLightSetPowerPacket(levelValue, durationValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 117}
    level = levelValue
    duration = durationValue
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)

def buildLightSetInfraredPacket(brightnessValue):
    fieldDictionary = {"tagged": 0, "source": 0, "target": 0, "ack": 0, "res": 0, "sequence": 0, "type": 122}
    brightness = brightnessValue
    payload = "" # need to build payload
    return PacketBuilderBase.buildPacket(fieldDictionary, payload)