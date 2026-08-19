from turtle import Turtle , Screen
import random
import turtle

tim = Turtle()
screen= Screen()
turtle.colormode(255)
tim.speed("fastest")
tim.pensize(10)

directions = [0, 90, 180, 270]

def my_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b) 

for _ in range(100):
    tim.color(my_color())
    tim.forward(30)
    tim.right(random.choice(directions))

screen.exitonclick()
 