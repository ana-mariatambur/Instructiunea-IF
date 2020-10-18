"""Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi."""
ac=int(input("Introduceti anul curent:"))
lc=int(input("Introduceti luna curenta:"))
zc=int(input("Introduceti ziua curenta:"))
an=int(input("Introduceti anul nasterii:"))
ln=int(input("Introduceti luna nasterii:"))
zn=int(input("Introduceti ziua nasterii:"))
if (ac<an) or (str(lc) in ('1,3,5,8,10,12') and (zc>31)) or (str(lc) in ('4,6,7,9,11') and (zc>30)) or (lc==2 and (zc>28)):
    print("Greseala in data curenta")
    'break'
if (ac<an) or (str(ln) in ('1,3,5,8,10,12') and (zn>31)) or (str(ln) in ('4,6,7,9,11') and (zn>30)) or (ln==2 and (zn>28)):
    print("Greseala in data nasterii")
    'break'
if lc<ln:
    print(ac-an-1,"ani")
if lc>ln:
    print(ac-an,"ani")
if (lc==ln) and (zc<zn):
    print(ac-an-1,"ani")
if (lc==ln) and (zc>zn):
    print(ac-an,"ani")
if (lc==ln) and (zc==zn):
    print(ac-an,"ani.Si la multi ani!!!")