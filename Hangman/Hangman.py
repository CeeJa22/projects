from words import word
import random
import string
    

def hangman():
    r_comp_word = word.upper()
    guesses = set()
    win = False
    w_letters = set(r_comp_word)
    
    exit = '0'
    
    lives = 10
    while lives != 0:
        print('You have used these letters: ', ' '.join(guesses))
        print(f'Your remaining lives = {lives}')
        

        current_word = [x if x in guesses else '-' for x in r_comp_word]
        print('Your word: ', ' '.join(current_word))
        
        guess = str(input('Enter a word or letter: \n').upper())
        if guess in guesses:
            print('\nYou have already guessed that letter. ')
        elif len(guess) == 0:
            guess = str(input('Enter a word or letter: \n').upper())
        elif guess == r_comp_word:
            current_word = [x for x in r_comp_word]
            print(f'You have guessed {r_comp_word} correctly! ')
            win = True
        elif guess in w_letters:
            w_letters.remove(guess)
            guesses.add(guess)
        elif guess == exit:
            print('Quitter!')
            break
        else:
            print('You lose!')
        lives -=1   
                        
hangman()
    

