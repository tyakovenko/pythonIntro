# Coffee Shop Management System
For this project, we will use the random tree model to predict the total sales based on transaction features. below are the steps to follow to get the possible result. For practice, replicate this process
but use the linear regressio model instead.

## Step 1: Get a dataset
When working with ML projects, you want to make sure that you have a reliable dataset. For these projects,
we will use pre-existing dataset. Kaggle and official government websites are great resources for reliable and diverse data. 

For this part use the following [dataset](https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales).

## Step 2: Clean and prepare the data
The first step in processing your data includes correctly loading the dataset and ensuring that no information was corrupt. 
At this stage, we can also perform some basic data cleaning and reformating to make the
next steps easier to work with. Usually, this initial step is done using basic pandas functions.

## Step 3: Perform Exploratory Data Analysis (EDA)
EDA is a crucial first step in data processing. Here, we will get a better understanding of all the data features (columns). 
More specifically, we will get a look at counts of missing values, all the unique values, value distributions, etc. Usually EDA consists of the following steps: 
* **3. Descriptive Statistics**
    * Use `describe()` to calculate mean, median, standard deviation, and quartiles.
    * **Goal:** Understand the central tendency and spread of the data distribution.

* **4. Univariate Analysis**
    * Analyze single variables using histograms, box plots, or bar charts.
    * **Goal:** Identify distributions, skewness, and outliers.

* **5. Bivariate/Multivariate Analysis**
    * Analyze relationships between variables using scatter plots, heatmaps, and correlation matrices.
    * **Goal:** Identify correlations or patterns between multiple features.

* **6. Outlier Detection**
    * Utilize visualizations (box plots, scatter plots) or statistical methods like the **Z-score**:
        $$z = \frac{x - \mu}{\sigma}$$
    * **Goal:** Detect and manage data points that deviate significantly from the rest of the set.

* **7. Feature Engineering**
    * Transform or create new variables to improve data insights.
    * **Common methods:** Scaling, encoding categorical variables, or creating ratios.

* **8. Summarize and Document**
    * Document findings, including data quality issues, patterns, and insights.
    * **Goal:** Inform future modeling or data-driven decision-making.

## Step 4: Train Machine Learning Models
Choose two different machine learning models and train them on the dataset. For this project, we will focus on supervised learning models: Linear Regression and Decision Tree.
These are two supervised learning models which are available through the sklearn library.

The target variable is Total Sales Amount which would predict the total sales amount based on transaction features.
### **1. Data Preparation**
* **Feature Selection:** Identify the target variable ($y$) and independent features ($X$).
* **Handling Missing Values:** Use imputation or remove rows, as standard Decision Tree implementations (like scikit-learn) require complete data.
* **Categorical Encoding:** Convert labels into numerical format using **Label Encoding** or **One-Hot Encoding**.

### **2. Dataset Splitting**
Divide the data into two or three sets to ensure the model generalizes well:
* **Training Set:** Usually 70-80% of the data.
* **Testing Set:** Remaining 20-30% to evaluate final performance.

### **3. Training**
* The algorithm recursively partitions the data by selecting the feature that provides the highest Information Gain or lowest Gini Impurity.
* This process continues until a stop condition is met (e.g., a node is pure or reaches a maximum depth).

### **4. Optional: Tree Pruning or Hyperparameter Tuning**
To prevent **overfitting** (where the tree is too complex), apply:
* **Pre-pruning:** Set `max_depth`, `min_samples_split`, or `min_samples_leaf`.
* **Post-pruning:** Removing branches that provide little power after the tree is fully grown (Cost Complexity Pruning).


Follow similar steps for the linear regression model. 

## Step 5: Evaluate performance of the two models
The models are usually evaluated base on their accuracy, precision, and recall. All of those metrics can be found in the confusion matrix.
#### **Evaluation**
* Use the test set to generate a **Confusion Matrix**.
* Calculate metrics: **Accuracy**, **Precision**, **Recall**, and **F1-Score**.


## Step 6: Visualize
Visualize the tree structure to interpret the decision logic. (scikit-learn plot_tree function)
Collect basic evaluation matrics and interpret them in context. Look at the confusion matrix. Explain why one algorithm would be better than other.