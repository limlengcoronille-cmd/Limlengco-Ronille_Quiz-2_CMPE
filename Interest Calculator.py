choice = ""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid entry! Please enter a number.")

print("---------------------------")
print("    Interest Calculator")
print("---------------------------")
print("1. Simple Interest")
print("2. Compound Interest")
print("3. Future Value")
print("4. Present Value")
print("5. Exit")
print("---------------------------")

while True:
    choice = input("Choose an Option: ")
    if choice not in ["1","2","3","4","5"]:
        print("Invalid option! Please choose.")
        continue

    if choice == "5":
        print("Thank you for using the program!")
    break

while True:
    if choice == "1":
        principal = get_number("Enter Principal Amount: ")
        rate = get_number("Enter Rate of Interest: ")
        time = get_number("Enter Time in Years: ")
        simple_interest = (principal * rate * time) / 100
        print("Formula: Sample Interest = P x R x T")
        print(f"{principal} x {rate} x {time} / 100")
        print(f"Simple Interest is: {simple_interest:.4f}")

    elif choice == "2":
        principal = get_number("Enter Principal Amount: ")
        rate = get_number("Enter Rate of Interest: ")
        time = get_number("Enter Time in Years: ")
        compound_interest = principal * (1 + rate / 100) ** time - principal
        print("Formula: Compound Interest = principal * (1 + rate / 100) ** time - principal")
        print(f"{principal} * (1 + {rate} / 100) ** {time} - {principal}")
        print(f"Compound Interest is: {compound_interest:.4f}")

    elif choice == "3":
        present_value = get_number("Enter Present Value: ")
        rate = get_number("Enter Rate of Interest: ")
        time = get_number("Enter Time in Years: ")
        future_value = present_value * (1 + rate / 100) ** time
        print("Formula: Future Value = present_value * (1 + rate / 100) ** time")
        print(f"{present_value} * (1 + {rate} / 100) ** {time}")
        print(f"Future Value is: {future_value:.4f}")

    elif choice == "4":
        future_value = get_number("Enter Future Value: ")
        rate = get_number("Enter Rate of Interest: ")
        time = get_number("Enter Time in Years: ")
        present_value = future_value / (1 + rate / 100) ** time
        print("Formula: Present Value = future_value / (1 + rate / 100) ** time")
        print(f"{future_value} / (1 + {rate} / 100) ** {time}")
        print(f"Present Value is: {present_value:.4f}")