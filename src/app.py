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
    st.title("Benvinguts al cinema de l'Àlex!🍿📽️")
    st.header("Cartellera de la setmana")
    st.write("")
    image_poster = "../assets/Posters.svg"
    st.image(image_poster,width=1300)

    # Fotos peli
    ##setup
    col1, col2, col3= st.columns(3)

    ##Foto 1
    with col1:
        if st.button("Disponibilitat", key="Botó 1")== True:
            session_state.counter = 2
            st.rerun()
       
    ##Foto 2
    with col2:
        if st.button("Disponibilitat", key= "Botó 2") == True:
            session_state.counter = 3
            st.rerun()

    ##Foto 3
    with col3:
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
                modal.open()
   
        
        if "A_02" in occuped_chairs:
            st.button("A_02")
            ChangeButtonColour("A_02","white","red")
            
        else:
            if st.button("A_02", key="A_02"):
                modal.open()
               
            
        if "A_03" in occuped_chairs:
            st.button("A_03")
            ChangeButtonColour("A_03","white","red")
        else:
            if st.button("A_03", key="A_03"):
                modal.open()

                

        if "A_04" in occuped_chairs:
            st.button("A_04")
            ChangeButtonColour("A_04","white","red")
        else:
            if st.button("A_04", key="A_04"):
                modal.open()

        if "A_05" in occuped_chairs:
            st.button("A_05")
            ChangeButtonColour("A_05","white","red")
        else:
            if st.button("A_05", key="A_05"):
                modal.open()

        if "A_06" in occuped_chairs:
            st.button("A_06")
            ChangeButtonColour("A_06","white","red")
        else:
            if st.button("A_06", key="A_06"):
                modal.open()

        if "A_07" in occuped_chairs:
            st.button("A_07")
            ChangeButtonColour("A_07","white","red")
        else:
            if st.button("A_07", key="A_07"):
                modal.open()

    with col3:
        if "B_01" in occuped_chairs:
            st.button("B_01")
            ChangeButtonColour("B_01","white","red")
        else:
            if st.button("B_01", key="B_01"):
                modal.open()
                
        
        if "B_02" in occuped_chairs:
            st.button("B_02")
            ChangeButtonColour("B_02","white","red")
        else:
            if st.button("B_02", key="B_02"):
                modal.open()
                
        
        if "B_03" in occuped_chairs:
            st.button("B_03")
            ChangeButtonColour("B_03","white","red")
        else:
            if st.button("B_03", key="B_03"):
                modal.open()
                

        if "B_04" in occuped_chairs:
            st.button("B_04")
            ChangeButtonColour("B_04","white","red")
        else:
            if st.button("B_04", key="B_04"):
                modal.open()
                

        if "B_05" in occuped_chairs:
            st.button("B_05")
            ChangeButtonColour("B_05","white","red")
        else:
            if st.button("B_05", key="B_05"):
                modal.open()
                

        if "B_06" in occuped_chairs:
            st.button("B_06")
            ChangeButtonColour("B_06","white","red")
        else:
            if st.button("B_06", key="B_06"):
                modal.open()
                

        if "B_07" in occuped_chairs:
            st.button("B_07")
            ChangeButtonColour("B_07","white","red")
        else:
            if st.button("B_07", key="B_07"):
                modal.open()
                

    with col4:
        if "C_01" in occuped_chairs:
            st.button("C_01")
            ChangeButtonColour("C_01","white","red")
        else:
            if st.button("C_01", key="C_01"):
                modal.open()


        if "C_02" in occuped_chairs:
            st.button("C_02")
            ChangeButtonColour("C_02","white","red")
        else:
            if st.button("C_02", key="C_02"):
                modal.open()
                

        if "C_03" in occuped_chairs:
            st.button("C_03")
            ChangeButtonColour("C_03","white","red")
        else:
            if st.button("C_03", key="C_03"):
                modal.open()
                

        if "C_04" in occuped_chairs:
            st.button("C_04")
            ChangeButtonColour("C_04","white","red")
        else:
            if st.button("C_04", key="C_04"):
                modal.open()
                

        if "C_05" in occuped_chairs:
            st.button("C_05")
            ChangeButtonColour("C_05","white","red")
        else:
            if st.button("C_05", key="C_05"):
                modal.open()
                

        if "C_06" in occuped_chairs:
            st.button("C_06")
            ChangeButtonColour("C_06","white","red")
        else:
            if st.button("C_06", key="C_06"):
                modal.open()

        if "C_07" in occuped_chairs:
            st.button("C_07")
            ChangeButtonColour("C_07","white","red")
        else:
            if st.button("C_07", key="C_07"):
                modal.open()
    with col5:
        pass

    with col6:
        if "D_01" in occuped_chairs:
            st.button("D_01")
            ChangeButtonColour("D_01","white","red")
        else:
            if st.button("D_01", key="D_01"):
                modal.open()

        if "D_02" in occuped_chairs:
            st.button("D_02")
            ChangeButtonColour("D_02","white","red")
        else:
            if st.button("D_02", key="D_02"):
                modal.open()
                

        if "D_03" in occuped_chairs:
            st.button("D_03")
            ChangeButtonColour("D_03","white","red")
        else:
            if st.button("D_03", key="D_03"):
                modal.open()
                

        if "D_04" in occuped_chairs:
            st.button("D_04")
            ChangeButtonColour("D_04","white","red")
        else:
            if st.button("D_04", key="D_04"):
                modal.open()
                

        if "D_05" in occuped_chairs:
            st.button("D_05")
            ChangeButtonColour("D_05","white","red")
        else:
            if st.button("D_05", key="D_05"):
                modal.open()
                

        if "D_06" in occuped_chairs:
            st.button("D_06")
            ChangeButtonColour("D_06","white","red")
        else:
            if st.button("D_06", key="D_06"):
                modal.open()
                

        if "D_07" in occuped_chairs:
            st.button("D_07")
            ChangeButtonColour("D_07","white","red")
        else:
            if st.button("D_07", key="D_07"):
                modal.open()

    with col7:
        if "E_01" in occuped_chairs:
            st.button("E_01")
            ChangeButtonColour("E_01","white","red")
        else:
            if st.button("E_01", key="E_01"):
                modal.open()

        if "E_02" in occuped_chairs:
            st.button("E_02")
            ChangeButtonColour("E_02","white","red")
        else:
            if st.button("E_02", key="E_02"):
                modal.open()

        if "E_03" in occuped_chairs:
            st.button("E_03")
            ChangeButtonColour("E_03","white","red")
        else:
            if st.button("E_03", key="E_03"):
                modal.open()

        if "E_04" in occuped_chairs:
            st.button("E_04")
            ChangeButtonColour("E_04","white","red")
        else:
            if st.button("E_04", key="E_04"):
                modal.open()

        if "E_05" in occuped_chairs:
            st.button("E_05")
            ChangeButtonColour("E_05","white","red")
        else:
            if st.button("E_05", key="E_05"):
                modal.open()

        if "E_06" in occuped_chairs:
            st.button("E_06")
            ChangeButtonColour("E_06","white","red")
        else:
            if st.button("E_06", key="E_06"):
                modal.open()

        if "E_07" in occuped_chairs:
            st.button("E_07")
            ChangeButtonColour("E_07","white","red")
        else:
            if st.button("E_07", key="E_07"):
                modal.open()

    
    with col8:
        if "F_01" in occuped_chairs:
            st.button("F_01")
            ChangeButtonColour("F_01", "white", "red")
        else:
            if st.button("F_01", key="F_01"):
                modal.open()

        if "F_02" in occuped_chairs:
            st.button("F_02")
            ChangeButtonColour("F_02", "white", "red")
        else:
            if st.button("F_02", key="F_02"):
                modal.open()

        if "F_03" in occuped_chairs:
            st.button("F_03")
            ChangeButtonColour("F_03", "white", "red")
        else:
            if st.button("F_03", key="F_03"):
                modal.open()

        if "F_04" in occuped_chairs:
            st.button("F_04")
            ChangeButtonColour("F_04", "white", "red")
        else:
            if st.button("F_04", key="F_04"):
                modal.open()

        if "F_05" in occuped_chairs:
            st.button("F_05")
            ChangeButtonColour("F_05", "white", "red")
        else:
            if st.button("F_05", key="F_05"):
                modal.open()

        if "F_06" in occuped_chairs:
            st.button("F_06")
            ChangeButtonColour("F_06", "white", "red")
        else:
            if st.button("F_06", key="F_06"):
                modal.open()

        if "F_07" in occuped_chairs:
            st.button("F_07")
            ChangeButtonColour("F_07", "white", "red")
        else:
            if st.button("F_07", key="F_07"):
                modal.open()


#Contingut dels modals
    if modal.is_open():
        with modal.container():
            st.write("Confirma el teu seient")
            chair = st.text_input("Confirma el teu seient")
            if st.checkbox("Comprar"):
                row_index = oppenheimer_worksheet[oppenheimer_worksheet["CHAIRS"]==chair].index[0]
                oppenheimer_worksheet.at[row_index, "AVAILABILITY"]="O"
                conn.update(worksheet="openheimer",data=oppenheimer_worksheet)
                st.cache_data.clear()
                st.success("Compra feta")
                time.sleep(2)
                modal.close()
                st.rerun()
            

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
                

#Funció principal de la pàgina
def main():
    
    session_state = st.session_state
    if "counter" not in session_state:
        session_state.counter = 1
    if "a" not in session_state:
        session_state.a = 0
    if "MAIN" not in session_state:
        session_state.MAIN = 0

    paginas = ["Inici", "Oppenheimer", "Nieve", "Barbie"]
    st.sidebar.title("Navega pel cinema")
    pagina_seleccionada = st.sidebar.radio("Selecciona la pàgina", paginas, index=session_state.counter -1)
    if pagina_seleccionada =="Inici":
        homepage(session_state)
    elif pagina_seleccionada == "Oppenheimer":
        openheimer(session_state)
    elif pagina_seleccionada == "Nieve":
        st.write("No")
    elif pagina_seleccionada == "Barbie":
        barbie()
    
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
        st.error("Username/password incorrect. Please try again.")
    elif authentication_status == None:
        st.warning("Please login to access the app.")





