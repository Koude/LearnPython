#!/usr/bin/python
# -*- coding: utf-8 -*-

low=0
high=100

guessed = False 

while guessed == False:
    guess = (low+high)//2
    judge = input("Is your secret number "+str(guess)+" ?"+"\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if judge == "l":
        low = guess
    elif judge == "h":
        high = guess
    elif judge == "c":
        guessed = True
    else:
        print("Sorry, I did not understand your input.")
    
print("Game over. Your secret number was: "+str(guess))
