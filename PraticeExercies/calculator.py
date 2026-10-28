a = float(input("Enter a first number :"))
op = input("Operator (+,=,*,/,^):" )
b = float(input("Enter second number: "))
result = None
if op == '+':
    print(f"result for {a} {op} {b} = {a+b}")

elif op == '-':
    print(f"result for {a} {op} {b} = {a-b}")

elif op == '*':
    print(f"result for {a} {op} {b} = {a*b}")

elif op == '/':
    if b == 0:
        print("Error : division by zero")
    else:
        print(f"result for {a} {op} {b} = {a/b}")
elif op == '^':
    print(f"result for {a} {op} {b} = {a**b}")
    
else:
    print(f"{op} is not Valid , Please Enter valid Operator ")
# print(f"result for {a} {op} {b} = {result}")
