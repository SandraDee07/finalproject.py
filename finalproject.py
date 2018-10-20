#importing the time module
import time
#welcome the player
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
#waiting
time.sleep(1)
print("Time to start guessing... good luck!")
time.sleep(0.5)
#word or phrase
word = "fresh prince of bel air"
print("This was a popular 90's show...")
#empty value for guessing
guesses = ''
turns = 10
#while loop
#if the turns are more than zero
while turns > 0:
    failed = 0
    #for every character in word   
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
        #and increase the failed counter by one
            failed += 1
    #if failed is less than 0, print winning message
    if failed == 0:        
        print("You won!!")
        break              
    print
    #ask the player to guess a letter
    guess = input("guess a character:") 
    #set the players guess to guesses
    guesses += guess                    
    #if letter not present
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")
    #if no more turns
        if turns == 0:    
            print("You Loose")
