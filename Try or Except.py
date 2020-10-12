# In lot of situations we get an error, in python
# Sometimes you might able to understand what error it refers to
# But most of time we dont understand what kind of error its displaying

# To fix this issue we use "Try / Except" command
# It is nothing but, we are instructing python to try some block of code, if something goes wrong use except command to show what kind of error

# Example 1:
print(10/2) # This will print the answer as 5

"""
# Example 2:
print(5/0) # We know something divided by zero is infinity, so we will get error here
# So we get error as below,
"""
"""
Traceback (most recent call last):
  File "C:/Users/PycharmProjects/pythonProject/Try or Except.py", line 12, in <module>
    print(5/0) # We know something divided by zero is infinity, so we will get error here
ZeroDivisionError: division by zero 
"""
# Actually "ZeroDivisionError: division by zero" this is the error, many might not understand what kind of error its referring to.

# So inorder to fix this issue we are instructing python to use "Try Except" command
try: # Here we are instructing python to try 5/0
    print(5/0)
except: # Here we are instructing python, if you get error, display the below code
    print("Invalid Input, Please try again with correct input")
# when we run this we get output as "Invalid Input, Please try again with correct input", because its an error

"""
# Example:
value = int(input("Enter a value: ")) # Here user can enter only number, if he enters string, we will get error
print(value)
"""

# Example with Try Except:
try:
    value = int(input("Enter a value: ")) # Here user can enter only integer number
    print(value)
except: # If user enters other than integer number, display below code as error
    print("Invalid input")