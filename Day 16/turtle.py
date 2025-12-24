import pokemon
from pokemon import Turtle, Screen

# Object = Class
kee = Turtle()
# Use a method
kee.shape("turtle")
kee.color("hot pink")
kee.forward(100)
print(kee)


my_screen = Screen()
# Use turtle attributes
print(my_screen.canvheight)

# Use a method
my_screen.exitonclick()