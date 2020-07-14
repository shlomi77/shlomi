password1 = str(input("enetr passworrd: "))
password2 = str(input("enetr passworrd: "))
tries = 0
while password1!= password2:
    password2 = str(input("enetr passworrd: "))

    tries+=1
    if tries==5:
        print("too many incorrect")
        break
    if password1==password2:
        print("success")
        break
