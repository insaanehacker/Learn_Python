# Lists and Tuples are same but Tuples have some key definitions modified themselves
# Tuples are immutable......The word immutable means the dta cant be mofied or changed after assigning them
# Lists are mutable....because we can change them as we like or modify them even after assigning

# Tuples are assigned by........().........
# Lets assign a variable to tuples
my_name = ("Ramesh", "Suresh")
   #          0         1..........These are index
   # Index in tuples start with 0
print(my_name) # we get output as Ramesh and suresh

# Now lets modify the values in the tuples using index
my_name = ("Ramesh", "Suresh")
   #          0         1..........These are index
my_name[1] = "John"
print(my_name) # When we print it...we will get error: "object does not support item assignment", because the item in the tuples cant be changed

# In tuples once a item is assigned it cant be changed or modified again...We use tuples in comples situation like a data should be assined, but it shoud not be modified or changed at any cause.

# Another example
coordinates = (2, 3)
coordinates[1] = 9
print(coordinates[1]) # When we print it...we will get error: "object does not support item assignment", because the item in the tuples cant be changed