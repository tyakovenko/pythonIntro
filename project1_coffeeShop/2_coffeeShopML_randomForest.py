import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# 1. Load and Clean Data
def load_and_clean_data(filepath, sheet='Transactions'):
    print(f"--- Loading data from {filepath} (Sheet: {sheet}) ---")
    df = pd.read_excel(filepath, sheet_name=sheet)

    # Feature Engineering
    df['total_sales'] = df['transaction_qty'] * df['unit_price']

    if not pd.api.types.is_datetime64_any_dtype(df['transaction_time']):
        df['transaction_hour'] = pd.to_datetime(df['transaction_time'], format='%H:%M:%S').dt.hour
    else:
        df['transaction_hour'] = df['transaction_time'].dt.hour

    cols_to_drop = ['transaction_id', 'transaction_date', 'transaction_time', 'product_detail']
    df = df.drop(columns=cols_to_drop)

    print("Data Loaded Successfully.")
    print("\n[Data Snapshot - Top 5 Rows]:")
    print(df.head())
    return df


# 2. Exploratory Data Analysis (EDA)
def perform_eda(df):
    print("\n--- Performing Exploratory Data Analysis ---")

    print("\n[Statistical Description]:")
    print(df.describe())

    print("\n[Most Common Values (Mode)]:")
    print(df.mode().iloc[0])  # Showing the first mode row for clarity

    # Visualizations
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='product_category', y='total_sales', estimator=sum)
    plt.xticks(rotation=45)
    plt.title("Total Sales by Product Category")
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')
    plt.title("Statistical Correlation Map")
    plt.show()
    print("EDA Visualizations generated.")


# 3. Data Preprocessing
def preprocess_data(df):
    print("\n--- Preprocessing Data for Model ---")

    le = LabelEncoder()
    categorical_cols = ['store_location', 'product_category', 'product_type']
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    print(f"Encoded columns: {categorical_cols}")

    X = df.drop('total_sales', axis=1)
    y = df['total_sales']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    print(f"Data Split: {len(X_train)} training samples, {len(X_test)} test samples.")

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Features scaled using StandardScaler.")
    return X_train, X_test, y_train, y_test


# 4. Model Building
def train_model(X_train, y_train):
    print("\n--- Training Random Forest Regressor ---")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model training complete.")
    return model


# 5. Evaluation & Performance Visualization
def evaluate_performance(model, X_test, y_test):
    print("\n--- Evaluating Model Performance ---")
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f">> Mean Absolute Error: ${mae:.2f}")
    print(f">> R-squared Score: {r2:.2f}")

    # Visualization
    plt.figure(figsize=(8, 8))
    plt.scatter(y_test, predictions, alpha=0.5, color='teal')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Model Performance: Actual vs. Predicted")
    plt.show()
    print("Evaluation plot generated.")

# --- Pipeline Execution ---
filePath = "data.xlsx"
data = load_and_clean_data(filePath)
perform_eda(data)
X_train, X_test, y_train, y_test = preprocess_data(data)
coffee_model = train_model(X_train, y_train)
evaluate_performance(coffee_model, X_test, y_test)