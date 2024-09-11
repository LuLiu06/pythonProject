number=[]
while True:
    input_num=input("Enter a number or press enter to quit: ")
    if input_num=="":
        break
    number.append(float(input_num))
number.sort(reverse=True)
top_five=number[:5]
print(top_five)





