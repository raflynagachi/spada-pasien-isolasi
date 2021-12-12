import streamlit as st

def app():
    st.header('Kesimpulan')
    st.markdown("""
    &ensp; berdasarkan hasil prediksi pasien isolasi dan icu, jumlah pasien mengalami penurunan dari periode sebelumnya. dimana pada periode 22 November 2021 - 21 Desember 2021, jumlah pasien isolasi tertinggi sebesar 202 pada tanggal 24 November 2021 dan jumlah pasien ICU tertinggi sebesar 40 pada tanggal 22 November 2021. berdasarkan BOR (Bed Occupancy Ratio) ideal dari Kemenkes RI yaitu 65% - 80%, sehingga dapat kita tetapkan rekomendasi Jumlah tempat tidur Isolasi dan ICU pada periode tersebut yaitu:  
    &emsp; Rekomendasi Jumlah Tempat Tidur Isolasi pada periode 22 November 2021 sampai 21 Desember 2021 adalah 238 - 337 dan Rekomendasi Jumlah Tempat Tidur ICU pada periode 22 November 2021 sampai 21 Desember 2021 adalah 47 - 67.
    """)
    # * Mengestimasi kebutuhan oksigen harian
