num = int(input("enter number"))
fact = []
for n in range(1, num+1):
    if num % n == 0:
        fact.append(n)
for a in fact:
    print(a)
