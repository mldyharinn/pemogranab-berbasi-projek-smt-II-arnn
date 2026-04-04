import parkirRoda2

class Motor:
    def __init__(self, plat, merk):
        self.plat = plat
        self.merk = merk

    def masuk(self):
        print("Motor", self.merk, "masuk parkir")

    def keluar(self, jam):
        biaya = parkirRoda2.hitung_biaya(jam)
        ket = parkirRoda2.status(jam)

        print("Motor", self.merk, "keluar")
        print("Lama parkir:", jam, "jam")
        print("Keterangan:", ket)
        print("Biaya:", biaya)


m1 = Motor("B1234AA", "Honda")
m2 = Motor("D5678BB", "Yamaha")

m1.masuk()
m1.keluar(2)

m2.masuk()
m2.keluar(3)