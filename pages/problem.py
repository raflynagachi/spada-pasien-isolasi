import streamlit as st

def app():
    st.header('Rumusan Masalah')
    st.markdown("""
    Problem statement proyek ini, yakni:
    * Kesulitan prediksi jumlah pasien ICU dan Isolasi COVID-19
    * Kesulitan mementukan rekomendasi jumlah tempat tidur ICU dan isolasi optimum
    """)
    # * Kesulitan prediksi estimasi kebutuhan oksigen harian
