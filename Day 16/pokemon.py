from unittest.mock import DEFAULT

from prettytable import PrettyTable

# Object = Class
table = PrettyTable()
name = table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
types = table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])

table.border = True
table.padding_width = True
print(table)
