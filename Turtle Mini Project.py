# Let's draw with package turtle

# import turtle
import turtle

# Set-up turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("red")
turtle.speed(100)

# draw a square

# for loop from 0 to 4

# use ctrl + / to comment out a load of code
# for i in range(6):
#     turtle.forward(50)
#     turtle.left(60)
#     i = i + 1

# for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
#     turtle.color(colours)
#     turtle.circle(100
#     turtle.left(10)
# turtle.done()

for i in range(24):
    for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(2.5)
turtle.done()