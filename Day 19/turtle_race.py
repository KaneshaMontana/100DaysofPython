from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a colour: ")
colours = ["violet", "red", "yellow", "green"]
y_positions = [-90, -70,-50, -30]

all_turtles = []

for index in range(0,4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[index])  # Assign a color to the turtle
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])  # Position each turtle
    all_turtles.append(new_turtle)
        


screen.exitonclick()
