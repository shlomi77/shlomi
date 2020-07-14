grade = int(input("enter grade: "))
sum1=0
sum2=0
count1=0
count2=0
while grade >=0 and grade <101:
    grade = int(input("enter grade: "))
    if grade >=60:
        count1+=1
        sum1=grade+sum1
    if grade <60:
        count2+=1
        sum2=grade+sum2

print(sum1/count1)
print(sum2/count2)