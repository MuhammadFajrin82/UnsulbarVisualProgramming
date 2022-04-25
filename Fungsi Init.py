class Motor:
    def __init__(self, inputMerek, inputBahanBakar, inputWarna):
        self.merek = inputMerek
        self.bahan_bakar = inputBahanBakar
        self.warna = inputWarna

Motor1 = Motor("Bentor","Bensin","Hijau")
Motor2 = Motor("Honda Scoopy","Bensin","Hitam")

print(Motor1.__dict__)
