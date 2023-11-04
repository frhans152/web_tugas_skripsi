import streamlit as st
from ML import KNN , lable, lable_class , df , train_test , df_test
from streamlit_option_menu import option_menu 
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split , KFold
from sklearn.metrics import mean_absolute_error , accuracy_score ,confusion_matrix , ConfusionMatrixDisplay 
from sklearn.preprocessing import LabelEncoder , MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('stress.csv')
df = {'Skor stress' : df['Skor stress'],'Keterangan':df['Keterangan']}
df = pd.DataFrame(df)
norm  = MinMaxScaler()
df['Skor stress'] = norm.fit_transform(df['Skor stress'].values.reshape(-1 ,1))
print(df.head())
X = df['Skor stress'].values.reshape(-1,1)
laben = LabelEncoder()
df['Keterangan'] = laben.fit_transform(df['Keterangan'].values.reshape(-1,1))
print(df.head())
y = df['Keterangan'].values.reshape(-1,1)

with st.sidebar :
    option = option_menu(
        menu_title="MAIN MENU" ,
        options=['Tes Tingkat Stres' , 'Detail Perhitungan'] , 
        icons = ['home' , 'book'] , 
        menu_icon='cast' , 
        default_index=0 , )

def find(data , f):
    for i in range(len(data)):
        if data[i] == f : return i
        

if option == "Detail Perhitungan": 
    df_dp = pd.read_csv('stress.csv')
    st.title('Detail Perhitungan')
    st.header("Dataset")
    st.dataframe(df_dp)
    st.header("Bagi Dataset ke train test")
    Train_size = st.number_input("Train")
    Test_size = st.number_input("Test")
    st.header("masukan K")
    K = int(st.number_input("K"))
    if st.button("Latih Dan Tes"):
        x_train  , x_test , y_train , y_test = train_test_split(X , y , test_size=Test_size , train_size=Train_size , random_state=1)
        cols1 , cols2 = st.columns(2,gap = 'small')
        with cols1:
            st.header("Train and Test X")
            st.write("Train")
            st.dataframe(x_train)
            st.write("Test")
            st.dataframe(x_test)
        with cols2:
            st.header("Train and Test Y")
            st.write("Train")
            st.dataframe(y_train)
            st.write("Test")
            st.dataframe(y_test)
        model = KNeighborsClassifier(n_neighbors=K , weights='distance' , metric='euclidean')
        model.fit(x_train , y_train)
        y_pred = model.predict(x_test)
        lable_asli = laben.inverse_transform(y_pred)
        akt = laben.inverse_transform(y_test)
        st.header("Hasil Prediksi")
        d = {"Prediksi" : list(lable_asli) , "Data Aktual" : list(akt)}
        dfh = pd.DataFrame(d)
        st.dataframe(dfh)
        mae = mean_absolute_error(y_test , y_pred)
        acc = accuracy_score(y_test , y_pred)
        st.write(f"MAE {mae} | Accuracy {acc}")
        kf = KFold(n_splits=5)
        scores = []
        for train_index, test_index in kf.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            model.fit(X_train, y_train)
            score = model.score(X_test, y_test)
            scores.append(score)
        rata_rata = np.sum(scores) / len(scores)
        st.write("Rata Rata Cross-Validation Score (K-fold):", rata_rata)
        st.header("Confusion Matrix")
        cm = confusion_matrix(y_test , y_pred[:20])
        cmd = ConfusionMatrixDisplay(confusion_matrix=cm , display_labels=['Normal' , 'Ringan' , 'Sedang' , 'Parah' , 'Sangat parah'])
        cmd.plot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        plt.show()
        
if option == "Tes Tingkat Stres" : 
    st.title("CEK TINGKAT STRESS KAMU")
    st.header("Login dulu")
    datah = [] ; nama = [] ; prodi = [] ; nim = []
    inpt1 = st.text_input("Nama")
    inpt2 = st.text_input("Prodi")
    inpt3 = st.text_input("NIM")
    if st.button("LOGIN"):
        st.write(f'''
            Nama : {inpt1}\n
            Prodi : {inpt2}\n
            NIM : {inpt3}\n
            ''')
    pilihan = {'Tidak ada atau tidak pernah' : 0 , 'Sesuai dengan yang dialami sampai tingkat tertentu, atau kadang-kadang' : 1,
               'sering' : 2 , 'Sangat sesuai dengan yang dialami, atau hampir setiap saat ' : 3}
    plh = list(pilihan.keys())
    vals = list(pilihan.values())
    st.header("Silahkan Mengisi Data Dibawah Untuk Mengecek Tingkat Stress")
    soal1 = st.radio(lable[0] , plh)
    soal2 = st.radio(lable[1] , plh)
    soal3 = st.radio(lable[2] , plh)
    soal4 = st.radio(lable[3] , plh)
    soal5 = st.radio(lable[4] , plh)
    soal6 = st.radio(lable[5] , plh)
    soal7 = st.radio(lable[6] , plh)
    soal8 = st.radio(lable[7] , plh)
    soal9 = st.radio(lable[8] , plh)
    soal10 = st.radio(lable[9] , plh)
    soal11 = st.radio(lable[10] , plh)
    soal12 = st.radio(lable[11] , plh)
    soal13 = st.radio(lable[12] , plh)
    soal14 = st.radio(lable[13] , plh)
    if st.button("Summit"):
        tamps = []
        tamps.append([soal1 , soal2 , soal3 , soal4 , soal5 , soal6 , soal7 , soal8 , soal9 , soal10 , soal11 , soal12 , soal13 , soal14])
        for i in range(len(tamps[0])):
            datah.append(vals[find(plh , tamps[0][i])])
        s = [sum(datah)]
        datah = datah + s
        print(datah)
        df = pd.read_csv('stress.csv')
        clasifikasi = KNN(df)
        hasils = clasifikasi.Class_Enggine(datah , k = 50 , auto_k=False)
        p = f'''Dari hasil analysis Program kami user bernama {inpt1} ,
        pada prodi {inpt2} Tingkat stres anda {hasils} , 
        Jika anda sudah merasa lelah dengan keadaan Maka dekatkan lah hati kepada Tuhan'''
        st.write(p)
