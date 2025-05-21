# ertekeles.py

pont = int(input("Pontok: ")) # bekeri a pontszamot

if pont >= 250: # ellenorzi az erteket
    print(f"tovabb mentel: {(pont / 500) * 100}%") # kiirja a tovabbjutast es a szazalekot
else:
    print("nem mentel tovabb") # nem ment tovabb a kocsog



# csapadek.py

from random import randint # random.randint() kell

szamok = [] # letrehozom a listat
for _ in range(10): # 10 szam kell ezert kell egy 10es for ciklus
    szamok.append(randint(0, 30)) # hozza adom a szamot a listahoz


print("A 10 hét átlagos csapadékmennyisége:")
for szam in szamok: # minden szamon vegig lepegetsz
    print(szam) # kiiratod a szamot


osszeg = sum(szamok) # osszead minden szamot
atlag = osszeg / len(szamok) # atlagot szamolsz
print(f"Az összes csapadék: {osszeg}") # kiiratod az osszeget
print(f"Az átlagos csapadék: {atlag}") # kiiratod az atlagot


def paros(szam):
    if szam%2==0:
        return True

paros_hetek = [] # letrehozom a listat
for i in range(0, len(szamok), 2): # minden masodik (paros index) szamon vegig lepegetsz
    paros_hetek.append(szamok[i]) # hozza adod a szamot a listahoz

paratlan_hetek = [] # letrehozom a listat
for i in range(1, len(szamok), 2): # minden masodik (paratlan index) szamon vegig lepegetsz
    paratlan_hetek.append(szamok[i]) # hozza adod a szamot a listahoz

print("Páros hét csapadékai:", end=" ") # kiiratod a kezdo szoveget
for szam in paros_hetek: # minden szamon vegig lepegetsz
    print(szam, end=" ") # kiiratod a szamokat egyesevel
print(f"összesen: {sum(paros_hetek)}") # osszesen ennyi volt a heten

print("Páros hét csapadékai:", end=" ") # kiiratod a kezdo szoveget
for szam in paratlan_hetek: # minden szamon vegig lepegetsz
    print(szam, end=" ") # kiiratod a szamokat egyesevel
print(f"összesen: {sum(paros_hetek)}") # osszesen ennyi volt a heten