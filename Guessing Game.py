# Now lets try to build a awesome guessing game
# If the user guess matches the computer guess, user wins or else he looses, or else we need him to enter again
"""
computer_guess = "Lion" # Here we assign a computer guess variable to "lion"
user_guess = "" # Here we assign a user guess from user_guess
while computer_guess != user_guess: # We specify condition that when computer guess is not equal to user guess
    user_guess = input("Enter your guess: ") # Get input from the user
    # If the answer is False we need to ask the user to enter the input again, so we use while loop

print("You win!") # If the user enter the correct guess "Lion", it exits out of the loop and prints "You win"
"""

# Lets make our game more interesting, we will give a count, to enter the correct guess
# If the count exceeds, we must tell the user " You loose"
computer = "Lion" # Here we assign a computer guess variable to "lion"
user_guess = "" # Here we assign a user guess from user_guess
guess_count = 0
guess_limit = 3
out_of_guesses = False

while user_guess != computer and not(out_of_guesses): # We specify condition that when computer guess is not equal to user guess
    if guess_count < guess_limit: # when guess count is less than guess limit
        user_guess = input("Enter your guess: ") # Get input from the user
        guess_count += 1 # Increment guess count by 1 till the condition satisfies or the condition is true
    else:
        out_of_guesses = True
    # If the answer is False we need to ask the user to enter the input again, so we use while loop

if out_of_guesses:
    print("Computer wins!")
else:
    print("You win!") # If the user enter the correct guess "Lion", it exits out of the loop and prints "you win"
