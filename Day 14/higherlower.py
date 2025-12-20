# 1. Import data, artwork, and random module

from artwork import higherlower, vs
from gameData import data
import random


# 2. Show the game logo
print(higherlower)

# 3.  Get the number of celebs in game data
game_nums = len(data)

def get_random_celeb():
    """Return one random celeb from game data based on a random number"""
    random_index = random.randint(0,game_nums-1)
    return data[random_index]

def assign_random_celeb():
    """ Assigns random celebs ensuring they don't match from game data"""
    celeb_a = get_random_celeb()
    celeb_b = get_random_celeb()
    while celeb_b == celeb_a:
        celeb_b = get_random_celeb()
    return celeb_a, celeb_b

def format_celeb (celeb):
    """ Formats celeb account info into a string """
    name = celeb['name']
    description = celeb['description']
    country = celeb['country']
    return (f"{name} is a {description} from {country}")


def check_answer(guess, followers_a, followers_b):
    """ Compares Celeb A and Celeb B's followers with the user guess"""
    if followers_a > followers_b and guess == "A":
        return True
    if followers_b > followers_a and guess == "B":
        return True
    else:
        return False

def game_loop(celeb_a, celeb_b):
    """ Makes the game repeatable. If it's correct user gets 1 point and celeb b becomes the  new celeb a. If not, end game"""
    score = 0
    game_should_continue = True

    while game_should_continue == True :
        print(f"Compare A: {format_celeb(celeb_a)}")
        print(vs)  # from artwork.py
        print(f"Against B: {format_celeb(celeb_b)}")
        user_guess = str(input("\n Who has the most followers? A or B ")).upper()

        # Check follower numbers
        celeb_a_followers = celeb_a["follower_count"]
        celeb_b_followers = celeb_b["follower_count"]
        is_correct = check_answer(user_guess, celeb_a_followers, celeb_b_followers)

        if is_correct == True:
            score += 1
            print(f"You are correct! Your score is: {score}")
            print("\n" * 20)
            print(higherlower)
            # Celeb b will become Celeb A
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
