# If statements is nothing but we specify a condition and we check whether the specified condition is true or false
# If the specified condition is true...The main program or condition will be executed
# If the specified condition does not match the actual condition, which means its false
# Then it will execute our else statements or other condition
# This is the if condition, We  need to specify colon at the end to specify condition inside the block

# Example
# Lets specify the condition to if statement that, If its raining wear a rain coat using boolean True condition
its_raining = True # Here i have assigned a variable its_raining and set it equal to True
if its_raining: # This is the if condition, means if the condition matches, execute this block of code
    print("You are wearing a RainCoat") # The condition matches here or the condition is true, so we get output as you are wearing raincoat

# Lets specify the condition to if statement that, If its raining wear a rain coat using string
its_raining = "Wear a RainCoat" # Here i have assigned a variable its_raining and set it equal to wear a raincoat
if its_raining: # This is the if condition, means if the condition matches, execute this block of code
    print("You are wearing a RainCoat") # The condition matches here or the condition is true, so we get output as you are wearing raincoat

# Lets specify the condition to if statement that, If its raining wear a rain coat using boolean False condition
its_raining = False # Here i have assigned a variable its_raining and set it equal to False
if its_raining: # This is the if condition, means if the condition matches, execute this block of code
    print("You are wearing a RainCoat") # The condition does not match here or the condition is false, so we dont get any output here

# Lets specify condition that, if its raining "Wear an raincoat" otherwise "Dont wear a raincoat" using boolean function
its_raining = True # Here i have assigned a variable its_raining and set it equal to True
if its_raining: # This is the if condition, means if the condition matches, execute this block of code
    print("Wear an raincoat")  # If the condition matches or the condition is true, so we get output as "Wear an raincoat"
else: # This is the otherwise condition, means if the condition does not matches, execute this block of code
    print("Dont wear an raincoat")
# Here we get output as "Wear an raincoat" because the condition matches or the specified condition is True

# Lets specify condition that, if its raining "Wear an raincoat" otherwise "Don't wear a raincoat" using boolean function
its_raining = False # Here i have assigned a variable its_raining and set it equal to False
if its_raining: # This is the if condition, We  need to specify colon at the end to specify condition inside the block
    print("Wear an raincoat")  # If the condition matches or the condition is true, so we get output as "Wear an raincoat"
else: # This is the otherwise condition, means if the condition does not matches, execute this block of code
    print("Don't wear an raincoat")
# Here we get output as "Dont wear an raincoat" because the condition does not matches or the specified condition is False

# Lets specify condition that, if its raining "Wear an raincoat" otherwise "Don't wear a raincoat" using boolean function
its_raining = False # Here i have assigned a variable its_raining and set it equal to False
its_snow = True
if its_raining: # This is the if condition, We  need to specify colon at the end to specify condition inside the block
    print("Wear an raincoat")  # If the condition matches or the condition is true, so we get output as "Wear an raincoat"
elif its_snow:  # If the else if condition matches or the condition is true, so we get output as "Snow season"
    print("Snow season")
else: # This is the otherwise condition, means if the condition does not matches, execute this block of code
    print("Don't wear an raincoat")
# Here we get output as "Snow season" because the condition matches or the specified condition is True

# Lets specify if else condition using operator
# We have........and,or,not operator to do our task in simple manner
# In "or" operator, if either one of the statement is true, the output will be true also if both the statement is true, the output will also be true
its_raining = False # Here i have assigned a variable its_raining and set it equal to False
its_snow = True # Here i have assigned a variable its_snow and set it equal to True
if its_raining or its_snow: # This will check whether raining or snow
    print("Climate is Bad")
else:
    print("Climate is good")
# Here we get output as "Climate is Bad" because one of the given condition is true

# Lets specify if else condition using operator
# We have........and,or,not operator to do our task in simple manner
# In "and" operator, the output will be true only when both the statements are true
its_raining = True # Here i have assigned a variable its_raining and set it equal to True
its_snow = True # Here i have assigned a variable its_snow and set it equal to True
if its_raining and its_snow: # This will check whether raining and its snow
    print("Climate is Bad")
else:
    print("Climate is good")
# Here we get output as "Climate is Bad" because one of the given condition is true

# Lets specify if else condition using operator
# We have........and,or,not operator to do our task in simple manner
# In "and" operator, the output will be true only when both the statements are true
its_raining = False # Here i have assigned a variable its_raining and set it equal to True
its_snow = False # Here i have assigned a variable its_snow and set it equal to True
if its_raining and its_snow: # This will check whether raining and its snow
    print("Climate is Bad")
else:
    print("Climate is good")
# Here we get output as "Climate is good" because one of the given condition is False

# Lets specify if else condition using operator
# We have........and,or,not operator to do our task in simple manner
# In "not" operator, True statement will be converted to False
# In "not" operator, False statement will be converted to True
its_raining = False # Here i have assigned a variable its_raining and set it equal to True
its_snow = False # Here i have assigned a variable its_snow and set it equal to True
if its_raining or not(its_snow): # This will check whether raining or its snow
    print("Climate is Bad")
else:
    print("Climate is good")
# Here we get output as "Climate is Bad" because one of the given condition is True

# Lets specify if else condition using operator
# We have........and,or,not operator to do our task in simple manner
# In "not" operator, True statement will be converted to False
# In "not" operator, False statement will be converted to True
its_raining = False # Here i have assigned a variable its_raining and set it equal to True
its_snow = False # Here i have assigned a variable its_snow and set it equal to True
if its_raining and not(its_snow): # This will check whether raining or its snow
    print("Climate is Bad")
else:
    print("Climate is good")
# Here we get output as "Climate is good" because one of the given condition is False