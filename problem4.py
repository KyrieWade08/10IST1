def main():
    while True:
        try:
            number = int(input("Enter a number (enter 999 to stop): "))
            
            if number == 999:
                print("Program Terminated")
                break
            elif number < 0:
                print(" Please enter a positive number.")
            else:
                print(f"The binary representation of {number} is {bin(number)[2:]}")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
