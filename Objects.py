# We already defined only overall structure in our student class
# Now we need to pass some interior data...This is the called object

# In order to use class we must need to import it from "Student" to our program
from Student import students # "Student" refers to our Student.py file and "student" refers to the class

# We already defined our function, now lets call it and enter the parameters
Student_Record_1 = students("Jim", "Five", "Second", "Eight", "Pass") # over here we are giving dat to our function parameter
print(Student_Record_1.name) # This will print student name
print(Student_Record_1.classroom) # This will print student classroom
print(Student_Record_1.floor) # This will print student floor
print(Student_Record_1.age) # This will print student age
print(Student_Record_1.academic) # This will print student academic

