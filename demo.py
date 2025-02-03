import random 
print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")
number_to_Guess=random.randrange(-30,100)

Chances =7
Guess_Counter=0

while  Guess_Counter < Chances:
    Guess_Counter+=1
    myguess=int(input("please enter your guess"))
    if myguess == number_to_Guess:
        print(f'the number is {number_to_Guess} and you found it right !! in the {Guess_Counter} attempt')
        break

    elif Guess_Counter>=Chances and myguess!=number_to_Guess:
            print(f'Sorry, the number is {number_to_Guess}. You have no more attempts left.')
           
    elif myguess<number_to_Guess:
            print('Too low, try higher')
    elif myguess>=number_to_Guess:
            print('Too high, try lower')

            # push only

