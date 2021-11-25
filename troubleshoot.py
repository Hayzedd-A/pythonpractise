print("""This is system troubleshoot! "
      Answer 'Yes' or 'No' to the following question""")
condition = input("Has power?")
if condition == "no":
    condition = input("Is plugged in?")
    if condition == "No":
        print("plug it in")
    if condition == "Yes":
        condition = input("Is the switch on?")
        if condition == "No":
            print("Turn switch on.")
        if condition == "Yes":
            condition = input("Fuse OK?")
            if condition == "No":
                print("Check fuse")
            if condition == "Yes":
                print("Seek other help.")
elif condition == "yes":
    print("Seek other help.")
