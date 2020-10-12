# We already built an normal calculator that can able to get input from the user and perform basic addition
# Lets create a better calculator to perform, +,-,* and / using if statements here

# Example
First_num = float(input("Enter your first number: ")) # Here we get first number from user
oper_per = input("Enter your operator: ") # Here we get operator from user
Second_num = float(input("Enter your second number: ")) # Here we get second number from user

if oper_per == "+": # Here we are checking whether the operator is equal to "+"
    print(First_num + Second_num) # This will add first and second number
elif oper_per == "-": # Here we are checking whether the operator is equal to "-"
    print(First_num - Second_num) # This will subtract first number by second number
elif oper_per == "*":
    print(First_num * Second_num)  # This will multiply first and second number
elif oper_per == "/":
    print(First_num / Second_num)  # This will divide first number by second number
else:
    print("Invalid operator") # If the operator does not matches the specified one, Invalid operator will be printed
