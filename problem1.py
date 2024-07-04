choice = int(input("Type 1 to convert celcius to fahrenheit. \Type 2 to convert fahrenheit to celcius."))

if choice == 1:
    Celcius1= int(input("What is the temperature in celsius"))
    Fahrenheit1 = (Celcius1 * 9 / 5 + 32)
    print("The temperature in fahrenheit is", Fahrenheit1, "degrees." )

if choice == 2:
    Fahrenheit2 = int(input("What is the temperature in fahrenheit?"))
    Celcius2 = ((Fahrenheit2-32)/1.8)
    print("The temperature in celcius is", Celcius2, "degrees.")
