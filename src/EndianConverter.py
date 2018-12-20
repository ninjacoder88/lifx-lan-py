def convert(binary_string):
    swapped_string = ""
    temp = binary_string
    
    while(len(temp) > 0):
        first_byte = temp[0:8]
        second_byte = temp[8:16]
        
        swapped_string += second_byte
        swapped_string += first_byte
        
        temp = temp[16:]
        
    return swapped_string
