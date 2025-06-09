# Importation des différentes librairies
import numpy as np # Calculs numériques
import pandas as pd # Importation du dataset
from sklearn.feature_extraction.text import CountVectorizer # Vectorisation
from sklearn.model_selection import train_test_split # Division du dataset
from sklearn.feature_extraction.text import TfidfTransformer # TF-IDF
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB # Classificateur Naïve Bayes
from sklearn import metrics # Métrique de performance
from sklearn.metrics import accuracy_score # Score de performance
import pickle # Association à une application web

# Importation de la base de données
spam_df = pd.read_csv("spam.csv", encoding = "latin-1")
spam_df.columns
spam_df = spam_df.iloc[:,0:2]
spam_df = spam_df.rename(columns={"v1" : "class", "v2" : "message"})
spam_df["class"] = spam_df["class"].map({"ham" : 0, "spam" : 1})

# Vectorisation
cv = CountVectorizer()
x = spam_df["message"]
y = spam_df["class"]
x_cv = cv.fit_transform(x)

# Division de la base de données 
x_train, x_test, y_train, y_test = train_test_split(x_cv, y, test_size=0.2, random_state=0)

# TF-IDF
tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train)

# Classificateur Naive Bayes
model = MultinomialNB()
model.fit(x_train, y_train)

# Performance du modèle
performance = model.score(x_test, y_test)
print(performance*100)
x_test_tfidf = tfidf_transformer.fit_transform(x_test)
y_pred = model.predict(x_test)
target_names = ["ham", "spam"]

# Test du détecteur de spam
## Exemple 1
msg1 = "You win 10 Dollars"
data = [msg1]
vect = cv.transform(data).toarray()
result = model.predict(vect)
print(result)

## Exemple 2
msg2 = "Hello, how are you ?"
data = [msg2]
vect = cv.transform(data).toarray()
result = model.predict(vect)
print(result)

# Application web
pickle.dump(model, open("spam.pkl", "wb"))
pickle.dump(cv, open("vectorizer.pkl", "wb"))
clf = pickle.load(open("spam.pkl", "rb"))

