# We will code a cool calculator with python, that will add a two numbers and display result

n1 = input("Enter the first number :") # This will get first number from user
n2 = input("Enter the second number: ") # This will get second number from user
print("The answer is:")
result = n1 + n2
print(result) # when we print it we dont get exact output, because the input type is form of string

# Inorder to rectify it, we can use int and float, but int cant handle with decimal numbers, but float can handle with decimal numbers

# Dealing with int ------ deals with whole numbers only
num1 = input("Enter the first number :") # This will get first number from user
num2 = input("Enter the second number: ") # This will get second number from user
print("The answer is:")
result = int(num1) + int(num2) # We are instructing, the number must be whole number
print(result) # when we print it we get the result

# Dealing with float
numb1 = input("Enter the first number :") # This will get first number from user
numb2 = input("Enter the second number: ") # This will get second number from user
print("The answer is:")
result = float(numb1) + float(numb2) # We are instructing, the number must be float type, so it can handle whole number too
print(result) # when we print it we get the result

