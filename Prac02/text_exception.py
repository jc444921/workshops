__author__ = 'jc444921'
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:              # if not a number
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:       # When type in zero for denominator
    print("Cannot divide by zero!")
print("Finished.")

