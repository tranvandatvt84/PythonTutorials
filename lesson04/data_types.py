import math


#String data type

# Literal assignment
first = "Dat"
last = "Tran"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(str(type(pizza) == str))
# print(str(isinstance(pizza, str)))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock mosuc from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?                    

I was just checked in.     
                        All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work! \tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                       "
multiline = "            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("X"))

# Boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric data types

# Integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(3.14)
print(type(gpa))
print(isinstance(gpa, float))

# Complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in fuctions for numbers

print(abs(gpa))

print(round(gpa))

print(round(gpa, 1))

# Math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you are attempt to cast incorrect data
# zip_value = int("New York")