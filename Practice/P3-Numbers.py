# There are three numeric types in Python:int, float and complex

x = 1   # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
print("----------------------------------")

#Integers: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x1 = 1
y1 = 35656222554887711
z1 = -3255522

print(type(x1))
print(type(y1))
print(type(z1))
print("----------------------------------")

#Float: Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x2 = 1.10
y2 = 1.0
z2 = -35.59

print(type(x2))
print(type(y2))
print(type(z2))
print("----------------------------------")

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x3 = 35e3
y3 = 12E4
z3 = -87.7e100

print(type(x3))
print(type(y3))
print(type(z3))
print("----------------------------------")

#Complex: Complex numbers are written with a "j" as the imaginary part:

x4 = 3j
y4 = -3j
z4 = 3.0j

print(type(x4))
print(type(y4))
print(type(z4))
print("----------------------------------")

#Type Conversion: You can convert from one type to another with the int(), float(), and complex() methods:

x5 = 1    # int
y5 = 2.8  # float
z5 = 1j   # complex

#convert from int to float:
a = float(x5)

#convert from float to int:
b = int(y5)

#convert from int to complex:
c = complex(x5)

print(a)
print(b)
print(c)
print("----------------------------------")
print(type(a))
print(type(b))
print(type(c))