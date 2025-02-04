# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John")
beatles.append("Paul")
beatles.append("George")
print("Step 2:", beatles)

# step 3
rest_of_the_band = ["Stu", "Pete"]

for member in rest_of_the_band:
    beatles.append(member)
    
print("Step 3:", beatles)

# step 4
for member in range(len(beatles)):
    print (beatles[member])
# print("Step 4:", beatles)