#! /usr/bin/env python3

import random

lowercase = ['z', 'p', 'v', 'x', 'u', 'd', 'f', 'g', 'b', 'c', 'w', 'o', 'l', 'm', 's', 'a', 'j', 'h', 'i', 'q', 't', 'e', 'n', 'r', 'y', 'k']
uppercase = ['U', 'A', 'V', 'F', 'W', 'O', 'G', 'Z', 'E', 'T', 'S', 'P', 'I', 'N', 'B', 'H', 'X', 'C', 'K', 'L', 'M', 'Q', 'Y', 'D', 'J', 'R']
nbs = ['5', '2', '7', '0', '6', '9', '8', '3', '1', '4']
sp_ch = ['!', '?', '%', '$', '(', ')', '[', ']', '{', '}', '&', '#', '-', '_']

password = []

def shuffle():
    random.shuffle(lowercase)
    random.shuffle(uppercase)
    random.shuffle(nbs)
    random.shuffle(sp_ch)

shuffle()

lenght = int(input("Enter the lenght of your password : "))

def passAppendLower():
    password.append(lowercase[rand])

def passAppendUpper():
    password.append(uppercase[rand])
    
def passAppendNb():
    password.append(nbs[rand_nb])

def passAppendSpCh():
    password.append(sp_ch[rand_spch])

for i in range(lenght):
    rand = random.randint(0,24)
    rand_nb = random.randint(0,8)
    rand_spch = random.randint(0,len(sp_ch)-1)
    random.choice([passAppendLower, passAppendUpper, passAppendNb, passAppendSpCh])()

print("Your randomly generated password is :", end = ' ')
for i in range(len(password)-1):
    print(password[i],end='')
print(password[len(password)-1], end = '\n')