hat_list = [1, 2, 3, 4, 5]

replace = int(input("Enter a number to replace the middle number: "))

hat_list[2] = replace
print(hat_list)

del hat_list[4]
print(hat_list)

print(len(hat_list))