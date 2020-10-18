"""La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi?"""
x=int(input("Locul:"))
if (x>=1) and (x<25):
    print("Alba")
elif(x>=25) and (x<50):
    print("Rosie")
elif(x>=50) and (x<75):
    print("Albastra")
elif(x>=75) and (x<=100):
    print("Neagra")
elif x>100:
    print("Nu a primit tricou")
else:
    'break'