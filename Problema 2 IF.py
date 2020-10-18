"""La ora de matematică Gigel este scos la tablă. Profesoara îi dictează trei numere şi îi cere să verifice dacă cele trei numere pot fi
laturile unui triunghi. Ajutaţi-l pe Gigel să afle rezultatul. Scrieţi un program care primeşte numerele lui Gigel, care sunt mai mici
ca 32000, şi returnează DA sau NU. """
l1=int(input("Introduceti lungimea primei laturi="))
l2=int(input("Introduceti lungimea a doua laturi="))
l3=int(input("Introduceti lungimea a treiei laturi="))
if (l1<32000) and (l2<32000) and (l3<32000) :
    if (l1+l2>l3) and (l1+l3>l2) and (l2+l3>l1) :
        print ("Da")
    else:
        print("Nu")