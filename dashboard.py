# dashboard.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data():
    # Load your dataset here
    return pd.read_csv('hour.csv')

# Function for Pertanyaan 1
def pertanyaan_1_visualisasi(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=data, x='weathersit', y='cnt', palette='Blues_r', ax=ax)
    ax.set_title('Pengaruh Cuaca terhadap Jumlah Rental Sepeda')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Rata-rata Jumlah Rental Sepeda')
    st.pyplot(fig)


# Function for Pertanyaan 2
def pertanyaan_2_visualisasi(data):
    user_comparison = data[['casual', 'registered']].mean().reset_index()
    user_comparison.columns = ['Tipe Pengguna', 'Rata-rata Jumlah Penyewaan']
    user_comparison['Tipe Pengguna'] = ['Casual', 'Registered']
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=user_comparison, x='Tipe Pengguna', y='Rata-rata Jumlah Penyewaan', palette='Blues', ax=ax)
    ax.set_title('Perbandingan Penyewaan Sepeda antara Pengguna Casual dan Pengguna Terdaftar')
    ax.set_xlabel('Tipe Pengguna')
    ax.set_ylabel('Rata-rata Jumlah Penyewaan')
    st.pyplot(fig)

# Function for Pertanyaan 3
def pertanyaan_3_visualisasi(data):
    holiday_effect = data.groupby('holiday')['cnt'].mean().reset_index()
    holiday_effect.columns = ['Hari Libur', 'Rata-rata Jumlah Penyewaan']
    holiday_effect['Hari Libur'] = ['Bukan Hari Libur', 'Hari Libur']
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=holiday_effect, x='Hari Libur', y='Rata-rata Jumlah Penyewaan', palette='Blues_r', ax=ax)
    ax.set_title('Pengaruh Hari Libur terhadap Permintaan Penyewaan Sepeda')
    ax.set_xlabel('Hari Libur')
    ax.set_ylabel('Rata-rata Jumlah Penyewaan')
    st.pyplot(fig)

def main():
    st.title('Dashboard Bike Sharing')
    data = load_data()

    # st.subheader('Pertanyaan 1: Apakah cuaca memengaruhi jumlah rental sepeda?')
    pertanyaan_1_visualisasi(data)

    # st.subheader('Pertanyaan 2: Bagaimana perbandingan perilaku perental casual dengan pengguna terdaftar dalam hal perilaku penyewaan sepeda?')
    pertanyaan_2_visualisasi(data)

    # st.subheader('Pertanyaan 3: Apakah kejadian hari libur (holiday) memengaruhi permintaan penyewaan sepeda?')
    pertanyaan_3_visualisasi(data)

if __name__ == "__main__":
    main()
