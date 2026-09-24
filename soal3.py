# Program Menampilkan Deret Fibonacci

n = int(input("Masukkan jumlah deret Fibonacci: "))

first = 0
second = 1

print("Deret Fibonacci:")

for i in range(n):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number