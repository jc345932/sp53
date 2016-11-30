try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (Enter a non zero): "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator (Enter a non zero): "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
"""
1.     When will a ValueError occur? When a non-numeric is entered
2.     When will a ZeroDivisionError occur? When a zero is entered as denominator
3.   Could you change the code to avoid the possibility of a ZeroDivisionError? Make a annoucement for user to suggest them dont take a zero for denominator and numerator.
"""