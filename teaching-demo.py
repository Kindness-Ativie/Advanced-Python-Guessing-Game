from random import randrange

def num_guessing_game():
    # start game values
    guess_counter: int = 0
    max_num: int = 1000
    secret_number: int = randrange(max_num)

    # start_message
    start_message: str = f'Guess the secret number 0 and {max_num}'
    print('Good luck!')

    user_guess: int = int(input(start_message)) # takes the user guess

    # while the game is running

    while True:
        # too high
        if user_guess > secret_number:
            guess += 1
            user_guess = int(input(f'Guesses: {guess_counter} -> Go lower: '))

