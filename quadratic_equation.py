def sqrt(num):
    lim = round(num/2)
    for i in range(1,lim):
        if i * i == num:
            return i
a = int(input("Enter the value of 'A'"))
b = int(input("Enter the value of 'B'"))
c = int(input("Enter the value of 'C'"))
d = b*b - 4*a*c
if d > 0:
    d = sqrt(d)
e = (-b - d)/2*a
f = (-b + d)/2*a
print (e)
print ("or")
print (f)