##author:  081911633028 / Ardina DN
##add dan sub (maks 3 angka)
##halo halo
class no1:
    def __init__(self,num1=None,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            self.num1 = num1
            self.num2 = num2
            self.num3 = num3
        elif num1!=None and num2!=None:
            self.num1 = num1
            self.num2 = num2
            self.num3 = 0
        elif num1!=None:
            self.num1 = num1
            self.num2 = 0
            self.num3 = 0
        else:
            self.num1 = 0
            self.num2 = 0
            self.num3 = 0
    def add(self):
        return(self.num1+self.num2+self.num3)
    def sub(self):
        return(self.num1-self.num2-self.num3)

x = int(input("Masukkan banyaknya angka (0-3): "))
if x==3:
    angka = int(input("Silakan pilih fungsi yang akan digunakan! (masukkan angkanya saja)\n1. Penjumlahan\n2. Pengurangan\nJawab: ")) 
    if angka==1:
        num1 = float(input("Masukkan angka 1: "))
        num2 = float(input("Masukkan angka 2: "))
        num3 = float(input("Masukkan angka 3: "))
        hasil = no1(num1,num2,num3)
        print("Hasil dari",num1,"ditambah",num2,"ditambah",num3,"adalah",hasil.add())
    if angka==2:
        num1 = float(input("Masukkan angka 1: "))
        num2 = float(input("Masukkan angka 2: "))
        num3 = float(input("Masukkan angka 3: "))
        hasil = no1(num1,num2,num3)
        print("Hasil dari",num1,"dikurang",num2,"dikurang",num3,"adalah",hasil.sub())
if x==2:
    angka = int(input("Silakan pilih fungsi yang akan digunakan! (masukkan angkanya saja)\n1. Penjumlahan\n2. Pengurangan\nJawab: ")) 
    if angka==1:
        num1 = float(input("Masukkan angka 1: "))
        num2 = float(input("Masukkan angka 2: "))
        hasil = no1(num1,num2)
        print("Hasil dari",num1,"ditambah",num2,"adalah",hasil.add())
    if angka==2:
        num1 = float(input("Masukkan angka 1: "))
        num2 = float(input("Masukkan angka 2: "))
        hasil = no1(num1,num2)
        print("Hasil dari",num1,"dikurang",num2,"adalah",hasil.sub())
if x==1:
    angka = int(input("Silakan pilih fungsi yang akan digunakan! (masukkan angkanya saja)\n1. Penjumlahan\n2. Pengurangan\nJawab: ")) 
    num1 = float(input("Masukkan angka: "))
    if angka==1:
        hasil = no1(num1)
        print("Hasil penjumlahan:",hasil.add())
    if angka==2:
        hasil = no1(num1)
        print("Hasil pengurangan:",hasil.sub())
            
if x==0:
    hasil = no1()
    print("Hasil penjumlahan:",hasil.add())
    print("Hasil pengurangan:",hasil.sub())
