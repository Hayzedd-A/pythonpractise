import math

#declaring valuables
add_array = []
result_array = []
carrier = 0
narray1 = []
narray2 = []

# collect user input
binary1 = int(input("enter binary number"))
binary2 = int(input("enter another binary number"))
base = int(input("enter binary base"))

#convert the integers to array 
array1 = [int(x) for x in str(binary1)]
array2 = [int(x) for x in str(binary2)]

#aligning the array and adding zero to empty element to complete the same digits
len1 = len(array1)
len2 = len(array2)
if len1 < len2:
    diff2 = len2 - len1
    for zero in range(0,diff2):
        narray1.append(0)
    for d in range(0,len1):
        narray1.append(array1[d])
    narray2 = array2
    len1 = len2
elif len1 > len2:
    diff1 = len1 - len2
    for zero in range(0,diff1):
        narray2.append(0)
    for d in range(0,len2):
        narray2.append(array2[d])
    narray1 = array1
    len2 = len1
else:
    narray1 = array1
    narray2 = array2
    
#fill zero into the operational array to avoid out of range
for zero in range(0,len1):
    add_array.append(0)
    
#adding the corresponding elements by binary methods 
for a in range(len1-1,-1,-1):
    add_array[a] = narray1[a] + narray2[a] + carrier
    result_array.append((add_array[a] % base))
    carrier = math.floor(add_array[a] / base)
    
#solving the carrier as the result maybe longer than the input
while carrier != 0:
    result_array.append((carrier % base))
    carrier = math.floor(carrier / base)
result_array.reverse()

#convert the array to integer 
result_integer = "".join(str(n) for n in result_array) 

#print out the result
print(result_integer)