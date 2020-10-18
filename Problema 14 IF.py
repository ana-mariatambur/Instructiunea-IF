"""Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?"""
n=int(input("Numarul sosirii:"))
c=n//4
if c==0:
    print("1 casuta")
elif c>0:
    print("A",c+1,"-a casuta")
else:
    'break'
