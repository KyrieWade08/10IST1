choice = int(input("Enter 1 for Addition.\nEnter 2 for Subtraction.\nEnter 3 for Multiplication\nEnter 4 for Division\n"))

if choice < 1 or choice > 4:
    print("Please enter a number between 1 and 4.")
else:
    Num_1 = int(input("Type a number: "))
    Num_2 = int(input("Type another number: "))

    if choice == 1:
        result = Num_1 + Num_2
        print(f"{Num_1} plus {Num_2} equals {result}")
    elif choice == 2:
        result = Num_1 - Num_2
        print(f"{Num_1} minus {Num_2} equals {result}")
    elif choice == 3:
        result = Num_1 * Num_2
        print(f"{Num_1} times {Num_2} equals {result}")
    elif choice == 4:
        if Num_2 != 0:
            result = Num_1 / Num_2
            print(f"{Num_1} divided by {Num_2} equals {result}")
        else:
            print("Undefined.")
