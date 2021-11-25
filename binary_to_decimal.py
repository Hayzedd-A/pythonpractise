binary = int(input("enter binary number"))
base = int(input("enter the base"))
binary_arr = [int(x) for x in str(binary)]
base_arr = [int(x) for x in str(base)]
# check if the base is correct
for t in binary_arr:
    if t >= base:
        print("The base is not valid")
        exit()
#
result = 0
p = -1
def power (number,power):
    if power == 0:
        return 1
    else:
        multiplier = number
        for n in range(1, power):
            number = number * multiplier
        return number
binary_len = len(binary_arr)
for num in range(binary_len-1, -1, -1):
    p += 1
    number = binary_arr[p] * power(base, num)
    result += number
print(result)
