import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Definir los botones 
button_labels = ["Home", "Experience", "Education", "Projects", "Skills", "Languages"]
button_icons = ['house', 'briefcase', 'mortarboard', 'clipboard-data', 'gear', 'translate']

# Obtener el índice del botón seleccionado
selected_index = button_labels.index(option_menu(None, button_labels, icons=button_icons, default_index=0, orientation="horizontal"))

# Crear 3 columnas para centrar contenido
col1, col2, col3 = st.columns([1,2,1])

if button_labels[selected_index] == "Home":

  with col1:
    st.write("")

  with col2:
    st.title("Jorge L. Rojas")
    st.subheader("Electronics Engineer and Software Developer")
    profile_pic = st.image("pic/pic-.png", width=250)
    st.write("Carrera 57 # 80 – 85 Apt 524 Sta. María del Campo Unit Itagüí-Antioquia.")
    st.write("+57 3008079369")
    st.write("ingenierorojas87@gmail.com")

    st.write("I am an electronics engineer with a passion for both programming and hardware. I thrive on continuously updating my knowledge and skills to stay at the forefront of technology.")
    st.write("I am highly proactive and enjoy tackling challenges head-on. When faced with obstacles, I take them personally until I find a solution, just like debugging in programming.")
    st.write("In addition to my technical skills, I also have experience as an educator. I have a background in developing projects and providing academic and technical guidance, making me well-rounded in both academic and practical aspects.")

    # Agregar más información si es necesario.

  with col3:
    st.write("")

elif button_labels[selected_index] == "Experience":

  with col1:
    st.write("")

  with col2:
    st.title("Experience")
    st.write("""
     **Programming Teacher (Media Técnica)** - Secretaría de Educación, Medellín (Abr 2018 - Actualidad)
    - Instructing students in grades 10 and 11 in various programming languages.
    - Providing guidance and support for different software development projects.         

    **Programming Teacher** - SENA CTM, Medellín (Jan 2017 - Dec 2018)
     - Teaching various programming languages to students.

    **Administrator TIC** - SENA SALUD, Medellín (Jul 2011 - Dec 2016)  
    - Management of technological elements necessary for teaching.
  
    """)


  with col3:  
    st.write("")

elif button_labels[selected_index] == "Education":
  
  with col1:
    st.write("")

  with col2:  
    st.title("Education")
    st.write("- Electrical Engineering - UDEC, Cundinamarca (Jul 2011)")

  with col3:
    st.write("")
      
elif button_labels[selected_index] == "Projects":

  with col1:
    st.write("")

  with col2:
    st.title("Projects")
    st.write("""
             
    **TECHNOLOGY CONSULTING**  
      - Provided guidance to students on developing projects involving fingerprint scanning, QR codes, web development (HTML/CSS/JS), and electronic prototyping using languages like Python, PHP, C/C++.

    **FULL STACK DEVELOPMENT**
      - Developed full stack solutions integrating frontend interfaces in HTML/CSS/JS with Python backends connected to MySQL databases. 
      - Experience building scalable and dynamic web applications and APIs.

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
    """)

  with col3:
    st.write("")

elif button_labels[selected_index] == "Skills":

  with col1:
    st.write("")

  with col2:
    st.title("Technical Skills")
    st.write("- Python, FastAPI, SQL Databases, REST APIs, JWT Authentication, OpenCV")
    st.write("- HTML, CSS, JavaScript, Bootstrap") 
    st.write("- Python, Flask, MySQL, REST, OpenCV")
    st.write("- HTML, CSS, JavaScript, Bootstrap")
    st.write("- PHP, C/C++, Java")
    st.write("- GIT Versions control")
    st.write("- Code Documentation and Comments")
    st.write("- Secure Application Deployment")

  with col3:
    st.write("")


elif button_labels[selected_index] == "Languages":

  with col1:
    st.write("")

  with col2:
    st.title("Languages")
    st.write("- Spanish: Native")
    st.write("- English: Intermediate")  

  with col3:
    st.write("")