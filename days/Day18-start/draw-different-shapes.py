from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()   
exit = False
while not exit:
    shape = screen.textinput(title="Choose a shape", prompt="What shape would you like to draw? (circle, square, triangle, dashed line)")

    if shape == "circle":
        tim.circle(50)
    elif shape == "square":
        for _ in range(4):
            tim.forward(100)
            tim.right(90)
    elif shape == "triangle":
        for _ in range(3):
            tim.forward(100)
            tim.right(120)
    elif shape == "dashed line":
        for i in range(20):
            tim.forward(15)
            tim.penup()
            tim.forward(15)
            tim.pendown()
    else:
        exit = True
