while True:
    number = int(input("Enter a number (enter 999 to stop): "))
    
    if number == 999:
        print("Program Terminated")
        break
    elif number < 0:
        print("Please choose a positive number.")
    else:
        print(f"The binary representation of {number} is {bin(number)[2:]}")
