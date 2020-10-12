# Lets make simple calculator that will do our exponent function
# 2^3 is 8.......means 2*2*2 = 8

# we will do this with function and for loop
def power_calculator(base_number, power_number): # We defined a function with two parameters..base and power number
    Result = 1 # setting variable equal to 1, it means we are assuming let result to be 1 initially
    for p_c in range(power_number): # Setting for loop in range of power number, so power_number will be excluded and before number will only be considered
        # Example if 3 is given, power_number will be excluded and 3 will be considered as input
        Result = Result * base_number # This will calculate the exact answer, this means the result will be multiplied with base number
    return Result # This will display the result to console

print(power_calculator(2, 3)) # When we call the function and specify the parameter value, we get the answer, here we get answer as 8, because...2^3 =8

# This time will get input from the user
base_number = int(input("Enter the base number: ")) # Here we assigned a variable base_number and we get input frm the user, exponent function must be whole number, so we use int, because to specify we use integer or whole number as input
power_number = int(input("Enter the base number: "))# Here we assigned a variable power_number and we get input frm the user, exponent function must be whole number, so we use int, because to specify we use integer or whole number as input
def power_calculator(base_number, power_number): # We defined a function with two parameters..base and power number
    Result = 1 # setting variable equal to 1
    for p_c in range(power_number): # Setting for loop in range of power number, so powernumber will be excluded and before number will be considered
        # Example if 3 is given, power_number will be excluded and 3 will be considered as input
        Result = Result * base_number # This will calculate the exact answer
    return Result # This will display the result to console

print(power_calculator(base_number, power_number)) # When we call the function and specify the parameter value, the base and power number will be obtained from the user directly



