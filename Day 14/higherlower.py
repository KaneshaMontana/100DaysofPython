# 1. Import data, artwork, and random module

from artwork import higherlower, vs
from gameData import data
import random


# 2. Show the game logo
print(higherlower)

# 3.  Get the number of celebs in game data
game_nums = len(data)

# 4. Create a function that gets a random celeb from the data list using a random number
def get_random_celeb():
    """Return one random celeb from game data based on a random number"""
    random_index = random.randint(0,game_nums-1)
    return data[random_index]

# 5. Create a function that formats a celeb's data into a readable string
#    e.g. "Selena Gomez, is a musician, from USA."
def format_celeb (celeb):
    name = celeb['name']
    description = celeb['description']
    country = celeb['country']
    return (f"{name} is a {description} from {country}")


# 5. Assign celebs to separate variables and ensure they don't match
def assign_random_celeb():
    """ Initialises random celeb from game data based on a random number"""
    celeb_a = get_random_celeb()
    celeb_b = get_random_celeb()
    while celeb_b == celeb_a:
        celeb_b = get_random_celeb()
    return celeb_a, celeb_b

# 6. Create function to check if the users answer correctly guesses who has the most followers
def check_answer(guess, followers_a, followers_b):

    if followers_a > followers_b and guess == "A":
        return True
    if followers_b > followers_a and guess == "B":
        return True
    else:
        return False

# 7. Start the game. If it's correct add 1 point and make celeb b the new celeb a. If not, end game
def game_loop(celeb_a, celeb_b):
    score = 0
    game_should_continue = True

    while game_should_continue == True :
        print(f"Compare A: {format_celeb(celeb_a)}")
        print(vs)  # from artwork.py
        print(f"Against B: {format_celeb(celeb_b)}")
        user_guess = str(input("\n Who has the most followers? A or B ")).upper()
        celeb_a_followers = celeb_a["follower_count"]
        celeb_b_followers = celeb_b["follower_count"]

        if check_answer(user_guess, celeb_a_followers, celeb_b_followers) == True:
            score += 1
            print(f"You are correct! Your score is: {score}")
            celeb_a = celeb_b
            celeb_b = get_random_celeb()
            while celeb_b == celeb_a:
                celeb_b = get_random_celeb()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

get_random_celeb()
a,b = assign_random_celeb()
game_loop(a,b)
