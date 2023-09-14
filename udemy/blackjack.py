import random

def blackjack():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)
user_selected_card=[]
machine_selected_card=[]
user_cards=0
machine_cards=0
while True:
    user_selected_card.append(blackjack())
    machine_selected_card.append(blackjack())
    user_cards=sum(user_selected_card)
    machine_cards=sum((machine_selected_card))
    if user_cards>21 and 11 in user_selected_card:
        user_selected_card.remove(11)
        user_selected_card.append(1)
    elif user_cards>21: 
        print("you loose")
        break
    if user_cards>17 and machine_cards>17:
        if user_cards>machine_cards:
            print("You win")
        elif user_cards<machine_cards:
            print("you loose")
        else:
            print("Draw") 
        break
print(user_selected_card)
print(machine_selected_card)