import pandas as pd
from turtle import Turtle, Screen

IMG = "blank_states_img.gif"

turtle = Turtle()
screen = Screen()
screen.title("Guess U.S. States Game")
screen.setup(width=800, height=500)
screen.addshape(IMG)
turtle.shape(IMG)


screen.mainloop()
