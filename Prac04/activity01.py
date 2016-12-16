__author__ = 'jc444921'

vowals= ['a','e','i','o','u']

vowal_count=0

name = input('Enter your name: ')

for c in name:
    if c.lower() in vowals:
        vowal_count+=1

#print('has ',vowal_count,'vowals.')

print('Out of {} letters, {} has {} vowals'.format(len(name),name,vowal_count))






