"""Se consideră trei numere întregi. Dacă toate sunt pozitive, să se afişeze numărul mai mare dintre al doilea şi al treilea număr, în
caz contrar să se calculeze suma primelor două numere. """
a=int(input("Introduceti primul numar:"))
b=int(input("Introduceti al doilea numar:"))
c=int(input("Introduceti al treilea numar:"))
if (a>0) and (b>0) and (c>0):
    if b>c:
        print (b)
    if c>b:
        print(c)
else:
    print(a+b)