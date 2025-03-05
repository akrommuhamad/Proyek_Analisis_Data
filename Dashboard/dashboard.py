import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("Dashboard/main_data.csv")

df = load_data()

# Sidebar: Pilihan Analisis
st.sidebar.title("Bike Sharing Dashboard")
analysis_option = st.sidebar.radio(
    "Pilih Analisis:",
    ("Tren Penyewaan Sepeda", "Pengaruh Cuaca", "Penyewaan: Hari Kerja vs Akhir Pekan")
)

# **1️⃣ Tren Penyewaan Sepeda**
if analysis_option == "Tren Penyewaan Sepeda":
    st.title("📈 Tren Penyewaan Sepeda")
    
    monthly_rentals = df.groupby("mnth")["cnt"].sum().reset_index()
    
    plt.figure(figsize=(10,5))
    sns.lineplot(x=monthly_rentals["mnth"], y=monthly_rentals["cnt"], marker="o", color="b")
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Penyewaan")
    plt.title("Tren Penyewaan Sepeda per Bulan")
    plt.xticks(range(1,13), ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
    st.pyplot(plt)

    st.write("📊 **Insight:** Penyewaan sepeda meningkat di musim panas dan menurun saat musim dingin.")

# **2️⃣ Pengaruh Cuaca terhadap Penyewaan**
elif analysis_option == "Pengaruh Cuaca":
    st.title("☀️ Pengaruh Cuaca terhadap Penyewaan Sepeda")

    weather_rentals = df.groupby("weathersit")["cnt"].mean().reset_index()
    
    plt.figure(figsize=(8,5))
    sns.barplot(x=weather_rentals["weathersit"], y=weather_rentals["cnt"], palette="coolwarm")
    plt.xlabel("Kondisi Cuaca (1=Baik, 3=Buruk)")
    plt.ylabel("Rata-rata Penyewaan")
    plt.title("Dampak Cuaca terhadap Penyewaan Sepeda")
    st.pyplot(plt)

    st.write("📊 **Insight:** Penyewaan sepeda menurun signifikan saat cuaca buruk.")

# **3️⃣ Perbedaan Penyewaan di Hari Kerja vs Akhir Pekan**
elif analysis_option == "Penyewaan: Hari Kerja vs Akhir Pekan":
    st.title("🏢 Hari Kerja vs Akhir Pekan")
    
    workday_rentals = df.groupby("workingday")["cnt"].mean().reset_index()

    plt.figure(figsize=(8,5))
    sns.barplot(x=workday_rentals["workingday"], y=workday_rentals["cnt"], palette="coolwarm")
    plt.xlabel("Hari Kerja (0=Akhir Pekan, 1=Hari Kerja)")
    plt.ylabel("Rata-rata Penyewaan")
    plt.title("Perbedaan Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan")
    st.pyplot(plt)

    st.write("📊 **Insight:** Penyewaan hampir sama antara hari kerja dan akhir pekan, menunjukkan penggunaan untuk transportasi dan rekreasi.")

    st.title("🎉 Dampak Hari Libur terhadap Penyewaan Sepeda")

    holiday_rentals = df.groupby("holiday")["cnt"].mean().reset_index()

    plt.figure(figsize=(8,5))
    sns.barplot(x=holiday_rentals["holiday"], y=holiday_rentals["cnt"], palette="coolwarm")
    plt.xlabel("Hari Libur (0=Bukan Libur, 1=Libur)")
    plt.ylabel("Rata-rata Penyewaan")
    plt.title("Dampak Hari Libur terhadap Penyewaan Sepeda")
    st.pyplot(plt)

    st.write("📊 **Insight:** Penyewaan sedikit lebih rendah pada hari libur, kemungkinan karena berkurangnya perjalanan rutin ke kantor/sekolah.")
