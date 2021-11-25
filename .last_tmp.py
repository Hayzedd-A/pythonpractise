#binary conversion
def binary_conv(decimal,base):
    import math
    binary = []
    output =[]
    decimal = int(input("enter decimal number"))
    base = int(input("enter conversion base"))
    while decimal != 0:
        binary.append(decimal % base)
        decimal = decimal / base
        decimal = math.floor(decimal)
    #output = binary.astype(int)
    #print(output)[::-1]
    length = len(binary)
    for a in range(length,0,-1):
        output.append(binary[a-1])
    result = "".join(str(n) for n in output)
    result = int(result)
    return result

ten = binary_conv(1,2)
print(ten)