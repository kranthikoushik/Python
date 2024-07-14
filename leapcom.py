year=int(input("Enter n value:"))
if year%400==0:
  print(year,"  is Leap Year")
elif year%100==0:
  print(year," is Common Year")
elif year%4==0:
  print(year," is Leap Year")
else:
  print(year," is Common Year")
