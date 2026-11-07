def ask_int():
    while True:
        try:
            age = int(input("Age: "))
            # print(age+1)
        except ValueError:
            print("Please type a number")
        else:
            print("Next year",age+1)
