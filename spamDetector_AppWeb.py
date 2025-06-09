# Importation de librairies
import pickle
import streamlit as st
import pandas as pd
from win32com.client import Dispatch

# Fonction speak
def speak(text) :
	speak = Dispatch("SAPI.SpVoice")
	speak.Speak(text)

# Chargement de la vectorisation
cv = pickle.load(open("vectorizer.pkl", "rb"))

# Chargement du modèle
model = pickle.load(open("spam.pkl", "rb"))

# Importation et pré traitement du dataframe
spam_df = pd.read_csv("spam.csv", encoding = "latin-1")
spam_df = spam_df.iloc[:,0:2]
spam_df = spam_df.rename(columns={"v1" : "class", "v2" : "message"})
spam_df["class"] = spam_df["class"].map({"ham" : 0, "spam" : 1})

# Création proprement dite de l'application
def main():
	st.title("Classificateur d'Emails et de Spams") # Titre de l'application
	st.subheader("Construit avec Python et Streamlit") # Sous_titre de l'application
	st.text("Cette application est destinée à détecter un spam, d'un mail correct.")
	st.text("Il se base sur un jeu de données obtenu depuis la plateforme kaggle et")
	st.text(" contient 5572 exemples. Ces exemples de mails corrects et de spam on")
	st.text("servi à développer un modèle de Maching Learning pour atteindre le but visé.")
	st.text("Base de données")
	st.dataframe(spam_df) # Affichage du dataframe

	st.image("Machine_Learning.jpg", caption = "Détection de spam", width=700)


	msg = st.text_input("Entrer un texte : ") # Récupération d'information
	if st.button("Prédire") :
		data = [msg]
		vect = cv.transform(data).toarray() # Vectorisation du message
		prediction = model.predict(vect) # Prédiction du résultat
		result = prediction[0]
		if result == 1 :
			st.error("Ceci est un spam.")
			speak("Ceci est un spam.")
		else :
			st.success("Ceci est un mail correct.")
			speak("Ceci est un mail correct.")
main()