import random
#Make a guess a number game
MIN = 1
MAX = 100
#Pick a number
correct = random.randint(MIN, MAX)

#Until they guess the number:
attempts = 0
while True:
    #Ask the user to guess a number
    while True:
        guess = input(f'Enter a number between {MIN} and {MAX}: ')
        #Validate input
        try:
            guess = int(guess)
            break
        except ValueError:
            print(f'Cannot convert {guess} to int')
        
    #If too high - print out 'too high'
    if guess > correct:
        print('Too high')
        attempts += 1
    #If too low - print 'too low'
    elif guess < correct:
        print('Too low')
        attempts += 1
    else:
        break
#Print out a nice string
print('Congratulations! You guessed the number!')
print(f'Guess {correct} in {attempts} guess')