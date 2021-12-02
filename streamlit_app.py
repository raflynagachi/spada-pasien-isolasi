import streamlit as st
import datetime
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import DateOffset

# set sidebar for input
min_date = datetime.datetime.strptime('2021-11-21', '%Y-%m-%d').date()
max_date = min_date + datetime.timedelta(days=365)
date = st.sidebar.date_input('Pick date: ', min_value=min_date, max_value=max_date)
datediff = (date - min_date).days
date_end = 356+datediff
# st.write((date_end))

# load the model from disk
filename = 'sarimax_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

data_merge = pd.read_csv('data_merge.csv')

data_merge['forecast'] = loaded_model.predict(start = 356, end = date_end, dynamic= True)
st.line_chart(data_merge[['forecast']])
