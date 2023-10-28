import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error , accuracy_score , classification_report
from sklearn.preprocessing import LabelEncoder

df_train = pd.read_csv('Train.csv')
df_test = pd.read_csv('Test.csv')
lable = ['1. Menjadi marah karena hal-hal kecil/sepele ' , 
      '6. Cenderung bereaksi berlebihan pada situasi ' ,
      '8. Kesulitan untuk relaksasi/bersantai ' , 
      '11. Mudah merasa kesal ' , 
      '12. Merasa banyak menghabiskan energi karena cemas ',
      '14. Tidak sabaran ' , 
      '18. Ketakutan tanpa alasan yang jelas ',
      '22. Tidak dapat menikmati hal-hal yang saya lakukan ' ,
      '27. Kesulitan untuk tenang setelah sesuatu yang mengganggu ',
      '29. Sulit untuk antusias pada banyak hal ',
      '32. Merasa tidak berharga ',
      '33. Tidak dapat memaklumi hal apapun yang menghalangi anda untuk menyelesaikan hal yang sedang Anda lakukan ',
      '35. Tidak ada harapan untuk masa depan ',
      '39. Anda Sering Gemetar (bukan karena penyakit fisik)' ,
      'Skor stress']
lable_class = 'Keterangan'

class KNN:
      ''' # HANDMADE KNN ENGGINE
      ini adalah implementasi dari mathematika manual KNN (Basic)'''
      def __init__(self , table):
            self.table = table 
      def search(self , data , model : str):
            '''Linear search'''
            if model == "knn" : 
                  for i in range(len(data)):
                        if data[i] == np.min(data): return i
            if model == "k" : 
                  for j in range(len(data)):
                        if data[i] == np.max(data): return j
      def write_History(self , actual : list , prediksi : list , name):
            le1 = LabelEncoder()
            le1.fit(actual)
            self.actual_le = le1.transform(actual)
            le2 = LabelEncoder()
            le2.fit(prediksi)
            prediksi_le = le2.transform(prediksi)
            if name == 'Train' : 
                  t = open('histori_Train.txt' , 'w')
                  eror = mean_absolute_error(self.actual_le , prediksi_le)
                  acs = accuracy_score(self.actual_le , prediksi_le)
                  self.report = classification_report(self.actual_le , prediksi_le)
                  t.write(f"{name}\n")
                  t.write(f"accuracy : {np.round(acs,decimals=2) * 100}% | Error : {np.round(eror,decimals=2)}")
                  t.close()
            if name == "Test" : 
                  t = open('histori_Test.txt' , 'w')
                  eror = mean_absolute_error(self.actual_le , prediksi_le)
                  acs = accuracy_score(self.actual_le , prediksi_le)
                  self.report = classification_report(self.actual_le , prediksi_le)
                  t.write(f"{name}\n")
                  t.write(f"accuracy : {np.round(acs,decimals=2) * 100}% | Error : {np.round(eror,decimals=2)}")
                  t.close()
      def Auto_K (self , range : int):
            self.piluh_k = [] ; self.ks = []
            for l in range(1, range-1):
                  self.ks.append(l)
                  pred = [] 
                  for i in range(len(self.table)):
                        inputs = [self.table['1. Menjadi marah karena hal-hal kecil/sepele '][i],
                                  self.table['6. Cenderung bereaksi berlebihan pada situasi '][i],
                                  self.table['8. Kesulitan untuk relaksasi/bersantai '][i],
                                  self.table['11. Mudah merasa kesal '][i],
                                  self.table['12. Merasa banyak menghabiskan energi karena cemas '][i],
                                  self.table['14. Tidak sabaran '][i],
                                  self.table['18. Ketakutan tanpa alasan yang jelas '][i],
                                  self.table['22. Tidak dapat menikmati hal-hal yang saya lakukan '][i],
                                  self.table['27. Kesulitan untuk tenang setelah sesuatu yang mengganggu '][i],
                                  self.table['29. Sulit untuk antusias pada banyak hal '][i],
                                  self.table['32. Merasa tidak berharga '][i],
                                  self.table['33. Tidak dapat memaklumi hal apapun yang menghalangi anda untuk menyelesaikan hal yang sedang Anda lakukan '][i],
                                  self.table['35. Tidak ada harapan untuk masa depan '][i],
                                  self.table['39. Anda Sering Gemetar (bukan karena penyakit fisik)'][i],
                                  self.table['Skor stress'][i]]
                        lasts = self.Class_Enggine(inputs , k = l , auto_k=False)
                        pred.append(lasts)
                  le2 = LabelEncoder()
                  le2.fit(pred)
                  prediksi_le = le2.transform(pred)
                  acs = accuracy_score(self.actual_le , prediksi_le)
                  self.piluh_k.append(acs)
            return self.ks[self.search(self.piluh_k , model='k')]
      def Train(self , k : np.int32 , auto_k : bool , name : str) :
            pred = [] 
            for i in range(len(self.table)):
                  inputs = [self.table['1. Menjadi marah karena hal-hal kecil/sepele '][i],
                            self.table['6. Cenderung bereaksi berlebihan pada situasi '][i],
                            self.table['8. Kesulitan untuk relaksasi/bersantai '][i],
                            self.table['11. Mudah merasa kesal '][i],
                            self.table['12. Merasa banyak menghabiskan energi karena cemas '][i],
                            self.table['14. Tidak sabaran '][i],
                            self.table['18. Ketakutan tanpa alasan yang jelas '][i],
                            self.table['22. Tidak dapat menikmati hal-hal yang saya lakukan '][i],
                            self.table['27. Kesulitan untuk tenang setelah sesuatu yang mengganggu '][i],
                            self.table['29. Sulit untuk antusias pada banyak hal '][i],
                            self.table['32. Merasa tidak berharga '][i],
                            self.table['33. Tidak dapat memaklumi hal apapun yang menghalangi anda untuk menyelesaikan hal yang sedang Anda lakukan '][i],
                            self.table['35. Tidak ada harapan untuk masa depan '][i],
                            self.table['39. Anda Sering Gemetar (bukan karena penyakit fisik)'][i],
                            self.table['Skor stress'][i]]
                  lasts = self.Class_Enggine(inputs , k = k , auto_k=auto_k)
                  pred.append(lasts)
            self.write_History(self.table[lable_class] , pred , name=name)
            return pred
      def Class_Enggine(self , data_input  ,k : np.int32, auto_k : bool):
            '''# Predict
            Method ini di gunakan untuk mengklasifikasi'''
            distance = [] 
            penampung = [[] for _ in range(k)]
            if auto_k : k = self.Auto_K(range=30)
            else : k = k
            for a in range(k):
                  for b in range(len(lable)):
                        penampung[a].append(self.table[lable[b]][a])
                        if len(penampung[a]) == len(data_input):
                              add = []
                              add.append(np.square(data_input[b] - penampung[a][b]))
                              ecludean = np.sqrt(np.sum(add))
                              distance.append(ecludean)
                        else : continue 
            return self.table[lable_class][self.search(distance , model='knn')]
      
knn = KNN(df_test)
tezt = knn.Train(k=41 , auto_k=False , name = "Test")
data = {"Real Data" : df_test[lable_class] , "KNN" : tezt}
df_tez = pd.DataFrame(data)

knn2 = KNN(df_train)
tezt2 = knn.Train(k=38 , auto_k=False , name = "Train")
data2 = {"Real Data" : df_test[lable_class] , "KNN" : tezt2}
df_tez2 = pd.DataFrame(data2)
print(df_tez2)
