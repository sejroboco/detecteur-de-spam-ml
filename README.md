
# 📧 SpamDetector

Un outil simple et rapide pour détecter automatiquement les spams dans les messages texte grâce au Machine Learning.

## 🚀 Objectif

Détecter si un message est un **spam** ou non, à l’aide d’un modèle d’apprentissage automatique basé sur **Naïve Bayes**, avec une interface utilisateur intuitive via **Streamlit**.

## 🧠 Méthodologie

Le pipeline de traitement comprend les étapes suivantes :

1. **Prétraitement des données** (nettoyage, encodage)
2. **Vectorisation** avec `CountVectorizer` puis pondération avec `TF-IDF`
3. **Entraînement** d’un modèle **Multinomial Naïve Bayes**
4. **Évaluation** de la performance (score de précision)
5. **Déploiement** d’une application web avec **Streamlit**

## 🧰 Outils & Librairies

- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [streamlit](https://streamlit.io/)
- [numpy](https://numpy.org/)

## 📈 Performance

- **Précision du modèle : 98.29%**
- Testé sur un jeu de données de mails issu de [Kaggle](https://www.kaggle.com/)

## 💻 Lancer l'application en local

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/spam-detector.git
cd spam-detector
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l'application Streamlit
Prendre le soin d'exécuter d'abord le fichier `Projet-ML.py` où le modèle a été créé afin de créer les fichiers `.pkl`.

```bash
streamlit run spamDetector_AppWeb.py
```

## 🧪 Exemple d'utilisation

```python
msg = ["Win 1000 dollars now!"]
vect = cv.transform(msg).toarray()
result = model.predict(vect)
print("Spam" if result[0] == 1 else "Not Spam")
```

## 🛠️ Idées d'amélioration

- Ajouter des algorithmes plus avancés (SVM, XGBoost)
- Nettoyage avancé du texte (lemmatisation, suppression des stopwords)
- Interface utilisateur plus personnalisée
- Ajout d’une API REST pour intégration avec d’autres applications

---

🎯 **Fait avec passion pour améliorer l'expérience utilisateur dans la détection automatique de messages indésirables.**

**Auteur** : Toussaint Boco
