max = 0
sum = 0
count=0
grade = int(input("enter grade: "))
while grade>=0 and grade<=100:


        if grade>max:

            max=grade
        sum=grade+sum
        count+=1
        avg=sum/count
        dif=max-avg
        print(max)
        print(avg)
        print(dif)
        grade = int(input("enter grade: "))
else:
    print("no")