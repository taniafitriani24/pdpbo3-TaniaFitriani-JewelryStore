from barang import Barang

class Barangnya(Barang):
    def __init__(self, nama, jumlah, warna, jenis):
        super().__init__(jumlah)
        self.nama = nama
        self.warna = warna
        self.jenis = jenis

    def get_nama(self):
        return self.nama

    def get_warna(self):
        return self.warna

    def get_jenis(self):
        return self.jenis