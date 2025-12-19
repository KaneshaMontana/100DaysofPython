# from Day13 import random
#
# wallet = 150
#
# print(f"You have £{wallet} in your wallet.")
# bet = float(input("How much would you like to bet: £ "))
# winnings = bet * 1.5
#
# player_deck = []
# computer_deck = []
# computer_score = -1
# player_score = -1
#
#
# def end_of_game(user, computer):
#     """ Needs improving: want to create a funtion that deducts money from the wallet based on if you won against the computer"""
#     print("  ---- Final Results ---- ")
#     print(f"These are your cards: {player_deck} = {player_score}.")
#     print(f"These are the dealer's cards: {computer_deck} = {computer_score}.")
#
#     if computer_score == player_score:
#         wallet += bet
#         print(f"It's a draw. Your £{bet} bet will be added back to your wallet")
#     elif computer_score == 0:
#         wallet += winnings
#         print(f"Computer lost, You won £{winnings}")
#     elif player_score > 21:
#         wallet -= bet
#         print(f"You lost £{bet}")
#     elif computer_score > 21:
#         wallet += winnings
#         print(f"You won £{winnings}")
#
#         print(f"Your wallet has £{wallet}")
#         play_again = input("Would you like to play again? Type 'y' or 'n': ")
#
#         if play_again == "y":
#             reveal_cards = False
#             player_deck.clear()
#             computer_deck.clear()
#         elif play_again == "n":
#             return game_over == False
#         else:
#             print("Try again.")
#
# def card_calculation(a):
#     total = sum(a)
#     for card in a:
#         if total == 21 and len(a) == 2:
#             return 0
#
#         if 11 in a and total > 21:
#             a.remove(11)
#             a.append(1)
#             return total
#
#     return total
#
# def deal_card():
#     """ Returns a random card from the deck """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
# def first_cards():
#     for num in range(2):
#         player_deck.append(deal_card())
#         computer_deck.append(deal_card())
#
# game_over = False
# first_cards()
#
# while not game_over:
#     player_score = card_calculation(player_deck)
#     computer_score = card_calculation(computer_deck)
#
#     print(f"These are your cards: {player_deck} = {player_score}")
#     print(f"One of the dealer's cards is: {computer_deck[0]}")
#     if player_score == 0 or computer_score == 0 or player_score > 21:
#         end_of_game(player_score, computer_score)
#         game_over = True
#     else:
#         choice = str(input("Type 'h' if you want to 'hit' or 's' if you want to 'stand': ")).lower()
#         if choice == "h":
#             player_deck.append(deal_card())
#             if player_score == 21 or player_score > 21:
#                 end_of_game(player_score, computer_score)
#                 game_over = True
#         elif choice == "s":
#             end_of_game(player_score, computer_score)
#             game_over = True
#         else:
#             print(choice)
#
#
# while computer_score != 0 and computer_score < 17:
#     computer_deck.append(deal_card())
#     computer_score = card_calculation(computer_deck)
