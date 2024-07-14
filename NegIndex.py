str1="Kranthi Koushik"
print(str1[-1])
print(str1[-2])
print(str1[-3])
print(str1[-4])
print(str1[-5])
print(str1[-6])
print(str1[-7])
print(str1[-8])
print(str1[-9])
print(str1[-9],str1[-8],str1[-7],str1[-6],str1[-5],str1[-4],str1[-3],str1[-2],str1[-1])
print(str1[-9]+str1[-8]+str1[-7]+str1[-6]+str1[-5]+str1[-4]+str1[-3]+str1[-2]+str1[-1])
print(str1[-1]+str1[-2]+str1[-3]+str1[-4]+str1[-5]+str1[-6]+str1[-7]+str1[-8]+str1[-9])

#step


print(str1[-12:])
print(str1[:-1])
print(str1[-12:-1])
print(str1[-1:-12:-2])
print(str1[12:1:-1])
print(str1[::-1])


#Can't be reassigned like this


print(str1[0])
print(str1[1])
str1[0]="r"
print(str1)
