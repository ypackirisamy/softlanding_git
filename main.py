from turtle import Turtle, Screen
import random


def random_steps(t_obj):
    step = random.randint(1, 11)
    t_obj.forward(step)


def main():
    colours = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle_names = []
    screen = Screen()
    screen.setup(width=500, height=400)
    user_input = (screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: " )).lower()
    y_pos = -120

    for i in range(len(colours)):
        t = Turtle(shape="turtle")
        t.penup()
        t.color(colours[i])
        y_pos = y_pos + 40
        t.goto(x=-230.0, y=y_pos)
        turtle_names.insert(i, t)

    end_of_screen = False
    win_status = "lose"
    position = 0

    while not end_of_screen:
        for i in range(6):
            random_steps(turtle_names[i])
            if turtle_names[i].xcor() >= 230:
                end_of_screen = True
                position = i

    if user_input == colours[position]:
        win_status = "win"

    print(f"The winner is the {colours[position]} turtle, You {win_status}!")

    screen.exitonclick()


main()

