# 2D list or 2 Dimensional is nothing but it can hold any number of list inside a list
# Nested loop is nothing but we are specifying a for loop inside a for loop

# Example
my_2d_array = [
    [0, 1, 2],
    [3, 4, 5],      # These all are separate list inside a list...This is called as 2D list
    [6, 7, 8],
    [0]
]
print(my_2d_array) # This will print the entire list

print("\n")

# We can also able to access a individual item using index number
# In 2D list......we have rows and columns
my_2d_array = [
    [0,  1,  2], # Row 1..........index 0
    [3,  4,  5], # Row 2..........index 1
    [6,  7,  8], # Row 3..........index 2
    [0]          # Row 4..........index 3
    #C1 #C2 #C3
    #I0 #I1 #I2
]
# Lets now try to print number 4, This can be accessed by specifying index number by row and column
print(my_2d_array[1][1]) # This means we are instructing python take the row index as 1 and take the column index as 1....means first row and first column
                         # When we priint it we get 4 as output
# Lets now try to print number 7, This can be accessed by specifying index number by row and column
print(my_2d_array[2][1]) # This means we are instructing python take the row index as 2 and take the column index as 1....means second row and first column
                         # When we priint it we get 7 as output
print("\n")

# In 2D list......we have rows and columns
my_2d_array = [
    [0,  1,  2], # Row 1
    [3,  4,  5], # Row 2
    [6,  7,  8], # Row 3
    [0]          # Row 4
    #C1 #C2 #C3
]
for row in my_2d_array: # This will print the my_2d_array row one by one
    print(row) # This will print row

# Nested loop
for row in my_2d_array:
    for col in row: # We are instructing python that print the column in the row separately one by one
        print(col) # This will print the column one by one

