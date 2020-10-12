# Sometimes we need to print every item in  a list or string or array or something
# Its very hard to print it manually
# To fix this issue we use for loop
# Condition for for loop:
        # for any variable in string or array or any data type: ...................do something

# For loop can print out every iteration in a item or something
# Example
my_string = "I love my country" # Here I have assigned a variable my_string and set it equal to a value
for string in my_string: # Here i have used for loop to print every word in my_string variable
    print(string) # This will print each letter in my_string one by one
# Output:
"""I

   l
   o
   v
   e

   m
   y

   c
   o
   u
   n
   t
   r
   y
"""
# print number in for loop
for number in range(10): # Here i have used for loop to print from "0 to 9", 10 will be neglected
    print(number) # This will print each number one by one from "0 t 9"

# We can use for loop to iterate a data or element  in an array
my_array = ["Jim", "Jack", "Carl"] # Here i have assigned a variable my_array and set it equal to a array value
for array in my_array: # Here i have used for loop to print every item in my_array variable
    print(array) # This will print every item in my_string one by one

# We can use for loop to consider only specific range
my_array = ["Jim", "Jack", "Carl", "Dolby"] # Here i have assigned a variable my_array and set it equal to a array value
for array in range((len(my_array))): # Here i have used for loop to print every item in my_array variable and range is to specify the range in my_variable element
    # We already know that len().....is used to find the length of value
    print(my_array[array]) # We pass our index too..[]..to print our data, because without passing index data, python cant process with the list

# We can also directly specify the range number
my_array = ["Jim", "Jack", "Carl", "Dolby"] # Here i have assigned a variable my_array and set it equal to a array value
for array in range(3): # Here i have used for loop to print every item in my_array variable and here range(3) refers the third item in the list

    print(my_array[array]) # We pass our index too....to print our data, because without passing index data, python cant process with the list without index
    # When we run we should get output as "jim, jack and carl" , because in range...last element will be neglected, so "Dolby" will get neglected

# Lets create a game
# If the index is 2 we must get output as "You won" or else we must get output as "You loose"
my_sample = ["friends", "fruit", "temple", "ghost"]
for sample in range(len(my_sample)):
    if sample == 2: # This specifies the length in my_sample is 2
        print("You won")
    else: # Or else print you loose
        print("You loose")

