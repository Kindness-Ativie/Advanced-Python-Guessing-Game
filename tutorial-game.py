from random import randrange

def num_guessing_game():
    # starting game values
    guess_counter: int = 0  # user score
    max_num: int = 1000  # maximum number
    secret_number: int = randrange(max_num)  # secret number

    # start message
    start_message: str = f'Guess the secret number between 0 and {max_num} -> '
    print('Good luck. Begin!')

    user_guess: int = int(input(start_message)) # takes the user guess


    # while game is running
    while True:
        # if user guess is too high
        if user_guess > secret_number:
            guess_counter += 1  # add 1 to guess counter
            user_guess = int(input(f'Guesses: {guess_counter} -> Go lower: '))
        # user guess is too low
        elif user_guess < secret_number:
            guess_counter += 1
            user_guess = int(input(f'Guesses: {guess_counter} -> Go higher: '))
        else:
            # winning screen! Woo!
            winning_message: str = f'You won! Yay! Secret number was {secret_number}! Number of attempts: {guess_counter}'
            print(winning_message)
            break
    

num_guessing_game()

