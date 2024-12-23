age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
income = float(input("Enter your annual income: "))
tax = 0
if age >= 18 and age < 60:
    if gender == "M":
        if income > 1000000:
            tax = income * 0.30
        elif 500000 < income <= 1000000:
            tax = income * 0.20
        else:
            tax = income * 0.10
    elif gender == "F":
        if income > 1000000:
            tax = income * 0.25
        elif 500000 < income <= 1000000:
            tax = income * 0.15
        else:
            tax = income * 0.05
    else:
        print("Invalid gender entered.")
elif age >= 60:
    if income > 1000000:
        tax = income * 0.20
    else:
        tax = income * 0.10
else:
    print("Tax calculation not applicable for underage individuals.")
if tax > 0:
    print(f"Your tax amount is: {tax:.2f}")
