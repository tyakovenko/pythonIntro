from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
'''
Step 1: Load in the dataset; 
Notes: we can use a built in dataset or a custom one from a csv, jscon, excel etc file
It is best to load the dataset in using pandas, seaborn, or  polars'''
df = sns.load_dataset('titanic').dropna(subset=['age', 'fare'])
X = df[['age']]  # Features (Needs to be 2D)
y = df['fare']   # Target

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Initialize and Train
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict
predictions = model.predict(X_test)
print(f"First prediction: {predictions[0]}")

