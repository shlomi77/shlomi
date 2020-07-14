
mus = 0
count = 0
sum = 0


for i in range(5):
    factor = float(input("enter factor: "))
    grade = int(input("enter grade: "))
    mus+=grade
    factor = grade * (factor / 100)
    newgrade = grade + factor
    print(grade)
    print(newgrade)
    count=count+1
    sum=sum+newgrade
    average=sum/count
    oriavg=mus/count
print("original grade average ",oriavg)
print("new grade average ",average)
print (average-oriavg)