# We already know that a list can hold bunch of data
# Now we are going to deal with functions in the list
# we use certain functions in the list to make our work more simple

my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_friends = ["Harry", "Don", "Jimmy", "Jack"] # I have assigned item in our list and set it to variable my_friends
print(my_country)
                # This both will print the value in the list respectively
print(my_friends)

# Imagine you have assigned thousands of item to the list, then u added new list....
# Now you want to combine both the previous list and current list
# Extend function helps us to combine two or more list as on list
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_friends = ["Harry", "Don", "Jimmy", "Jack"] # I have assigned item in our list and set it to variable my_friends
my_country.extend(my_friends) # Here I have  assigned a new variable and used extend function
# This will combine two list : my_country and my_friends and will assign it to variable my_country
print(my_country) # This will combine two list : my_country and my_friends and will assign it to variable my_country

# We can also add another item to the nd of the list
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_friends = ["Harry", "Don", "Jimmy", "Jack"] # I have assigned item in our list and set it to variable my_friends
my_friends.append("Mike") # This will add Mike to the end of my_friends list
print(my_friends)

# We can also insert any item in the list, To do it we need to specify index number which we want to insert item
# suppose we want to insert a item before London, Index number of London is 1
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_friends = ["Harry", "Don", "Jimmy", "Jack"] # I have assigned item in our list and set it to variable my_friends
my_country.insert(1, "South Africa") # London has index 1, then South Africa is the item we want to insert
print(my_country) # This will insert South Africa before London

# We can remove specific item from the list
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_friends = ["Harry", "Don", "Jimmy", "Jack"] # I have assigned item in our list and set it to variable my_friends
my_friends.remove("Don") # This will remove Don from my_friends list.. means inside () you need to specify the item you want to remove from the list
print(my_friends) # Don will be removed from the list and it display the rest output

# We can also remove the last item from the list
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_friends = ["Harry", "Jimmy", "Jack"] # I have assigned item in our list and set it to variable my_friends
my_friends.pop() # this will remove last iem from friends list....means pop will remove last item from the list
print(my_friends)

# We can find the index number in the list using index fuction
country = ["America", "Ethiopia", "Africa", "India"] # I have specified a values to my list
     #        0           1          2         3     ................These are the index
print(country.index("Ethiopia")) # This will display output as 1, because Ethiopia is in index 1
# Index is a function which is used to access element in  a list

# We can also create a copy of list and assign it to a variable
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_friends = ["Harry", "Jimmy", "Jack"] # I have assigned item in our list and set it to variable my_friends
my_dummy = my_country.copy() # This will copy the items of my_country to my_dummy
print(my_dummy) # This will displays output as my_country because its a copy of my_country list

# We can also count the item in the list
my_country = ["America", "London", "London", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
print(my_country.count("London")) # This will count London and displays 3, because London is repeated three times

# We can also sort or arrange the list in numerical or alphabetical order using sort function
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_country.sort() # This will arrange my_country element in alphabetical order
print(my_country)

# We can also reverse the item in the list
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_country.reverse() # This will reverse my_country element in reversed order
print(my_country)

# We can clear all the item in the list
my_country = ["America", "London", "Ethiopia", "India"] # I have assigned item in our list and set it to variable my_country
my_friends = ["Harry", "Jimmy", "Jack"] # I have assigned item in our list and set it to variable my_friends
my_country.clear() # This will clear all the item from the list
print(my_country) # This will displays empty list because everything in my_country list has been cleared using clear command
