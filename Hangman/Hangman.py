from words import word
import random
import string

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


print(logo)   

def hangman():
    r_comp_word = word.upper()
    guesses = set()
    win = False
    w_letters = set(r_comp_word)
    
    stages = ['''
            +---+
            |   |
            O   |
            /|\  |
            / \  |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
            /|\  |
            /    |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
            /|\  |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
            /|   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            ''', '''
            +---+
            |   |
                |
                |
                |
                |
            =========
            ''']
    
    
    print('You can quit by typing - 0')
    
    exit = '0'
    
    stage_num = -1
    lives = 6
    while lives != 0:
        print('You have used these letters: ', ' '.join(guesses))
        print(f'Your remaining lives = {lives}')
        

        current_word = [x if x in guesses else '-' for x in r_comp_word]
        print('Your word: ', ' '.join(current_word))
        
        guess = str(input('Enter a word or letter: \n').upper())
        if guess in guesses:
            print(stages[stage_num])
            print('\nYou have already guessed that letter. ')
        elif guess == exit:
            print(stages[-7])
            print('Quitter!')
            break
        elif len(guess) == 0:
            guess = str(input('Enter a word or letter: \n').upper())
        elif guess == r_comp_word:
            current_word = [x for x in r_comp_word]
            print(f'You have guessed {r_comp_word} correctly! ')
            win = True
        elif guess in w_letters:
            print(stages[stage_num])
            w_letters.remove(guess)
            guesses.add(guess)    
        elif guess != r_comp_word:
            stage_num -=1
            lives -= 1
            print(stages[stage_num])
            guesses.add(guess)
            if lives == 0:
                print(stages[stage_num])
                print(f'You lose, the word was {r_comp_word}')
        
        
           
                        
hangman()
    

