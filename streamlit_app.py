import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import background, problem, purposes,\
    about, forecasting # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("UGM-01 Kelompok 9")

# Add all your applications (pages) here
app.add_page("Forecasting", forecasting.app)
app.add_page("Latar Belakang", background.app)
app.add_page("Rumusan Masalah", problem.app)
app.add_page("Tujuan Penelitian", purposes.app)
app.add_page("About Us", about.app)

# The main app
app.run()
