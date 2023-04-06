
# modules
import random 
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

# Select a random word from the list
chosen_word = random.choice(word_list).lower()
chosen_word_length = len(chosen_word)

# Testing 
print(f"Your chosen word is: {chosen_word} ")




# Display _ for every character of the chosen word
display = []

for _ in range(chosen_word_length):
    display += "_"
print(stages[6])



end_of_game = False
lives = 6

# Get user to  a guess
while not end_of_game:
    guess = input("Please make a guess: ").lower()

# for each char positiion in the chosen word
# iterate the total number of characters -1
# len = total num of chars
# range (0,x)
    for char_position in range(chosen_word_length):
        cw_letter = chosen_word[char_position]
        if cw_letter == guess:
            display[char_position] = cw_letter
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")


    # # try 1: display lives by getting the char position of each stage
    for stage in range(len(stages)):
        stage_position = stages[lives]
    
    if lives == 6 and cw_letter == guess:
        print(stage_position)
        print("You haven't lost a life")
    elif lives >= 1 or lives <= 5:
        print(stage_position)
        print(f"You have {lives} lives left")


