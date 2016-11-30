"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'

def get_Fah(celsius):
    fahrenheit = celsius * 9 /5 +32
    return fahrenheit
def get_Cel(fahrenheit):
    celsius = 5/9 * (fahrenheit - 32)
    return celsius



def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_Fah(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = get_Cel(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
main()