#many different ways to run ML models but we will focus on sklearn for now
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Clean data
df = sns.load_dataset('penguins').dropna()

# Encode the target ('species') into 0, 1, 2
le = LabelEncoder()
df['species_enc'] = le.fit_transform(df['species'])

# Features (X) and Target (y)
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df['species_enc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model A: Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# Model B: Random Forest
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)


dt_preds = dt_model.predict(X_test)
rf_preds = rf_model.predict(X_test)

print(f"Decision Tree Accuracy: {accuracy_score(y_test, dt_preds):.2%}")
print(f"Random Forest Accuracy: {accuracy_score(y_test, rf_preds):.2%}")