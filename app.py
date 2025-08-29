import streamlit as st
from streamlit_option_menu import option_menu
from requirements

st.title("Aplikasi Sederhana Kalkulator, Konversi Suhu, dan Fibonacci")
st.write("Pilih salah satu menu di bawah ini untuk menggunakan aplikasi.")
selected = option_menu(
    menu_title=None,
    options=["Kalkulator", "Konversi Suhu", "Fibonacci"],
    icons=["calculator", "thermometer-half", "list-ol"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Kalkulator
if selected == "Kalkulator":
    st.header("Kalkulator Sederhana")
    num1 = st.number_input("Masukkan angka pertama:", value=0)
    num2 = st.number_input("Masukkan angka kedua:", value=0)
    operation = st.selectbox("Pilih operasi:", ["Tambah", "Kurang", "Kali", "Bagi"])
    
    if st.button("Hitung"):
        if operation == "Tambah":
            result = num1 + num2
        elif operation == "Kurang":
            result = num1 - num2
        elif operation == "Kali":
            result = num1 * num2
        elif operation == "Bagi":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Pembagian dengan nol"
        st.write(f"Hasil: {result}")

# Konversi Suhu
elif selected == "Konversi Suhu":
    st.header("Konversi Suhu")
    suhu = st.number_input("Masukkan suhu dalam Celsius:", value=0)
    target_unit = st.selectbox("Konversi ke:", ["Fahrenheit", "Kelvin"])
    
    if st.button("Konversi"):
        if target_unit == "Fahrenheit":
            result = (suhu * 9/5) + 32
            st.write(f"Hasil: {result} °F")
        elif target_unit == "Kelvin":
            result = suhu + 273.15
            st.write(f"Hasil: {result} K")

# Fibonacci
elif selected == "Fibonacci":
    st.header("Deret Fibonacci")
    n = st.number_input("Masukkan jumlah bilangan Fibonacci yang diinginkan:", min_value=1, value=10, step=1)
    
    if st.button("Generate"):
        fib_sequence = []
        a, b = 0, 1
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b
        st.write(f"Deret Fibonacci: {fib_sequence}")

        