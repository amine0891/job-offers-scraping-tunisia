import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import seaborn as sns

# Charger tous les fichiers CSV dans un seul dataframe
all_files = glob("*.csv")  # si tes CSV sont dans le même dossier
dfs = []

for file in all_files:
    df = pd.read_csv(file)
    # Extraire domaine depuis le nom du fichier
    if "informatique" in file:
        df["Domaine"] = "Informatique"
    elif "electrique" in file:
        df["Domaine"] = "Électrique"
    elif "commercial" in file:
        df["Domaine"] = "Commercial"
    elif "tourisme" in file:
        df["Domaine"] = "Tourisme"
    elif "gestion" in file:
        df["Domaine"] = "Gestion-Comptabilité-Finance"
    elif "transport" in file:
        df["Domaine"] = "Transport"
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)
data.to_csv("all_jobs.csv", index=False, encoding='utf-8-sig')

# Compter le nombre d’offres par domaine
offres_par_domaine = data['Domaine'].value_counts()

# Créer le graphique
plt.figure(figsize=(8, 5))
offres_par_domaine.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Nombre d'offres par domaine", fontsize=14)
plt.xlabel("Domaine", fontsize=12)
plt.ylabel("Nombre d'offres", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Top 5 des entreprises
top_entreprises = data['Entreprise'].value_counts().head(5)

plt.figure(figsize=(8, 5))
top_entreprises.plot(kind='barh', color='cornflowerblue', edgecolor='black')

plt.title("Top 5 des entreprises qui recrutent le plus", fontsize=14)
plt.xlabel("Nombre d'offres", fontsize=12)
plt.ylabel("Entreprise", fontsize=12)
plt.gca().invert_yaxis()  # la plus grande en haut
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


# Regrouper les données par domaine et localisation
offres_par_domaine_localisation = data.groupby(['Domaine', 'Localisation']).size().unstack(fill_value=0)

# Afficher un heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(offres_par_domaine_localisation, annot=True, fmt="d", cmap="Blues")
plt.title("Nombre d'offres par domaine et par localisation")
plt.xlabel("Localisation")
plt.ylabel("Domaine")
plt.tight_layout()
plt.show()
