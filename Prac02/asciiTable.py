__author__ = 'jc444921'
lower = 40
upper = 100
print("Enter a number (" + str(lower) + "-" + str(upper) + "): ")

str= "Enter a number ({}-{}): ".format(lower,upper)
print(str)

print("ASCII  CHAR")
for i in range(lower, upper):
     print("{:5} {:>5}".format(i, chr(i)))


