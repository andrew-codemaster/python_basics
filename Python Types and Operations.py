# Python Types

print(type("hello"))
print(type(12))
print(type(4.27))
print(type(False))

# Moving to integers
print(4.72, int(4.72))  # Python rounds down
print(4.05, int(4.05))

# Rounding up
print(4.72, int(4.72), int(round(4.72)))    # Use round command

# Moving strings to integers
print("12345", int("12345"))
print(type("12345"))
print(type(int("12345")))

# Moving to floats
print(float(18))
print(float(12345))

# Moving to strings
print(str(18))
print(str(19.5))
print(type(str(195.5)))
5
# Logical Operators
# There are 3 different logical op: 'and', 'or', 'not'

# and means both need to be true
x = 6
print(x > 0 and x < 5)
print(5 < x < 7)

# or means either can be true
y = 26
print(y % 2 == 0 or y % 3 == 0)

# not operator negates
z = 5
print(not(z == 4 or z == 6))
