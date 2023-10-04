from collectons import dequeue

class AntrianBank
    def_init_(self):
        self.antrian = deque()
    
    def masuk (self.pelanggan):
        self.antrian.append(pelanggan)
        
    def keluar(self):
        if len(self.antrian) > 0:
            return self.antrian.popleft()
        else:
            print ("Antrian kosong. Tidak ada pelanggan yang dapat keluar")
            
#Contoh penggunaan:
antrian_bank.AntrianBank()
antrian_bank.masuk("Pelanggan 1")
antrian_bank.masu("Pelanggan 2")

print (antrian_bank.Keluar(1))
print (antrian_bank.keluar(1))
print (antrian.bank.keluar(1))