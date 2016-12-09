__author__ = 'jc444921'
"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
integer = 0
while not finished:
    try:
        integer = int(input("Enter the integer: "))
        finished=True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", integer)

