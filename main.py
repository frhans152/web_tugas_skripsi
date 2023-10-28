import streamlit as st
from ML import KNN , lable , df_train ,df_test , lable_class
from streamlit_option_menu import option_menu 
import pandas as pd

with st.sidebar :
    option = option_menu(
        menu_title="MAIN MENU" ,
        options=['Tes Tingkat Stres' , 'Di Balik Layar'] , 
        icons = ['home' , 'book'] , 
        menu_icon='cast' , 
        default_index=0 , )

def find(data , f):
    for i in range(len(data)):
        if data[i] == f : return i
        
if option == "Di Balik Layar": 
    st.title("DI Balik Layar")
    st.header("Data Test")
    st.dataframe(data=df_test)
    st.header("Data Train")
    st.dataframe(data=df_train)
    k = int(st.number_input("Masukan nilai K"))
    mode = st.text_input("Train / test")
    if st.button("Coba"):
        if mode == "Train" :
            knn = KNN(df_train)
            hasilh = knn.Train(k = k , auto_k=False , name = "Train")
            inputs = {lable[0] : df_train['1. Menjadi marah karena hal-hal kecil/sepele '],
                      lable[1] : df_train['6. Cenderung bereaksi berlebihan pada situasi '],
                      lable[2] : df_train['8. Kesulitan untuk relaksasi/bersantai '],
                      lable[3] : df_train['11. Mudah merasa kesal '],
                      lable[4] : df_train['12. Merasa banyak menghabiskan energi karena cemas '],
                      lable[5] : df_train['14. Tidak sabaran '],
                      lable[6] : df_train['18. Ketakutan tanpa alasan yang jelas '],
                      lable[7] : df_train['22. Tidak dapat menikmati hal-hal yang saya lakukan '],
                      lable[8] : df_train['27. Kesulitan untuk tenang setelah sesuatu yang mengganggu '],
                      lable[9] : df_train['29. Sulit untuk antusias pada banyak hal '],
                      lable[10]: df_train['32. Merasa tidak berharga '],
                      lable[11]: df_train['33. Tidak dapat memaklumi hal apapun yang menghalangi anda untuk menyelesaikan hal yang sedang Anda lakukan '],
                      lable[12]: df_train['35. Tidak ada harapan untuk masa depan '],
                      lable[13]: df_train['39. Anda Sering Gemetar (bukan karena penyakit fisik)'],
                      lable[14]: df_train['Skor stress'],
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
            hasilh = knn.Train(k = k , auto_k=False , name = "Train")
            inputs = {lable[0] : df_test['1. Menjadi marah karena hal-hal kecil/sepele '],
                      lable[1] : df_test['6. Cenderung bereaksi berlebihan pada situasi '],
                      lable[2] : df_test['8. Kesulitan untuk relaksasi/bersantai '],
                      lable[3] : df_test['11. Mudah merasa kesal '],
                      lable[4] : df_test['12. Merasa banyak menghabiskan energi karena cemas '],
                      lable[5] : df_test['14. Tidak sabaran '],
                      lable[6] : df_test['18. Ketakutan tanpa alasan yang jelas '],
                      lable[7] : df_test['22. Tidak dapat menikmati hal-hal yang saya lakukan '],
                      lable[8] : df_test['27. Kesulitan untuk tenang setelah sesuatu yang mengganggu '],
                      lable[9] : df_test['29. Sulit untuk antusias pada banyak hal '],
                      lable[10]: df_test['32. Merasa tidak berharga '],
                      lable[11]: df_test['33. Tidak dapat memaklumi hal apapun yang menghalangi anda untuk menyelesaikan hal yang sedang Anda lakukan '],
                      lable[12]: df_test['35. Tidak ada harapan untuk masa depan '],
                      lable[13]: df_test['39. Anda Sering Gemetar (bukan karena penyakit fisik)'],
                      lable[14]: df_test['Skor stress'],
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
        clasifikasi = KNN(df_train)
        hasils = clasifikasi.Class_Enggine(datah , k = 10 , auto_k=False)
        p = f'''Dari hasil analysis Program kami user bernama {inpt1} ,
        pada prodi {inpt2} Tingkat stres anda {hasils} , 
        Jika anda sudah merasa lelah dengan keadaan Maka dekatkan lah hati kepada Tuhan'''
        st.write(p)
