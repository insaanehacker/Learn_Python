# Inheritance is a simple concept to inherit a functionalities of a class inside a class
# In simple, Suppose inside a class we fined thousands of function now we want them to use in our new class
# Its very tedious task to copy and paste all of them, it makes our code lengthy too
# Instead we can use inheritance, In inheritance we are just inheriting a class inside a class

# Example
# we have created a class and defined two function inside a class
# Now we want the to use this class function in another class, instead of copy:paste we can inherit the class
class school:
    def student(self):
        return "I am listening listening to my teacher"

    def teacher(self):
        return "I am teaching my students"
