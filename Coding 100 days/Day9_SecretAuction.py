from turtle import clear
import Day9_SecretAuction_Logo

for lines in Day9_SecretAuction_Logo.logo:
    print(lines)
print("WELCOME TO THE SECRET AUCTION")

bids = {}
bidding_finished = False


def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    pass


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)
        for lines in Day9_SecretAuction_Logo.logo:
            print(lines)