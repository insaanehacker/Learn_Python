# In a lot of situation you must read a file, whether it may be a text or csv or anything
# This can be done by inbuilt read function in python
# If we have the file in our same directory we can directly access it by specifying file name
# But if we have the file in another directory, we must specify the directory followed by the file to access it

# To read a file we need to open it right?
# So first we use open command
# I have specified a text file inside my directory
Read_my_file = open("read.txt", "r") # "r" specifies read command in python
print(Read_my_file.read()) # "read()... is a function which allow us to read the file
Read_my_file.close() # After reading just close the file

# We can also check the file is readable or not using readable function
Read_my_file = open("read.txt", "r") # "r" specifies read command in python
print(Read_my_file.readable()) # "readable()....function will display True or False
                               # We get True if file is readable, and False if its not readable
                               # Here we get otput as True, because we specified python to read file using "r" function
Read_my_file.close() # After reading just close the file

# We can also able to read a file line by line
Read_my_file = open("read.txt", "r") # "r" specifies read command in python
print(Read_my_file.readline()) # "readline()....function will allow us to read line by line
Read_my_file.close() # After reading just close the file

print("\n")

# We can also able to read a file line by line
# Here we will use for loop to print line by line, because its difficult to specify print again and again using print command for each line
Read_my_file = open("read.txt", "r") # "r" specifies read command in python
for read in Read_my_file:
    print(read) # This will read line by line
Read_my_file.close() # After reading just close the file

# We can also able to read lines using readlines()
Read_my_file = open("read.txt", "r") # "r" specifies read command in python
print(Read_my_file.readlines()) # "readlines()....function will allow us to read lines as list
Read_my_file.close() # After reading just close the file

print("\n")

# We can also able to access the list by specifying index number
Read_my_file = open("read.txt", "r") # "r" specifies read command in python
print(Read_my_file.readlines()[1]) # "readlines()["index number of list"]....function will allow us to access a specific item in a list
                                   # Here we have given index value as 1, so we will get output as 'data = xyz' only
Read_my_file.close() # After reading just close the file