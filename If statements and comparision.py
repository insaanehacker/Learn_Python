# We already learnt the basics of if else statements, where to use it......etc
# Now lets use the same if statements inside our function to do our task using comparision operators
# >= ...........greater than equal to
# <= ...........less than equal to
# == ...........This checks whether the assigned function is equal or not
# != ...........not equal to


# Now lets check the maximum number using if statements using our function
def f_max(data1, data2, data3): # Here i have defined function and passed three parameters
    if data1 >= data2 and data1 >= data3: # This checks whether data1 is greater than all or not
        return data1 # This will return data1 value to console if the condition matches
    elif data2 >= data1 and data2 >= data3: # This checks whether data2 is greater than all or not
        return data2 # This will return data1 value to console if the condition matches
    else: # This is else condition if no condition matches, use the else condition as output
        return data3 # This will return data1 value to console if the condition matches

print(f_max(37,12,37.7)) # We use return statements in our function, inorder to print our output we need to specify print statements and the call our function with our parameters
# We should get output as 37.7, because 3.5 is the maximum value.

# Now lets check the minimum number using if statements using our function
def f_max(data1, data2, data3): # Here i have defined function and passed three parameters
    if data1 <= data2 and data1 <= data3: # This checks whether data1 is lesser than all or not
        return data1 # This will return data1 value to console if the condition matches
    elif data2 <= data1 and data2 <= data3: # This checks whether data2 is lesser than all or not
        return data2 # This will return data1 value to console if the condition matches
    else: # This is else condition if no condition matches, use the else condition as output
        return data3 # This will return data1 value to console if the condition matches

print(f_max(37,12,37.7)) # We use return statements in our function, inorder to print our output we need to specify print statements and the call our function with our parameters
# We should get output as 12, because 3.5 is the minimum value.