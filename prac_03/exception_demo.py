"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the entered value is not an integer

2. When will a ZeroDivisionError occur?
    When the entered denominator is a zero

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    When zero is entered prompt the user for an new valid value

"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")