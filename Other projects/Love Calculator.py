print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

lovers = name1 + name2

# adding the TRUE words
t = lovers.count("t")
r = lovers.count("r")
u = lovers.count("u")
e = lovers.count("e")
true_score = str(t + r + u + e)

#  adding the LOVE words
l = lovers.count("l")
o = lovers.count("o")
v = lovers.count("v")
e = lovers.count("e")
l_score = str(l + o + v + e)

love_score = true_score + l_score
love_score_int = int(love_score)

# if statements
if (love_score_int < 10) or (love_score_int > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif (love_score_int >= 40) and (love_score_int <= 50):
    print(f"Your score is {love_score}, you are alright together.")
    
else:
    print(f"Your score is {love_score}.")