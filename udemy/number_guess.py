import random;
print(""" welcome to Number Guessing Game
 I'm thinking of a number between 1 and 100""")

times=input("Choose a difficulty. Type Hard or Easy \n").lower()
number=random.randint(1,100)
print(number)
if times=="easy":
    no_of_times=10
elif times=="hard":
    no_of_times=5
else:
    print("Inavalied input")
for i in range(no_of_times,0,-1):
    print(f"You have {i} attempts remaining to guess the number.")
    guess=int(input("Make a guess"))
    if number>guess:
        print("Too High")
    elif number<guess:
        print("Too Low")
    else:
        print(f"You got it! The answer was {number}")
        break
    if i==1:
        print("you have run out of guesses, you loose")
        break