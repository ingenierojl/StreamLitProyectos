import streamlit as st
import streamlit_option_menu
print(streamlit_option_menu.__file__)
from streamlit_option_menu import option_menu

# Definir los botones y sus iconos
button_labels = ["Home", "Experience", "Education", "Projects", "Skills", "Languages"]
button_icons = ['house', 'briefcase', 'mortarboard', 'clipboard-data', 'gear', 'translate']

# Obtener el índice del botón seleccionado
selected_index = button_labels.index(option_menu(None, button_labels, icons=button_icons, default_index=0, orientation="horizontal"))

# Si el botón seleccionado es "Skills", establecer el ancho a 100%
if button_labels[selected_index] == "Skills":
    st.write('<style>div[data-testid="stHorizontalBlock"] > div:nth-child(5) {width: 100%;}</style>', unsafe_allow_html=True)

# Verificar el botón seleccionado y mostrar el contenido correspondiente
if button_labels[selected_index] == "Home":
    st.header("Jorge L. Rojas")
    st.subheader("Electrical Engineer and Software Developer.")
   # Agregar la imagen y especificar el ancho
    profile_pic = st.image("pic/pic-.png", width=250) 

    # Centrar los elementos usando columns y expandir a pantalla completa
    col1, col2, col3 = st.columns([1,3,1])

    with col1:
        st.write("")

    with col2:
        st.write("Carrera 57 # 80 – 85 Apt 524 Sta. María del Campo Unit Itagüí-Antioquia.")
        st.write("+57 3008079369")
        st.write("ingenierorojas87@gmail.com")

    with col3:
        st.write("")
    
        st.write("") # Espacio adicional abajo
  
elif button_labels[selected_index] == "Experience":
    st.header("Experience")
    st.write("""
    **Programming Teacher** - SENA CTM, Medellín (Jan 2017 - Dec 2018)
  
    - Teaching various programming languages to students.
  
    **ICT Administrator** - SENA SALUD, Medellín (Jul 2011 - Dec 2016) 
  
    - Management of technological elements necessary for teaching.
    """)
  
elif button_labels[selected_index] == "Education":
    st.header("Education")
    st.write("- Electrical Engineering - UDEC, Cundinamarca (Jul 2011)")
  
elif button_labels[selected_index] == "Projects":
    st.header("Projects")

    st.write("""
    **MOBILE DEVELOPMENT**
    - Developed mobile applications using Kotlin and Java.  
    - Gained experience in UI design and implementation.

    **RASPBERRY PI PROJECTS**
    - Created projects involving electronic signal processing and actuators controlled by Raspberry Pi devices.
    - Focused on integrating hardware and software solutions.  

    **VOICE-CONTROLLED HOSPITAL BED**  
    - Frontend and backend control application for voice-operated hospital bed.
    - Android mobile app using voice recognition API in Kotlin.
    - Bluetooth module on the bed for serial communication with Arduino.

    **TELE-EDUCATION SERVER**
    - Linux server for audio, video, and medical signal transmission.  
    - Developed in Python, C++, HTML, and CSS. 
    - Focused on tele-education and telemedicine.

    **TECHNOLOGY CONSULTING** 
    - Provided guidance to students on developing projects involving fingerprint scanning, QR codes, web development (HTML/CSS/JS), and electronic prototyping using languages like Python, PHP, C/C++.

    **FULL STACK DEVELOPMENT**
    - Developed full stack solutions integrating frontend interfaces in HTML/CSS/JS with Python backends connected to MySQL databases.
    - Experience building scalable and dynamic web applications and APIs.
    """)
  
elif button_labels[selected_index] == "Skills":
    st.header("Technical Skills")
    st.write("- Python, FastAPI, SQL Databases, REST APIs, JWT Authentication, OpenCV")  
    st.write("- HTML, CSS, JavaScript, Bootstrap")
    st.write("- Asynchronous Programming with Generators")
    st.write("- Code Documentation and Comments")
    st.write("- Secure Application Deployment")

    st.write("- Python, Flask, MySQL, REST, OpenCV")
    st.write("- HTML, CSS, JavaScript, Bootstrap")
    st.write("- PHP, C/C++, Java")
    st.write("- Assembly Language for Motorola PIC")
  
elif button_labels[selected_index] == "Languages":
    st.header("Languages")
    st.write("- Spanish: Native")
    st.write("- English: Intermediate")