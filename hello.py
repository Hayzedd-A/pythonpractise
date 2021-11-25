#-*-coding:utf8;-*-
#qpy:console
num = int(input("enter a digit"))
fact = num
for n in range(1,num):
    fact = fact * n
print(fact)
