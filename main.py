# pylint:disable=E1101
import pandas as pd
from turtle import Turtle, Screen

IMG = "blank_states_img.gif"

turtle = Turtle()
turtle.hideturtle()
screen = Screen()
screen.title("Guess U.S. States Game")
screen.setup(width=725, height=491)
screen.tracer(0)
screen.addshape(IMG)
screen.bgpic(IMG)


data = pd.read_csv("50_states.csv")
data["state"] = data["state"].str.lower()
# lowered_to_dict = data.to_dict()
print(data["state"])
is_game_running = True
list_of_guessed_states = []
while is_game_running:
    screen.update()
    if len(list_of_guessed_states) != 50:
        guess_input = screen.textinput(
            f"{len(list_of_guessed_states)}/50 States Correct",
            "What's another state name?",
        )
        if (guess_input.lower() in data.values) and not (
            guess_input.lower() in list_of_guessed_states
        ):
            list_of_guessed_states.append(guess_input.lower())
            turtle.penup()
            turtle.hideturtle()
            coords = data[data.state == guess_input.lower()]
            turtle.goto(int(coords.x) - 10, int(coords.y))
            turtle.write(
                arg=f"{guess_input.capitalize()}", font=("Courier", 8, "normal")
            )
    elif len(list_of_guessed_states) == 50:
        print("You have guessed all 50 states!")
        is_game_running = False


screen.mainloop()
