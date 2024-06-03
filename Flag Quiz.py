import turtle
import random

scn = turtle.Screen()
scn.bgcolor("white")
points = 0
lives = 3
currentFlag = None

t = turtle.Turtle()
turtle.title("My Turtle Program")
t.pu()


def germany():
    t.goto(0, 0)
    t.fillcolor("black")
    t.pd()
    t.begin_fill()
    # Black
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    # Red
    t.goto(0, -30)
    t.fillcolor("red")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    # Yellow
    t.goto(0, -60)
    t.fillcolor("yellow")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()


def lithuania():
    t.goto(0, 0)
    t.fillcolor("yellow")
    t.pd()
    t.begin_fill()
    # Yellow
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    # Green
    t.goto(0, -30)
    t.fillcolor("green")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    # red
    t.goto(0, -60)
    t.fillcolor("red")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()


def spain():
    t.goto(0, 0)
    t.fillcolor("red")
    t.pd()
    t.begin_fill()
    # red
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(20)
        t.rt(90)
    t.end_fill()
    t.pu()
    # yellow
    t.goto(0, -20)
    t.fillcolor("yellow")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(40)
        t.rt(90)
    t.end_fill()
    t.pu()
    # red
    t.goto(0, -60)
    t.fillcolor("red")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(20)
        t.rt(90)
    t.end_fill()
    t.pu()


def russia():
    t.goto(0, 0)
    t.fillcolor("white")
    t.pd()
    t.begin_fill()
    # white
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    # blue
    t.goto(0, -30)
    t.fillcolor("blue")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()
    # red
    t.goto(0, -60)
    t.fillcolor("red")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()
    t.pu()


def poland():
    t.goto(0, 0)
    t.fillcolor("white")
    t.pd()
    t.begin_fill()
    # white
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(45)
        t.rt(90)
    t.end_fill()
    t.pu()
    # Red
    t.goto(0, -45)
    t.fillcolor("red")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(45)
        t.rt(90)
    t.end_fill()
    t.pu()


def indonesia():
    t.goto(0, 0)
    t.fillcolor("red")
    t.pd()
    t.begin_fill()
    # red
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(45)
        t.rt(90)
    t.end_fill()
    t.pu()
    # white
    t.goto(0, -45)
    t.fillcolor("white")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(90)
        t.fd(45)
        t.rt(90)
    t.end_fill()
    t.pu()


def italy():
    t.goto(0, 0)
    t.fillcolor("green")
    t.pd()
    t.begin_fill()
    # green
    for i in range(2):
        t.fd(50)
        t.rt(90)
        t.fd(80)
        t.rt(90)
    t.end_fill()
    t.pu()
    # white
    t.goto(50, 0)
    t.fillcolor("white")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(50)
        t.rt(90)
        t.fd(80)
        t.rt(90)
    t.end_fill()
    t.pu()
    # red
    t.goto(100, 0)
    t.fillcolor("red")
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(50)
        t.rt(90)
        t.fd(80)
        t.rt(90)
    t.end_fill()
    t.pu()


flags = [germany, lithuania, spain, russia, poland, indonesia, italy]

while lives > 0 and len(flags) > 0:
    t.reset()
    currentFlag = random.choice(flags)
    currentFlag()

    inputFlag = input("What countries flag is this? (lower Case): ")

    if inputFlag == currentFlag.__name__:
        flags.remove(currentFlag)
        points += 1
    else:
        lives = lives - 1
    print(f"You have {points} points and {lives} lives. ")

if lives <= 0:
    print("You died")
else:
    print("You won!")

turtle.exitonclick()
