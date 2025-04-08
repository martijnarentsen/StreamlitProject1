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
verkopen_per_locatie = df.groupby('Locatie')['Verkoop'].sum()

# Maak een eenvoudige staafgrafiek
st.write("Verkoop per locatie:")
st.bar_chart(verkopen_per_locatie)
