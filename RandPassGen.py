#! /usr/bin/env python3

import random
import sys

lowercase = ['z', 'p', 'v', 'x', 'u', 'd', 'f', 'g', 'b', 'c', 'w', 'o', 'l', 'm', 's', 'a', 'j', 'h', 'i', 'q', 't', 'e', 'n', 'r', 'y', 'k']
uppercase = ['U', 'A', 'V', 'F', 'W', 'O', 'G', 'Z', 'E', 'T', 'S', 'P', 'I', 'N', 'B', 'H', 'X', 'C', 'K', 'L', 'M', 'Q', 'Y', 'D', 'J', 'R']
nbs = ['5', '2', '7', '0', '6', '9', '8', '3', '1', '4']
sp_ch = ['!', '?', '%', '$', '(', ')', '[', ']', '{', '}', '&', '#', '_']

password = []

def shuffle():
    random.shuffle(lowercase)
    random.shuffle(uppercase)
    random.shuffle(nbs)
    random.shuffle(sp_ch)

shuffle()

def passAppendLower():
    global choice_lower
    if choice_lower.lower() == 'y' or choice_lower == '':
        password.append(lowercase[rand])
    else:
        pass

def passAppendUpper():
    global choice_upper
    if choice_upper.lower() == 'y' or choice_upper == '':
        password.append(uppercase[rand])
    else:
        pass
    
def passAppendNb():
    global choice_nb
    if choice_nb.lower() == 'y' or choice_nb == '':
        password.append(nbs[rand_nb])
    else:
        pass
   

def passAppendSpCh():
    global choice_spch
    if choice_spch.lower() == 'y' or choice_spch == '':
        password.append(sp_ch[rand_spch])   
    else:
        pass


length = int(input("Enter the lenght of your password : "))
nb_pass = input("How many passwords do you want to generate ? (Leave empty for one): ")

choice_lower =  input("Do you want to use lower case letters ? (Y/n)")
choice_upper =  input("Do you want to use upper case letters ? (Y/n)")
choice_nb =     input("Do you want to use numbers ? (Y/n)")
choice_spch =   input("Do you want to use special characters ? (Y/n)")

if nb_pass == '':
    nb_pass = '1'

print()

if nb_pass == '1':
    print("Your randomly generated password is :")
else:
    print("Your randomly generated passwords are :")
print()

# PassGen

try:
    for i in range(int(nb_pass)):
        for y in range(length):
            rand = random.randint(0,24)
            rand_nb = random.randint(0,8)
            rand_spch = random.randint(0,len(sp_ch)-1)
            random.choice([passAppendLower, passAppendUpper, passAppendNb, passAppendSpCh])()
        print(str(i+1)+'.', end=' ')
        for i in range(len(password)-1):
            print(password[i],end='')
        print(password[len(password)-1], end = '\n')
        password.clear()
        print()

except Exception:
    print("[!] You entered a non-valid number of generations.")
    sys.exit(1)

###############################################################################################

print()