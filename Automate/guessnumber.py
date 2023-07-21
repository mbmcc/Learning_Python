#!/usr/bin/env python

###############
# Author : Matthew McCourry
# Contact: github.com/mbmcc
# Title : Guess the Number
# Description : <https://automatetheboringstuff.com/2e/chapter3/>
# 
# Created : Wed Jul 19 2023
# Last modified : same
###############

import random

print('Hello. What is your name?')
name = input()

print('Well, ', name, ', I am thinking of a number between One and Twenty. Can you guess my number?')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ', name, ' you guessed my number in', str(guessesTaken), 'guesses!')
else:
    print('Nope. The number I was thinking of was ', str(secretNumber))

