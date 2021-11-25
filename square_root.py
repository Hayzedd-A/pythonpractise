while True:
    def sqrt(num):
        for i in range(1,num):
            if i * i == num:
                return i
                break
    root = int(input("enter root")) 
    print(sqrt(root))