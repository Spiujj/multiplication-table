import random 

print("1.En faza 10")
print("2.En faza 30")
print("3.En faza 70")
print("4.En faza 100")
sonuç=input("Hangisi:")
çarpi="*"


def on():
    
    sayi= random.randint(0,10)
    sayibir= random.randint(0,10)
    işlemsonuç=sayi * sayibir
    işlev=input(f"{sayi}{çarpi}{sayibir}:")
    if int(işlev)==işlemsonuç:
        print("Tebrikler, bildiniz!")
    else:
        print("Üzgünüm, bilemediniz!")    
def otuz():
    sayi= random.randint(0,30)
    sayibir= random.randint(0,30)
    işlemsonuç=sayi * sayibir
    işlev=input(f"{sayi}{çarpi}{sayibir}:")
    if int(işlev)==işlemsonuç:
        print("Tebrikler, bildiniz!")
    else:
        print("Üzgünüm, bilemediniz!")    
def yetmiş():
    sayi= random.randint(0,70)
    sayibir= random.randint(0,70)
    işlemsonuç=sayi * sayibir
    işlev=input(f"{sayi}{çarpi}{sayibir}:")
    if int(işlev)==işlemsonuç:
        print("Tebrikler, bildiniz!")
    else:
        print("Üzgünüm, bilemediniz!")    

def yuz():
    sayi= random.randint(0,100)
    sayibir= random.randint(0,100)
    işlemsonuç=sayi * sayibir
    işlev=input(f"{sayi}{çarpi}{sayibir}:")
    if int(işlev)==işlemsonuç:
        print("Tebrikler, bildiniz!")
    else:
        print("Üzgünüm, bilemediniz!")    

if sonuç=="1":
    on()
if sonuç=="2":
    otuz()    
if sonuç=="3":
    yetmiş()    
if sonuç=="4":
    yuz()    
                                    
