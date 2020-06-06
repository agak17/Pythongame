#import random module
import random 
game_options = ['Rock' , 'Paper' , 'Scissors']

#Start game
print("Welcome to Rock, Paper, Scissors!")

#Player 1
user_input = input("Your go! Input you choice now...")

#Computer randomised option 
print("I choose...")
computer_option = random.choice(game_options)
print (computer_option)

#Game outcomes
if computer_option == user_input:
    print("Draw")

if computer_option == "Rock" and user_input == "Scissors":
    print("You lose!")
elif computer_option == "Rock" and user_input == "Paper" :
    print("You win!")

if computer_option == "Paper" and user_input == "Scissors":
    print("You win!")
elif computer_option == "Paper" and user_input == "Rock"  :
    print("You lose!")

if computer_option == "Scissors" and user_input == "Rock" :
    print("You win!")
elif computer_option == "Scissors" and user_input == "Paper" :
    print("You lose!")

#End of game 
print("End of game!")