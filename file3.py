##author:  081911633028 / Ardina DN
##vektor
import numpy as arr

class vektor():
    global vektor1
    global vektor2
    
    def __init__(self,vektor1=None,vektor2=None):
        if vektor1!=None and vektor2!=None:
            self.vektor1 = vektor1
            self.vektor2 = vektor2
        elif vektor1!=None:
            self.vektor1 = vektor1
        else:
            return(None)
    def jumlah2Vektor(self,vektor1=None,vektor2=None):
        if vektor1!=None and vektor2!=None:
            return (arr.add(self.vektor1,self.vektor2))
        elif vektor1!=None:
            return (self.vektor1)
        else:
            return(None)
    def selisih2Vektor(self,vektor1=None,vektor2=None):
        if vektor1!=None and vektor2!=None:
            return abs(arr.subtract(self.vektor1,self.vektor2)) ##selisih selalu mutlak (absolut)
        elif vektor1!=None:
            return(self.vektor1)
        else:
            return(None)
    def tampilVektor(self,vektor1=None):
        if vektor1!=None:
            self.vektor1=vektor1
            return self.vektor1
        else:
            return("Tidak ada vektor")
        
vektor1 = []
vektor2 = []
x = int(input("Masukkan banyak vektor (0-2): "))
print("-------------------------------------------------")
if x==1:
    panjang = int(input("Masukkan banyaknya angka (panjang vektor): "))
    print("\n-------------------------------------------------")
    for angka in range (0,panjang):
        angka = int(input("Masukkan angka: "))
        vektor1.append(angka)
    hasil = vektor(vektor1)
    print("\n-------------------------------------------------")
    print("Vektor:",hasil.tampilVektor(vektor1))
    print("-------------------------------------------------")
    print("Penjumlahan:",hasil.jumlah2Vektor(vektor1))
    print("Selisih:",hasil.selisih2Vektor(vektor1))
    print("-------------------------------------------------")
if x==2:
    panjang = int(input("Masukkan banyaknya angka (panjang vektor): "))
    print("\n-------------------------------------------------")
    print("[VEKTOR 1]")
    for angka in range (0,panjang):
        angka = int(input("Masukkan angka: "))
        vektor1.append(angka)
    print("-------------------------------------------------")
    print("[VEKTOR 2]")
    for angka in range (0,panjang):
        angka = int(input("Masukkan angka: "))
        vektor2.append(angka)
    hasil = vektor(vektor1,vektor2)
    print("-------------------------------------------------")
    selisih = hasil.selisih2Vektor(vektor1,vektor2) ##dihitung terlebih dahulu agar vektor1 nya tidak "tumpuk"
    jumlah = hasil.jumlah2Vektor(vektor1,vektor2)
    print("Vektor1:",hasil.tampilVektor(vektor1))
    print("Vektor2:",hasil.tampilVektor(vektor2))
    print("-------------------------------------------------")
    print("Penjumlahan:",jumlah)
    print("Selisih:",selisih)
    print("-------------------------------------------------")
if x==0:
    hasil = vektor()
    print(hasil.tampilVektor())