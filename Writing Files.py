# In a lot of situation you must write a file, create a new file, add changes to existing file
# This can be done by inbuilt write function in python
# If we have the file in our same directory we can directly access it by specifying file name
# But if we have the file in another directory, we must specify the directory followed by the file to access it
# File can be anything like html,text,csv......etc
# Write() command can handle with all the types of data
# But we must be safe, if we run the file again and again, the data can be assigned un properly while appending data to our exiting file or changing data to our existing file

# To  write a file we need to open it right?
# So first we use open command
# I have specified a text file inside my directory
# Lets append a new text line to our text file
# Append function will add a new text or data to the end of the line
Write_my_file = open("write.txt", "a") # "a" will add a new line to the end of out text line or anything
print(Write_my_file.write("\nLike - Computer")) # "write()...is a function which allow us to write or change modification in existing file
                                              # This will add a new text or data "Like - Computer" to our existing file
Write_my_file.close() # After writing just close the file

# Write function will allow us to write to our existing file or create a new file
# Lets create a new file using write function
Write_my_file = open("write1.txt", "w") # "w" will write data to our existing file or it can even create a new file
                                        # Here when we run this program, It automatically creates a new file write1.txt
print(Write_my_file.write("\nLike - Computer")) # "write()...is a function which allow us to write or change modification in existing file
                                              # This will add a new text or data "Like - Computer" to our existing file
Write_my_file.close() # After writing just close the file

