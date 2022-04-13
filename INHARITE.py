from distutils.log import warn


class toko():
    def __init__(self,warna,jenis,harga):
        self.warna = warna
        self.jenis = jenis
        self.harga = harga

    def cek_id_toko(self):
        print('Warna :',self.warna,'\nJenis :',self.jenis, '\nHarga :',self.harga)

class tokoPensil(toko):
    def cek_id_toko(self):
        print('Cetak Toko Pensil')

toko1 = toko('Kuning','Cat air', 20000)
toko2 = tokoPensil('Hitam','Pensil 2B', 5000)

toko1.cek_id_toko()
toko2.cek_id_toko()

    