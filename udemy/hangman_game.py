import random

word_list = ["ardvark", "baboon", "camel", "elephant", "giraffe", "kangaroo", "penguin", "rhinoceros", "octopus", "squirrel"]
word_selected=list(random.choice(word_list))
word_len=len(word_selected)
n=0
dashed_word=list(word_len*"_")

stages = ['''
+---+
| |
O |
/|\ |
/ \ |
|
''', '''
+---+
| |
O |
/|\ |
/ |
|
''', '''
+---+
| |
O |
/|\ |
|
|
''', '''
+---+
| |
O |
/| |
|
|
=========''', '''
+---+
| |
O |
| |
|
|
''', '''
+---+
| |
O |
|
|
|
''', '''
+---+
| |
|
|
|
|
''']


while n<=6:
    print(' '.join(dashed_word))
    user_guess=input("Guess a letter ")
    if user_guess in dashed_word:
        print(f"You already guessed the word")
    for i in range(word_len):
        if user_guess==word_selected[i]:
            dashed_word[i]=user_guess
    if user_guess not in word_selected:
        print("Wrong guess. Lose a life")
        n+=1
        print(stages[-n])
        if n>=6:
            print("You loose! ")
            break

    if '_' not in dashed_word:
        print("You win")
        break
    
        

            
    