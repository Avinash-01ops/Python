#Strings in python are surrounded by either single quotation marks, or double quotation marks.'hello' is the same as "hello".

a = "Hello,World"
print(a)

#lowercase
print("Print lowercase string")
print(a.lower())

#uppercase
print("Print uppercase string")
print(a.upper())

#Remove Whitespace: Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
print("Remove whitespaces from string")
print(a.strip())

#Replace String: The replace() method replaces a string with another string
print("Replace string")
print(a.replace("H", "J"))

#Split String: The split() method splits the string into substrings if it finds instances of the separator
print("Split, string")
print(a.split(",")) # returns ['Hello', ' World!']

#Count String: The count() method returns the number of times a specified value occurs in a string
print("Count string")
print(a.count("l"))

#Slicing: You can return a range of characters from a string by using the slice syntax.
print(a[2:5])

#String Concatenation: To concatenate, or combine, two strings you can use the + operator.
b = "Hello"
c = "World"
d = b + c
print(d)
print(b+" "+c)



