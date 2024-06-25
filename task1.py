def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (Celsius, Fahrenheit, or Kelvin): ").lower()

    if unit == "celsius":
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
    elif unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} Kelvin.")
    elif unit == "kelvin":
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit.")
    else:
        print("Invalid unit of measurement.")

if __name__ == "__main__":
    main()
