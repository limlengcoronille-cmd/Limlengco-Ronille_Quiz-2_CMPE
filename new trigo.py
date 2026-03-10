import math

choice = 0

while choice != 4:
    print("----------------------------------")
    print(" Basic Trigonometry Calculator")
    print("----------------------------------")
    print(" 1. Sine")
    print(" 2. Cosine")
    print(" 3. Tangent")
    print(" 4. Exit")

    try:
        choice = int(input("Enter your Choice: "))

        if choice == 4:
            print("Thank you for uusing the program.")
            break

        if choice not in [1, 2, 3]:
            print("Invalid Input")
            continue

        while True:
            try:
                angle = float(input("Enter Angle in Degrees: "))
                break
            except ValueError:
                print("Invalid angle. Please enter a number.")

        rad = math.radians(angle)

        if choice == 1:
            result = math.sin(rad)
            print("Formula: sin(θ)")
            print(f"Solution: sin({angle}) = {result}")

        elif choice == 2:
            result = math.cos(rad)
            print("Formula: cos(θ)")
            print(f"Solution: cos({angle}) = {result}")

        elif choice == 3:
            result = math.tan(rad)
            print("Formula: tan(θ)")
            print(f"Solution: tan({angle}) = {result}")

        print("Answer:", result)

    except ValueError:
        print("Invalid Choice")