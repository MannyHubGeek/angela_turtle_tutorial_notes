import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

manny = Turtle()
manny.shape("circle")
#manny.color("green")


# manny.forward(100)
# manny.right(90)
# manny.forward(100)
# manny.right(90)
# manny.forward(100)
# manny.right(90)
# manny.forward(100)
# manny.right(90)
# manny.forward(100)

# manny.hideturtle()
# for _ in range(4):
#     manny.forward(100)
#     manny.right(90)


# for _ in range(50):
#     manny.pendown()
#     manny.forward(20)
#     manny.penup()
#     manny.forward(20)


# def shape(sides):
#     ang = 360 / sides
#     for _ in range(sides):
#         manny.forward(100)
#         manny.right(ang)


# colors = ["red","orange","yellow","green","blue","indigo","purple"]
# for n in range(3, 11):
#     manny.pencolor(random.choice(colors))
#     shape(n)



# def shape():
#     manny.pensize(10)
#     posx = range(300)
#     posy = range(300)
#     manny.goto(random.choice(posy), random.choice(posx))
#     n = range(1, 500)
#     manny.speed(5)
#
#
# while True:
#     colors = ["red","orange","yellow","green","blue","indigo","purple"]
#     manny.pencolor(random.choice(colors))
#     shape()


# def walk():
#
#         n = range(1, 500)
#         manny.forward(random.choice(n))
#         manny.right(random.choice(n))
#         manny.left(random.choice(n))
#         manny.backward(random.choice(n))
#
# while True:
#     colors = ["red","orange","yellow","green","blue","indigo","purple"]
#     manny.pencolor(random.choice(colors))
#     walk()






def walk():
    manny.pensize(10)
    directions = [0, 90, 180, 270]
    manny.forward(30)
    manny.setheading(random.choice(directions))
    manny.speed(5)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g, b)
    return random_color


while True:
    n = range(255)
    manny.color(random_color())
    walk()






















screen = Screen()
screen.exitonclick()