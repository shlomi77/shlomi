num1= int (input("enter number: "))
if num1 >=100 and num1<1000:
    num2= num1%10
    num3=num1//100
    num4=num1//10%10
    print(num2+num3+num4)
else:
    print("error")
