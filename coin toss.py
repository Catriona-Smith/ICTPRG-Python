# coin toss
import random 
i = 0
heads = 0
tails = 0
while i<10:
    i += 1
    coin = random.randint(1,2)
    if coin == 1:
        print ('head')
        heads += 1
    else:
        print('tails')
        tails += 1
print ('number of heads', heads)
print ('number of tails', tails)