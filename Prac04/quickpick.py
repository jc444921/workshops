__author__ = 'jc444921'
from  random import randint

num_of_pick = int(input("How many quick picks?"))

pick_of_6_number = []
num = 0

for i in range(0, num_of_pick):
    num = randint(1, 45)
    for j in range(0, 6):
         while num in pick_of_6_number:
             num=randint(1, 45)
         pick_of_6_number.append(num)
    print(sorted(pick_of_6_number))
    pick_of_6_number = []
