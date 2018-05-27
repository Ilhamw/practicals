MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def main():
    global celsius, fahrenheit, choice
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_celcius_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_fahrenheit_to_celcius()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celcius_to_fahrenheit():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32

def convert_fahrenheit_to_celcius():
    global celsius
    celsius = (fahrenheit - 32) * 5.0 / 9

main()