import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# 1. Data Ingestion & Cleaning
def load_and_clean_data(filepath, sheet='Transactions'):
    """
    Modified to accept .xlsx files.
    Added 'sheet' parameter in case your data isn't on the first tab.
    """
    # Use read_excel instead of read_csv
    df = pd.read_excel(filepath, sheet_name=sheet)

    # Feature Engineering: Calculate our target variable
    df['total_sales'] = df['transaction_qty'] * df['unit_price']

    # Convert time strings to usable numerical features
    # Note: Excel often imports time as actual datetime objects already!
    if not pd.api.types.is_datetime64_any_dtype(df['transaction_time']):
        df['transaction_hour'] = pd.to_datetime(df['transaction_time'], format='%H:%M:%S').dt.hour
    else:
        df['transaction_hour'] = df['transaction_time'].dt.hour

    # Drop columns that won't help the model
    cols_to_drop = ['transaction_id', 'transaction_date', 'transaction_time', 'product_detail']
    df = df.drop(columns=cols_to_drop)

    return df


# 2. Exploratory Data Analysis (EDA)
def perform_eda(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='product_category', y='total_sales', estimator=sum)
    plt.xticks(rotation=45)
    plt.title("Total Sales by Product Category")
    plt.show()

    # Statistical Correlation Heatmap
    # Note: We only correlate numeric columns
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')
    plt.title("Statistical Correlation Map")
    plt.show()


# 3. Data Preprocessing
def preprocess_data(df):
    # Encode categorical text into numbers
    le = LabelEncoder()
    categorical_cols = ['store_location', 'product_category', 'product_type']
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    X = df.drop('total_sales', axis=1)
    y = df['total_sales']

    # Split and Scale
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test


# 4. Model Building
def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


# 5. Evaluation & Performance Visualization
def evaluate_performance(model, X_test, y_test):
    predictions = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"Mean Absolute Error: ${mae:.2f}")
    print(f"R-squared Score: {r2:.2f}")

    # Visualization: Predicted vs Actual
    plt.figure(figsize=(8, 8))
    plt.scatter(y_test, predictions, alpha=0.5, color='teal')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Model Performance: Actual vs. Predicted")
    plt.show()

# --- Pipeline Execution ---
filePath = "data.xlsx"
data = load_and_clean_data(filePath)
perform_eda(data)
X_train, X_test, y_train, y_test = preprocess_data(data)
coffee_model = train_model(X_train, y_train)
evaluate_performance(coffee_model, X_test, y_test)