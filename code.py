print("List Cewekk yang gw suka: ")
print()
class cinta:
    def __init__(self, nama, umur, asal):
        self.nama = nama
        self.umur = umur
        self.asal = asal

    def data(self):
        print("Nama: ", self.nama)
        print("Umur: ", self.umur, "tahun")
        print("Asal: ", self.asal)

firstLove = cinta("Kim Ji Won", 19, "Seoul, Korea Selatan")
firstLove.data()
print()
secondLove = cinta("Kim Yoo Jung ", 20, "Busan, Korea Selatan")
secondLove.data()
print()
lastLove = cinta("Go Yoon Jung", 18, "Seoul, Korea Selatan")
lastLove.data()
