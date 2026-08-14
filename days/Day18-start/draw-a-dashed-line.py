from turtle import Turtle, Screen

tim = Turtle()
tim.color("green")


for i in range(20):
    tim.forward(15)
    tim.penup()
    tim.forward(15)
    tim.pendown()   

screen = Screen()
screen.exitonclick()    