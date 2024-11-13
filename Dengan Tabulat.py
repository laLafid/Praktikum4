from tabulate import tabulate

apt = []

while True:
    Nama = input("Masukkan Nama: ")
    NIM = input("Masukkan NIM: ")
    Tugas = float(input("Masukkan Nilai Tugas: "))
    UTS = float(input("Masukkan Nilai UTS: "))
    UAS = float(input("Masukkan Nilai UAS: "))
    Akhir = ((Tugas * 0.3) + (UTS * 0.35) + (UAS * 0.35))
    apt.append({
        "Nama": Nama,
        "NIM": NIM,
        "Nilai Tugas": Tugas,
        "Nilai UTS": UTS,
        "Nilai UAS": UAS,
        "Nilai Akhir": Akhir
    })
    ulang = input("Tambah data lagi? (y/t): ").lower()
    if ulang == "t":
        break

headers = ["No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"]
table = [[i+1, data["Nama"], data["NIM"], data["Nilai Tugas"], data["Nilai UTS"], data["Nilai UAS"], data["Nilai Akhir"]] for i, data in enumerate(apt)]

print(tabulate(table, headers=headers, tablefmt="grid"))
