__author__ = 'jc444921'
income=float(input("Income:"))
def tax_return(income):
    if income>16000:
        return (income-16000) * 0.30
print(tax_return(income))