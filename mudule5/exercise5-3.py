user_input=int(input("Enter a number: "))
if user_input>1:
    
    prime=True
    for i in range(2,user_input):

        if user_input%i==0:
            prime=False
            break

    if prime==True:
        print("This is a prime number.")
    else:
        print("This is not a prime number.")
else:
    print("This is not a prime number.")
