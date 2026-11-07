def temp(val,option):
    ans = -1
    if option == "F":
        ans = val * 9 / 5 + 32
    elif option == "C":
        ans = (val - 32) * 5 / 9
    else:
        print("please enter correct option F/C")
    return ans

convert = input("Convert To (F/C) :")
temperature = float(input("Temperature: "))
print(f"{temperature} = {temp(temperature,convert):.1f} {convert}")
