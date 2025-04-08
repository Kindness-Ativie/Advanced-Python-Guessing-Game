from random import randrange

# creating a class (cake) to store our player info
class Player:
    # creates the parameters (ingredients) to make player
    def __init__(self, username, high_score, last_attempt):
        self.username = username
        self.high_score = high_score
        self.last_attempt = last_attempt

    # prints the player as a nicely formatted string (text)
    def __str__(self):
        return f"{self.username} HIGH SCORE: {self.high_score} LAST ATTEMPT: {self.last_attempt}"


# holds all existing players
all_players: list[Player] = []


# shows all our current players in the game 
def display_all_players():

    # checks if the all_players list is empty first
    if not all_players:
        print("There are no players!")
    else:
        # numbers our players for us and shows all players in the all_players list
        starting_num: int = 1

        # formats players into a list like 1) SamplePlayer 2) CoolCorbin 
        for player in all_players:
            print(starting_num, end=") ")
            print(player)
            starting_num += 1


# creates players and checks if it already exists
def get_player_name() -> str:

    # 1) user types player name they'd like
    try_player_name: str = str(input('Enter your player name @_@: '))
    
    # 2) checking if player name is already taken
    for existing_player in all_players:
        while existing_player.username == try_player_name:
            try_player_name: str = str(input(f'Sorry {existing_player.username} is already taken. :( -->: '))

    # displays welcome message and returns player name
    print(f'WELCOME, {try_player_name}! 0_0')
    return try_player_name



def num_guessing_game():
   
    # starting game values
    guess_counter: int = 0  
    max_num: int = 1000  
    secret_number: int = (randrange(max_num))

    # start message
    start_message: str = f'Guess the secret number between 0 and {max_num} ->: '
    print('Good luck. Begin!')

    user_guess = int(input(start_message))  # takes user guess
    
    # while the game is running
    while True:
        # if user guesses too high
        if user_guess > secret_number:
            guess_counter += 1
            user_guess = int(input(f'Guesses: {guess_counter} -> Go lower: '))
        # user guesses too low
        elif user_guess < secret_number:
            guess_counter += 1
            user_guess = int(input(f'Guesses: {guess_counter} -> Go higher: '))
        # users guess equals the secret number
        else:
            # winning screen
            print(f'You won! The secret number was {secret_number}! Number of attempts {guess_counter}')
            score: int = guess_counter
            break


# adding a player to our game
sample_player: Player = Player('SamplePlayer', 0, 0)
all_players.append(sample_player)
      
# creating our own player
get_player_name()

# calling (summoning) our displaying players function
display_all_players()
