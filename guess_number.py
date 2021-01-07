num = [3, 5, 14, 12, 25, 21, 28, 8, 17]

while True:
    guess = input('Guess a number on the list beween 1 and 30, or press q to quit: ')
    if guess.lower()[0] == 'q':
        print('Quitting...')
        break
    else:
        try:
            guess = int(guess)
        except ValueError:
            print('You need to enter an integer as a guess or q to quit')
    
    if guess in num:
        print("You guessed one!!!!!!")
    else:
        print("Please try again")
