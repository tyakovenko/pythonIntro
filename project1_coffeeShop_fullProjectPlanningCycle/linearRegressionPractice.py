import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "/Users/thechairman/PycharmProjects/pythonIntro/project1_coffeeShop_fullProjectPlanningCycle/data.xlsx"
sheet = "Transactions"
df = pd.read_excel(filepath, sheet_name=sheet)

#convert times and dates
df['transaction_time'] = pd.to_timedelta(df['transaction_time'].astype(str))
df['hour'] = df['transaction_time'].dt.components['hours']

# 3. Feature Engineering: Calculate Total Revenue & Day of Week
df['total_revenue'] = df['transaction_qty'] * df['unit_price']
df['day_of_week'] = df['transaction_date'].dt.day_name()

# 4. Basic Descriptive Statistics
print("--- Dataset Info ---")
print(df.info())
print("\n--- Numerical Summary ---")
print(df.describe())


# --- 5. Advanced EDA Add-ons ---

# Set visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 10))

# A. Hourly Revenue Trend (The "Morning Rush" Analysis)
plt.subplot(2, 2, 1)
hourly_rev = df.groupby('hour')['total_revenue'].sum().reset_index()
sns.lineplot(data=hourly_rev, x='hour', y='total_revenue', marker='o', color='teal')
plt.title('Total Revenue by Hour of Day')
plt.xlabel('Hour (24h Format)')
plt.ylabel('Revenue ($)')

# B. Top 5 Product Categories by Revenue
plt.subplot(2, 2, 2)
top_cats = df.groupby('product_category')['total_revenue'].sum().nlargest(5).reset_index()
sns.barplot(data=top_cats, x='total_revenue', y='product_category', palette='viridis')
plt.title('Top 5 Revenue-Generating Categories')

# C. Store Location Performance
plt.subplot(2, 2, 3)
store_perf = df.groupby('store_location')['total_revenue'].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=store_perf, x='total_revenue', y='store_location', palette='magma')
plt.title('Revenue by Store Location')

# D. Heatmap: Day of Week vs. Hour (Staffing Optimization)
plt.subplot(2, 2, 4)
# Define order for days
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_table = df.pivot_table(index='day_of_week', columns='hour', values='total_revenue', aggfunc='sum').reindex(days_order)
sns.heatmap(pivot_table, cmap='YlGnBu', annot=False)
plt.title('Sales Heatmap: Day vs. Hour')

plt.tight_layout()
plt.show()

# 6. Deep Dive: Average Transaction Value (ATV)
atv = df['total_revenue'].sum() / df['transaction_id'].nunique()
print(f"\n--- Key Metric ---")
print(f"Average Transaction Value (ATV): ${atv:.2f}")