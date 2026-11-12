import random

print("================================")
print("          APOTEK SEHAT")
print("================================")
print("           DATA OBAT")
print("--------------------------------")

print("1. Paracetamol")
print("   Harga: Rp5000 | Stok: 20 | Murah | Tersedia")

print("2. Vitamin C")
print("   Harga: Rp7000 | Stok: 25 | Murah | Tersedia")

print("3. Antasida")
print("   Harga: Rp8000 | Stok: 15 | Murah | Tersedia")

print("4. Oralit")
print("   Harga: Rp3000 | Stok: 30 | Murah | Tersedia")

print("5. Obat Batuk")
print("   Harga: Rp12000 | Stok: 10 | Mahal | Tersedia")

print("6. Ibuprofen")
print("   Harga: Rp9000 | Stok: 18 | Murah | Tersedia")

print("7. CTM")
print("   Harga: Rp4000 | Stok: 0 | Murah | Tidak tersedia")

print("8. Promag")
print("   Harga: Rp6000 | Stok: 20 | Murah | Tersedia")

print("9. Betadine")
print("   Harga: Rp15000 | Stok: 12 | Mahal | Tersedia")

print("10. Obat Flu")
print("    Harga: Rp10000 | Stok: 5 | Mahal | Tersedia")

print("--------------------------------")
print("       KUIS TRUE / FALSE")
print("--------------------------------")

# Daftar pertanyaan
soal = [
    ("Berapa harga Paracetamol?", "angka", "==", 5000),
    ("Berapa stok Vitamin C?", "angka", ">", 20),
    ("Antasida termasuk obat murah? (ya/tidak)", "teks", "==", "ya"),
    ("Berapa harga Oralit?", "angka", "<", 5000),
    ("Obat Batuk termasuk kategori mahal? (ya/tidak)", "teks", "==", "ya"),
    ("Berapa stok Ibuprofen?", "angka", ">=", 18),
    ("Apakah CTM tidak tersedia? (ya/tidak)", "teks", "==", "tidak"),
    ("Berapa harga Promag?", "angka", "!=", 6000),
    ("Berapa harga Betadine?", "angka", "<=", 15000),
    ("Apakah Obat Flu tersedia? (ya/tidak)", "teks", "==", "ya")
]

# Mengacak pertanyaan
random.shuffle(soal)

lanjut = "ya"

while lanjut == "ya" and len(soal) > 0:

    pertanyaan = soal.pop(0)

    print("\nPERTANYAAN:")
    print(pertanyaan[0])

    jawab = input("Masukkan jawaban: ").strip().lower()

    # Memeriksa jenis jawaban
    if pertanyaan[1] == "angka":
        try:
            jawab = int(jawab.replace(".", "").replace(",", ""))
        except ValueError:
            print("Masukkan jawaban berupa angka!")
            soal.append(pertanyaan)
            continue

    # Operator pembanding
    if pertanyaan[2] == "==":
        hasil = jawab == pertanyaan[3]

    elif pertanyaan[2] == "!=":
        hasil = jawab != pertanyaan[3]

    elif pertanyaan[2] == ">":
        hasil = jawab > pertanyaan[3]

    elif pertanyaan[2] == "<":
        hasil = jawab < pertanyaan[3]

    elif pertanyaan[2] == ">=":
        hasil = jawab >= pertanyaan[3]

    elif pertanyaan[2] == "<=":
        hasil = jawab <= pertanyaan[3]

    print("Hasil:", hasil)

    if len(soal) > 0:
        lanjut = input(
            "\nApakah ingin melanjutkan? (ya/tidak): "
        ).strip().lower()
    else:
        print("\nSemua pertanyaan telah selesai!")

print("\n================================")
print("TERIMA KASIH TELAH MENGGUNAKAN")
print("         APOTEK SEHAT")
print("================================")