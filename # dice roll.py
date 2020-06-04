# dice roll
n = int(input ('How many times do you want the dice to roll? '))
a = []
c = 0
import random
while c < n:
    c += 1
    d = random.randint (1,6)
    print (d)
    b = input('would you like this number to be counted? (y/n) ')
    if b == 'y':
        a.append (d)
print ('the sum of the numbers is', sum(a))
print ('the numbers counted were', a )