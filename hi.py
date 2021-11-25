num = int(input(""))
string = input("")
if len(string) == num:
    out_string = []
    result = ""
    for a in string:
        out_string.append(a * 3)
    for a in out_string:
        result += str(a)
    print(result)
else:
    print("length of string is not correct")
