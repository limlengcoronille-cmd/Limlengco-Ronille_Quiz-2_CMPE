print("Welcome to my Calculator")
print("This is made by Ronille E. Limlengco")

while True:
    try:
        num1 = float(input("Input 1st number:"))
        operator = input("Select an Operator (+, -, *, /, sqr, r)")
        
        if operator != "sqr":
            num2 = float(input("Input 2nd number:"))

        if operator == "+":
            sum = float(num1) + float(num2)
            print(sum)
            
        elif operator == "-":
            difference = float(num1) - float(num2)
            print(difference)

        elif operator == "*":
            product = float(num1) * float(num2)
            print(product)
            
        elif operator == "/":
            quotient = float(num1) / float(num2)
            print(quotient)

        elif operator == "sqr":
            sqr = float(num1)  ** 0.5
            print(sqr)

        elif operator == "r":
            r = float(num1) % float(num2)
            print(r)

        else:
            print("Invalid Input, please to try again")
            
    except ValueError:
            print("Invalid Input, please try again")
            continue