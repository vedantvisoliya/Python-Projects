# Python Temperature Converter

unit = input("is the temperature in celcius or fahrenheit? (C/F): ").lower()
temperature = float(input("Enter the temperature: "))

if (unit == "c"):
    temperature = (9/5 * temperature) + 32
    print(f"Temperature is {round(temperature)} F")
elif (unit == "f"):
    temperature = (temperature - 32) * (5/9)
    print(f"Temperature is {round(temperature)} C")
else:
    print(f"{unit} is a Invalid Unit")