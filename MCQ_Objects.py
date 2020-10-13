# To use class in our object we must import it
from MCQ import Question_Parameters

# We need to assign questions to a variable, so lets use lists or array to assign questions
questions_prompt = [
    "What is the color of Rose?\n(a) Red\n(b) Green\n(c) Violet\n\n",
    "What is the color of Sky?\n(a) Red\n(b) Green\n(c) Blue\n\n",
    "What is the color of Apple?\n(a) Grey\n(b) Red\n(c) Violet\n\n",
]

# Now we need to assign correct answers associated with questions_prompt
C_Answer = [
    Question_Parameters(questions_prompt[0], "a"),
    Question_Parameters(questions_prompt[1], "c"),
    Question_Parameters(questions_prompt[2], "b"),
]



# Now lets define function ask lists of question we wanna ask with user
def Mcq_test(C_Answer):
    print("Enter your choice: ")
    Score = 0
    for test in C_Answer:
        U_Answer = input(test.Questions_Prompt)
        if U_Answer == test.U_Answer:
            Score += 1
        if Score == 3:
            print("Congrats you are brilliant")
        elif Score == 2:
            print("Try hard next time")
        else:
            print("You loose, Try again")
    print("You have scored " + str(Score) + "/" + str(len(questions_prompt)) + " Correct")

Mcq_test(C_Answer)



