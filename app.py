import streamlit as st
import requests

# Définir le titre de la page
st.set_page_config(page_title="Analyseur de sentiments")

# Titre de l'application
st.title("Analyse de sentiment par IA")

# Ajouter une image de fond
st.image("fond.png")

# Afficher une présentation
st.write("Bienvenue dans notre analyseur de sentiments !\n"
         "Celui-ci fonctionne avec un modèle de machine learning et a été entraîné sur 1 600 000 tweets.")

# Ajouter un champ de saisie pour la phrase
phrase = st.text_input("Entrez une phrase :")

# Ajouter un bouton pour lancer l'analyse
if st.button("Analyser"):
    # Envoyer la phrase à l'API et récupérer la prédiction
    response = requests.post("https://api-backend-vspacy.herokuapp.com/prediction", data={'phrase': phrase})
    
    # Traiter la réponse de l'API
    if response.status_code == 200:
        result = response.json()
        if float(result['prediction']) < 0.2:
            st.write("La phrase est positive")
        elif float(result['prediction']) < 0.4:
            st.write("La phrase semble être positive")
        elif float(result['prediction']) < 0.6:
            st.write("La phrase semble être neutre")
        elif float(result['prediction']) < 0.8:
            st.write("La phrase semble être négative")
        else:
            st.write("La phrase est négative")
    else:
        st.write("Une erreur s'est produite lors de la requête à l'API.")