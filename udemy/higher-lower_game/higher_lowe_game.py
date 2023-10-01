import random
import data
import os
dataset=data.data_set
item1=random.choice(dataset)
score=0
while True:
   
    item2=random.choice(dataset)
    print(f"Compare A: {item1['name']} a {item1['description']} from {item1['country']}")
    print("")
    print("")
    print("VS")
    print("")
    print("")
    print(f"Against B: {item2['name']} a {item2['description']} from {item2['country']}")
    
    user_input=input("Who has more followers? Type 'A' or 'B \n").lower()
    if user_input=='a' and item1['follower_count'] > item2['follower_count']:
        score+=1
        print(f"You're right! Current SCore {score}")
    elif user_input=='b' and item1['follower_count'] < item2['follower_count']:
        score+=1
        print(f"You're right! Current SCore {score}")
    else:
        os.system('cls')
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    item1=item2
        