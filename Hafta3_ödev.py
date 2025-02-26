
def asal_mi():
    sayi=int(input("lütfen sayı giriniz"))
    asal=None

    if(sayi % 2 ==0):
        çift_mi=True
    else:
        çift_mi=False
    if(çift_mi):
        if(sayi==2):
            asal=True
        else:
            asal=False
    else:
        for i in range(3,sayi,2):
          print(i)
          if(sayi%i==0):
              asal=False
              break
          elif(sayi%i>0):
              asal=True
    return asal


print(asal_mi())
