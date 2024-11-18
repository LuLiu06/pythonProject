var num1,num2,num3

num1=parseInt(prompt("Enter the first number: "))
num2=parseInt(prompt("Enter the second number: "))
num3=parseInt(prompt("Enter the third number: "))

output_text=
    "The three number is: " + num1 + ", "+num2 +"," + num3 + '<br>'+
    "Sum: "+ (num1+num2+num3) + "<br>"+
    "product: "+ (num1*num2*num3)+ "<br>"+
    "Average: "+(num1+num2+num3)/3 + "<br>"

output_object=document.getElementById("output")
output_object.innerHTML=output_text