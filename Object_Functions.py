# Class function is that we can use a function inside a class
# To modify or give a specific information about that class
 # Example
# Refer Class & Objects, it is same program, To show it as an example, i created new fine here
class students:
    # Inside class we need some students data right?
    # Lets define a function to represent student data
    # Most importantly in "class" we use initialize function to define our data
    def __init__(self, name, classroom, floor, age, academic): # "__init__(self)" is init or initialize function
                                                               # In "objects" when we enter the parameters "name, classroom, floor, age, academic", we are actaully calling this init function
                                                               # when we pass the "name, classroom, floor, age, academic" it gets stored in this attributes defined in the function
        # "self" is used hold the attributes in our function
        # Here "self" is referring to the attributes of "name, classroom, floor, age, academic"
        # self.something will assigns our data to actual attributes in our objects
        self.name = name # This will assigns, the actual attributes of the objects name is equal to the "name" parameter, this means the name of the student is equal to the name we passed in
        self.classroom = classroom # This will assigns, the actual attributes of the objects name is equal to the "class" parameter, this means the classroom of the student is quaual to the classroom we passed in
        self.floor = floor # This will assigns, the actual attributes of the objects name is equal to the "floor" parameter, this means the floor of the student is quaual to the floor we passed in
        self.age = age # This will assigns, the actual attributes of the objects name is equal to the "age" parameter, this means the age of the student is equal to the age we passed in
        self.academic = academic # This will assigns, the actual attributes of the objects name is equal to the "academic" parameter, this means the academic of the student is equal to the academic we passed in


# The above data only defines the overall structure of classroom and students based on age

# Now lets define a function inside a class to check whether the student in school or not
# Here we don't need to use init, only self is must here, self should be inside the parameters of the defined function
    def check_in_school(self): # Here we used self to call our object
        if self.age == "8":
            return "Student in school"
        else:
            return "Student escaped from the school"

