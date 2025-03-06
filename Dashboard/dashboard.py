import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Dashboard/main_data.csv", parse_dates=["dteday"])

df = load_data()

# Sidebar
st.sidebar.title("Bike Sharing Dashboard")
option = st.sidebar.selectbox("Pilih Visualisasi", ["Tren Penyewaan Bulanan", "Pengaruh Cuaca", "Hari Kerja vs Akhir Pekan"])

# 1️⃣ Tren Penyewaan Sepeda per Bulan
if option == "Tren Penyewaan Bulanan":
    st.subheader("Tren Penyewaan Sepeda per Bulan")
    
    monthly_rentals = df.groupby("mnth", observed=True)["cnt"].sum().reset_index()

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=monthly_rentals, x="mnth", y="cnt", marker="o", color="b")
    plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.xlabel("Bulan")
    plt.ylabel("Total Penyewaan Sepeda")
    plt.grid()

    st.pyplot(plt)

# 2️⃣ Pengaruh Cuaca terhadap Penyewaan
elif option == "Pengaruh Cuaca":
    st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")

    weather_rentals = df.groupby("weathersit", observed=True)["cnt"].mean().reset_index()
    weather_labels = {1: "Cerah", 2: "Mendung", 3: "Hujan/Salju"}
    weather_rentals["weathersit"] = weather_rentals["weathersit"].map(weather_labels)

    plt.figure(figsize=(8, 5))
    sns.barplot(x="weathersit", y="cnt", data=weather_rentals, palette="Blues_r")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Rata-rata Penyewaan Sepeda")

    st.pyplot(plt)

# 3️⃣ Penyewaan pada Hari Kerja vs Akhir Pekan
elif option == "Hari Kerja vs Akhir Pekan":
    st.subheader("Perbandingan Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")

    workday_rentals = df.groupby("workingday", observed=True)["cnt"].mean().reset_index()
    workday_rentals["workingday"] = workday_rentals["workingday"].map({0: "Akhir Pekan", 1: "Hari Kerja"})

    plt.figure(figsize=(6, 5))
    sns.barplot(x="workingday", y="cnt", data=workday_rentals, palette="coolwarm", order=["Hari Kerja", "Akhir Pekan"])
    plt.xlabel("Kategori Hari")
    plt.ylabel("Rata-rata Penyewaan Sepeda")

    st.pyplot(plt)



