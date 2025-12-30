# base_converter_streamlit.py

import streamlit as st

st.set_page_config(page_title="Divyansh Ajinkya Data Representation", page_icon="dav2.png", layout="centered")

st.title("Data Base Converter™")
st.image("4.png")
st.markdown("Convert numbers between **Decimal**, **Binary**, **Octal**, and **Hexadecimal** bases.")

# --- Input Fields ---
n = st.text_input("Enter Number:", "")
a = st.selectbox("Select Initial Base:", ["Decimal(10)", "Binary(2)", "Octal(8)", "Hexadecimal(16)"])
b = st.selectbox("Select Final Base:", ["Decimal(10)", "Binary(2)", "Octal(8)", "Hexadecimal(16)"])

# --- Conversion Logic ---
def convert_number(n, a, b):
    if not n:
        return "Please enter a number."
    try:
        # Convert to decimal first
        if a == "Decimal(10)":
            dec = int(n)
        elif a == "Binary(2)":
            dec = int(n, 2)
        elif a == "Octal(8)":
            dec = int(n, 8)
        elif a == "Hexadecimal(16)":
            dec = int(n, 16)
        else:
            return "Invalid base selected."

        # Convert from decimal to target base
        if b == "Decimal(10)":
            return str(dec)
        elif b == "Binary(2)":
            return bin(dec)[2:]
        elif b == "Octal(8)":
            return oct(dec)[2:]
        elif b == "Hexadecimal(16)":
            return hex(dec)[2:].upper()
        else:
            return "Invalid conversion target."

    except ValueError:
        return "❌ Invalid input for the selected base."

# --- Convert Button ---
if st.button("Convert!"):
    result = convert_number(n, a, b)
    st.subheader("✅ Result:")
    st.markdown(f"<h2 style='color:#FFFFFF;'>{result}</h2>", unsafe_allow_html=True)
