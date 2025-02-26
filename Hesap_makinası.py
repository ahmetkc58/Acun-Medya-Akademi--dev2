def hesap_makinası(sayi1,sayi2,işlem):

    if(işlem=="+"):
        return sayi1+sayi2
    elif(işlem=="-"):
        return  sayi1-sayi2
    elif(işlem=="*"):
        return sayi1*sayi2
    elif(işlem=="/"):
        if (sayi2 == 0):
            return "ikinci sayınız 0 "
        else:
            return sayi1/sayi2

print(hesap_makinası(12,4,"/"))
