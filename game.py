import random

import colorama
from termcolor import colored

GUESS = 'Guess #{}: '
PROMPT = 'Pick a number between 1 and {}'
LESS = 'My number is LESS THAN (<) {}'
GREATER = 'My number is GREATER THAN (>) {}'

def difficulty_output():
    print('Guessing Game')
    print('Choose your difficulty')
    print('1 - Easy (1-10)')
    print('2 - Less Easy (1-100)')
    print('3 - Crazy Town (1-1000)')


def get_choice():
    n = 0
    while not n:
        try:
            difficulty_output()
            choice_num = input('Difficulty choice: ')
            n = int(choice_num)
        except ValueError:
            n = 0
        finally:
            if not 1 <= n <= 3:
                n = 0
                print('Not a valid option. Please try again')
                print()
    return n

def game_loop(n):
    start_range = 1
    end_range = 10**n
    random.seed()
    guess_me = random.randint(start_range, end_range)

    user_guess = 0
    num_guesses = 1
    print(PROMPT.format(end_range))
    while user_guess != guess_me:
        try:
            nb_guess = input(GUESS.format(num_guesses))
            user_guess = int(nb_guess)
        except ValueError:
            user_guess = -1
        finally:
            if 1 > user_guess or user_guess > end_range:
                print(PROMPT.format(end_range))
            elif guess_me < user_guess:
                print(colored(LESS.format(user_guess), 'green', attrs=['bold']))
                num_guesses += 1
            elif guess_me > user_guess:
                print(colored(GREATER.format(user_guess), 'red', attrs=['bold']))
                num_guesses += 1

    print()
    print('Good Job! It took you {} guesses.'.format(num_guesses))

if __name__ == '__main__':
    colorama.init()
    continue_game = 'y'
    while continue_game == 'y':
        game_loop(get_choice())
        print()
        continue_text = input('Play again (Yes or No): ')
        if continue_text:
            continue_game = continue_text[0].lower()
        else:
            continue_game = 'n'

