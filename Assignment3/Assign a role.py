age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
experience = int(input("Enter your years of experience: "))
if 21 <= age <= 35:
    if gender == "M":
        if experience >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == "F":
        if experience >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
    else:
        print("Invalid gender entered.")
elif age > 35:
    print("Manager Role")
else:
    print("Age not eligible for any role.")
