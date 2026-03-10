import math
choice = ""
while choice != "6":
    print("----------------------------------")
    print(" Basic Statistics Calculator")
    print("----------------------------------")
    print(" 1. Mean \n 2. Median \n 3. Mode \n 4. Sample Standard Deviation \n 5. Range \n 6. Exit")

    choice = input("Enter your Choice: ")
    try: 
        if choice in ["1", "2", "3", "4", "5"]:
         data = input("Enter numbers (EX. 5, 10, 15): ")
         num = list(map(float, data.split(",")))

        if choice == "1":
            result = sum(num) / len(num)
            print(f"Solution: ({' + '.join(map(str, num))}) / {len(num)}")
            print(f"          = {sum(num)} / {len(num)}")
            print("Answer:", result)
            
        elif choice =="2":
            num.sort()
            n = len(num)
            middle = n // 2

            if n % 2 == 0:
                result = (num[middle-1] + num[middle]) / 2
                print(f"Middle Numbers: {num[middle-1]} and {num[middle]}")
            else:
                result = num[middle]
                print("Middle Numbers", num[middle])

            print("Formula: Middle value of sorted data")
            print("Answer:", result)

        elif choice == "3":
            counts = max(set(num), key=num.count)
            if num.count(counts) == 1:
                print("There is no mode.")
            else:
                result = counts
                print("Formula: Most frequent number")
                print("Answer:", result)

        elif choice == "4":
            mean = sum(num) / len(num)
            variance = sum((x - mean) ** 2 for x in num) / (len(num) - 1)
            result = math.sqrt(variance)
            print("Formula: SD = √( Σ(x - mean)² / (n - 1) )")
            print(f"Solution: √( ({num} - {mean})² + ({num} - {mean})² / {len(num) - 1} )")
            print(f"        = √( {variance} )")
            print(f"Answer: {result}")

        elif choice == "5": 
            result = max(num) - min(num)
            print("Formula: Range = Max - Min")
            print(f"Solution: {max(num)} - {min(num)}")
            print(f"        = {result}")
            print(f"Answer: {result}")

        elif choice == "6":
            print("Thank you for using the program!")

    except ValueError: 
        print("Invalid, Please try again")