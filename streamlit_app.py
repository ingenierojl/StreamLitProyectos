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
    st.write("Carrera 57 # 80 – 85 Apt 524 Sta. María del Campo Unit Itagüí-Antioquia.")
    st.write("+57 3008079369")
    st.write("ingenierorojas87@gmail.com")
  
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
    **VOICE-CONTROLLED HOSPITAL BED** 
  
    - Frontend and backend control application for voice-operated hospital bed.
    - Android mobile app using voice recognition API in Kotlin.
    - Bluetooth module on the bed for serial communication with Arduino.
  
    **TELE-EDUCATION SERVER**
  
    - Linux server for audio, video, and medical signal transmission.
    - Developed in Python, C++, HTML, and CSS.
    - Focused on tele-education and telemedicine.
  
    **ACCESS CONTROL SYSTEM** 
  
    - Prototype access control with fingerprint readers and RFID cards.
    - Connection to MySQL databases.
    - Integration with external platform through API.
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