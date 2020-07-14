sum=0
count=0
for i in range(6):
    num = int(input("enter number: "))
    if num%2==0:
        count=count+1
        sum=sum+num
print(sum)
print(sum/count)
print(count)