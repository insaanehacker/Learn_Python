# Lets define a function which will print user name and will find users current_age
user_name = input("Enter your name: ") # This will get name from the user
user_birth = int(input("Enter Date of birth year: ")) # This will get the DOB year from the user
present_year = 2020
current_age = 1 # we are assuming current age is 1 initially
def user_current_age(user_birth):
    current_age = present_year - user_birth # This will subtract user DOB year from present year
    return str(user_name) + "is " + str(current_age) + " years old!" # This will tell the user his age with his name

print(user_current_age(user_birth)) # We are calling the function with print statements, because we used return in our function

