user_input=input("Enter a number: ")
if user_input!="":
    s=int(user_input)
    l=int(user_input)

    while user_input!="":
        number=int(user_input)
        if number<s:
            s=number
        if number>l:
            l=number
        user_input=input("Enter a number: ")
    print(f"The largest number is {l},and the smallest number is {s}.")
else:
    print("Please enter a number.")