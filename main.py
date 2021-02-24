from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")

# MAKES A SQUARE
# for _ in  range(4):
#     tim.forward(100)
#     tim.left(90)

# DRAW DASHED LINE
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# DRAW SHAPES
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for sides in range(3, 11):
#     colors = ["red", "orange", "blue", "yellow", "purple", "black", "gray", "green"]
#
#     tim.color(random.choice(colors))
#     draw_shape(sides)

#RANDOM WALK
# tim.hideturtle()
# tim.speed(10)
# tim.pensize(10)
#
#
# direction = [0, 90, 180, 270]
# colors = ["red", "orange", "blue", "pink", "purple", "green", "gold"]
#
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(direction))
#     tim.forward(30)


screen = Screen()
screen.exitonclick()
