"""La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
numărul de boabe de porumb."""
a=int(input("Numarul de gaini:"))
b=int(input("Numarul de boabe de porumb:"))
c=b//a
d=b-c*a
if c<d:
    print("Curcanul mai mult cu",d-c,"boabe")
elif c>d:
    print("Gainile mai mult cu",c-d,"boabe")
else:
    print("Egalitate")