import streamlit as st
from PIL import Image
def app():
    st.header('Latar Belakang')
    image = Image.open('images/covid_article.png')
    st.image(image, caption='Covid articles')
    st.markdown("""
    sumber: 
    * https://news.detik.com/berita/d-5646248/tempat-tidur-isolasi-pasien-covid-di-140-rs-dki-terisi-90-icu-94, Jumat, 16 Jul 2021
    * https://tirto.id/tempat-tidur-rs-covid-19-di-dki-jakarta-terisi-93-persen-ghhA, 28 Juni 2021
    ---
    """)
    st.markdown("""
        &emsp; Pada tanggal 16 Juli 2021 data keterisian tempat tidur atau bed occupancy rate (BOR) untuk pasien covid-19 dirumah sakit jakarta masih tinggi. Keterisian tempat tidur isolasi mencapai 90 persen, sedangkan keterisian ruang ICU 94 persen.
        
        &emsp; Berdasarkan data dari pemprov DKI Jakarta per Jum’at (16/7/2021), saat ini ada 140 rumah sakit yang menangani pasien covid-19. dari ratusan rumah sakit tersebut kapasitas tempat tidur isolasi sudah terisi 90 persen atau sebanyak 10.394. Kemudian ruang ICU RS Jakarta telah terpakai sebanyak 94 persen atau 1.436.
        
        &emsp; Tentunya bukan hal yang mustahil kejadian ini bisa terjadi kapan saja sehingga perlu adanya antisipasi dan langkah efektif dari pemerintah dalam mengeluarkan kebijakan terkait kebutuhan rumah sakit dalam menghadapi pandemi covid-19. terdapat beberapa hambatan yaitu sulitnya memprediksi jumlah pasien ICU dan Isolasi dan kesulitan menentukan rekomendasi jumlah tempat tidur.
    """)