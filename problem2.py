print("In the form of ax + by + cz = d, ex + fy + gz = h, ix + jy + kz = l")
    
try:
        a = float(input("What is a? "))
        b = float(input("What is b? "))
        c = float(input("What is c? "))
        d = float(input("What is d? "))
        e = float(input("What is e? "))
        f = float(input("What is f? "))
        g = float(input("What is g? "))
        h = float(input("What is h? "))
        i = float(input("What is i? "))
        j = float(input("What is j? "))
        k = float(input("What is k? "))
        l = float(input("What is l? "))
        
        D = a * (f * k - g * j) - b * (e * k - g * i) + c * (e * j - f * i)
        
        if D == 0:
            print("The system of equations has no unique solution.")
        else:
            DX = d * (f * k - g * j) - b * (h * k - g * l) + c * (h * j - f * l)
            DY = a * (h * k - g * l) - d * (e * k - g * i) + c * (e * l - h * i)
            DZ = a * (f * l - h * j) - b * (e * l - h * i) + d * (e * j - f * i)
            
            x = DX / D
            y = DY / D
            z = DZ / D
            
            print(f"x is {x}, y is {y}, z is {z}")
    
except ValueError:
        print("Please enter numerical values only.")
except ZeroDivisionError:
        print("Undefined.")
