# Lets build a simple program that can able to translate vowels to "s"
# vowels.........aeiou

def Translate(phrase): # Here we define function as Translate and phrase value
    Translator = "" # We set translator to empty string initially
    for letter in phrase: # This will take each letter in phrase
        if letter in "aeiou": # This will compare each letter in phrase with "aeiou", if condition matches
            Translator = Translator + "s"  # If we find vowels in phrase, replace the letter by s
        else:
            Translator = Translator + letter # Just print the actual word or letter, this means condition fails here

    return Translator


print(Translate("I love you")) # We specify the parameter as phrase "I love you" and we call the function

# But we can modify this program
phrase = input("Enter the phrase: ")  # This will get phrase from the user
def Translate(phrase): # Here we define function as Translator and pass phrase value
    Translator = "" # We set translator to empty string initially
    for letter in phrase: # This will take each letter in phrase
        if letter in "aeiouAEIOU": # This will compare each letter in phrase with "aeiou" or "AEIOU", if condition matches
            if letter.lower() in "aeiou": # This will check the letter is lowercase
                if letter.isupper(): # This will check the letter is upper case
                    Translator = Translator + "S"  # If we find vowels in phrase, replace the letter by S
                else:
                    Translator = Translator + "s"  # If we find vowels in phrase, replace the letter by s

        else:
            Translator = Translator + letter # Just print the actual word or letter, this means condition fails here

    return Translator


print(Translate(phrase)) # We specify the parameter as phrase and we call the function


# New my phrase
phrase = input("Enter the phrase: ")  # This will get phrase from the user
def Translate(phrase): # Here we define function as Translator and pass phrase value
    Translator = "" # We set translator to empty string initially
    for letter in phrase: # This will take each letter in phrase
        if letter in "aeiouAEIOU": # This will compare each letter with "aeiou" or "AEIOU", if condition matches
            if letter.islower(): # This will check the letter is lower case
                Translator = Translator + "s"  # If we find vowels in phrase, replace the letter by s
            else: # If the letter is not lower case, execute below code
                Translator = Translator + "S"  # If we find vowels in phrase, replace the letter by S
        else:
            Translator = Translator + letter # Just print the actual word or letter, this means condition fails here

    return Translator


print(Translate(phrase)) # We specify the parameter as phrase and we call the function