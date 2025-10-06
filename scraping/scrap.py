from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pandas as pd
import time
import random

# Chemin vers EdgeDriver
service = Service(r"C:\Users\moham\Desktop\projet web scrapping\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# URL filtrée "informatique"
url = "https://www.emploitunisie.com/recherche-jobs-tunisie/?f%5B0%5D=im_field_offre_metiers%3A28"
driver.get(url)
time.sleep(random.uniform(2,4))  # pause aléatoire pour simuler un humain

jobs = []

# Récupérer toutes les offres sur la page
job_elements = driver.find_elements(By.CLASS_NAME, "card-job")

for job in job_elements:
    try:
        # Lien complet
        lien = job.get_attribute("data-href").strip()
        
        # Titre
        titre = job.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").text.strip()
        
        # Entreprise
        entreprise = job.find_element(By.CLASS_NAME, "card-job-company").text.strip()
        
        # Localisation
        try:
            localisation = job.find_element(By.XPATH, ".//ul/li[contains(text(),'Région')]").text.replace("Région de :","").strip()
        except:
            localisation = ""
        
        # Date de publication
        try:
            date_pub = job.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        except:
            date_pub = ""
        
        jobs.append({
            "Titre": titre,
            "Entreprise": entreprise,
            "Localisation": localisation,
            "Date": date_pub,
            "Lien": lien
        })
    except:
        continue

# Créer DataFrame et sauvegarder CSV
df = pd.DataFrame(jobs)
df.to_csv("emploitunisie_transport.csv", index=False, encoding='utf-8-sig')

print("Scraping terminé ! Nombre d'offres :", len(jobs))

driver.quit()
