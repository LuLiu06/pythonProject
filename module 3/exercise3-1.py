length=float(input("Enter the length of the zander: "))
if length<42:
    gap=42-length
    print(f"You have to release the fish back to the lake, there is a {gap:.2f} centimeters below the size limit.")
else:
    print("You can keep the fish!")