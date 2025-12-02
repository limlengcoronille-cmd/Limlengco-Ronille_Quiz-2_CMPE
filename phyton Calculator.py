print("Welcome to my Calculator")
print("This is just a simple Calculator but please still enjoy")
print("This is made by Ronille E. Limlengco") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
valid_operator = ["+", "-", "*", "/", "sqr""", "r"]
while True:
    try:
        num1 = float(input("Input 1st number:"))
        operator = input("Select an Operator (+, -, *, /, sqr, r):")
        if operator not in valid_operator:
           print("Invalid Operator, please try again")
           continue

        if operator != "sqr":
            num2 = float(input("Input 2nd number:"))

        if operator == "+":
            sum = float(num1) + float(num2)
            print(sum)
        else:
            print("Invalid Input, please try again")
        
        if operator == "-":
            difference = float(num1) - float(num2)
            print(difference)
        else:
            print("Invalid Input, please try again")
        
        if operator == "*":
            product = float(num1) * float(num2)
            print(product)
        else:
            print("Invalid Input, please try again")
        
        if operator == "/":
            quotient = float(num1) / float(num2)
            print(quotient)
        else:
            print("Invalid Input, please try again")
        
        if operator == "sqr":
            sqr = float(num1)  ** 0.5
            print(sqr)
        else:
            print("Invalid Input, please try again")
        
        if operator == "r":
            r = float(num1) % float(num2)
            print(r)
        else:
            print("Invalid Input, please try again")
            
    except ValueError:
            print("Invalid Input, please try again")
            continue