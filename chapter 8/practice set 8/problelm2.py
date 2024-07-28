# Write a python program using function to convert Celsius to Fahrenheit.


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

C = float(input("Enter Temperature in Celsius: "))
print(f"Fahrenheit: {round(celsius_to_fahrenheit(C), 2)} °F")
