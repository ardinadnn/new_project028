##author:  081911633028 / Ardina DN
##BendaBulat
from math import pi

class BendaBulat:
    def __init__(self,radius,tinggi=None):
        self.radius = radius
        if tinggi!=None:
            self.tinggi = tinggi
    def luasLingkaran(self):
        return(pi*self.radius**2)
    def volumeBola(self):
        return(4/3*pi*self.radius**3)
    def luasPermukaanTabung(self):
        return(2*pi*self.radius*(self.radius+self.tinggi))
    def volumeSilinder(self):
        return(pi*self.radius**2*self.tinggi)
    

angka = int(input("Pilih (masukkan angka saja):\n1. Luas lingkaran\n2. Volume bola\n3. Luas permukaan tabung\n4. Volume silinder\nJawab: "))
if angka == 1:
    radius = float(input("Masukkan jari-jari: "))
    hasil = BendaBulat(radius)
    print("--------------------------------")
    print("Luas lingkaran:",hasil.luasLingkaran()) 
    print("--------------------------------")
    
elif angka==2:
    radius = float(input("Masukkan jari-jari: "))
    hasil = BendaBulat(radius)
    print("--------------------------------")
    print("Volume bola:",hasil.volumeBola())
    print("--------------------------------")
    
elif angka==3:
    radius = float(input("Masukkan jari-jari: "))
    tinggi = float(input("Masukkan tinggi: "))
    hasil = BendaBulat(radius,tinggi)
    print("--------------------------------")
    print("Luas permukaan tabung:",hasil.luasPermukaanTabung())
    print("--------------------------------")
    
elif angka==4:
    radius = float(input("Masukkan jari-jari: "))
    tinggi = float(input("Masukkan tinggi: "))
    hasil = BendaBulat(radius,tinggi)
    print("--------------------------------")
    print("Volume silinder:",hasil.volumeSilinder())
    print("--------------------------------")

##BendaSegi4
class BendaSegi4:
    def __init__(self,panjang,lebar=None,tinggi=None):
        self.panjang = panjang
        if lebar!=None and tinggi!=None:
            self.lebar = lebar
            self.tinggi = tinggi
    def luasBujurSangkar(self):
        return(self.panjang**2)
    def volumeKubus(self):
        return(self.panjang**3)
    def luasPersegiPanjang(self):
        return(self.panjang*self.lebar)
    def volumeBalok(self):
        return(self.panjang*self.lebar*self.tinggi)
    
angka = int(input("Pilih bangun ruang (masukkan angka saja):\n1. Luas bujur sangkar\n2. Volume kubus\n3. Luas persegi panjang\n4. Volume balok\nJawab: "))
if angka == 1:
    panjang = float(input("Masukkan sisi: "))
    hasil = BendaSegi4(panjang)
    print("--------------------------------")
    print("Luas bujur sangkar:",hasil.luasBujurSangkar())
    print("--------------------------------")
    
elif angka==2:
    panjang = float(input("Masukkan sisi: "))
    hasil = BendaSegi4(panjang)
    print("--------------------------------")
    print("Volume kubus:",hasil.volumeKubus())
    print("--------------------------------")
    
elif angka==3:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    hasil = BendaSegi4(panjang,lebar,tinggi=0)
    print("--------------------------------")
    print("Luas persegi panjang:",hasil.luasPersegiPanjang())
    print("--------------------------------")
elif angka==4:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    tinggi = float(input("Masukkan tinggi: "))
    hasil = BendaSegi4(panjang,lebar,tinggi)
    print("--------------------------------")
    print("Volume balok:",hasil.volumeBalok())
    print("--------------------------------")