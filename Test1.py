import streamlit as st
import pandas as pd

# Titel van je app
st.title("Test1.py")

# Laad het databestand
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Laat de data zien in Streamlit
st.write("Hier is je verkoopdata:")
st.dataframe(df)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Laad de data
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Groepeer per locatie
verkopen_per_locatie = df.groupby('Locatie')['Verkoop'].sum()

# Plot
fig, ax = plt.subplots()
verkopen_per_locatie.plot(kind='bar', ax=ax)
ax.set_title('Verkoop per Locatie')
ax.set_xlabel('Locatie')
ax.set_ylabel('Aantal verkopen')

st.pyplot(fig)

