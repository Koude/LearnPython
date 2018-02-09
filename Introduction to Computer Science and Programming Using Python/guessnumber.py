low=0
high=100

guess = (low+high)//2
judge = input("Is your secret number "+str(guess)+" ?"+"\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while judge!="c":
    if judge == "l":
        low = guess
    elif judge == "h":
        high = guess
    else:
        print("Sorry, I did not understand your input.")
    guess = (low+high)//2
    judge = input("Is your secret number "+str(guess)+" ?"+"\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
print("Game over. Your secret number was: "+str(guess))
