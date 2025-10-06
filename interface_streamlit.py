import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('all_jobs.csv')

# ------------------------------
# Titre de l'application
# ------------------------------
st.title("Dashboard Offres d'Emploi Tunisie")
st.markdown("Analyse des offres par domaine, entreprises et localisation")

# ------------------------------
# Nombre d'offres par domaine
# ------------------------------
st.header("Nombre d'offres par domaine")
offres_par_domaine = data['Domaine'].value_counts()

# Matplotlib
fig1, ax1 = plt.subplots()
offres_par_domaine.plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_ylabel("Nombre d'offres")
ax1.set_xlabel("Domaine")
st.pyplot(fig1)

# ------------------------------
# Top 5 des entreprises qui recrutent le plus
# ------------------------------
st.header("Top 5 des entreprises qui recrutent le plus")
top_entreprises = data['Entreprise'].value_counts().head(5)

# Matplotlib
fig2, ax2 = plt.subplots()
top_entreprises.plot(kind='barh', color='mediumseagreen', ax=ax2)
ax2.set_xlabel("Nombre d'offres")
ax2.set_ylabel("Entreprise")
ax2.invert_yaxis()
st.pyplot(fig2)

# ------------------------------
# Offres par domaine et localisation (heatmap)
# ------------------------------
st.header("Offres par domaine et localisation")
offres_par_domaine_localisation = data.groupby(['Domaine', 'Localisation']).size().unstack(fill_value=0)

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(offres_par_domaine_localisation, annot=True, fmt="d", cmap="Blues", ax=ax3)
ax3.set_xlabel("Localisation")
ax3.set_ylabel("Domaine")
st.pyplot(fig3)
