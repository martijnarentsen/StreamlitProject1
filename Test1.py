import streamlit as st
import pandas as pd

# Titel van de pagina
st.title("Dashboard")

# Laad de data
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Toon de data in de app
st.write("Overzicht van de data:")
st.dataframe(df)

# Groepeer de data per locatie
prijs_per_land = df.groupby('land')['prijs'].sum()

# Maak een eenvoudige staafgrafiek
st.write("prijs per land:")
st.bar_chart(prijs_per_land)

# Maak een eenvoudige lijngrafiek
st.write("prijs per land:")
st.line_chart(prijs_per_land)
