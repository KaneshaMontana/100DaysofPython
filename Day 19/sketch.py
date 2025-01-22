from turtle import Turtle, Screen

kee = Turtle()
screen = Screen()


def move_forwards():
    kee.forward(10)

def move_backwards():
    kee.backward(10)

def move_clockwise():
    kee.right(10)


def move_counter_clockwise():
    kee.left(10)

def clear_drawing():
    kee.clear()
    kee.reset()

screen.listen()
screen.onkey(key="f", fun=move_forwards)
screen.onkey(key="b", fun=move_backwards)
screen.onkey(key="c", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="r", fun=clear_drawing)
screen.exitonclick()
