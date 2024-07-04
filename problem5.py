choice = int(input("Enter 1 for addition. \nEnter 2 for subtraction. \nEnter 3 for multiplication\nEnter 4 for division"))
Num_1=int(input("Type a number"))
Num_2=int(input("Type a number"))
if choice == 1:
    addition=(Num_1+Num_2)
    print(addition)
if choice == 2:
    subtraction=(Num_1-Num_2)
    print(subtraction)
if choice == 3:
    multiplication=(Num_1*Num_2)
    print(multiplication)
if choice == 4:
    division=(Num_1/Num_2)
    print(division) 
