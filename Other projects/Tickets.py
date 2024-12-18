print("Welcome to the our booking system\n")
height = int(input("How tall are you in cm?\n"))
age = int(input("How old are you?\n"))
bill = 0

if height > 120:
    if age < 12:
        bill = 5
        print("Child tickets cost £5\n")

    elif age <= 18:
        bill = 7
        print("Youth tickets are £7\n")

    elif age >= 45 and age <= 55:
        bill = 0
        print("You get a free adult ticket")
        
    else:
        bill = 12
        print("Adult tickets cost £12\n")
    
    photo = input("Do you want a photo taken? Y or N ").upper 
    if photo == "Y":
        bill += 3
    
    print(f"Your bill is £{bill}")
    
else:
    print("Sorry, you are not tall enough to get onto our rides\n")