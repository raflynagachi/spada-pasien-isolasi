import streamlit as st
import datetime
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import DateOffset

############################# FUNCTION DEF
def prediksi(model, days):
      # Create forecast object
  forecast = model.get_forecast(steps=days)

  # Extract predicted mean attribute
  df_prediksi = forecast.predicted_mean
  return df_prediksi

def plot_data(col, df_a, df_b):
  plt.figure(figsize=(12,5))
  fig, ax = plt.subplots()
  # Plot past CO2 levels
  ax.plot(df_a.index, df_a, label='past')
  
  # Plot the prediction means as line
  ax.plot(df_b.index, df_b, label='predicted')

  # Plot legend and show figure
  ax.legend()
  col.pyplot(fig)
############################# END FUNCTION DEF

def app():
  ############################# STREAMLIT CODE
  st.header('Tugas Akhir: Analisis Pasien Isolasi Covid-19 guna Optimalisasi Ketersediaan Tempat Tidur di Rumah Sakit (studi kasus: DKI Jakarta)')
  st.markdown('---')
  # set sidebar for input
  min_date = datetime.datetime.strptime('2021-11-21', '%Y-%m-%d').date()
  max_date = min_date + datetime.timedelta(days=365)
  date = st.date_input('Pick a date: ', min_value=min_date, max_value=max_date)
  datediff = (date - min_date).days
  date_end = 356+datediff
  st.write(("{} days after {}: \n".format(datediff, min_date)))

  # load dataset for plotting purpose
  df_isolasi = pd.read_csv('dataset/df_isolasi.csv', parse_dates=[0], index_col=0)
  df_icu = pd.read_csv('dataset/df_icu.csv', parse_dates=[0], index_col=0)

  # load the saved model
  filename_isolasi = 'saved_model/isolasi_model.pkl'
  filename_icu = 'saved_model/icu_model.pkl'
  isolasi_model = pickle.load(open(filename_isolasi, 'rb'))
  icu_model = pickle.load(open(filename_icu, 'rb'))

  # predict
  df_prediksi_isolasi = prediksi(isolasi_model, datediff)
  df_prediksi_icu = prediksi(icu_model, datediff)

  # plotting
  col1, col2 = st.columns(2)
  col1.write("Prediksi pasien isolasi")
  plot_data(col1, df_isolasi, df_prediksi_isolasi)
  col2.write("Prediksi ICU")
  plot_data(col2, df_icu, df_prediksi_icu)

  # rekomendasi 
  df_rekom_isolasi = pd.DataFrame()
  df_rekom_icu = pd.DataFrame()
  df_rekom_isolasi['TT Isolasi Batas Atas'] = round(df_prediksi_isolasi/0.6)
  df_rekom_isolasi['TT Isolasi Batas Bawah'] = round(df_prediksi_isolasi/0.85)
  df_rekom_icu['TT ICU Batas Atas'] = round(df_prediksi_icu/0.6)
  df_rekom_icu['TT ICU Batas Bawah'] = round(df_prediksi_icu/0.85)

  df_rekom_isolasi.sort_values('TT Isolasi Batas Atas', ascending=False, inplace=True)
  df_rekom_icu.sort_values('TT ICU Batas Atas', ascending=False, inplace=True)

  st.write('Rekomendasi Jumlah Tempat Tidur Isolasi pada periode 22-11-2021 sampai 21-12-2021 adalah {} - {}.'.format(
    df_rekom_isolasi['TT Isolasi Batas Bawah'][0],
    df_rekom_isolasi['TT Isolasi Batas Atas'][0]
  ))

  st.write('Rekomendasi Jumlah Tempat Tidur ICU pada periode 22-11-2021 sampai 21-12-2021 adalah {} - {}.'.format(
    df_rekom_icu['TT ICU Batas Bawah'][0],
    df_rekom_icu['TT ICU Batas Atas'][0]
  ))

  ############################# END STREAMLIT CODE
  
if __name__ == '__main__':
  app()