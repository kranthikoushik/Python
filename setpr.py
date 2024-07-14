set1={"Kranthi","Koushik","Avilala","Anime"}
set1.discard("Kranthi")
print(set1)
set1.remove("Anime")

set2={2,3,4,5,6}
set3={2,4,5,6,7,8}
print(set2|set3)
print(set2&set3)
print(set2-set3)
print(set2^set3)

set4=frozenset([3,4,5,6,7])
print(set4)
for i in set4:
    set4.add(40)
