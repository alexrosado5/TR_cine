# Importar llibreries
import streamlit as st
import streamlit.components.v1 as components
from streamlit_gsheets import GSheetsConnection
import streamlit_authenticator as stauth
from streamlit_modal import Modal
import time
import base64
from PIL import Image
#Expandir la pagina
st.set_page_config(layout="wide")
# Background image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

#Funció per canviar color dels botons
def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}';
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)


def homepage(session_state):

    # Pàgina principal
    set_background("../assets/Fondo homepage.jpg")
    # Títol webpage
    st.image("../assets/titulo.png")
    st.write("")
    st.image("../assets/Cartellera.png",width=700)
    st.write("")
    st.write("")
    st.write("")
    st.write("")


    # Fotos peli
    ##setup
    col1, col2, col3= st.columns(3)

    ##Foto 1
    with col1:
        st.image("../assets/oppemheimer2.jpeg", width=300)
        if st.button("Disponibilitat", key="Botó 1")== True:
            session_state.counter = 2
            st.rerun()
       
    ##Foto 2
    with col2:
        st.image("../assets/barbiesi.jpg", width=316)
        if st.button("Disponibilitat", key= "Botó 2") == True:
            session_state.counter = 3
            st.rerun()

    ##Foto 3
    with col3:
        st.image("../assets/sociedad.jpg",width=320)
        if st.button("Disponibilitat", key = "Botó 3") == True:
            session_state.counter = 4
            st.rerun()
    # Custom HTML/CSS for the banner
    custom_html = """
    <div class="banner">
        <img src="https://raw.githubusercontent.com/alexrosado5/TR_cine/main/assets/Banner.png" alt="Banner Image">
    </div>
    <style>
        .banner {
            width: 110%;
            height: 200px;
            overflow: hidden;
        }
        .banner img {
            width: 100%;
            object-fit: cover;
        }
    </style>
    """
    # Display the custom HTML
    st.components.v1.html(custom_html)
#Subpagina Openheimer(x1)
def openheimer(session_state):
    set_background("../assets/Fondo homepage.jpg")

    modal = Modal(
    "Confirma el teu seient", 
    key="modals",)
    #Crear connexió base de dades
    conn = st.connection("gsheets", GSheetsConnection)
    oppenheimer_worksheet = conn.read(worksheet="openheimer", usecols=["CHAIRS","AVAILABILITY"])
    oppenheimer_worksheet.dropna(inplace=True)

    chairs_opp=[]
    availability_opp=[]
    #Llegir base de dades
    for index, row in oppenheimer_worksheet.iterrows():
        chairs_opp.append(row["CHAIRS"])
        availability_opp.append(row["AVAILABILITY"])
    #Llegir seient ocupats
    occuped_chairs=[]
    for i in range(len(availability_opp)):
        if availability_opp[i]=="O":
            occuped_chairs.append(chairs_opp[i])

    #Setup pagina oppenhimer
    st.image("../assets/Oppenheimert.png")
    st.write("*Hora de la sessió: 17:00h. Preu de l'entrada: 9€*")
    st.write("Escull el teu seient.")
    # Custom HTML/CSS for the banner
    custom_html = """
    <div class="banner">
        <img src="https://raw.githubusercontent.com/alexrosado5/TR_cine/main/assets/Pantalla%20cine.png" alt="Banner Image">
    </div>
    <style>
        .banner {
            width: 110%;
            height: 200px;
            overflow: hidden;
        }
        .banner img {
            width: 100%;
            object-fit: cover;
        }
    </style>
    """
    # Display the custom HTML
    st.components.v1.html(custom_html)
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    #Crear els seients
    with col1:
        pass

    with col2:
        if "A_01" in occuped_chairs:
            st.button("A_01")
            ChangeButtonColour("A_01","white","red")
        else:
            if st.button("A_01", key="A_01"):
                session_state.a = "A_01"
                modal.open()
                
   
        
        if "A_02" in occuped_chairs:
            st.button("A_02")
            ChangeButtonColour("A_02","white","red")
            
        else:
            if st.button("A_02", key="A_02"):
                session_state.a = "A_02"
                modal.open()
                
               
            
        if "A_03" in occuped_chairs:
            st.button("A_03")
            ChangeButtonColour("A_03","white","red")
        else:
            if st.button("A_03", key="A_03"):
                session_state.a = "A_03"
                modal.open()
                

                

        if "A_04" in occuped_chairs:
            st.button("A_04")
            ChangeButtonColour("A_04","white","red")
        else:
            if st.button("A_04", key="A_04"):
                session_state.a = "A_04"
                modal.open()
                

        if "A_05" in occuped_chairs:
            st.button("A_05")
            ChangeButtonColour("A_05","white","red")
        else:
            if st.button("A_05", key="A_05"):
                session_state.a = "A_05"
                modal.open()
                

        if "A_06" in occuped_chairs:
            st.button("A_06")
            ChangeButtonColour("A_06","white","red")
        else:
            if st.button("A_06", key="A_06"):
                session_state.a = "A_06"
                modal.open()
                

        if "A_07" in occuped_chairs:
            st.button("A_07")
            ChangeButtonColour("A_07","white","red")
        else:
            if st.button("A_07", key="A_07"):
                session_state.a = "A_07"
                modal.open()
                

    with col3:
        if "B_01" in occuped_chairs:
            st.button("B_01")
            ChangeButtonColour("B_01","white","red")
        else:
            if st.button("B_01", key="A_08"):
                session_state.a = "B_01"
                modal.open()
                
                
        
        if "B_02" in occuped_chairs:
            st.button("B_02")
            ChangeButtonColour("B_02","white","red")
        else:
            if st.button("B_02", key="A_09"):
                session_state.a = "B_02"
                modal.open()
                
                
        
        if "B_03" in occuped_chairs:
            st.button("B_03")
            ChangeButtonColour("B_03","white","red")
        else:
            if st.button("B_03", key="A_10"):
                session_state.a = "B_03"
                modal.open()
                
                

        if "B_04" in occuped_chairs:
            st.button("B_04")
            ChangeButtonColour("B_04","white","red")
        else:
            if st.button("B_04", key="A_11"):
                session_state.a = "B_04"
                modal.open()
                
                

        if "B_05" in occuped_chairs:
            st.button("B_05")
            ChangeButtonColour("B_05","white","red")
        else:
            if st.button("B_05", key="A_12"):
                session_state.a = "B_05"
                modal.open()
                
                

        if "B_06" in occuped_chairs:
            st.button("B_06")
            ChangeButtonColour("B_06","white","red")
        else:
            if st.button("B_06", key="A_13"):
                session_state.a = "B_06"
                modal.open()
                
                

        if "B_07" in occuped_chairs:
            st.button("B_07")
            ChangeButtonColour("B_07","white","red")
        else:
            if st.button("B_07", key="A_14"):
                session_state.a = "B_07"
                modal.open()
                
                

    with col4:
        if "C_01" in occuped_chairs:
            st.button("C_01")
            ChangeButtonColour("C_01","white","red")
        else:
            if st.button("C_01", key="A_15"):
                session_state.a = "C_01"
                modal.open()
                


        if "C_02" in occuped_chairs:
            st.button("C_02")
            ChangeButtonColour("C_02","white","red")
        else:
            if st.button("C_02", key="A_16"):
                session_state.a = "C_02"
                modal.open()
                
                

        if "C_03" in occuped_chairs:
            st.button("C_03")
            ChangeButtonColour("C_03","white","red")
        else:
            if st.button("C_03", key="A_17"):
                session_state.a = "C_03"
                modal.open()
                
                

        if "C_04" in occuped_chairs:
            st.button("C_04")
            ChangeButtonColour("C_04","white","red")
        else:
            if st.button("C_04", key="A_18"):
                session_state.a = "C_04"
                modal.open()
                
                

        if "C_05" in occuped_chairs:
            st.button("C_05")
            ChangeButtonColour("C_05","white","red")
        else:
            if st.button("C_05", key="A_19"):
                session_state.a = "C_05"
                modal.open()
                
                

        if "C_06" in occuped_chairs:
            st.button("C_06")
            ChangeButtonColour("C_06","white","red")
        else:
            if st.button("C_06", key="A_20"):
                session_state.a = "C_06"
                modal.open()
                

        if "C_07" in occuped_chairs:
            st.button("C_07")
            ChangeButtonColour("C_07","white","red")
        else:
            if st.button("C_07", key="A_21"):
                session_state.a = "C_07"
                modal.open()
                
    with col5:
        pass

    with col6:
        if "D_01" in occuped_chairs:
            st.button("D_01")
            ChangeButtonColour("D_01","white","red")
        else:
            if st.button("D_01", key="A_22"):
                session_state.a = "D_01"
                modal.open()
                

        if "D_02" in occuped_chairs:
            st.button("D_02")
            ChangeButtonColour("D_02","white","red")
        else:
            if st.button("D_02", key="A_23"):
                session_state.a = "D_02"
                modal.open()
                
                

        if "D_03" in occuped_chairs:
            st.button("D_03")
            ChangeButtonColour("D_03","white","red")
        else:
            if st.button("D_03", key="A_24"):
                session_state.a = "D_03"
                modal.open()
                
                

        if "D_04" in occuped_chairs:
            st.button("D_04")
            ChangeButtonColour("D_04","white","red")
        else:
            if st.button("D_04", key="A_25"):
                session_state.a = "D_04"
                modal.open()
                
                

        if "D_05" in occuped_chairs:
            st.button("D_05")
            ChangeButtonColour("D_05","white","red")
        else:
            if st.button("D_05", key="A_26"):
                session_state.a = "D_05"
                modal.open()
                
                

        if "D_06" in occuped_chairs:
            st.button("D_06")
            ChangeButtonColour("D_06","white","red")
        else:
            if st.button("D_06", key="A_27"):
                session_state.a = "D_06"
                modal.open()
                
                

        if "D_07" in occuped_chairs:
            st.button("D_07")
            ChangeButtonColour("D_07","white","red")
        else:
            if st.button("D_07", key="A_28"):
                session_state.a = "D_07"
                modal.open()
                

    with col7:
        if "E_01" in occuped_chairs:
            st.button("E_01")
            ChangeButtonColour("E_01","white","red")
        else:
            if st.button("E_01", key="A_29"):
                session_state.a = "E_01"
                modal.open()
                

        if "E_02" in occuped_chairs:
            st.button("E_02")
            ChangeButtonColour("E_02","white","red")
        else:
            if st.button("E_02", key="A_30"):
                session_state.a = "E_02"
                modal.open()
             

        if "E_03" in occuped_chairs:
            st.button("E_03")
            ChangeButtonColour("E_03","white","red")
        else:
            if st.button("E_03", key="A_31"):
                session_state.a = "E_03"
                modal.open()
                

        if "E_04" in occuped_chairs:
            st.button("E_04")
            ChangeButtonColour("E_04","white","red")
        else:
            if st.button("E_04", key="A_32"):
                session_state.a = "E_04"
                modal.open()
                

        if "E_05" in occuped_chairs:
            st.button("E_05")
            ChangeButtonColour("E_05","white","red")
        else:
            if st.button("E_05", key="A_33"):
                session_state.a = "E_05"
                modal.open()
                

        if "E_06" in occuped_chairs:
            st.button("E_06")
            ChangeButtonColour("E_06","white","red")
        else:
            if st.button("E_06", key="A_34"):
                session_state.a = "E_06"
                modal.open()
                

        if "E_07" in occuped_chairs:
            st.button("E_07")
            ChangeButtonColour("E_07","white","red")
        else:
            if st.button("E_07", key="A_35"):
                session_state.a = "E_07"
                modal.open()
                

    
    with col8:
        if "F_01" in occuped_chairs:
            st.button("F_01")
            ChangeButtonColour("F_01", "white", "red")
        else:
            if st.button("F_01", key="A_36"):
                session_state.a = "F_01"
                modal.open()
                

        if "F_02" in occuped_chairs:
            st.button("F_02")
            ChangeButtonColour("F_02", "white", "red")
        else:
            if st.button("F_02", key="A_37"):
                session_state.a = "F_02"
                modal.open()
                

        if "F_03" in occuped_chairs:
            st.button("F_03")
            ChangeButtonColour("F_03", "white", "red")
        else:
            if st.button("F_03", key="A_38"):
                session_state.a = "F_03"
                modal.open()
                

        if "F_04" in occuped_chairs:
            st.button("F_04")
            ChangeButtonColour("F_04", "white", "red")
        else:
            if st.button("F_04", key="A_39"):
                session_state.a = "F_04"
                modal.open()
    

        if "F_05" in occuped_chairs:
            st.button("F_05")
            ChangeButtonColour("F_05", "white", "red")
        else:
            if st.button("F_05", key="A_40"):
                session_state.a = "F_05"
                modal.open()
                

        if "F_06" in occuped_chairs:
            st.button("F_06")
            ChangeButtonColour("F_06", "white", "red")
        else:
            if st.button("F_06", key="A_41"):
                session_state.a = "F_06"
                modal.open()
                

        if "F_07" in occuped_chairs:
            st.button("F_07")
            ChangeButtonColour("F_07", "white", "red")
        else:
            if st.button("F_07", key="A_42"):
                session_state.a = "F_07"
                modal.open()


#Contingut dels modals
    if modal.is_open():
        with modal.container():
            st.write("Confirma el teu seient")
            st.write("*Els diners no seràn retornats en cap cas.*")
            chair = st.text_input("Confirma el seient seleccionat")
            if st.checkbox("Comprar"):
                if session_state.a==chair:
                    with st.spinner("Processant la teva compra..."):
                        row_index = oppenheimer_worksheet[oppenheimer_worksheet["CHAIRS"]==chair].index[0]
                        oppenheimer_worksheet.at[row_index, "AVAILABILITY"]="O"
                        conn.update(worksheet="openheimer",data=oppenheimer_worksheet)
                    st.cache_data.clear()
                    st.success("Compra feta ✅")
                    time.sleep(2)
                    modal.close()
                    st.rerun()
                else:
                    with st.spinner("Processant la teva compra..."):
                        time.sleep(5)
                    st.error("Seient incorrecte ❌")
                    time.sleep(2)
                    modal.close()
                    st.rerun()
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        pass
    
    with col2:
        pass

    with col3:
        pass

    with col4:
        pass

    with col5:
        pass

    with col6:
        pass

    with col7:
        pass

    with col8:
        if st.button("Pàgina d'inici"):
            session_state.counter=1
            st.rerun()
            

def barbie(session_state):

    set_background("../assets/Fondo homepage.jpg")
    modal = Modal(
    "Confirma el teu seient", 
    key="modals",)

    #Crear connexió base de dades
    conn = st.connection("gsheets", GSheetsConnection)
    barbie_worksheet = conn.read(worksheet="barbie", usecols=["CHAIRS","AVAILABILITY"])
    barbie_worksheet.dropna(inplace=True)

    chairs_opp=[]
    availability_opp=[]
    #Llegir base de dades
    for index, row in barbie_worksheet.iterrows():
        chairs_opp.append(row["CHAIRS"])
        availability_opp.append(row["AVAILABILITY"])
    #Llegir seient ocupats
    occuped_chairs=[]
    for i in range(len(availability_opp)):
        if availability_opp[i]=="O":
            occuped_chairs.append(chairs_opp[i])

    st.image("../assets/barbielove.png", width=300)
    st.write("*Hora de la sessió: 20:30h. Preu de l'entrada: 9€*")
    st.write("Escull el teu seient.")
    # Custom HTML/CSS for the banner
    custom_html = """
    <div class="banner">
        <img src="https://raw.githubusercontent.com/alexrosado5/TR_cine/main/assets/Pantalla%20cine.png" alt="Banner Image">
    </div>
    <style>
        .banner {
            width: 110%;
            height: 200px;
            overflow: hidden;
        }
        .banner img {
            width: 100%;
            object-fit: cover;
        }
    </style>
    """
    # Display the custom HTML
    st.components.v1.html(custom_html)
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    #Crear els seients
    with col1:
        pass

    with col2:
        if "A_01" in occuped_chairs:
            st.button("A_01")
            ChangeButtonColour("A_01","white","red")
        else:
            if st.button("A_01", key="B_01"):
                session_state.b = "A_01"
                modal.open()
                
   
        
        if "A_02" in occuped_chairs:
            st.button("A_02")
            ChangeButtonColour("A_02","white","red")
            
        else:
            if st.button("A_02", key="B_02"):
                session_state.b = "A_02"
                modal.open()
                
               
            
        if "A_03" in occuped_chairs:
            st.button("A_03")
            ChangeButtonColour("A_03","white","red")
        else:
            if st.button("A_03", key="B_03"):
                session_state.b = "A_03"
                modal.open()
                

                

        if "A_04" in occuped_chairs:
            st.button("A_04")
            ChangeButtonColour("A_04","white","red")
        else:
            if st.button("A_04", key="B_04"):
                session_state.b = "A_04"
                modal.open()
                

        if "A_05" in occuped_chairs:
            st.button("A_05")
            ChangeButtonColour("A_05","white","red")
        else:
            if st.button("A_05", key="B_05"):
                session_state.b = "A_05"
                modal.open()
                

        if "A_06" in occuped_chairs:
            st.button("A_06")
            ChangeButtonColour("A_06","white","red")
        else:
            if st.button("A_06", key="B_06"):
                session_state.b = "A_06"
                modal.open()
                

        if "A_07" in occuped_chairs:
            st.button("A_07")
            ChangeButtonColour("A_07","white","red")
        else:
            if st.button("A_07", key="B_07"):
                session_state.b = "A_07"
                modal.open()
                

    with col3:
        if "B_01" in occuped_chairs:
            st.button("B_01")
            ChangeButtonColour("B_01","white","red")
        else:
            if st.button("B_01", key="B_08"):
                session_state.b = "B_01"
                modal.open()
                
                
        
        if "B_02" in occuped_chairs:
            st.button("B_02")
            ChangeButtonColour("B_02","white","red")
        else:
            if st.button("B_02", key="B_09"):
                session_state.b = "B_02"
                modal.open()
                
                
        
        if "B_03" in occuped_chairs:
            st.button("B_03")
            ChangeButtonColour("B_03","white","red")
        else:
            if st.button("B_03", key="B_10"):
                session_state.b = "B_03"
                modal.open()
                
                

        if "B_04" in occuped_chairs:
            st.button("B_04")
            ChangeButtonColour("B_04","white","red")
        else:
            if st.button("B_04", key="B_11"):
                session_state.b = "B_04"
                modal.open()
                
                

        if "B_05" in occuped_chairs:
            st.button("B_05")
            ChangeButtonColour("B_05","white","red")
        else:
            if st.button("B_05", key="B_12"):
                session_state.b = "B_05"
                modal.open()
                
                

        if "B_06" in occuped_chairs:
            st.button("B_06")
            ChangeButtonColour("B_06","white","red")
        else:
            if st.button("B_06", key="B_13"):
                session_state.b = "B_06"
                modal.open()
                
                

        if "B_07" in occuped_chairs:
            st.button("B_07")
            ChangeButtonColour("B_07","white","red")
        else:
            if st.button("B_07", key="B_14"):
                session_state.b = "B_07"
                modal.open()
                
                

    with col4:
        if "C_01" in occuped_chairs:
            st.button("C_01")
            ChangeButtonColour("C_01","white","red")
        else:
            if st.button("C_01", key="B_15"):
                session_state.b = "C_01"
                modal.open()
                


        if "C_02" in occuped_chairs:
            st.button("C_02")
            ChangeButtonColour("C_02","white","red")
        else:
            if st.button("C_02", key="B_16"):
                session_state.b = "C_02"
                modal.open()
                
                

        if "C_03" in occuped_chairs:
            st.button("C_03")
            ChangeButtonColour("C_03","white","red")
        else:
            if st.button("C_03", key="B_17"):
                session_state.b = "C_03"
                modal.open()
                
                

        if "C_04" in occuped_chairs:
            st.button("C_04")
            ChangeButtonColour("C_04","white","red")
        else:
            if st.button("C_04", key="B_18"):
                session_state.b = "C_04"
                modal.open()
                
                

        if "C_05" in occuped_chairs:
            st.button("C_05")
            ChangeButtonColour("C_05","white","red")
        else:
            if st.button("C_05", key="B_19"):
                session_state.b = "C_05"
                modal.open()
                
                

        if "C_06" in occuped_chairs:
            st.button("C_06")
            ChangeButtonColour("C_06","white","red")
        else:
            if st.button("C_06", key="B_20"):
                session_state.b = "C_06"
                modal.open()
                

        if "C_07" in occuped_chairs:
            st.button("C_07")
            ChangeButtonColour("C_07","white","red")
        else:
            if st.button("C_07", key="B_21"):
                session_state.b = "C_07"
                modal.open()
                
    with col5:
        pass

    with col6:
        if "D_01" in occuped_chairs:
            st.button("D_01")
            ChangeButtonColour("D_01","white","red")
        else:
            if st.button("D_01", key="B_22"):
                session_state.b = "D_01"
                modal.open()
                

        if "D_02" in occuped_chairs:
            st.button("D_02")
            ChangeButtonColour("D_02","white","red")
        else:
            if st.button("D_02", key="B_23"):
                session_state.b = "D_02"
                modal.open()
                
                

        if "D_03" in occuped_chairs:
            st.button("D_03")
            ChangeButtonColour("D_03","white","red")
        else:
            if st.button("D_03", key="B_24"):
                session_state.b = "D_03"
                modal.open()
                
                

        if "D_04" in occuped_chairs:
            st.button("D_04")
            ChangeButtonColour("D_04","white","red")
        else:
            if st.button("D_04", key="B_25"):
                session_state.b = "D_04"
                modal.open()
                
                

        if "D_05" in occuped_chairs:
            st.button("D_05")
            ChangeButtonColour("D_05","white","red")
        else:
            if st.button("D_05", key="B_26"):
                session_state.b = "D_05"
                modal.open()
                
                

        if "D_06" in occuped_chairs:
            st.button("D_06")
            ChangeButtonColour("D_06","white","red")
        else:
            if st.button("D_06", key="B_27"):
                session_state.b = "D_06"
                modal.open()
                
                

        if "D_07" in occuped_chairs:
            st.button("D_07")
            ChangeButtonColour("D_07","white","red")
        else:
            if st.button("D_07", key="B_28"):
                session_state.b = "D_07"
                modal.open()
                

    with col7:
        if "E_01" in occuped_chairs:
            st.button("E_01")
            ChangeButtonColour("E_01","white","red")
        else:
            if st.button("E_01", key="B_29"):
                session_state.b = "E_01"
                modal.open()
                

        if "E_02" in occuped_chairs:
            st.button("E_02")
            ChangeButtonColour("E_02","white","red")
        else:
            if st.button("E_02", key="B_30"):
                session_state.b = "E_02"
                modal.open()
             

        if "E_03" in occuped_chairs:
            st.button("E_03")
            ChangeButtonColour("E_03","white","red")
        else:
            if st.button("E_03", key="B_31"):
                session_state.b = "E_03"
                modal.open()
                

        if "E_04" in occuped_chairs:
            st.button("E_04")
            ChangeButtonColour("E_04","white","red")
        else:
            if st.button("E_04", key="B_32"):
                session_state.b = "E_04"
                modal.open()
                

        if "E_05" in occuped_chairs:
            st.button("E_05")
            ChangeButtonColour("E_05","white","red")
        else:
            if st.button("E_05", key="B_33"):
                session_state.b = "E_05"
                modal.open()
                

        if "E_06" in occuped_chairs:
            st.button("E_06")
            ChangeButtonColour("E_06","white","red")
        else:
            if st.button("E_06", key="B_34"):
                session_state.b = "E_06"
                modal.open()
                

        if "E_07" in occuped_chairs:
            st.button("E_07")
            ChangeButtonColour("E_07","white","red")
        else:
            if st.button("E_07", key="B_35"):
                session_state.b = "E_07"
                modal.open()
                

    
    with col8:
        if "F_01" in occuped_chairs:
            st.button("F_01")
            ChangeButtonColour("F_01", "white", "red")
        else:
            if st.button("F_01", key="B_36"):
                session_state.b = "F_01"
                modal.open()
                

        if "F_02" in occuped_chairs:
            st.button("F_02")
            ChangeButtonColour("F_02", "white", "red")
        else:
            if st.button("F_02", key="B_37"):
                session_state.b = "F_02"
                modal.open()
                

        if "F_03" in occuped_chairs:
            st.button("F_03")
            ChangeButtonColour("F_03", "white", "red")
        else:
            if st.button("F_03", key="B_38"):
                session_state.b = "F_03"
                modal.open()
                

        if "F_04" in occuped_chairs:
            st.button("F_04")
            ChangeButtonColour("F_04", "white", "red")
        else:
            if st.button("F_04", key="B_39"):
                session_state.b = "F_04"
                modal.open()
    

        if "F_05" in occuped_chairs:
            st.button("F_05")
            ChangeButtonColour("F_05", "white", "red")
        else:
            if st.button("F_05", key="B_40"):
                session_state.b = "F_05"
                modal.open()
                

        if "F_06" in occuped_chairs:
            st.button("F_06")
            ChangeButtonColour("F_06", "white", "red")
        else:
            if st.button("F_06", key="B_41"):
                session_state.b = "F_06"
                modal.open()
                

        if "F_07" in occuped_chairs:
            st.button("F_07")
            ChangeButtonColour("F_07", "white", "red")
        else:
            if st.button("F_07", key="B_42"):
                session_state.b = "F_07"
                modal.open()
        

    #Contingut dels modals
    if modal.is_open():
        with modal.container():
            st.write("Confirma el teu seient")
            st.write("*Els diners no seràn retornats en cap cas.*")
            chair = st.text_input("Confirma el seient seleccionat")
            if st.checkbox("Comprar"):
                if session_state.b==chair:
                    with st.spinner("Processant la teva compra..."):
                        row_index = barbie_worksheet[barbie_worksheet["CHAIRS"]==chair].index[0]
                        barbie_worksheet.at[row_index, "AVAILABILITY"]="O"
                        conn.update(worksheet="barbie",data=barbie_worksheet)
                    st.cache_data.clear()
                    st.success("Compra feta ✅")
                    time.sleep(2)
                    modal.close()
                    st.rerun()
                else:
                    with st.spinner("Processant la teva compra..."):
                        time.sleep(5)
                    st.error("Seient incorrecte ❌")
                    time.sleep(2)
                    modal.close()
                    st.rerun()
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        pass
    
    with col2:
        pass

    with col3:
        pass

    with col4:
        pass

    with col5:
        pass

    with col6:
        pass

    with col7:
        pass

    with col8:
        if st.button("Pàgina d'inici"):
            session_state.counter=1
            st.rerun()

    
def nieve(session_state):
    set_background("../assets/Fondo homepage.jpg")
    modal = Modal(
    "Confirma el teu seient", 
    key="modals",)

    #Crear connexió base de dades
    conn = st.connection("gsheets", GSheetsConnection)
    nieves_worksheet = conn.read(worksheet="nieves", usecols=["CHAIRS","AVAILABILITY"])
    nieves_worksheet.dropna(inplace=True)

    chairs_opp=[]
    availability_opp=[]
    #Llegir base de dades
    for index, row in nieves_worksheet.iterrows():
        chairs_opp.append(row["CHAIRS"])
        availability_opp.append(row["AVAILABILITY"])
    #Llegir seient ocupats
    occuped_chairs=[]
    for i in range(len(availability_opp)):
        if availability_opp[i]=="O":
            occuped_chairs.append(chairs_opp[i])
    
    st.image("../assets/La Sociedad de la nieve.png",width=1000)
    st.write("*Hora de la sessió: 22:30h. Preu de l'entrada: 9€*")
    st.write("Escull el teu seient.")

    # Custom HTML/CSS for the banner
    custom_html = """
    <div class="banner">
        <img src="https://raw.githubusercontent.com/alexrosado5/TR_cine/main/assets/Pantalla%20cine.png" alt="Banner Image">
    </div>
    <style>
        .banner {
            width: 110%;
            height: 200px;
            overflow: hidden;
        }
        .banner img {
            width: 100%;
            object-fit: cover;
        }
    </style>
    """
    # Display the custom HTML
    st.components.v1.html(custom_html)
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    #Crear els seients
    with col1:
        pass

    with col2:
        if "A_01" in occuped_chairs:
            st.button("A_01")
            ChangeButtonColour("A_01","white","red")
        else:
            if st.button("A_01", key="C_01"):
                session_state.c = "A_01"
                modal.open()
                
   
        
        if "A_02" in occuped_chairs:
            st.button("A_02")
            ChangeButtonColour("A_02","white","red")
            
        else:
            if st.button("A_02", key="C_02"):
                session_state.c = "A_02"
                modal.open()
                
               
            
        if "A_03" in occuped_chairs:
            st.button("A_03")
            ChangeButtonColour("A_03","white","red")
        else:
            if st.button("A_03", key="C_03"):
                session_state.c = "A_03"
                modal.open()
                

                

        if "A_04" in occuped_chairs:
            st.button("A_04")
            ChangeButtonColour("A_04","white","red")
        else:
            if st.button("A_04", key="C_04"):
                session_state.c = "A_04"
                modal.open()
                

        if "A_05" in occuped_chairs:
            st.button("A_05")
            ChangeButtonColour("A_05","white","red")
        else:
            if st.button("A_05", key="C_05"):
                session_state.c = "A_05"
                modal.open()
                

        if "A_06" in occuped_chairs:
            st.button("A_06")
            ChangeButtonColour("A_06","white","red")
        else:
            if st.button("A_06", key="C_06"):
                session_state.c = "A_06"
                modal.open()
                

        if "A_07" in occuped_chairs:
            st.button("A_07")
            ChangeButtonColour("A_07","white","red")
        else:
            if st.button("A_07", key="C_07"):
                session_state.c = "A_07"
                modal.open()
                

    with col3:
        if "B_01" in occuped_chairs:
            st.button("B_01")
            ChangeButtonColour("B_01","white","red")
        else:
            if st.button("B_01", key="C_08"):
                session_state.c = "B_01"
                modal.open()
                
                
        
        if "B_02" in occuped_chairs:
            st.button("B_02")
            ChangeButtonColour("B_02","white","red")
        else:
            if st.button("B_02", key="C_09"):
                session_state.c = "B_02"
                modal.open()
                
                
        
        if "B_03" in occuped_chairs:
            st.button("B_03")
            ChangeButtonColour("B_03","white","red")
        else:
            if st.button("B_03", key="C_10"):
                session_state.c = "B_03"
                modal.open()
                
                

        if "B_04" in occuped_chairs:
            st.button("B_04")
            ChangeButtonColour("B_04","white","red")
        else:
            if st.button("B_04", key="C_11"):
                session_state.c = "B_04"
                modal.open()
                
                

        if "B_05" in occuped_chairs:
            st.button("B_05")
            ChangeButtonColour("B_05","white","red")
        else:
            if st.button("B_05", key="C_12"):
                session_state.c = "B_05"
                modal.open()
                
                

        if "B_06" in occuped_chairs:
            st.button("B_06")
            ChangeButtonColour("B_06","white","red")
        else:
            if st.button("B_06", key="C_13"):
                session_state.c = "B_06"
                modal.open()
                
                

        if "B_07" in occuped_chairs:
            st.button("B_07")
            ChangeButtonColour("B_07","white","red")
        else:
            if st.button("B_07", key="C_14"):
                session_state.c = "B_07"
                modal.open()
                
                

    with col4:
        if "C_01" in occuped_chairs:
            st.button("C_01")
            ChangeButtonColour("C_01","white","red")
        else:
            if st.button("C_01", key="C_15"):
                session_state.c = "C_01"
                modal.open()
                


        if "C_02" in occuped_chairs:
            st.button("C_02")
            ChangeButtonColour("C_02","white","red")
        else:
            if st.button("C_02", key="C_16"):
                session_state.c = "C_02"
                modal.open()
                
                

        if "C_03" in occuped_chairs:
            st.button("C_03")
            ChangeButtonColour("C_03","white","red")
        else:
            if st.button("C_03", key="C_17"):
                session_state.c = "C_03"
                modal.open()
                
                

        if "C_04" in occuped_chairs:
            st.button("C_04")
            ChangeButtonColour("C_04","white","red")
        else:
            if st.button("C_04", key="C_18"):
                session_state.c = "C_04"
                modal.open()
                
                

        if "C_05" in occuped_chairs:
            st.button("C_05")
            ChangeButtonColour("C_05","white","red")
        else:
            if st.button("C_05", key="C_19"):
                session_state.c = "C_05"
                modal.open()
                
                

        if "C_06" in occuped_chairs:
            st.button("C_06")
            ChangeButtonColour("C_06","white","red")
        else:
            if st.button("C_06", key="C_20"):
                session_state.c = "C_06"
                modal.open()
                

        if "C_07" in occuped_chairs:
            st.button("C_07")
            ChangeButtonColour("C_07","white","red")
        else:
            if st.button("C_07", key="C_21"):
                session_state.c = "C_07"
                modal.open()
                
    with col5:
        pass

    with col6:
        if "D_01" in occuped_chairs:
            st.button("D_01")
            ChangeButtonColour("D_01","white","red")
        else:
            if st.button("D_01", key="C_22"):
                session_state.c = "D_01"
                modal.open()
                

        if "D_02" in occuped_chairs:
            st.button("D_02")
            ChangeButtonColour("D_02","white","red")
        else:
            if st.button("D_02", key="C_23"):
                session_state.c = "D_02"
                modal.open()
                
                

        if "D_03" in occuped_chairs:
            st.button("D_03")
            ChangeButtonColour("D_03","white","red")
        else:
            if st.button("D_03", key="C_24"):
                session_state.c = "D_03"
                modal.open()
                
                

        if "D_04" in occuped_chairs:
            st.button("D_04")
            ChangeButtonColour("D_04","white","red")
        else:
            if st.button("D_04", key="C_25"):
                session_state.c = "D_04"
                modal.open()
                
                

        if "D_05" in occuped_chairs:
            st.button("D_05")
            ChangeButtonColour("D_05","white","red")
        else:
            if st.button("D_05", key="C_26"):
                session_state.c = "D_05"
                modal.open()
                
                

        if "D_06" in occuped_chairs:
            st.button("D_06")
            ChangeButtonColour("D_06","white","red")
        else:
            if st.button("D_06", key="C_27"):
                session_state.c = "D_06"
                modal.open()
                
                

        if "D_07" in occuped_chairs:
            st.button("D_07")
            ChangeButtonColour("D_07","white","red")
        else:
            if st.button("D_07", key="C_28"):
                session_state.c = "D_07"
                modal.open()
                

    with col7:
        if "E_01" in occuped_chairs:
            st.button("E_01")
            ChangeButtonColour("E_01","white","red")
        else:
            if st.button("E_01", key="C_29"):
                session_state.c = "E_01"
                modal.open()
                

        if "E_02" in occuped_chairs:
            st.button("E_02")
            ChangeButtonColour("E_02","white","red")
        else:
            if st.button("E_02", key="C_30"):
                session_state.c = "E_02"
                modal.open()
             

        if "E_03" in occuped_chairs:
            st.button("E_03")
            ChangeButtonColour("E_03","white","red")
        else:
            if st.button("E_03", key="C_31"):
                session_state.c = "E_03"
                modal.open()
                

        if "E_04" in occuped_chairs:
            st.button("E_04")
            ChangeButtonColour("E_04","white","red")
        else:
            if st.button("E_04", key="C_32"):
                session_state.c = "E_04"
                modal.open()
                

        if "E_05" in occuped_chairs:
            st.button("E_05")
            ChangeButtonColour("E_05","white","red")
        else:
            if st.button("E_05", key="C_33"):
                session_state.c = "E_05"
                modal.open()
                

        if "E_06" in occuped_chairs:
            st.button("E_06")
            ChangeButtonColour("E_06","white","red")
        else:
            if st.button("E_06", key="C_34"):
                session_state.c = "E_06"
                modal.open()
                

        if "E_07" in occuped_chairs:
            st.button("E_07")
            ChangeButtonColour("E_07","white","red")
        else:
            if st.button("E_07", key="C_35"):
                session_state.c = "E_07"
                modal.open()
                

    
    with col8:
        if "F_01" in occuped_chairs:
            st.button("F_01")
            ChangeButtonColour("F_01", "white", "red")
        else:
            if st.button("F_01", key="C_36"):
                session_state.c = "F_01"
                modal.open()
                

        if "F_02" in occuped_chairs:
            st.button("F_02")
            ChangeButtonColour("F_02", "white", "red")
        else:
            if st.button("F_02", key="C_37"):
                session_state.c = "F_02"
                modal.open()
                

        if "F_03" in occuped_chairs:
            st.button("F_03")
            ChangeButtonColour("F_03", "white", "red")
        else:
            if st.button("F_03", key="C_38"):
                session_state.c = "F_03"
                modal.open()
                

        if "F_04" in occuped_chairs:
            st.button("F_04")
            ChangeButtonColour("F_04", "white", "red")
        else:
            if st.button("F_04", key="C_39"):
                session_state.c = "F_04"
                modal.open()
    

        if "F_05" in occuped_chairs:
            st.button("F_05")
            ChangeButtonColour("F_05", "white", "red")
        else:
            if st.button("F_05", key="C_40"):
                session_state.c = "F_05"
                modal.open()
                

        if "F_06" in occuped_chairs:
            st.button("F_06")
            ChangeButtonColour("F_06", "white", "red")
        else:
            if st.button("F_06", key="C_41"):
                session_state.c = "F_06"
                modal.open()
                

        if "F_07" in occuped_chairs:
            st.button("F_07")
            ChangeButtonColour("F_07", "white", "red")
        else:
            if st.button("F_07", key="C_42"):
                session_state.c = "F_07"
                modal.open()
        

    #Contingut dels modals
    if modal.is_open():
        with modal.container():
            st.write("Confirma el teu seient")
            st.write("*Els diners no seràn retornats en cap cas.*")
            chair = st.text_input("Confirma el seient seleccionat")
            if st.checkbox("Comprar"):
                if session_state.c==chair:
                    with st.spinner("Processant la teva compra..."):
                        row_index = nieves_worksheet[nieves_worksheet["CHAIRS"]==chair].index[0]
                        nieves_worksheet.at[row_index, "AVAILABILITY"]="O"
                        conn.update(worksheet="nieves",data=nieves_worksheet)
                    st.cache_data.clear()
                    st.success("Compra feta ✅")
                    time.sleep(2)
                    modal.close()
                    st.rerun()
                else:
                    with st.spinner("Processant la teva compra..."):
                        time.sleep(5)
                    st.error("Seient incorrecte ❌")
                    time.sleep(2)
                    modal.close()
                    st.rerun()
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        pass
    
    with col2:
        pass

    with col3:
        pass

    with col4:
        pass

    with col5:
        pass

    with col6:
        pass

    with col7:
        pass

    with col8:
        if st.button("Pàgina d'inici"):
            session_state.counter=1
            st.rerun()
                

#Funció principal de la pàgina
def main():
    
    session_state = st.session_state
    if "counter" not in session_state:
        session_state.counter = 1
    if "a" not in session_state:
        session_state.a = 0
    if "MAIN" not in session_state:
        session_state.MAIN = 0
    if "b" not in session_state:
        session_state.b = 0
    if "c" not in session_state:
        session_state.c = 0

    paginas = ["Inici", "Oppenheimer", "Barbie", "Nieve"]
    st.sidebar.title("Navega pel cinema")
    pagina_seleccionada = st.sidebar.radio("Selecciona la pàgina", paginas, index=session_state.counter -1)
    if pagina_seleccionada =="Inici":
        homepage(session_state)
    elif pagina_seleccionada == "Oppenheimer":
        openheimer(session_state)
    elif pagina_seleccionada == "Nieve":
        nieve(session_state)
    elif pagina_seleccionada == "Barbie":
        barbie(session_state)
    
if __name__=="__main__":

    #Sheet connection
    conn = st.connection("gsheets", type=GSheetsConnection)
    users_worksheet = conn.read(worksheet="users", usecols=["USER", "PASSWORD"])

    #Files amb valors restants
    users_worksheet.dropna(inplace=True)
    # Obtenir user/password/data

    users=[]
    passwords=[]
 


    for index, row in users_worksheet.iterrows():
        users.append(row["USER"])
        passwords.append(row['PASSWORD'])   
    

    #Obtenir els credentials 

    names=[]
    for user in users:
        names.append(user)
    credentials = {"usernames":{}}
    for index in range(len(names)):
        credentials["usernames"][names[index]] = {"name": names[index], "password":passwords[index]}
    
    #Autent. de l'usuari
    authenticator = stauth.Authenticate(credentials, "Streamlit", "main")
    name, authentication_status, username = authenticator.login("main")

    #Si Autent. Run main
    if authentication_status:
        authenticator.logout(':red[Log out]', 'sidebar')
        main()
    elif authentication_status == False:
        st.error("Usuari/Contrasenya incorrectes. Torna a provar.")
    elif authentication_status == None:
        st.warning("Inicia sessió")





