# python compound interest calculator

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if (principal < 0):
        print("Principal amount can't be less than zero.")
        continue
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if (rate < 0):
        print("Interest Rate can't be less than zero.")
        continue
    else:
        break

while True:
    time = float(input("Enter the time: "))
    if (time < 0):
        print("Time can't be less than zero.")
        continue
    else:
        break

amount = principal * pow((1+(rate/100)), time)

print(f"Amount after {time} year's is ${amount: .2f}")