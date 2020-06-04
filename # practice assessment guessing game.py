# practice assessment guessing game
print ('Guess the number between 0 and 25')
import random
guesslog = []
n = random.randint (0,25)
c = 0
while c < 7:
    c += 1
    guess = int(input ('Enter guess: '))
    guesslog.append (guess)
    if guess == n:
        print ('It is', n)
        print ('You guessed correctly in', c, 'tries')
        print ('Your guess log:', guesslog)
        break
    else:
        while guess != n:
            if c < 7:
                if guess < n:
                    print ("It's greater than that")
                    break
                else:
                    print ("It's less than that")
                    break
            else:
                print ('You Lost! The correct number was', n)
                print('Your guess log:', guesslog)
                break