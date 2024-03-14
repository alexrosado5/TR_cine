# Importar llibreries
import streamlit as st


# Pàgina principal

# Títol webpage
st.title("Benvinguts al cinema de l'Àlex")
st.write("Cartellera")

# Fotos peli
##setup
col1, col2, col3 = st.columns(3)

##Foto 1
argument = "Seients"
with col1:
    st.header("Oppenheimer")
    image = "../assets/opp.jpeg"
    st.image(image, use_column_width=True)
    st.button(argument, key="Botó 1")

##Foto 2
with col2:
    st.header("Nieve")
    image1 = "../assets/scc.jpeg"
    st.image(image1,use_column_width= True)
    st.button(argument, key= "Botó 2")

##Foto 3
with col3:
    st.header("Barbie")
    image2 = "../assets/bar.jpeg"
    st.image(image2, use_column_width=True)
    st.button(argument, key = "Botó 3")

#Coloquem una barra lateral per poder navegar per les subpàgines
paginas = ["Inici", "Oppenheimer", "Barbie", "Nieve"]
p_seleccionat = st.sidebar.radio("Selecciona la pàgina", paginas)



