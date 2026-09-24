# Program Menampilkan Bilangan Ganjil

n = int(input("Masukkan batas angka: "))

print("Bilangan ganjil:")

for number in range(1, n + 1, 2):
    print(number, end=" ")