import streamlit as st
from PIL import Image

def app():
    st.header('Pemabahasan')
    st.subheader('Dataset')
    st.markdown("""
    &emsp; Dataset yang digunakan merupakan data keterisian tempat tidur rumah sakit pada wilayah DKI Jakarta untuk pasien isolasi dan ICU sejak tanggal 1 Desember 2020 - 21 November 2021
    yang berjumlah 356 hari pengamatan.
    Data training: 1 December 2020 - 22 Oktober 2021
    Data testing: 23 Oktober 2021 - 21 November 2021
    """)
    image = Image.open('images/dataset_head.png')
    st.image(image, caption='Dataset head')

    # plotting
    col1, col2 = st.columns(2)
    col1.write("History total pasien isolasi")
    image = Image.open('images/data_total_pasien_isolasi.png')
    col1.image(image, caption='Dataset head')
    col2.write("History total ICU")
    image = Image.open('images/data_total_pasien_icu.png')
    col2.image(image, caption='Dataset head')

    st.subheader('Modeling')
    st.markdown("""
    &emsp; ARIMA sering juga disebut metode runtun waktu Box-Jenkins. ARIMA sangat baik ketepatannya untuk peramalan jangka pendek, sedangkan untuk peramalan jangka panjang ketepatan peramalannya kurang baik. Biasanya akan cenderung flat (mendatar/konstan) untuk periode yang cukup panjang. 
    ARIMA adalah singkatan dari AutoRegressive Integrated Moving Average. Ini adalah generalisasi dari AutoRegressive Moving Average yang lebih sederhana dan menambahkan gagasan integrasi.
    Notasi standar digunakan untuk ARIMA(p,d,q) dimana parameter disubstitusikan dengan nilai integer dimana,  
    &ensp; p : Jumlah pengamatan lag yang dimasukkan dalam model, disebut juga orde lag.  
    &ensp; d: Berapa kali data pengamatan dilakukan differencing, juga disebut degree of differencing.  
    &ensp; q: Ukuran jendela rata-rata bergerak, juga disebut urutan rata-rata bergerak.
    """)

    st.subheader('Evaluasi Model')
    st.markdown("""
    &emsp; setelah dilakukan pemodelan maka ditemukan model untuk pasien isolasi yaitu ARIMA(8,2,2) dengan nilai RMSE 25.36
    """)

    col1, col2 = st.columns(2)
    # col1.write("Prediksi total pasien isolasi")
    image = Image.open('images/evaluasi-1.png')
    col1.image(image, caption='Prediksi total pasien isolasi')
    # col2.write("Prediksi pasien isolasi (all)")
    image = Image.open('images/evaluasi-2.png')
    col2.image(image, caption='Prediksi pasien isolasi (all)')    

    st.markdown("""
    &emsp; model untuk pasien ICU yaitu Model ARIMA (4,1,0) dengan RMSE 9.27
    """)
    
    col1, col2 = st.columns(2)
    # col1.write("Prediksi total pasien ICU")
    image = Image.open('images/evaluasi-3.png')
    col1.image(image, caption='Prediksi total pasien ICU')
    # col2.write("Prediksi total pasien ICU (all)")
    image = Image.open('images/evaluasi-4.png')
    col2.image(image, caption='Prediksi total pasien ICU (all)')  
