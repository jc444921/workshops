__author__ = 'jc444921'
Instruction = "welcome to out progress. \nInput negative number of Item to quit"
print(Instruction)
numofItem = 1
while numofItem > 0:
    numofItem = int(input("Pleaseinput the number of Item: "))
    costPerItem = float(input("The shipping Cost for Each Item: $"))

    totalShipCost = numofItem * costPerItem
    if totalShipCost > 100:
        totalShipCost = totalShipCost * 0.9
    print("The Total Cost for delivering your products is : ", totalShipCost)


cost = float(input("Shipping cost: $ "))
while cost >0:
    if cost > 100:
        discount=cost*0.1
        print("The total shipping cost is : $ ", cost-discount)
    else:
        print("The total shipping cost is : $ ", cost)
    cost = float(input("Shipping cost: $ "))
print("Invalid number of items!")



