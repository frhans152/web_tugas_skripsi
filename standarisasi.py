import numpy as np

class Standarisasi:
    '''Standarisasi data adalah proses mengubah data sehingga setiap fitur memiliki rata-rata 0 dan simpangan baku 1. 
    Dengan melakukan standarisasi, kita menghilangkan perbedaan skala antara fitur, 
    sehingga setiap fitur memiliki pengaruh yang seimbang dalam perhitungan jarak.
    Ini membuat perhitungan jarak lebih adil dan mewakili hubungan antara fitur lebih baik.'''
    def __init__(self , data) :
        self.data = data
    def mu(self , data):
        n = len(data)
        rata_rata = lambda n : np.sum(data)/n 
        return np.round(rata_rata(n),decimals=2)
    def Standart_Deviasi(self , data):
        n = len(data)
        muX = self.mu(data) ; x_muX2 = []
        for i in range(n) : 
            x_muX2.append(np.square(data[i] - muX))
        sigma = lambda n , seq_X : np.sqrt(np.sum(seq_X) / n)
        return sigma(n , x_muX2)
    def Enggine(self):
        standart = map(lambda data : np.round(
            data - self.mu(self.data) / self.Standart_Deviasi(self.data) , decimals=2) , self.data)
        return np.array(list(standart))
St = Standarisasi([2,3,5,7])
print(St.Enggine())