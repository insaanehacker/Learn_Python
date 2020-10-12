# Suppose we want to add  a bunch of data in python.....
# It is very tedious task to add a variable one by one and assigning value to it

# That's why lists help us to do it in a simple way

# List is denoted by '[]' ........two square brackets,
# Inside the square brackets...we specify our values or data

# Example
country = ["America", "Ethiopia", "Africa", "India"] # I have specified a values to my list
     #        0           1          2         3     ................These are the index

print(country) # This will print everything in the list

# What to do if we want to access a particular element in the list
# Here comes our index....It will allow us to access a item in a list
# In lists, index starts with 0
country = ["America", "Ethiopia", "Africa", "India"] # I have specified a values to my list
     #        0           1          2         3     ................These are the index
print(country[0]) # This will display output as America

# Suppose we want to access all elements starting from a specific element and dont want to access others
# Suppose we want to access ethiopia, afica and india only
country = ["America", "Ethiopia", "Africa", "India"] # I have specified a values to my list
     #        0           1          2         3     ................These are the index
print(country[1:]) # This will print starting from ethiopia to last.....Because ethiopia is in index of 1

# We can also specify range in list
country = ["America", "Ethiopia", "Africa", "India"] # I have specified a values to my list
     #        0           1          2         3     ................These are the index
print(country[0:3]) # This will print america, ethiopia and africa.....India will be excluded...
# India will be excluded from the list because, in range....the last element will not be considered

# We can also able to replace a specific element in the list
country = ["America", "Ethiopia", "Africa", "India"] # I have specified a values to my list
     #        0           1          2         3     ................These are the index
country[1] = "London" # This will replace ethiopia by london
print(country)

# We can also specify index no by negative
country = ["America", "Ethiopia", "Africa", "India"] # I have specified a values to my list
    #        -4           -3         -2        -1     ................These are the index
print(country[-4]) # This will print output as america, because america is in index -4

country = ["America", "Ethiopia", "Africa", "India"] # I have specified a values to my list
     #        0           1          2         3     ................These are the index
print(country.index("Ethiopia")) # This will display output as 1, because Ethiopia is in index 1
# Index is a function which is used to access element in  a list
