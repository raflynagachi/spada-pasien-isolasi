import streamlit as st

def app():
    st.header('Tujuan Penelitian')
    st.markdown("""
    Pemanfaatan Machine Learning untuk menerapkan langkah efektif
    bagi Pemerintah dalam menetapkan kebijakan selama pandemi COVID-19.
      
    Tujuan penelitian dibagi menjadi 2, yakni:
    * Prediksi jumlah pasien ICU dan isolasi COVID-19
    * Rekomendasi jumlah tempat tidur ICU dan isolasi optimum berdasarkan BOR
    """)
    # * Mengestimasi kebutuhan oksigen harian
