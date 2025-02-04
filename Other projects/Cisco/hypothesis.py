number = int(input("Enter a number to test Collatz' hypothesis: "))
steps = 0

if number <= 0:
    print("Please enter a number greater than 0")
else:
    print(f"Starting value: {number}")


    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)
        steps += 1

    else:
        print(f"There were {steps} steps")