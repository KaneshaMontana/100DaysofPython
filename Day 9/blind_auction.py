import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

continue_bids = True
bids = {}
highest_bid = {}

while continue_bids:
    name = input("What is your name?: ").lower()
    bid_price = int(input("What is your bid price?: "))

    bids[name] = bid_price

    ask = input("Are there any more bidders? 'yes' or 'no': ").lower()

    if ask == "yes":
        os.system('cls' if os.name=='nt' else 'clear')
        continue_bids = True
    else:
        continue_bids = False
        print(bids)
        highest_bidder = ""
        highest_bid = 0
        for bidder in bids:
            if bids[bidder] > highest_bid:
                highest_bidder = bidder
                highest_bid = bids[bidder]
        print(
            f"The highest bidder is {highest_bidder} with a bid of {bids[highest_bidder]}"
        )
