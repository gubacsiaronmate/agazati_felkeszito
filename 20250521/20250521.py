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


# helsinki.py

sportolok = []
with open("helsinki.txt", "r", encoding="utf-8") as f: # megnyitod a fajlt
    for line in f: # minden soron vegig lepegetsz
        line = line.strip().split(" ") # levagod a folosleges szokozoket "sor vege" karaktereket es szokozonkent felbontod
        sportolok.append( # hozzaadod az adatokat a listahoz
            { # dictionary-t hozol letre hozza
                "helyezes": int(line[0]),
                "szam": int(line[1]),
                "sportag": line[2],
                "versenyszam": line[3],
            }
        )

print(f"Helsinki sportolok: {len(sportolok)}") # kiiratod a sportolok szamat


arany = 0 # aranyak szama
ezust = 0 # ezustok szama
bronz = 0 # bronzok szama
for sportolo in sportolok: # minden sportolon vegig lepegetsz
    if sportolo["helyezes"] == 1: # ha arany van
        arany += 1
    elif sportolo["helyezes"] == 2: # ha ezust van
        ezust += 1
    elif sportolo["helyezes"] == 3: # ha bronz van
        bronz += 1

print(f"Arany: {arany}") # kiiratod az aranyat
print(f"Ezust: {ezust}") # kiiratod az ezustot
print(f"Bronz: {bronz}") # kiiratod a bronzt


pontszam = 0 # pontok szama
for sportolo in sportolok: # minden sportolon vegig lepegetsz
    if sportolo["helyezes"] == 1: # ha elso helyezett +7 pont
        pontszam += 7
    elif sportolo["helyezes"] == 2: # ha masodik helyezett +5 pont
        pontszam += 5
    elif sportolo["helyezes"] == 3: # ha harmadik helyezett +4 pont
        pontszam += 4
    elif sportolo["helyezes"] == 4: # ha negyedik helyezett +3 pont
        pontszam += 3
    elif sportolo["helyezes"] == 5: # ha otodik helyezett +2 pont
        pontszam += 2
    elif sportolo["helyezes"] == 6: # ha hatodik helyezett +1 pont
        pontszam += 1

print(f"Pontszam: {pontszam}") # kiiratod a pontszamot


uszas = 0 # uszo ermek szama
torna = 0 # torna ermek szama
for sportolo in sportolok: # minden sportolon vegig lepegetsz
    if sportolo["sportag"] == "uszas": # ha uszas
        uszas += 1
    elif sportolo["sportag"] == "torn": # ha torna
        torna += 1

if uszas > torna: # ha a uszas nagyobb
    print("Uszas tobb")
elif torna > uszas: # ha a torna nagyobb
    print("Torna tobb")
else: # ha egyenloek
    print("Egyenloek")


with open("helsinki2.txt", "w", encoding="utf-8") as f: # megnyitod a fajlt
    for sportolo in sportolok: # minden sportolon vegig lepegetsz
        if sportolo["sportag"] != "kajakkenu": # ha nem kajakkenu azaz helyesen van irva
            # minden helyezeshez igazodva beirod a pontszamot is
            if sportolo["helyezes"] == 1:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {7} {sportolo['sportag']} {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 2:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {5} {sportolo['sportag']} {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 3:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {4} {sportolo['sportag']} {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 4:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {3} {sportolo['sportag']} {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 5:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {2} {sportolo['sportag']} {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 6:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {1} {sportolo['sportag']} {sportolo['versenyszam']}\n")
        else:
            # ha kajakkenu van beirva kijavitod es megint pontszam
            if sportolo["helyezes"] == 1:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {7} kajak-kenu {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 2:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {5} kajak-kenu {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 3:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {4} kajak-kenu {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 4:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {3} kajak-kenu {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 5:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {2} kajak-kenu {sportolo['versenyszam']}\n")
            elif sportolo["helyezes"] == 6:
                f.write(f"{sportolo['helyezes']} {sportolo['szam']} {1} kajak-kenu {sportolo['versenyszam']}\n")

# 8as az buzis en nem ertem
