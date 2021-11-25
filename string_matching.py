user_string = str(input("Enter two words separated by a space"))
user_array = user_string.split(" ")
list1 = user_array[0]
list2 = user_array[1]
c = -1
length1 = len(list1)
length2 = len(list2)
for a in list1:
    c += 1
    b = 0
    #print("for loop")
    if list2[b] == a:
        found = 1
        print(a)
        if (length1 - (c + 1)) >= length2:
            if found >= 1:
                while length2 > 1:
                    length2 -= 1
                    b += 1
                    c += 1
                    print("while loop")
                    if list2[b] == list1[c]:
                        found += 1
                        print(list2[b])
                    else:
                        found = 0
                        print("break")
                        break
        print(b, found)
if found == len(list2):
    print("Yes")
else:
    print("No")
