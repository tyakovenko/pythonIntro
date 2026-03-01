import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "/home/taya/PycharmProjects/pythonIntro/project1_coffeeShop_fullProjectPlanningCycle/data.xlsx"
sheet = "Transactions"
df = pd.read_excel(filepath, sheet_name=sheet)

#convert times and dates
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['transaction_time'] = pd.to_timedelta(df['transaction_time'])
df['hour'] = df['transaction_time'].dt.components['hours']

# 3. Feature Engineering: Calculate Total Revenue & Day of Week
df['total_revenue'] = df['transaction_qty'] * df['unit_price']
df['day_of_week'] = df['transaction_date'].dt.day_name()

# 4. Basic Descriptive Statistics
print("--- Dataset Info ---")
print(df.info())
print("\n--- Numerical Summary ---")
print(df.describe())