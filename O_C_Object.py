from Object_Functions import students # Object_Function is file and students is class

student_1 = students("Jim", "Five", "Second", "8", "Pass")
                                                                # Here we are calling function defined inside class
student_2 = students("Jim", "Five", "Second", "9", "Pass")

print(student_1.check_in_school()) # We get result as "Student in school", because age is 8
print(student_2.check_in_school()) # We get result as "Student escaped from the school", here age is not equal to 8
