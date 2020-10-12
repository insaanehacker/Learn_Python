# This is main and important part in all programming
# Commenting:
    # This means we are specifying operation to our program using comment, It will helps others to understand our code
# For example, You got job in a company as developer, now you have written many lines of code
# Now your higher official commands you to move over to other job
# Your programming work you did before is pending now!
# The officer gives your job to someone, to complete the remaining part in the incompleted code
# If he can't able to understand your code, the work keeps pending
# So to avoid such situation we use comment, We can give some instruction in plain text that what this code is for and what will happen if i run this code
# The lines you have commented will not be executed, only your code will be executed

# Commenting in python is very simple, we use "#" then we can start typing as many lines we want to comment
# Suppose you feel some block of code is blocking your request, instead of deleting it we can comment those block of codes using """ at starting and """ in the end

# Example:
print("Hello World !")  # This will print Hello world! as output
                        # Note only the code will be executed not this comment word

# Example 2:
print("data")
print("read")
print("well")

print("\n")

# Now let us comment only the read, this means both the data and well will be executed not the read
print("data")
"""
print("read") # See when we commented it, print("read") automatically changed into green color, means this this neglected or will not be read by python
"""
print("well")
# When we run this program, we get "data" and "well" as output, "read" will be neglected or python will not consider it, because it is commented