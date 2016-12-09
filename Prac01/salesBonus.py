__author__ = 'jc444921'
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $ "))
if sales < 1000:
    print("salesBonus: $", 0.1 * sales)
else:
    print("salesBonus: $", 0.15 * sales)

sales = float(input("Enter sales: $ "))
if sales < 1000:
    Bonus = 0.1 * sales
    print("Bonus is : ", Bonus)
else:
    Bonus = 0.15 * sales
    print("Bonus is : ", Bonus)

sales = float(input("Enter sales: $ "))
while sales > 0:
    if sales < 1000:
        Bonus = 0.1 * sales
        print("Bonus is : ", Bonus)
    else:
        Bonus = 0.15 * sales
        print("Bonus is : ", Bonus)
    sales = float(input("Enter sales: $ "))