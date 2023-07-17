import streamlit as st
from streamlit_option_menu import option_menu


selected = option_menu(None, 
    options=["Home","Projects", "Contact"],
    menu_icon="cast",
    icons=["house","book","envelope"],
    default_index=0,
    orientation="horizontal")



if selected == "Home":
    st.title(f"tu has seleccionadoo {selected}")
if selected == "Projects":
    st.title(f"tu has seleccionado {selected}")
if selected == "Contact":
    st.title(f"tu has seleccionado {selected}")

