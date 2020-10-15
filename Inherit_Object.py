# Now we need to call the function in class, but before we need to import our both classes
from Inheritance import school # Inheritance is the file and school is the class
from Inherit_Class_2 import school_data # Inheritance_Class_2 is the file and school_data is the class

# Now lets assign a new variable to each class, separately
School_main = school() # School() refers to the "school" class, ().......refers the self
School_Dummy = school_data() # School_Dummy() refers to the "school_data" class, ().......refers the self

# Now we can call the function using our variable easily
print(School_main.teacher())   # This will print "I am teaching my students",
                               # Here teacher() refers to the teacher function in class

print(School_main.student())   # This will print "I am listening listening to my teacher",
                               # Here student() refers to the student function in class
                               
print(School_Dummy.register()) # This will print "This defines the attendance register",
                               # Here register() refers to the register function in class



