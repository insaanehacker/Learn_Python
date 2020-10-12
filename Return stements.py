# Sometimes we must get a value from a function
# This can be obtained by using return statements
# Whenever we use return statements in our function in order to call the function we must specify print command to print output to the console


# Example without return statements
# Lets print a square of number using function
def sqr(number):
    number*number # This will square the number passed in function call parameter

sqr(16) # Here i have given parameter, means the number as 16, When we print this we dont get anything as output
# Because python does not return anything here

# Lets print the same using print
print(sqr(16)) # Here we get result as none, because python don't have anything to print as output

# Example with return statements
# Lets print a square of number using function
def sqr(number):
    return number*number # return statements will return the value or data we want

print(sqr(16)) # Here we get result as 256, because return statements is used to return the value

# We cant execute extra command in return statement while using function
# Example we will try to print "Hello World" after return statement in a function
def sqr(number):
    return number*number # return statements will return the value or data we want
    print("Hello world") # We dont get anything as output here, because whenever python see our return command only that code will be executed and rest will be neglected
    # only the return command will be executed and result will be printed over to the console.

print(sqr(16)) # Here we get result as 256, because return statements is used to return the value
