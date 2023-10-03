import streamlit as st
from streamlit_option_menu import option_menu

options = ["Home", "Experience", "Education", "Projects", "Languages", "Skills"]  
icons = ['house', 'briefcase', 'mortarboard', 'clipboard-data', 'translate', "gear"]

selected = option_menu(None, options, icons=icons,  
                      default_index=0,
                      orientation="horizontal",
                      element_id="skills-icon")

if selected == "Home":

    st.header("Jorge L. Rojas")
    st.subheader("Electrical Engineer and Software Developer.")
    st.write("Carrera 57 # 80 – 85 Apt 524 Sta. María del Campo Unit Itagüí-Antioquia.")
    st.write("+57 3008079369") 
    st.write("ingenierorojas87@gmail.com")

elif selected == "Experience":

    st.header("Experience")
    st.write("""
    **Programming Teacher** - SENA CTM, Medellín (Jan 2017 - Dec 2018)
    - Teaching various programming languages to students.  
    **ICT Administrator** - SENA SALUD, Medellín (Jul 2011 - Dec 2016) 
    - Management of technological elements necessary for teaching.
    """)

elif selected == "Education":

    st.header("Education")
    st.write("- Electrical Engineering - UDEC, Cundinamarca (Jul 2011)")
    
elif selected == "Projects":

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

elif selected == "Skills":
    
    st.header("Technical Skills")
    
    st.markdown('<i class="material-icons">gear</i>', unsafe_allow_html=True) 
    
    st.write("- Python, FastAPI, SQL Databases, REST APIs, JWT Authentication, OpenCV")
    st.write("- HTML, CSS, JavaScript, Bootstrap")
    st.write("- Asynchronous Programming with Generators")
    st.write("- Code Documentation and Comments")
    st.write("- Secure Application Deployment")
    st.write("- Python, Flask, MySQL, REST, OpenCV")
    st.write("- HTML, CSS, JavaScript, Bootstrap")
    st.write("- PHP, C/C++, Java")
    st.write("- Assembly Language for Motorola PIC")
    
elif selected == "Languages":

    st.header("Languages")
    st.write("- Spanish: Native") 
    st.write("- English: Intermediate")
    