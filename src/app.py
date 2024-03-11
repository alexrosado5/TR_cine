# Importar llibreries
import streamlit as st


# Pàgina principal

# Títol webpage
st.title("Benvinguts al cinema de l'Àlex")
st.write("Cartellera")

# Foto peli

st.header("Oppenheimer")

image = "../assets/opp.jpeg"
st.image(image, width = 300)

