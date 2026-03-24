# 🚀 Python AI & ML Portfolio

This repository contains my progress and projects through the world of Python and Machine Learning.

---

## 🛡️ Logistic Regression Spam Classifier
**Status: Complete** | **Model: Logistic Regression** | **Accuracy: 97.68%**

Built as part of my AI Portfolio, this project uses Natural Language Processing (NLP) to classify messages as either "Spam" or "Ham" (Legitimate).

### 📈 Model Performance
We achieved a high accuracy of **97.68%** using `TfidfVectorizer` and `LogisticRegression` from the Scikit-Learn library.

#### What the AI Learned
By analyzing the dataset, the Logistic Regression model identified these words as the strongest indicators of a spam message:

![Top Spam Indicators](logisticRegression/spam_features.png)

### 🛠️ Key Features
- **TF-IDF Vectorization**: Analyzes word importance across the entire message dataset.
- **Data Cleaning**: Custom preprocessing pipeline to remove punctuation, numbers, and standardize text.
- **Bootstrap Reporting**: Generates a clean HTML report of the model's findings.

### 📁 Technical Details
You can find the implementation details in the [`/logisticRegression`](./logisticRegression) folder:
- [`implementation.py`](./logisticRegression/implementation.py): The core training and reporting script.
- [`spam.csv`](./logisticRegression/spam.csv): The raw dataset of 5,500+ messages.
- [`index.html`](./logisticRegression/index.html): The standalone report page.

---

*(Continuing through the ML Roadmap...)*