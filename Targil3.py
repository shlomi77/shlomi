name = str (input("enter name: "))
age = int (input ("enter age: "))
c_year = int (input ("enter current year: "))
f_year = int (input("enter future year: "))
calc = f_year - c_year
final = age + calc

print (name + " will be " + str(final)+  " years old in the year " + str(f_year))