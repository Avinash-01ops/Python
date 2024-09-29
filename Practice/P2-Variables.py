#Varioable Names
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Assigning multiple values to variables in single line
x, y, z = "Apple","Orange","Mango"
print(x)
print(y)
print(z)

#Output multiple variables values
print(x+" "+y+" "+z)

#Global variable

x = "awesome"

def myfunc():
    print("Python is "+x)
myfunc()
