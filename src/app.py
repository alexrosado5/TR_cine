# Importar llibreries
import streamlit as st
from streamlit_gsheets import GSheetsConnection


#Sheet connection


def homepage(session_state):
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
        if st.button("Seients", key="Botó 1")== True:
            session_state.counter = 2
            st.rerun()
            
        


    ##Foto 2
    with col2:
        st.header("Nieve")
        image1 = "../assets/scc.jpeg"
        st.image(image1, width = 235)
        if st.button("Seients", key= "Botó 2") == True:
            session_state.counter = 3
            st.rerun()

    ##Foto 3
    with col3:
        st.header("Barbie")
        image2 = "../assets/bar.jpeg"
        st.image(image2, width = 235)
        if st.button("17:45", key = "Botó 3") == True:
            session_state.counter = 4
            st.rerun()

#Subpagina Openheimer(x1)
def openheimer():
    st.title("Escull els teus seients")
    image3 = "../assets/Pantalla cine.png"
    st.image(image3, width= 800)
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        pass

    with col2:
        for i in range(0, 10):
            st.button(f"A{i}")

    with col3:
        for i in range(0, 10):
            st.button(f"B{i}")

    with col4:
        pass
    with col5:
        pass

    with col6:
        pass

    with col7:
        for i in range(0, 10):
            st.button(f"D{i}")
    with col8:
        for i in range(0, 10):
            st.button(f"E{i}")

def barbie():
    st.image("../assets/barbielove.png", width=200)
    st.title("Escull els teus seients")
    image4 = "../assets/Pantalla cine.png"
    st.image(image4, width= 800)
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        pass

    with col2:
        for i in range(0, 10):
            st.button(f"A{i}")

    with col3:
        for i in range(0, 10):
            st.button(f"B{i}")

    with col4:
        pass
    with col5:
        pass

    with col6:
        pass

    with col7:
        for i in range(0, 10):
            st.button(f"D{i}")
    with col8:
        for i in range(0, 10):
            st.button(f"E{i}")
                
        

#Subpagina Nieve(x2)


#Funció principal de la pàgina
def main():
    
    session_state = st.session_state
    if "counter" not in session_state:
        session_state.counter = 1

    paginas = ["Inici", "Oppenheimer", "Nieve", "Barbie"]
    pagina_seleccionada = st.sidebar.radio("Selecciona la pàgina", paginas, index=session_state.counter -1)
    if (pagina_seleccionada =="Inici"):
        homepage(session_state)
    elif (pagina_seleccionada == "Oppenheimer"):
        openheimer()
    elif pagina_seleccionada == "Nieve":
        st.write("No")
    elif pagina_seleccionada == "Barbie":
        barbie()
    


if __name__=="__main__":
    main()

