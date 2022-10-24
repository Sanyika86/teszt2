'''
#1,50 és 100 között kiprintelni a számokat a while ciklus segítségével

for x in range(50,101,1):
    print(x)
    
#2, Kérünk be a felhasználótól 5 db egész számot és írjuk ki azokat amelyek 2 ve
#l és 3al oszthatóak.
for x in range(1,6,1):
    szam = int(input("Adj meg egy számot: "))
    if szam %2 ==0 and szam %3 ==0:
        print("Osztható")
    else:
        print("Nem osztható")
'''
#3. 50 és 100 között írjunk ki minden 3. értéket while ciklus segítségével
"""
szam = 50
while szam <= 99:
    print(szam)
    szam = szam +3
    
"""

#4.feladat: Kérjünk be 5 db gyümölcs nevet és ha alma akkor kiírjuk, hogy piros. Más esetben kiírjuk, hogy egészséges.
"""
x = 1


while x < 6:
    y = input("Kérem a gyümölcs nevét:")
    if y == "alma":
        print("Piros")
        
    else:
        print("Egészséges")
"""

#5.feladat: Kérjünk be egész számokat mind addig, amíg nem kapunk 1000-nél nagyobb értéket.
"""

y = int(input("Kérem a számot:"))

while y < 1000:
    y = int(input("Kérem a számot:"))

"""

# 500 és 1000 között írjuk ki azokat, amelyek oszthatóak 3-mal és 5-tel osztható számokat.
"""
x = 500

while x < 1001:
    
    if x % 3 == 0 and x % 5 == 0:
        print(x)
    x += 1




# 10 és 20 paratlan szamok kiiratasa
x = 10
while x < 20:
    if x % 2 != 0:
        print(x)
    x += 1
# kerjuk be 5 egesz szamot kiirjuk pozitiv vagy negativ
x = 1
while x <= 5:
    x += 1
    szam = int(input("Kérem a számot"))
    if szam > 0:
        print("pozitiv")
    else:
        print("negativ")
   """
"""
for x in range(1,6,1):
    szam = int(input("Kérem a számot"))
    if szam > 0:
        print("pozitiv")
    else:
        print("negativ")
"""
"""
#kérjunk be 2 db egész számot egyenlőek e vagy nem
szam = int(input("Kérek egy számot:"))
szam1 = int(input("Kérek egy számot:"))
if szam == szam1:
    print("A számok egyenlőek")
else:
    print("A számok nem egyenlőek")
"""
#kérjunk 5 db egész számot és megviszgáljuk minden számról hogy 50 és 100 közé esik e
"""
for x in range (1,6,1):
    szam1 = int(input("Kérek egy számot:"))
    if szam1> 50 and szam1 < 100:
        print("A szám 50-100 közé esik")
    else:
        print("nem oda esik!")
    
 """

# 10 és 20 közötti párosak:
"""
x = 10

while x < 21:
    
    if x % 2 == 0:
        print(x)
    x += 1

"""

# 5 db szám bekérése és duplázzuk az értékeket!


x = 1


while x < 6:
    
    szam = int(input("Kérem a számot!"))
    
    dupla = szam * 2
    
    print("A megadott szám kétszerese:",dupla)
    
    x += 1











        





     