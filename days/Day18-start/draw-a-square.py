from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.color("green")

for i in range(4):
    timmy.forward(100)
    timmy.right(90) 

screen.exitonclick()    