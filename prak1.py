class Penjumlahan:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def hitung_penjumlahan(self):
        return self.angka1 + self.angka2

def main():
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        penjumlahan = Penjumlahan(angka1, angka2)

        hasil = penjumlahan.hitung_penjumlahan()

        print("Hasil penjumlahan:", hasil)
    except ValueError:
        print("Masukkan harus berupa angka.")

if __name__ == "__main__":
    main()
