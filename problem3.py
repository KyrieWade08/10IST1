a = float(input('What is the value of the variable "A"? '))
b = float(input('What is the value of the variable "B"? '))
c = float(input('What is the value of the variable "C"? '))

discriminant = (b**2 - 4*a*c)

if discriminant >= 0:
    X = (-b + (discriminant**0.5)) / (2*a)
    Y = (-b - (discriminant**0.5)) / (2*a)
else:
    real_part = -b / (2*a)
    imaginary_part = (-discriminant)**0.5 / (2*a)
    X = complex(real_part, imaginary_part)
    Y = complex(real_part, -imaginary_part)

print("The two value  of X are", X, "and", Y)
