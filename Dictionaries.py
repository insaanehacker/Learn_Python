# When we hear the name dictionary, we need to realize that its something dealing with keys value pairs
# Keys are something we define and values are the pairs we set to key
# Dictionaries are denoted with.........{}...........
# Keys can hold any data type, but they must be unique, means the key assigned must be different from others

# Example
# Lets convert "mar" to "march" using dictionaries
convert_month = {"mar": "March"} # This will assign mar to March in dictionaries
print(convert_month["mar"]) # This will print March

# We can specify many keys and values followed by comma, but the condition is the keys must be unique
# Key and value can take any data type
data = {
    8: "I love America",
    "Feb": "February",
    3: True,
    4: 65.7,
    "num": 6,
    True : "Gift"
}
# Print output
print(data[8]) # This will print "I love America"
print(data["Feb"]) # This will print February
print(data[3]) # This will print True
print(data[4]) # This will print 65.7
print(data["num"]) # This will print 6
print(data[True]) # This will print Gift

print("\n")

# The above output can be printed using get function
print(data.get(8)) # This will print "I love America"
print(data.get("Feb")) # This will print February
print(data.get(3)) # This will print True
print(data.get(4)) # This will print 65.7
print(data.get("num")) # This will print 6
print(data.get(True)) # This will print Gift
