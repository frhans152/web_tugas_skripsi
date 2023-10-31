import streamlit as st
from ML import KNN , lable, lable_class , df , train_test , df_test
from streamlit_option_menu import option_menu 
import pandas as pd

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
    st.title("DI Balik Layar")
    st.header("Full Data Set")
    st.header("Data TerNormalisasi")
    st.dataframe(data=df )
    ratio = st.number_input("masukan rasio pembagi dataset contoh : 0.30")
    bagi = train_test(df , ratio=ratio)
    df_train = pd.read_csv('train.csv')
    df_test =  pd.read_csv('test.csv')
    if st.button("generate data"):
        st.header("Data Test")
        df_test = df_test.iloc[:,-2:]
        st.dataframe(data=df_test)
        st.header("Data Train")
        df_train = df_train.iloc[:,-2:]
        st.dataframe(data=df_train)
    k = int(st.number_input("Masukan nilai K"))
    mode = st.selectbox(label='Pilih mode' , options=["Train" , "Test"])
    if st.button("Coba"):
        if mode == "Train" :
            knn = KNN(df_train)
            hasilh = knn.Train(k = k , auto_k=False , name = "Train")
            inputs = {lable[14]: df_train['Skor stress'],
                      lable_class: df_train[lable_class],
                      "KNN" : hasilh}
            df = pd.DataFrame(inputs)
            st.dataframe(df)
            akur = open('histori_Train.txt' , 'r')
            akur1 = akur.readlines()
            for data in akur1 : 
                st.write(data)
            st.write(knn.report)
            akur.close()
        if mode == "Test" :
            knn = KNN(df_test)
            hasilh = knn.Train(k = k , auto_k=False , name = "Test")
            inputs = {lable[14]: df_test['Skor stress'],
                      lable_class: df_test[lable_class],
                      "KNN" : hasilh}
            df = pd.DataFrame(inputs)
            st.dataframe(df)
            akur = open('histori_Test.txt' , 'r')
            akur1 = akur.readlines()
            for data in akur1 : 
                st.write(data)
            st.write(knn.report)
            akur.close()
            
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
