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
        st.button("Seients", key = "Botó 3")
        
#Subpagina Openheimer(x1)
def openheimer():
    st.write("Hello")

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

