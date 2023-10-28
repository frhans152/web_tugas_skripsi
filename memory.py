import pandas as pd
class table:
    def __init__(self , nama:str , NIM:int , prodi:str , skor:int , keadaan:str , next) :
        self.nama = nama
        self.NIM = NIM
        self.prodi = prodi
        self.skor = skor
        self.keadaan = keadaan
        self.next = next
class Memory:
    def __init__(self):
        self.head = None
        self.df = self.show()
    def append(self ,  nama:str , NIM:int , prodi:str , skor:int , keadaan:str):
        node = table(nama , NIM , prodi , skor , keadaan , self.head)
        self.head = node
    def show(self):
        if self.head is None:
            return None
        iters = self.head
        nama = [] ; nim = [] ; prodi = [] ; skor = [] ; keadaan = []
        while iters :
            nama.append(iters.nama)
            nim.append(iters.NIM)
            prodi.append(iters.prodi)
            skor.append(iters.skor)
            keadaan.append(iters.keadaan)
            iters = iters.next
        data = {'Nama' : nama , 'NIM' : nim , 'Skor' : skor , 'Keadaan' : keadaan}
        df = pd.DataFrame(data)
        return df