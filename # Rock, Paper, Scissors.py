# Rock, Paper, Scissors
import random
while True:
    a = input('paper, scissors or rock? ')
    b = random.randint(1,3)
    if b == 1:
        b = 'paper'
        print (b)
    else:
        if b == 2:
            b = 'scissors'
            print (b)
        else:
            if b == 3:
                b = 'rock'
                print (b)
    if a == b:
        print ('tie')
    else: 
        if a == 'paper' and b == 'scissors':
            print ('you lose')
        else:
            if a == 'paper' and b == 'rock':
                print ('you win')
            else:
                if a == 'scissors' and b == 'paper':
                    print ('you win')
                else:
                    if a == 'scissors' and b == 'rock':
                        print ('you lose')
                    else:
                        if a == 'rock' and b == 'paper':
                            print ('you lose')
                        else:
                            if a == 'rock' and b == 'scissors':
                                print ('you win')