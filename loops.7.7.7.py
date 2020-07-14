sum = 0
sum1 = 0
for i in range(5):
    num = int(input("enter num: "))
    if num >10:
         mod = num % 10
         sum = mod + sum
    if num < 10:
         sum1 = num + sum1



    print (sum + sum1)

