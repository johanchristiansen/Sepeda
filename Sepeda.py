import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
# Dataframe pertama
hour_df = pd.read_csv("hour.csv")
# Dataframe kedua
day_df = pd.read_csv("day.csv")

# Hitung total peminjaman sepeda (cnt) berdasarkan musim
total_cnt_by_season = hour_df.groupby('season')['cnt'].sum().reset_index()
# Urutkan musim berdasarkan total peminjaman sepeda secara menurun
total_cnt_by_season = total_cnt_by_season.sort_values(by='cnt', ascending=False)

# Hitung rata-rata peminjaman sepeda (cnt) untuk hari kerja dan hari libur
avg_cnt_by_day = day_df.groupby('workingday')['cnt'].mean().reset_index()
# Ubah label workingday menjadi 'Hari Libur' dan 'Hari Kerja'
avg_cnt_by_day['workingday'] = avg_cnt_by_day['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})

# Streamlit app
st.title('Data Peminjaman Sepeda')

# Visualisasi pertama
st.subheader('Total Peminjaman Sepeda Berdasarkan Musim')
plt.figure(figsize=(10, 6))
plt.bar(total_cnt_by_season['season'], total_cnt_by_season['cnt'], color='skyblue')
plt.title('Total Peminjaman Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Total Peminjaman Sepeda')
plt.xticks(ticks=total_cnt_by_season['season'], labels=['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot()

# Visualisasi kedua
st.subheader('Rata-rata Peminjaman Sepeda per Hari')
plt.figure(figsize=(8, 5))
plt.bar(avg_cnt_by_day['workingday'], avg_cnt_by_day['cnt'], color=['blue', 'green'])
plt.title('Rata-rata Peminjaman Sepeda per Hari')
plt.xlabel('Jenis Hari')
plt.ylabel('Rata-rata Peminjaman Sepeda')
st.pyplot()
