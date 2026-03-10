import math
choice = ""
while choice != "4":
    print("----------------------------------")
    print(" Basic Trigonometry Calculator")
    print("----------------------------------")
    print(" 1. Sine \n 2. Cosine \n 3. Tangent \n 4. Exit")

    try: 
        choice = input("Enter your Choice:")
        while True:
            try:
                angle = float(input("Enter Angle in Degrees: "))
                break
            except ValueError:
                print("Invalid angle. Please enter a number.")
            
        if choice == "1":
            result = math.sin(math.radians(angle))
            print("Formula: sin(θ)")
            print("Solution: sin(", angle, ") =", result)
            print("Answer:", result)

        elif choice == "2":
            result = math.cos(math.radians(angle))
            print("Formula: cos(θ)")
            print("Solution: cos(", angle, ") =", result)
            print("Answer:", result)

        elif choice == "3":
            result = math.tan(math.radians(angle))
            print("Formula: cos(θ)")
            print("Solution: tan(", angle, ") =", result)
            print("Answer:", result)

        elif choice == "4":
            exit()

        else:
            print("Invalid Input")

    except ValueError:
        print("Invalid Choice")