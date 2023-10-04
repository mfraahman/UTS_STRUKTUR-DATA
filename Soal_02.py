def hitung_faktorial(n):
    if n == 0:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

# Contoh penggunaan:
bilangan = 5
hasil_faktorial = hitung_faktorial(bilangan)
print("Faktorial dari", bilangan, "adalah", hasil_faktorial)
