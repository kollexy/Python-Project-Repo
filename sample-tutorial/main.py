# User inputs the lower bound and upper bound of the range.
# The compiler generates a random integer between the range and store it in a variable for future references.
# For repetitive guessing, a while loop will be initialized.
# If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
# Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
# And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
# Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.

#

import random

import math

lower = int(input("Enter lower of number:\n"))
upper = int(input("Enter upper of number:\n"))
my_rand = random.randint(lower, upper)

my_math = round(math.log(upper - lower + 1, 2))

print(my_math)

print("\n\tYou've only ",
      my_math,
      " chances to guess the integer!\n")


## initialise count

def guess_function():
    count = 0
    while count < my_math:
        count += 1
        guess_a_number = int(input("enter your guess: \n"))
        if guess_a_number == my_rand:
            print("Congrats!")
        elif guess_a_number > my_rand:
            print("try again, your guess is greater")
        else:
            print("try again, your guess is lower")


guess_function()

# guess_function()
