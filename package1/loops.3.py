num = int(input("enter number: "))

while num>99 and num<1000:

    num1 = num%10
    num2=num//100
    num3=num//10%10
    print(num2+num3+num1)
    num = int(input("enter another number: "))
print("error")
