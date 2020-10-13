# In python we can use any datatype to build our program
# But its very difficult to crete complex data in real world programming
# So we use Class and Objects to make our job simpler
# With class we can able to create our own datatype, and objects is used to give birth to our class
# Generally "Class" is like an instrument's which helps externally or simple means a map or overall structure
# "Objects" is like an main tool to perform our task internally
# For example, with class and objects we can model a phone or water bottle or anything we want

# Imagine you have are in your school, your classroom will be empty without students
# We never ever call it as empty classroom
# Similarly when we use keyword "class" we are just referring to overall structure of the class and not referring interior data or organization
# We all know that a classroom without students are useless
# Here i am referring to objects, means it makes sense when students are in class....it means students are the interior data....
# The interior data we are referring is called an objects

# Now lets create a class named students
# When we use "class" we are only referring to overall structure
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


# The above data only defines the overall structure of classroom and students
# To define the attributes internally, we use objects
