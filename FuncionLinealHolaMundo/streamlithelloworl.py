import streamlit as st
import pandas as pd

st.write(""" # My first app Hello *world* """)
st.write(""" # Mi primera aplicacion hola mundo """)

df = pd.read_csv("Libro2.csv")
st.line_chart(df)
st.write(""" # f(x)=2x """)

