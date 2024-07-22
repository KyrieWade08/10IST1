def main():
    try:
        choice = int(input("Type 1 to convert Celsius to Fahrenheit.\nType 2 to convert Fahrenheit to Celsius.\n"))

        if choice == 1:
            try:
                Celsius1 = float(input("What is the temperature in Celsius? "))
                Fahrenheit1 = (Celsius1 * 9 / 5) + 32
                print("The temperature in Fahrenheit is", Fahrenheit1, "degrees.")
            except ValueError:
                print("Please enter a number")

        elif choice == 2:
            try:
                Fahrenheit2 = float(input("What is the temperature in Fahrenheit? "))
                Celsius2 = (Fahrenheit2 - 32) * 5 / 9
                print("The temperature in Celsius is", Celsius2, "degrees.")
            except ValueError:
                print("Please enter a number.")

        else:
            print("Please enter 1 or 2.")

    except ValueError:
        print("Please enter a number.")

if __name__ == "__main__":
    main()
