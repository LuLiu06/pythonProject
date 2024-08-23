talents=float(input("Enter the talents: "))
pounds=float(input("Enter the pounds: "))
lots=float(input("Enter the lots: "))
grams=talents*20*pounds*32*lots*13.3
kilograms=int(grams/1000)
left_grams=grams % 1000
print(f"The weight in modern units is: {kilograms} kilograms and {left_grams:.2f} grams")