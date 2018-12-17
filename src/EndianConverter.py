def convert(binaryString):
    swappedString = ""
    temp = binaryString
    
    while(len(temp) > 0):
        firstByte = temp[0:8]
        secondByte = temp[8:16]
        
        swappedString += secondByte
        swappedString += firstByte
        
        temp = temp[16:]
        
    return swappedString
