# -*- coding: utf-8 -*-
"""StreamlitDashboard_Rachel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s-oYaMa6UqfdZxXmqblTNG9ynV40ppUR
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

@st.cache_resource
def load_data():
  ds_hour = pd.read_csv("../dataset/hour.csv")
  return ds_hour

data = load_data()

st.title("Bike Share Dashboard")
st.sidebar.title("Profile")
st.sidebar.markdown("**Name: Rachel Gultom**")
st.sidebar.markdown("**Email: rachelgultom5@gmai.com**")

st.sidebar.title("Bike Share Dataset")

if st.sidebar.checkbox("Show Dataset"):
  st.subheader("Raw Data")
  st.write(data)

if st.sidebar.checkbox("Show Statistics"):
  st.subheader("Statistics")
  st.write(data.describe())

st.sidebar.markdown("[Sumber Dataset] : https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset")

st.sidebar.markdown('** Weather: **')
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Party cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds' )
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')


col1, col2 = st.columns(2)

with col1:
  season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
  data['season_label'] = data['season'].map(season_mapping)

  season_count = data.groupby('season_label')["cnt"].sum().reset_index()
  fig_season_count = px.bar(season_count, x='season_label',
                            y='cnt', title='Season-wise Bike Share Count')
  st.plotly_chart(fig_season_count, use_container_width=True,
                  height = 400, width=600)

with col2:
  weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
  fig_weather_count = px.bar(weather_count, x='weathersit',
                            y='cnt', title='Weather-wise Bike Share Count')
  st.plotly_chart(fig_weather_count, use_container_width=True,
                  height = 400, width=800)

hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(hourly_count, x='hr',
                            y='cnt', title='Hourly Bike Share Count')
st.plotly_chart(fig_hourly_count, use_container_width=True,
                  height = 400, width=600)

fig_humadity_chart = px.scatter(data, x='hum', y='cnt', title='Bike Share Count vs Humidity')
st.plotly_chart(fig_humadity_chart)

fig_wind_speed_chart = px.scatter(data, x='windspeed', y='cnt', title='Bike Share Count vs Wind Speed')
st.plotly_chart(fig_wind_speed_chart)

fig_temp_chart = px.scatter(data, x='temp', y='cnt', title='Bike Share Count vs Temperature')
st.plotly_chart(fig_temp_chart, use_container_width=True, height=400, width=800)

st.sidebar.title("About")
st.sidebar.info("Dashboard ini menggunakan streamlit yang berfungsi untuk memvisualisasikan sekumpulan data yang ada di dalam dataset yaitu Bike Share Dataset."
                "Dashboard ini menampilkan informasi tentang penyewaan sepeda berdasarkan banyak variabel diantaranya seperti suhu,musim,kecepatan angin,hari libur,kelembapan dan variabel lainnya")