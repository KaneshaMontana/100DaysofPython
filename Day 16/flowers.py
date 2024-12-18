# Understanding the difference between class, methods, attributes
# Understanding self

class flowers():
    def __init__(self, name, colour):
        self.name = name 
        self.colour = colour

    def get_name(self):
        return self.name

    def get_colour(self):
        return self.colour


order1 = flowers("cherry blossom", "pink")
print(order1.get_name())
order2 = flowers("rose", "red")
print(order2.get_colour())