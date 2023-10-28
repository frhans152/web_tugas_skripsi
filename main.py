import streamlit as st
from memory import Memory
from ML import KNN , lable , df_train

def find(data , f):
    for i in range(len(data)):
        if data[i] == f : return i
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
    akur = open('histori_Train.txt' , 'r')
    ak = []
    for t in akur :
        data = t.split()
        for i in range(len(data)):
            if data[i] == 'accuracy' :
                ak.append(data[2])
    p = f'''Dari hasil analysis Program kami user bernama {inpt1} ,
    pada prodi {inpt2} Tingkat stres anda {hasils} dengan akurasi program(Training dan Test) : {ak[0]} , 
    Jika anda sudah merasa lelah dengan keadaan Maka dekatkan lah hati kepada Tuhan'''
    st.write(p)