grade = int(input("enter grade: "))
count = 0
sum=0

while grade >=0 and grade<=100:


    if grade>=60:
        sum= sum+grade
        count = count+1
    else:
        if grade<60:
            print("failed")
    grade = int(input("enter grade: "))
print(sum/count)
print(count)