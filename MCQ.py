# Now lets create multiple choice questions, which will get answer from the user and checks it correct or wrong
# At last to display the marks based on it
# This can be done with the help of string and variables, but it can be made simple with our class and objects

# Lets create a class and def initialize function
class Question_Parameters:
    def __init__(self, Questions_Prompt, U_Answer):
        self.Questions_Prompt = Questions_Prompt # This will assign Question object to Questions we pass
        self.U_Answer = U_Answer # This will assign Answer object to Answer we pass

# Now our class is defined, so next job is to define a function that will define questions as object
