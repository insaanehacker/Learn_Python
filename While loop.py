# We know loop means repeating or executing things again and again
# While loop is used to execute the block of code again and again till the condition is True
# When the condition becomes False, It comes out of the loop
# To specify while loop we must declare a variable
# In order to use While loop we must specify a condition, which means only that block of code will be True

# Example
i = 1 # Here I have declared a variable i and i set it equal to 1, because of the starting value
while i <= 15: # Here I have specified condition that the value of i must be less than 15
    print(i) # This will print the current number of i
    # i = i + 1 # We need to check each condition, Here i have specified...i = i + 1...It will increment the i value and checks whether the number satisfied the given condition or not
    # The above i can also be coded as,
    i += 1 # We need to check each condition, Here i have specified...i = i + 1...It will increment the i value and checks whether the number satisfied the given condition or not
# When we run the program we will get the output as 1 to 15, because when the i = 16, the condition fails, therefore it gets out of the loop
print("\n")

# Lets print the number in reversed order using while loop
i = 10 # Here i have declared a variable i and set it equal to 10, because of the starting value
while i >= 1: # Here I have specified condition that the value of i must be less than 1
              # Because reverse order is.....maximum value >= minimum value
    print(i)
    i -= 1 # We need to check each condition, Here i have specified...i = i - 1...It will decrement the i value and checks whether the number satisfied the given condition or not
# When we run the program we will get the output as 10 to 1
