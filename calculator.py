def calculator():
    
    while(True):
        
        def addition(a, b):
            return a+b

        def subtraction(a, b):
            return a-b

        def multiplication(a, b):
            return a*b

        def float_division(a, b):
            return a/b

        def floor_division(a, b):
            return a//b

        def exponential(a, b):
            return a**b

        def modulus_or_remainder(a, b):
            return a%b

        print("Press q to exit")
        z = input("What calculation you want to perform?: ")
        if z == "q":
            break
        else:
            try: 
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
                    
                if z == "addition": 
                    c = print(addition(a, b))
                elif z == "subtraction":
                    c = print(subtraction(a, b)) 
                elif z == "multiplication":
                    c = print(multiplication(a, b)) 
                elif z == "float_division":
                    c = print(float_division(a, b)) 
                elif z == "floor_division":
                    c = print(floor_division(a, b)) 
                elif z == "exponential" :
                    c = print(exponential(a, b))
                elif z == "modulus_or_remainder" :
                    c = print(modulus_or_remainder(a, b))
                
            except Exception as e:
                print(f"Invalid input...:- {e}")
        
    print("Thanks for using the calculator")    


calculator()         


            