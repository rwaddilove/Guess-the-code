# Mastermind
# set the code length

import random
import os

def new_code(difficulty,codelen):
    s = ""
    for i in range(codelen):
        s = s + str(random.randint(0,difficulty))   #limit digits, eg. 01234
    return s

def enter_guess(codelen):
    s = ""
    while s.isdigit()==False or len(s)!=codelen:
        print(f"\nEnter the {codelen} digit code: ",end="")
        s = input()
    return s

def check_guess(guess,code,codelen):
    score = ""
    code = list(i for i in code)
    guess = list(i for i in guess)
    #exact match
    for i in range(codelen):
        if guess[i] == code[i]:    #a match?
            score = score + "X"    #right char, right place
            code[i] = " "
            guess[i] = " "
    #right char, wrong place
    for i in range(codelen):
        for j in range(codelen):
            if  not (guess[i]==" " or code[j]==" "):
                if guess[i]==code[j]:
                    score = score + "o"
                    code[j] = " "
    return score

def set_difficulty():
    print("\nMax number, eg. 5 uses digits 0-5 only.")
    s = "z"         #dummy value    - set to ""?
    while not s in ['3','4','5','6','7','8','9']:
        s = input("Enter 3 (easy) to 9 (hard): ")
    return int(s)

def set_codelen():    #choose length of code - number of digits
    print("\nCode length, eg. 4 is a 4-digit code.")
    s = "z"           #dummy value   - set to ""?
    while not s in ['3','4','5','6','7','8','9']:
        s = input("Enter 3 (easy) to 9 (hard)? ")
    return int(s)

def set_goes():
    turns = ""
    ok = False
    while not ok:
        turns = input("How many turns in the game? (5-15) ")
        if turns.isdigit():
            turns = int(turns)
            if turns>4 and turns<16: ok=True
    return turns

def show_title():
    os.system('cls') if os.name=='nt' else os.system('clear')
    print("----------------------------------")
    print("    M A S T E R M I N D")
    print("----------------------------------")
    print(f"Guess the digits in a secret code!")
    print("X means right code, right place.")
    print("o means right code, wrong place.\n")

#============== MAIN ==============
show_title()
print("Let's set the difficulty.\n")
goes = set_goes()
codelen = set_codelen()    #length of secret code
difficulty = set_difficulty()
code = new_code(difficulty,codelen)
done = False
history = ["","","","","","","","","","",""]
score = ""
while not done and goes>0:
    guess = enter_guess(codelen)
    score = check_guess(guess,code,codelen)
    history[goes] = f"Guess {goes:02d}: {guess} Score: {score}"
    show_title()
    for i in range(10,0,-1):
        if history[i] > "": print(history[i])
    if guess==code: done = True
    goes = goes -1

if done == True:
    print("\nWell done! You got it!\n")
else:
    print("\nNo turns left! You failed!")
    print(f"The code was {code}.\n")

#END
