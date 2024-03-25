# Importar llibreries
import streamlit as st


def homepage():
    # Pàgina principal

    # Títol webpage
    st.title("Benvinguts al cinema de l'Àlex")
    st.write("Cartellera")

    # Fotos peli
    ##setup
    col1, col2, col3 = st.columns(3)

    ##Foto 1
    with col1:
        st.header("Oppenheimer")
        image = "../assets/opp.jpeg"
        st.image(image, width = 220)
        button_clicked= st.button("Seients", key="Botó 1")
        st.write(button_clicked)
        
        

    ##Foto 2
    with col2:
        st.header("Nieve")
        image1 = "../assets/scc.jpeg"
        st.image(image1, width = 235)
        st.button("Seients", key= "Botó 2")

    ##Foto 3
    with col3:
        st.header("Barbie")
        image2 = "../assets/bar.jpeg"
        st.image(image2, width = 235)
        st.button("17:45", key = "Botó 3")
       
       
#Subpagina Openheimer(x1)
def openheimer():
    st.title("Escull els teus seients")
    image3 = "../assets/Pantalla cine.png"
    st.image(image3, width= 800)
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        for i in range(1, 0):
            st.button(f"A{i}")

    with col2:
        for i in range(1, 11):
            st.button(f"A{i}")

    with col3:
        for i in range(1, 11):
            st.button(f"B{i}")

    with col4:
        for i in range(1, 0):
            st.button(f"D{i}")
    with col5:
        for i in range(1, 0):
            st.button(f"A{i}")

    with col6:
        for i in range(1, 0):
            st.button(f"D{i}")

    with col7:
        for i in range(1, 11):
            st.button(f"D{i}")
    with col8:
        for i in range(1, 11):
            st.button(f"E{i}")

                
        

#Subpagina Nieve(x2)


#Funció principal de la pàgina
def main():
    paginas = ["Inici", "Oppenheimer", "Barbie", "Nieve"]
    pagina_seleccionada = st.sidebar.radio("Selecciona la pàgina", paginas)

    if (pagina_seleccionada =="Inici"):
        homepage()
    elif pagina_seleccionada == "Oppenheimer":
        openheimer()
    elif pagina_seleccionada == "Nieve":
        st.write("No")
    elif pagina_seleccionada == "Barbie":
        st.write("Si")


if __name__=="__main__":
    main()

