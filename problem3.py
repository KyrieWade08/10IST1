a = int(input('What is the value of the variable "A"?'))
b = int(input('What is the value of the variable "B"?'))
c = int(input('What is the value of the variable "C"?'))

X = (-b + ((b**2 - 4 * a * c)**1/2))/2*a
Y = (-b - ((b**2 - 4 * a * c)**1/2))/2*a
print ("The value of X is", X, "and" , Y)
