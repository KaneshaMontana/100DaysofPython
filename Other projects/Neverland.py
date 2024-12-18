('''
                                 \__/,'`.,'`._,
                                /,-. \  /    <_,
                                > - )/ /     <_,
                                \__,/ /      ,'
                                _/_(_/______/__
                               ( (_ ,,--'---^,\\
                           ___/ \   / ___,'
                          /,---' \\ \_   `.
                          `      /    `.   \
                                 |      \_  \
                                 |/\/\/\| `. \
                                  \ |  /\   `.`.
                                   \( /\ \    `.`.
                                    | \ `.`._,  `-\_,
                                    | /|  `-' 
                                    |/\(
                                    |(_\\_
                                    | / \ (
                                   /_/gnv\_\
''')

print("Welcome to Neverland's maze\n")
print("Your mission, with the help of Tinkerbell, is to save the lost boys from Captain Hook\n.There are several traps set up so BEWARE!!!\n")
dec_1 = input("You enter the maze and there are two paths. Where do you want to go? Type 'L' or 'R':\n").upper()

if dec_1 == "L":
  print("You walk further into the maze and find a key\n")

elif dec_1 == "R":
    print("You fell into a pit of venomous spiders. GAME OVER\n")

else:
  print("Invalid character. Try again\n")

dec_2 = input("\nYou also come across a ladder that you can use to climb over, but Tinkerbell isn't sure it is safe\n.Do you listen to Tinkbell or do climb over?\n Type 'T' or 'C':").upper()

if dec_2 == "T":
    print("Tinkerbell leads you to a cave where the Lost Boys are being held\n")

elif dec_2 == "C":
    print("You attempt to use the ladder and end up breaking your legs. GAME OVER\n")

else:
  print("Invalid character. Try again\n")
    
    
dec_3 =  input("There are three doors.\n What door will you choose? 'Red', 'Green' or 'Yellow'.\n Type 'R', 'G', or 'Y':\n").upper()

if dec_3 == "R":
    print("You attempt to grab the door handle and get electrocuted. GAME OVER\n")

elif dec_3 == "G":
    print("You use the key and get the lost boys back to safety.\n")

elif dec_3 == "Y":
    print("Captain Hook finds you and locks you in. GAME OVER\n")

else:
  print("Invalid character. Try again\n")