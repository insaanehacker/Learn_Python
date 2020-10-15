from Inheritance import school # Inheritance is the file and school is the class

# Now lets create another class here
class school_data(school): # Here inside the "school_data" class, we are inheriting our old class "school"
    def register(self):
        return "This defines the attendance register"


