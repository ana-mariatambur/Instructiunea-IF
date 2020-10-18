"""Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. """
aa=int(input("Introduceti numarul bilelor albe mici:"))
ab=int(input("Introduceti numarul bilelor albe mari:"))
ba=int(input("Introduceti numarul bilelor rosii mici:"))
bb=int(input("Introduceti numarul bilelor rosii mari:"))
ca=int(input("Introduceti numarul bilelor verzi mici:"))
cb=int(input("Introduceti numarul bilelor verzi mari:"))
print("Totalul bilelor:",aa+ab+ba+bb+ca+cb)
if aa+ba+ca>ab+bb+cb:
    print("Mari:",ab+bb+cb,"bile")
else:
    print("Mici:",aa+ab+ca,"bile")
if (aa+ab>ba+bb) and (aa+ab>ca+cb):
    print("Albe:",aa+ab,"bile")
elif (ba+bb>aa+ab) and (ba+bb>ca+cb):
    print("Rosii:",ba+bb,"bile")
else:
    print("Verzi:",ca+cb,"bile")