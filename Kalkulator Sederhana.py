def jumlah (a,b):
    jumlah = a+b
    return jumlah

def kurang (a,b):
    kurang = a-b
    return kurang

def kali (a,b):
    kali = a*b
    return kali

def bagi (a,b):
    bagi = a/b
    return bagi

lagi='y'
while lagi=='y':

    print("\n\t Kalkulator Sederhana\n")
    print("\n 1.Penjumlahan \n 2.Pengurangan \n 3.Perkalian \n 4.Pembagian \n")

    a = int(input("Bilangan 1 : "))
    b = int(input("Bilangan 2 : "))
    c = int(input("Operasi [1/2/3/4]: "))

    if(c==1):
        print(a, "+" ,b, "=",jumlah(a,b))
    elif(c==2):
        print(a, "-" ,b, "=",kurang(a,b))
    elif(c==3):
        print(a, "*" ,b, "=",kali(a,b))
    elif(c==4):
        print(a, "/" ,b, "=",bagi(a,b))
    else:
        print("Operasi tidak tersedia")
    lagi=input("Ulang Lagi [y/t]?")
