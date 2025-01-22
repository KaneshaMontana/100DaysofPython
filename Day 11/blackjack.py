import random

wallet = 150

print(f"You have £{wallet} in your wallet.")
bet = float(input("How much would you like to bet: £ "))
winnings = bet * 1.5

player_deck = []
dealer_deck = []
computer_score = -1
user_score = -1


def end_of_game(user, computer):
    """ Needs improving: want to create a fucntionn that deducts money from the wallet based on if you woi against the computer"""
    print("  ---- Final Results ---- ")
    print(f"These are your cards: {player_deck} = {user_score}.")
    print(f"These are the dealer's cards: {dealer_deck} = {computer_score}.")

    if computer_score == user_score:
        wallet += bet
        print(f"It's a draw. Your £{bet} bet will be added back to your wallet")
    elif computer_score == 0:
        wallet += winnings
        print(f"Computer lost, You won £{winnings}")
    elif user_score > 21:
        wallet -= bet
        print(f"You lost £{bet}")
    elif computer_score > 21:
        wallet += winnings
        print(f"You won £{winnings}")

        print(f"Your wallet has £{wallet}")
        play_again = input("Would you like to play again? Type 'y' or 'n': ")

        if play_again == "y":
            reveal_cards = False
            player_deck.clear()
            dealer_deck.clear()
        elif play_again == "n":
            return game_over == False
        else:
            print("Try again.")

def card_calculation(a):
    total = sum(a)
    for card in a:
        if total == 21 and len(a) == 2:
            return 0
        
        if 11 in a and total > 21:
            a.remove(11)
            a.append(1)
            return total
        
    return total

def deal_card():
    """ Returns a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def first_cards():
    for _ in range(2): 
        player_deck.append(deal_card())
        dealer_deck.append(deal_card())

game_over = False
first_cards()

while not game_over:
    user_score = card_calculation(player_deck)
    computer_score = card_calculation(dealer_deck)

    print(f"These are your cards: {player_deck} = {user_score}")
    print(f"One of the dealer's cards is: {dealer_deck[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        end_of_game(user_score, computer_score)
        game_over = True
    else:
        choice = str(input("Type 'h' if you want to 'hit' or 's' if you want to 'stand': ")).lower()
        if choice == "h":
            player_deck.append(deal_card())
            if user_score == 21 or user_score > 21:
                end_of_game(user_score, computer_score)
                game_over = True
        elif choice == "s":
            end_of_game(user_score, computer_score)
            game_over = True
        else:
            print(choice)


while computer_score != 0 and computer_score < 17:
    dealer_deck.append(deal_card())
    computer_score = card_calculation(dealer_deck)
