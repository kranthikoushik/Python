week=int(input("Enter week :"))
if week==1:
    print("Monday")
elif week==2:
    print("Tuesday")
elif week==3:
    print("Wednesday")
elif week==4:
    print("Thursday")
elif week==5:
    print("Friday")
elif week==6:
    print("Saturday")
elif week==7:
    print("Sunday")
else:
    print("Week value is not valid")



w=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week=int(input("Enter week:"))
if week>0 and week<8:
    print(w[week-1])
else:
    print("Week value is not valid")
