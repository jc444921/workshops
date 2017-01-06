__author__ = 'jc444921'
"""
CP1404/CP5632 Prac04 Walkthrough Example
Starter code for cumulative total income program
"""

def main():
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()

def main():
    incomes = []
    number_of_month= int(input("How many months? "))

    for month in range(1, number_of_month + 1):
        income = float(input("Enter income for month {:2}: ".format(str(month))))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()