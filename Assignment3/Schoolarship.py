age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
score = int(input("Enter your academic score (out of 100): "))
if 18 <= age <= 25:
    if gender == "M":
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender == "F":
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    else:
        print("Invalid gender entered.")
else:
    print("Age not eligible for scholarship consideration.")
