from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
screen.title("Random Walk")

turtle = Turtle()
turtle.speed("fastest")
turtle.pensize(10)

colours = ["red", "blue", "green", "yellow", "purple", "orange"]

for _ in range(100):
    turtle.forward(30)
    turtle.color(random.choice(colours))
    turtle.right(random.choice([0, 90, 180, 270]))

screen.exitonclick()