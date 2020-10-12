# Suppose we have created tons of python files, Now you wanna use any one of them in your new python file
# We have two options: Either we can copy all the code and paste it over our new python code or just import it
# If we copy and paste it again in our new file, it makes our code lengthy one, Technically that's not an gud idea
# We can able to import the same python file using "import" keyword

# For example, i have a python file to print the name and current age of user, name of the python file is "Modules_Sample.py"
# Let me import it here
import Modules_Sample # Modules_Sample is my python file
# Now we can do any task defined in that code already
# Below is the code, that i already created in it
"""
# Lets define a function which will print user name and will find users current_age
user_name = input("Enter your name: ") # This will get name from the user
user_birth = int(input("Enter Date of birth year: ")) # This will get the DOB year from the user
present_year = 2020
current_age = 1 # we are assuming current age is 1 initially
def user_current_age(user_birth):
    current_age = present_year - user_birth # This will subtract user DOB year from present year
    return str(user_name) + "is " + str(current_age) + " years old!" # This will tell the user his age with his name

print(user_current_age(user_birth)) # We are calling the function with print statements, because we used return in our function
"""
# Now let me call the function
user_birth = 1 # Here we are assuming let user_birth is 1
Modules_Sample.user_current_age(user_birth) # Here we are calling the function
                                            # We get ouput to enter name and birth year
                                            # Automatically python calculates the age of the user with name
                                            # We wrote only two lines of code, we got the exact answer
                                            # THis is the power of "import" function

# Like wise we can import any modules or files to python

