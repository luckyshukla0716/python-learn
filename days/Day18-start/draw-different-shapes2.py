from turtle import Turtle, Screen
import random

t = Turtle()

colours = ["red", "blue", "green", "yellow", "purple", "orange"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for _ in range(3, 11):
    t.color(random.choice(colours))
    draw_shape(_)        
    
