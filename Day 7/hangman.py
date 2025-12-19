
# modules
from Day13 import random
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
    guess = input("\nPlease make a guess: ").lower()

# for each char positiion in the chosen word
# iterate the total number of characters -1
# len/x = total num of chars
# range (0,x)

    if guess in display:
        print(f"\nYou have entered the letter {guess} before. Try another letter")

    for char_position in range(chosen_word_length):
        cw_letter = chosen_word[char_position]
        if cw_letter == guess:
            display[char_position] = cw_letter
    
    if guess not in chosen_word:
        lives -= 1
        print (f" \nThe letter {guess} is not in the chosen word. Try another letter")
        if lives == 0:
            end_of_game = True
            print("\nYou lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"\n{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\nYou win.")


    print(stages[lives])
    print(f"\nYou have {lives} lives left")

