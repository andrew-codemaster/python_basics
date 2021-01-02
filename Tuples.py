# Tuples in Python

# Like a list but can't modify elements in a tuple

tuple_fruit = ("apples", 4, "bananas", 5, "oranges", 6)
print(tuple_fruit)
print(type(tuple_fruit))

list_fruit = ["apples", 4, "bananas", 5, "oranges", 6]
print(list_fruit)
print(type(list_fruit))

# We can modify elements within a list
# We can't modify elements within a tuple
list_fruit[0] = "strawberries"
print(list_fruit)

# We can perform similar operations on tuples

# Slicing Tuples
print(tuple_fruit[0:5])

# Concatenation of tuples
tuple_fruit = tuple_fruit[0:4] + ("cherries", 10)
print(tuple_fruit)

# Proper notation for tuple with one element
x = (5, )
print(type(x))

# Length of a tuple
print(len(tuple_fruit))

# Another way to create a tuple
another_tuple = tuple(("Hello", 18, True))
print(type(another_tuple))

# Converting a tuple to a list and back

tuple_fruit = list(tuple_fruit)
print(type(tuple_fruit))

tuple_fruit.append("Pears")

tuple_fruit = tuple(tuple_fruit)
print(tuple_fruit)
print(type(tuple_fruit))

# Unpacking tuples
fruit = ("apples", "bananas", "pears", "oranges", "blueberries")

(one, two, three, four, five) = fruit
print(one)

# An * assigns the remaining elements to that element
(one, two, *three) = fruit
print(one)
print(two)
print(tuple(three))

# Incorporate loops with tuples
for i in range(len(fruit)):
    print(fruit[i])




