# Imagine you have coded thousands of lines and suppose you want it again in your code
# It is impossible or its a tedious task to copy and paste everything one by one again
# That's why function comes into a role to make your job more simpler

# A function is defined by a key word........def variable name()...Inside () we pass values they are called parameters
# Lets define a function
def my_name():
    print("Hello") # We are instructing python to display output as "Hello"
#4 s....................These space are called indentation

                # When we run this, we dont get output because, we still dint call the function

# Lets define a function and call it
def my_name():  # I have defined function with a variable "my_name"
    print("Hello") # We are instructing python to display output as "Hello"
my_name() # Now we called the function using the same variable defined to the function
          # This will diplay output as "Hello"

# Example: Lets print our name and age using function
def my_data(name, age):  # Here the name and age inside the brackets are called parameters, you can give any parameters you want
    print("Hi " + name +", you are " + str(age))
my_data("Insaane", 32) # Now we called the function using the my_data variable defined to the function

# Example :Lets print our name and age with user input using function
def my_data():
    name = input("Enter your name :")
    age = input("Enter your age: ")
    print("Hi " + name +", you are " + str(age))
my_data() # Now we called the function using the my_data variable defined to the function

# So whenever you have group of codes, inorder to use them again we can group it into a function and we can use it  when needed by function call
