import os
auctions={}
while True:
    os.system('cls')
    name=input("Enter the name of bidder\n")
    amount=int(input("enter the amount to be bid \n"))
    auctions[name]=amount
    response=input("If anyone to bid type 'yes' else 'No' \n").lower()
    if response=='no':
       break

highest_bid=max(auctions.values())
winners=[name for name , bid in auctions.items() if highest_bid==bid]

for winner in winners:
    print(f"winner: {winner} bid: {highest_bid}")