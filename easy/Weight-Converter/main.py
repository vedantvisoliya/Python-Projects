# Python Weight Converter
weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pound ? (K or L): ").lower()

if (unit == 'k'):
    weight = weight * 2.205
    unit = "Lbs."
elif (unit == 'l'):
    weight = weight / 2.205
    unit = "Kg."
else:
    print("Error: Invalid Unit")

print(f"your weight is {round(weight)} {unit}")