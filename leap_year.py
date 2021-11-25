questions = int(input("Enter the number of year you'll like to know"))
years = []
for e in range(questions):
    years.append(int(input("Enter a year sample")))
for each in years:
    if 1000 <= each <= 100000:
        if each % 4 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Sorry!, year is out of range")
