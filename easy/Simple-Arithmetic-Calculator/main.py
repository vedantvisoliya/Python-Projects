# Python Calculator

operator = input("Enter a operator [*, /, +. -]: ")
number1 = float(input("Enter number one: "))
number2 = float(input("Enter number two: "))

if (operator == '+'):
    print(f"{number1} + {number2} = {round(number1+number2)}")
elif (operator == '-'):
    print(f"{number1} - {number2} = {round(number1-number2)}")
elif (operator == '/'):
    if (number2 == 0):
        print(f"{number1} / {number2} = infinite")
    else:
        print(f"{number1} / {number2} = {round(number1/number2)}")
elif (operator == '*'):
    print(f"{number1} * {number2} = {round(number1*number2)}")
else:
    print(f"Invalid Operation[{operator}]")