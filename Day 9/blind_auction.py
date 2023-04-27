import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

continue_bids = True
bids = {}
highest_bid = {}

while continue_bids:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid price?: £"))                
    bids[name] = bid_price
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no': ").lower()

    if more_bidders == "yes":
        os.system('cls' if os.name=='nt' else 'clear')
        continue_bids = True
    elif more_bidders == "no":
        continue_bids = False
        highest_bidder = ""
        highest_bid = 0
        for bidder in bids:
            if bids[bidder] > highest_bid:
                highest_bidder = bidder
                highest_bid = bids[bidder]
        print(f"The highest bidder is {highest_bidder} with a bid of £{bids[highest_bidder]}")
