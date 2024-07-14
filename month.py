mon=[31,(28,29),31,30,31,30,31,31,30,31,30,31]
m=int(input("Enter the Month:"))
if m>=1 and m<=12:
    print(mon[m-1],"days")
else:
    print("No month value")
