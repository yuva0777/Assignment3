age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
membership_type = input("Enter the membership type (Monthly/Yearly): ")
membership_fee = 0 
if 18 <= age < 30:
    if gender == "M":
        if membership_type == "Monthly":
            membership_fee = 50
        elif membership_type == "Yearly":
            membership_fee = 500
    elif gender == "F":
        if membership_type == "Monthly":
            membership_fee = 45
        elif membership_type == "Yearly":
            membership_fee = 450
elif 30 <= age <= 50:
    if membership_type == "Monthly":
        membership_fee = 60
    elif membership_type == "Yearly":
        membership_fee = 600
elif age > 50:
    if membership_type == "Monthly":
        membership_fee = 40
    elif membership_type == "Yearly":
        membership_fee = 400
else:
    print("Age not eligible for membership.")
if membership_fee > 0:
    print(f"Membership Fee: Rs{membership_fee}")
