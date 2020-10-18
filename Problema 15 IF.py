"""Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
ce clasa va fi repartizat (A, B, C, D sau E)?. """
x=int(input("Numarul de ordine:"))
c=x//25
if c==0:
    print("A")
elif c==1:
    print("B")
elif c==2:
    print("C")
elif c==3:
    print("D")
elif (c==4) or (x==125):
    print("E")
elif c>5:
    print("Nu a fost admis")
else:
    'break'