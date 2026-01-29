import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset('penguins')

# Drop rows with missing values for a cleaner analysis
df = df.dropna()

sns.histplot(data=df, x="flipper_length_mm", hue="species", kde=True)
plt.title("Distribution of Flipper Length by Species")
plt.show()