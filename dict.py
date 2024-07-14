#Creating Diectionary using dict
dic={}
dic=dict({"Name":"Kranthi","ID":23,"Loc":"TPT"})
print(dic)

#Creating as Pair
dic=dict([("Name","Koushik"),("ID",25)])
print(dic)

#Sample Program
Det={"Name":"Arjun","ID":60,"Sal":25000,"Loc":"Bangalore"}
print("Name:%s"%Det["Name"])
print("ID:%d"%Det["ID"])
print("Sal:%d"%Det["Sal"])
print("Loc:%s"%Det["Loc"])

#Sample Program dynamic values
Det={"Name":"Arjun","ID":60,"Sal":25000,"Loc":"Bangalore"}
print(Det)
Det["Name"]=input("Name:")
Det["ID"]=int(input("ID:"))
Det["Sal"]=int(input("Sal:"))
Det["Loc"]=input("Loc:")
print(Det)

#del keyword

del Det["ID"]
print(Det)

#Pop Keyword


Det.pop("Loc")
print(Det)

#Printing keys and values using Iteration

det={1:"Anime",2:"Lol",3:"Emoji"}
for i in det.keys():
    print(i)
for j in det.values():
    print(j)
