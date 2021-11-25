user_string = str(input("Enter two words separated by a space"))
user_string1 = str(input("Enter two words separated by a space"))
user_array = user_string.split(" ")
user_array1 = user_string1.split(" ")

list1 = user_array[0]
list2 = user_array[1]
for d in range(2):
    length = len(list2) - 1
    found = c = -1
    for a in range(len(list1) - len(list2) + 1):
        c += 1
        while length >= 0:
            if list2[length] == list1[length + c]:
                length -= 1
                found += 1
            else:
                length = len(list2) - 1
                found = -1
                break
    if found == (len(list2) - 1):
        print("Yes")
    else:
        print("No")
    list1 = user_array1[0]
    list2 = user_array1[1]
