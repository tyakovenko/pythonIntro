#Dataset: https://www.kaggle.com/datasets/venky73/spam-mails-dataset

import pandas as pd
import numpy as np
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 1. LOAD DATA (Assuming file is named 'spam.csv')
df = pd.read_csv('spam.csv', encoding='latin-1')
# Rename columns to standard 'text' and 'label' if necessary
df = df[['text', 'label']]

# 2. CLASSIC DATA CLEANING
def clean_text(text):
    text = str(text).lower() # Lowercase
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text) # Remove punctuation
    text = re.sub(r'\d+', '', text) # Remove numbers
    return text

df['text'] = df['text'].apply(clean_text)

# 3. PRE-PROCESSING (Vectorization)
# We use TF-IDF to turn words into numbers based on importance
tfidf = TfidfVectorizer(stop_words='english', max_features=3000)
X = tfidf.fit_transform(df['text'])
y = df['label'] # 1 for Spam, 0 for Ham

# 4. TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. IMPLEMENT LOGISTIC REGRESSION
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. EVALUATE
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

# 7. GENERATE RESULTS FOR GITHUB PAGES
# Create a visualization of the Top 10 "Spam Indicator" words
feature_names = tfidf.get_feature_names_out()
coefficients = model.coef_[0]
top_indices = np.argsort(coefficients)[-10:]

plt.figure(figsize=(10, 5))
plt.barh([feature_names[i] for i in top_indices], [coefficients[i] for i in top_indices], color='crimson')
plt.title("Top 10 Words Predicting Spam")
plt.xlabel("Coefficient Strength (How 'Spammy' is the word?)")
plt.savefig("spam_features.png")

# Generate the static HTML
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Spam Filter Project</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-dark text-white p-5">
    <div class="container bg-secondary p-5 rounded shadow">
        <h1>Logistic Regression Spam Classifier</h1>
        <p class="lead">Built for my AI Portfolio</p>
        <hr>
        <h3>Model Accuracy: <span class="badge bg-success">{acc:.2%}</span></h3>
        <div class="row mt-4">
            <div class="col-md-7">
                <img src="spam_features.png" class="img-fluid rounded border">
            </div>
            <div class="col-md-5">
                <h4>What the AI Learned:</h4>
                <p>By analyzing the dataset, the Logistic Regression model identified these words as the strongest indicators of a spam message.</p>
            </div>
        </div>
    </div>
</body>
</html>
"""
with open("index.html", "w") as f:
    f.write(html_content)