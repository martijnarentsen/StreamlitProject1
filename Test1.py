import streamlit as st
import pandas as pd

# Titel van je app
st.title("Test1.py")

# Laad het databestand
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Laat de data zien in Streamlit
st.write("Hier is je verkoopdata:")
st.dataframe(df)

