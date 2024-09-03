username="python"
password="rules"
attempt=0
while attempt<5:
    input_user=input("Enter your username: ")
    input_password=input("Enter your password: ")
    if input_user==username and input_password==password:
        print("Welcome!")
        break
    else:
        print("Please enter your username and password again.")
        attempt+=1
if attempt==5:
    print("Access denied.")