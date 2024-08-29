value=float(input("Enter your hemoglobin value: "))
gender=input("Enter your gender: ").lower()
if gender =="female":
    if 117<=value<=155:
        print("Your hemoglobin is normal.")
    elif value<117:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
elif gender=="male":
    if 134<=value<=167:
        print("Your hemoglobin is normal.")
    elif value<134:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
else:
    print("Invalid")
