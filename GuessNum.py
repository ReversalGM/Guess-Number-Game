# Guess the number game
from random import randint
from math import log2
from math import ceil

# recieves input from console and checks if it is valid number
def int_input():
    while True:
        try:
            result = int(input())
            return result
        except ValueError:
            print("INVALID INPUT, please enter a number")

# attempt is number of guesses before win or loss, optimal attempt is max attempt required in worst case scenario, max_attempt is max attempt
# allowed in the game difficulty   
def game_end(attempt, optimal_attempt, max_attempt):
    if attempt < optimal_attempt:
        print("Lucky you! You guessed the number in {} attempts".format(attempt))
    elif attempt == optimal_attempt:
        print("Good job! You guessed the number in {} attempts".format(attempt))
    elif (attempt > optimal_attempt) & (attempt <= max_attempt):
        print("You gussed the number in {} attempts, but you can do better. The optimal solution is {} or less".format(attempt, optimal_attempt))
    else:
        print("You exceeded the max number of {} attempts, try again!".format(max_attempt))

    while True:
        print("Play Again? Y/N")
        decision = input()
        if decision == "Y":
            return True
        elif decision == "N":
            return False
        else :
            print("INVALID INPUT, please enter \"Y\" or \"N\"")
            continue
    
# lbound and ubound is the range, max_attempt is maximum number of attempts before failure
def game_gen(lbound, ubound, max_attempt):
    choices = ubound - lbound + 1
    optimal = ceil(log2(choices))
    number = randint(lbound, ubound)
    for guess in range(max_attempt):
        print("Take a guess")
        num_guessed = int_input()
        if num_guessed == number:
            return game_end(guess + 1, optimal, max_attempt)
        elif num_guessed < number:
            print("Your guess is too low")
            continue
        else:
            print("Your guess is too high")
            continue
    return game_end(max_attempt + 1, optimal, max_attempt)
        


print("Please enter your name")
name = input()
print("Hello " + name + ", thank you for playing the guess the number game!")
game_open = True #set to false to stop playing after a round is over

while game_open:
    print("Please select difficulty")
    print("Enter 1 for easy, 2 for medium, 3 for hard, 4 for custom")
    print("Easy: random number between 1-10")
    print("Medium: random number between 1-100")
    print("Hard: random number between 1-1000")
    print("Custom: choose your own range")
    gamemode = input() #string
    if gamemode == "1":
        game_open = game_gen(1, 10, 10)
    elif gamemode == "2":
        game_open = game_gen(1, 100, 20)
    elif gamemode == "3":
        game_open = game_gen(1, 1000, 30)
    elif gamemode == "4":
        while True:
            print("Choose upper bound")
            upper_bound = int_input()
            print("Choose lower bound")
            lower_bound = int_input()
            print("Choose max number of attempts")
            max_attempt = int_input()
            if (lower_bound <= upper_bound)&(max_attempt >= 0):
                break
            else:
                print("INVALID INPUT, make sure lowerbound is less than upperbound and max attempts is greater than 0")
            
        game_open = game_gen(lower_bound, upper_bound, max_attempt)
    else:
        print("INVALID INPUT")
