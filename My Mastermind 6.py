# Mastermind
# check guess input

import random
import os

CODELEN = 4    #length of secret code

def new_code(d):
    s = ""
    for i in range(CODELEN):
        s = s + str(random.randint(0,d))
    return s

def enter_guess():
    str = "abcde"
    while str.isdigit()==False or len(str)!=CODELEN:
        print(f"\nEnter the {CODELEN} digit code: ",end="")
        str = input()
    return str

def check_guess(guess,code):
    x = ""
    code = list(x for x in code)
    guess = list(x for x in guess)
    #exact match
    for i in range(CODELEN):
        if guess[i] == code[i]:    #a match?
            x = x + "X"             #right char, right place
            code[i] = " "
            guess[i] = " "
    #right char, wrong place
    for i in range(CODELEN):
        for j in range(CODELEN):
            if  not (guess[i]==" " or code[j]==" "):
                if guess[i]==code[j]:
                    x = x + "o"
                    code[j] = " "
    return x

def set_difficulty():
    s = "zz"
    while s!='4' and s!='5' and s!='6' and s!='7' and s!='8' and s!='9':
        print("Enter difficulty 4-9: ", end="")
        s = input()
    return int(s)

#============== MAIN ==============
goes = 9
history = ["","","","","","","","","","",""]
score = ""
print("\n----------------------")
print(" M A S T E R M I N D")
print("---------------------")
print(f"You have {goes} attempts to guess a {CODELEN} digit code.")
print("X means right code, right place.")
print("o means right code, wrong place.\n")
difficulty = set_difficulty()
code = new_code(difficulty)
done = False
while not done and goes>0:
#    print(f"\nPlay Mastermind!\n{goes} guesses left. ",end="")
#    print(f"\nPlay Mastermind! Guess the hidden code... ")
    guess = enter_guess()
    score = check_guess(guess,code)
    history[goes] = "Guess " + str(goes) + ": " + guess + " Score: " + score #+ " (" + code + ")"
    os.system('cls')
    print("\n----------------------")
    print(" M A S T E R M I N D")
    print("---------------------\n")
    for i in range(10,0,-1):
        if history[i] > "": print(history[i])
    if guess==code: done = True
    goes = goes -1

if done == True:
    print("\nWell done! You got it!\n")
else:
    print("No turns left! You failed!")
    print(f"The code was {code}.\n")

#END
