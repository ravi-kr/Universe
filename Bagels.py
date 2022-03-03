# Credits: inventwithpython.com
"""
Bagels, by Ravi Kumar ravikumar483@gmail.com
A deductive logic game where you must guess a number based on Clues.
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, A deductive logic game.
          By Ravi Kumar ravikumar483@gmail.com
          
          I am thinking of a {}-digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say:       That Means:
          Pico              One digit is correct but in the wrong position.
          Fermi             One digit is correct but in the right position.
          Bagels            No digit is correct.
          
          For example, if the secret number was 248 and your guess was 843, the 
          clues would be Fermi Pico.'''.format(NUM_DIGITS))
          
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess#{}: '.format(numGuesses))
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            
            numGuesses += 1
            
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))
                
        print('Do you want to play again? (yes or no)')
        
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
    
def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and a secret number pair."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
            
        elif guess[i] in secretNum:
            clues.append('Pico')
            
    if len(clues) == 0:
        return 'Bagels'
    
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()    
    
