import EndianConverter
import time

def bin_to_int(bits):
    return int(bits, 2)

def parse_string(bits):
    label = ""
    temp_bits = bits
    while(len(temp_bits) > 0):
        label += chr(bin_to_int(temp_bits[0:8]))
        temp_bits = temp_bits[8:]
    label = label.replace("\x00", "")
    return label

def parse_time(format, bits):
    unix_time_stamp_nanoseconds = parse_int(format, bits)
    epoch_time = int(unix_time_stamp_nanoseconds / 1000000000)
    #time_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))
    return epoch_time

def parse_float(format, bits):
    if(format == "f32"):
        swapped_bits = EndianConverter.convert(bits)
        sign = swapped_bits[0]
        exponent = bin_to_int(swapped_bits[1:9])
        fraction = bin_to_int(swapped_bits[9:32]) / 8388607
        
        result = exponent + fraction
        if(sign == 1):
            result = result * -1
        return result
    return "invalid format"

def parse_int(format, bits):
    if(format == "u8"):
        return bin_to_int(bits)
    if(format == "s8"):
        s = bin_to_int(bits[0:1])
        i = bin_to_int(bits[1:8])
        return i if s == 0 else i * -1
    if(format == "u16"):
        return bin_to_int(EndianConverter.convert(bits))
    if(format == "s16"):
        b = EndianConverter.convert(bits)
        s = bin_to_int(b[0:1])
        i = bin_to_int(b[1:16])
        return i if s == 0 else i * -1
    if(format == "u32"):
        return bin_to_int(EndianConverter.convert(bits))
    if(format == "s32"):
        b = EndianConverter.convert(bits)
        s = bin_to_int(b[0:1])
        i = bin_to_int(b[1:32])
        return i if s == 0 else i * -1
    if(format == "u64"):
        return bin_to_int(EndianConverter.convert(bits))
    return "invalid format"