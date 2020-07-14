day = int(input("enter day: "))
month = int(input("enter month: "))
year = int(input("enter year: "))
year1 = year%100




if (day >0 and day<=31) and  (month >0 and month <=12) and (year >=1950 and year <=2020 ):
    if 0<year1<10:
     print(str(day)+"/"+str(month)+"/"+"0"+str(year1))
    else:
     print(str(day)+"/"+str(month)+"/"+str(year1))
if day <0 or day >31:
    print ("invalid day input")
if month <0 or month >12:
    print("invalid month input")
if year <1950 or year > 2020:
    print ("invalid year input")





