# fungsi untuk memastikan input adalah angka
# dan mengulangi permintaan jika input bukan angka
# jjuga membatasi nilai dari 0 hingga 100.
def nilai(str):
    while True:
        try:
            poin = float(input(str))
            if poin < 0 or poin > 100:
                print(f"Nilai harus berkisar dari 0 hingga 100.")
            else:
                return poin
        except ValueError:
            print("Input harus berupa angka!!")

# list yang kosong
r = []

# perulangan untuk meminta input dari pengguna
while True:
    Nama     = input("Masukkan Nama: ")
    NIM      = int(input("Masukkan NIM (e.g. 123456789): "))
    Tugas    = nilai("Masukkan Nilai Tugas: ")
    UTS      = nilai("Masukkan Nilai UTS: ")
    UAS      = nilai("Masukkan Nilai UAS: ")
    Akhir    = ((Tugas*0.3) + (UTS*0.35) + (UAS*0.35))
    
    # menyimpan data ke list
    r.append({
        "Nama": Nama, 
        "NIM": NIM, 
        "Nilai Tugas": Tugas, 
        "Nilai UTS": UTS, 
        "Nilai UAS": UAS, 
        "Nilai Akhir": Akhir
        })
    
    # setelahnya akan menanyakan apakah pengguna ingin menambahkan data
    # jika input adalah "t" maka loop berhenti
    ulang    = input("Tambah data lagi? (y/t): ").lower()
    if ulang == "t":
        break
    
# untuk mencetak table data
print('_'*70)
print(f"| {'No':^3} | {'Nama':^10} | {'NIM':^10} | {'Tugas':^6} | {'UTS':^6} | {'UAS':^6} | {'Akhir':^6} |")
print('='*70)
for i, data in enumerate(r, start=1):
    print(f"| {i:^3} | {data['Nama']:^10} | {data['NIM']:^10} | {data['Nilai Tugas']:^6.1f} | {data['Nilai UTS']:^6.1f} | {data['Nilai UAS']:^6.1f} | {data['Nilai Akhir']:^6.1f} |")
print('‾'*70)