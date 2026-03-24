# Dataset: https://www.kaggle.com/datasets/venky73/spam-mails-dataset

import pandas as pd
import numpy as np
import re
import string
import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
print("Loading data...")
df = pd.read_csv('spam.csv', encoding='latin-1')
# Rename columns to standard 'text' and 'label' if necessary
df = df[['text', 'label']]

# 2. CLASSIC DATA CLEANING
def clean_text(text):
    text = str(text).lower() # Lowercase
    # Remove punctuation
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove extra whitespace
    text = " ".join(text.split())
    return text

print("Cleaning text...")
df['text'] = df['text'].apply(clean_text)

# 3. PRE-PROCESSING (Vectorization)
# We limit features to the most common 2,500 to keep the model lightweight for the browser
MAX_FEATURES = 2500
tfidf = TfidfVectorizer(stop_words='english', max_features=MAX_FEATURES)
X = tfidf.fit_transform(df['text'])
y = df['label'] # 'spam' or 'ham'

# 4. TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. IMPLEMENT LOGISTIC REGRESSION
print("Training model...")
model = LogisticRegression(class_weight='balanced') # Use balanced to handle spam/ham imbalance
model.fit(X_train, y_train)

# 6. EVALUATE
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {acc:.2%}")

# 7. GENERATE VISUALIZATIONS
print("Generating visualizations...")

# Feature Importance Plot
feature_names = tfidf.get_feature_names_out()
coefficients = model.coef_[0]
# Use class 1 (spam) coefficients
top_indices = np.argsort(coefficients)[-15:]

plt.style.use('dark_background')
plt.figure(figsize=(10, 6))
plt.barh([feature_names[i] for i in top_indices], [coefficients[i] for i in top_indices], color='#00d1b2')
plt.title("Top 15 Most 'Spammy' Words", fontsize=14, pad=15)
plt.xlabel("Spam Coefficient Strength")
plt.tight_layout()
plt.savefig("spam_features.png", facecolor='#1e1e1e')
plt.close()

# Confusion Matrix Plot
plt.figure(figsize=(6, 5))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.title("Confusion Matrix")
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.close()

# 8. EXPORT MODEL FOR INTERACTIVE DEMO (Browser-safe JSON)
# For the browser predict() logic: y = sigmoid(sum(tfidf_vector * weights) + intercept)
# Convert numpy types to basic Python types for JSON serialization
v_serializable = {str(k): int(v) for k, v in tfidf.vocabulary_.items()}

model_data = {
    "vocabulary": v_serializable,
    "idf": tfidf.idf_.tolist(),
    "coefficients": coefficients.tolist(),
    "intercept": model.intercept_[0],
    "accuracy": acc
}

with open("model_metadata.js", "w") as f:
    f.write(f"const MODEL_DATA = {json.dumps(model_data)};")

# 9. GENERATE PREMIUM PORTFOLIO HTML
html_content = rf"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Spam Filter | Logistic Regression Showcase</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #00d1b2;
            --secondary: #3273dc;
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text: #f1f5f9;
        }}
        
        body {{
            background: var(--bg);
            color: var(--text);
            font-family: 'Space Grotesk', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 40px 20px;
        }}

        header {{
            text-align: center;
            margin-bottom: 60px;
            animation: fadeIn 1s ease-out;
        }}

        h1 {{
            font-size: 3.5rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}

        .hero-stats {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }}

        .stat-card {{
            background: var(--card-bg);
            padding: 20px 40px;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }}

        .stat-card:hover {{ transform: translateY(-5px); }}

        .stat-value {{
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--primary);
        }}

        /* LIVE PREDICTOR */
        .predictor-section {{
            background: rgba(45, 212, 191, 0.05);
            padding: 40px;
            border-radius: 24px;
            border: 1px solid rgba(45, 212, 191, 0.2);
            margin-bottom: 60px;
        }}

        textarea {{
            width: 100%;
            height: 120px;
            background: #111827;
            border: 1px solid #374151;
            border-radius: 12px;
            color: white;
            padding: 15px;
            box-sizing: border-box;
            font-family: inherit;
            font-size: 1rem;
            margin: 20px 0;
            resize: none;
        }}

        .prediction-box {{
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            font-weight: bold;
            font-size: 1.5rem;
            display: none;
            transition: all 0.5s ease;
        }}

        .grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }}

        .card {{
            background: var(--card-bg);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.05);
        }}

        img {{
            width: 100%;
            border-radius: 12px;
            margin-top: 15px;
        }}

        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}

        @media (max-width: 768px) {{ .grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Spam Sniper v2.0</h1>
            <p>A Logistic Regression powered filter trained on 5,500+ messages.</p>
        </header>

        <section class="predictor-section">
            <h2>Live Interactive Predictor</h2>
            <p>Type any email message below to see the AI classify it in real-time (running locally in your browser!)</p>
            <textarea id="emailInput" placeholder="Enter email text here... e.g. 'Congratulations! You won a free iPhone.'"></textarea>
            <div id="result" class="prediction-box">
                Status: <span id="statusLabel">-</span> | Spam Prob: <span id="probLabel">0%</span>
            </div>
        </section>

        <div class="hero-stats">
            <div class="stat-card">
                <div class="stat-value">{acc:.2%}</div>
                <div class="stat-label">Model Accuracy</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{MAX_FEATURES}</div>
                <div class="stat-label">Features Tracked</div>
            </div>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Semantic Insights</h3>
                <p>These words represent the strongest mathematical signals for "Spam" in the dataset.</p>
                <img src="spam_features.png" alt="Feature Importance">
            </div>
            <div class="card">
                <h3>Reliability Check</h3>
                <p>The confusion matrix shows our ability to distinguish between legitimate mail (Ham) and Spam.</p>
                <img src="confusion_matrix.png" alt="Confusion Matrix">
            </div>
        </div>

        <div style="margin-top: 60px; text-align: center; color: #64748b;">
            <p>Built with Scikit-Learn • Deployed via GitHub Pages</p>
        </div>
    </div>

    <script src="model_metadata.js"></script>
    <script>
        const textarea = document.getElementById('emailInput');
        const resultBox = document.getElementById('result');
        const statusLabel = document.getElementById('statusLabel');
        const probLabel = document.getElementById('probLabel');

        textarea.addEventListener('input', (e) => {{
            const text = e.target.value.toLowerCase().replace(/[^a-z\s]/g, "");
            if (text.trim().length === 0) {{
                resultBox.style.display = 'none';
                return;
            }}

            // 1. Simple Tokenization
            const tokens = text.split(/\s+/).filter(t => t.length > 0);
            
            // 2. TF & Dot Product with Weights
            let score = MODEL_DATA.intercept;
            let tfCount = {{}};
            
            tokens.forEach(token => {{
                if (MODEL_DATA.vocabulary.hasOwnProperty(token)) {{
                    tfCount[token] = (tfCount[token] || 0) + 1;
                }}
            }});

            // Apply TF-IDF (approx) and weights
            // Sklearn Tfidf: log((N+1)/(df+1)) + 1
            let dotProduct = MODEL_DATA.intercept;
            let l2Norm = 0;
            let vectors = [];

            Object.keys(tfCount).forEach(token => {{
                const idx = MODEL_DATA.vocabulary[token];
                const tf = 1; // binary tf or count matches sklearn's default? Count.
                // Note: we use simplified TF-IDF for browser demo
                const idf = MODEL_DATA.idf[idx];
                const weight = MODEL_DATA.coefficients[idx];
                
                // Sklearn default is count * idf
                const val = tfCount[token] * idf;
                vectors.push({{val, weight}});
                l2Norm += val * val;
            }});

            l2Norm = Math.sqrt(l2Norm);
            if (l2Norm > 0) {{
                vectors.forEach(v => {{
                    dotProduct += (v.val / l2Norm) * v.weight;
                }});
            }}

            // 3. Sigmoid Function
            const probability = 1 / (1 + Math.exp(-dotProduct));
            
            // Update UI
            resultBox.style.display = 'block';
            probLabel.innerText = (probability * 100).toFixed(1) + "%";
            
            if (probability > 0.5) {{
                statusLabel.innerText = "SPAM";
                resultBox.style.background = "rgba(239, 68, 68, 0.2)";
                resultBox.style.color = "#f87171";
                resultBox.style.border = "1px solid #ef4444";
            }} else {{
                statusLabel.innerText = "HAM (Legit)";
                resultBox.style.background = "rgba(34, 197, 94, 0.2)";
                resultBox.style.color = "#4ade80";
                resultBox.style.border = "1px solid #22c55e";
            }}
        }});
    </script>
</body>
</html>
"""


with open("index.html", "w") as f:
    f.write(html_content)

print("Project successfully upgraded! Visuals and interactive model generated.")