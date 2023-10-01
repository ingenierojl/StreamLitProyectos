import streamlit as st
import streamlit_option_menu
print(streamlit_option_menu.__file__)
from streamlit_option_menu import option_menu


selected = option_menu(None, ["Home", "Experiencia", "Educación", "Proyectos", "Habilidades", "Idiomas"],
    icons=['house', 'briefcase', 'mortarboard', 'clipboard-data', 'gear', 'translate'], 
    default_index=0, orientation="horizontal") 


if selected == "Home":

  st.header("Jorge L. Rojas")

  st.subheader("Ingeniero electrónico y desarrollador de software.")

  st.write("Carrera 57 # 80 – 85 Apto 524 Unidad Sta. María del Campo Itagüí-Antioquia.")
  st.write("+57 3008079369")
  st.write("ingenierorojas87@gmail.com")
  
elif selected == "Experiencia":

  st.header("Experiencia")
  
  st.write("""
  **Profesor de programación** - SENA CTM, Medellín (Ene 2017 - Dic 2018)
  
  - Enseñanza de diferentes lenguajes de programación a estudiantes.
  
  **Administrador de TICs** - SENA SALUD, Medellín (Jul 2011 - Dic 2016) 
  
  - Gestión de elementos tecnológicos necesarios para la enseñanza.
  """)
  
elif selected == "Educación":

  st.header("Educación")

  st.write("- Ingeniería Electrónica - UDEC, Cundinamarca (Jul 2011)")
  
elif selected == "Proyectos":

  st.header("Proyectos")

  st.write("""
  **CAMA TELE-OPERADA POR COMANDOS DE VOZ** 
  
  - Aplicación de control frontend y backend para operar una cama hospitalaria por voz.
  - App móvil Android que usa API de reconocimiento de voz en Kotlin.
  - Módulo Bluetooth en la cama para comunicación serial con Arduino.
  
  **SERVIDOR DE TELE-EDUCACIÓN**
  
  - Servidor en Linux para transmisión de audio, video y señales médicas.
  - Desarrollado en Python, C++, HTML y CSS.
  - Enfocado en tele-educación y telemedicina.
  
  **SISTEMA DE CONTROL DE ACCESO** 
  
  - Prototipo de control de acceso con lectores de huella y tarjetas RFID.
  - Conexión a bases de datos MySQL.
  - Integración con plataforma externa mediante API.
  """)
  
elif selected == "Habilidades":

  st.header("Habilidades Técnicas")

  st.write("- Python, Flask, MySQL, REST, OpenCV")
  st.write("- HTML, CSS, JavaScript, Bootstrap")
  st.write("- PHP, C/C++, Java")
  st.write("- Ensamblador para Motorola PIC")
  
elif selected == "Idiomas":

  st.header("Idiomas")
  
  st.write("- Español: Nativo")
  st.write("- Inglés: Intermedio")