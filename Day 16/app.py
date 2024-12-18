from turtle import Turtle, Screen

# kee == object, Turtle == Class
kee = Turtle()
print(kee)

kee.shape("turtle")
kee.color("DeepPink1")
kee.forward(100)
kee.pen(shown=True, pencolor="Blue")
# kee.pensize(12)
# kee.penup(True)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
