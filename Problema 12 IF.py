"""“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă
iubeşte …. """
x=int(input("Numarul petalelor:"))
if x>0:
    print("Ma iubeste...")
    if x%6==0:
        print("...un pic")
    elif x%6==5:
        print("...de loc")
    elif x%6==4:
        print("...la nebunie")
    elif x%6==3:
        print("...cu pasiune")
    elif x%6==2:
        print("...mult")
    else:
        print("...un pic")
else:
    'break'