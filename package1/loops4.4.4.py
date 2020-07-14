num = int(input("enter numero: "))
a=0
count = 0
while num!=0:
  count+=1
  num1=num%10
  a=a*10+num1
  num = num//10
  print(num1,end='')
print('')
print(a*2)




