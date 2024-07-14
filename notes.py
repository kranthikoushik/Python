am=int(input("Enter Amount:"))
note500=note100=note50=note10=0
if am>=500:
    note500=am//500
    am-=note500*500
if am>=100:
    note100=am//100
    am-=note100*100
if am>=50:
    note50=am//50
    am-=note50*50
if am>=10:
    note10=am//10
    am-=note10*10
print("Total Number of notes:")
print("note500",note500)
print("note100",note100)
print("note50",note50)
print("note10",note10)



