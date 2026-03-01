# Project Execution Plan: Foundations of Machine Learning for Small Projects

This document outlines a structured plan for a beginner-level Machine Learning training project using public datasets.
These general steps can be reused for private datasets and other ML projects.
For these projects it is recommended to use various AI tools and try to incorporate existing ML libraries. It is crucial that all of your final code is inspected and double checked by you. Each of the sections contains a note about suggested automation.

---
## Phase 0: Project Planning
Clearly identify the general steps you must follow to complete your project. Use this general template to get you started but in most cases you would have to add project specific steps. 

For larger projects, it is a good practice to have a seperate planning document which includes technical resources and diagrams that reflect the project execution plan. 

For documentation purposes, include your project set up and flow steps into a markdown file. 
## Phase 1: Research & Problem Scoping
**Goal:** Define the objective and select the right data.

**Why is this important?**

Without having a clear problem statement your final project may not be helpful to resolving the problem at hand. Researching the field also helps to see solutions that others have come up with and how you can incorporate them into your project.

* **Identify the Task Type:**
    * **Regression:** Predicting a continuous numerical value (e.g., House Prices).
    * **Classification:** Predicting a discrete label or category (e.g., Titanic Survival).
    * **Other:** Clustering, Anomaly Detection, Recommendations, Dimension Reduction, etc.
* **Select a Dataset:**
    * Select your dataset. Best publicly available resources are Kaggle and HuggingFace.
    * When selecting the dataset, look into data profiling and evaluate the data quality. Domain knowledge/research should inform your final selection.
* **Domain Research:** * Research "real world" context. This step is crucial to ensuring that you have a good quality dataset that will help resolve your task.
> **💡 Automation Note:** After clearly defining your problem statement, use AI to brainstorm model types and get preliminary domain specific research.

> **💡 Automation Note:** Use a `config.yaml` file to define your project parameters (e.g., dataset URL, target variable name, and task type). This allows you to swap datasets later without changing your core logic.

---

## Phase 2: Data Acquisition & EDA
**Goal:** Understand the "shape" and "health" of your data.
**Why is this important?**

This step ensures that you have a "good" dataset to help you answer your problem statement. The ML model will only be as good as the dataset it's trained on. A good dataset has the following characteristics:
* Representativeness: The dataset represents the problem you're trying to solve in a real-world manner. 
* Balance: The dataset is not biased towards one or other type of information.
* Quantity: The dataset has enough data points and features to train your model.
* Cleanliness and Integrity: The dataset contains clean data points and is trustworthy. With publically available datasets, the description normally gives you a good idea about these features. For private datasets, focus on integrity and methods of collection.

**EDA Steps:**
* **Load Data:** Use `pandas` to import your dataset: `df = pd.read_csv('data.csv')`.
* **Initial Inspection:**
    * `df.info()`: Check for data types and non-null counts.
    * `df.describe()`: View statistical summaries (mean, min, max).
* **Data Visualization:**
    * **Histograms:** Check for data distribution and skewness.
    * **Box Plots:** Identify outliers that might skew your model.
    * **Correlation Heatmap:** Identify which features have the strongest relationship with your target variable.
    * **Other:** The majority of the datasets would have domain specific vizualisations that would be helpful in understanding the dataset.
> **💡 Automation Note:** Instead of writing individual plot commands every time, use an automated EDA tool like `ydata-profiling` or `Sweetviz`. These generate a full HTML report of your data with one line of code.

---

## Phase 3: Data Preprocessing
**Goal:** Clean and format data for algorithmic processing.

* **Handling Missing Values:** Impute numerical values with `median` and categorical with `mode`.
*  Remove all not-needed features
* **Categorical Encoding:** Convert text to numbers via One-Hot or Label Encoding.
* **Feature Scaling:** Use `StandardScaler` to normalize numerical ranges.
* **Train/Test Split:** Divide data into Training (80%) and Test (20%) sets.


> **💡 Automation Note:** Use **Scikit-Learn Pipelines** (`Pipeline` and `ColumnTransformer`). This bundles your cleaning and scaling steps into a single "object" that prevents data leakage and makes your workflow repeatable.

---

## Phase 4: Modeling & Evaluation
**Goal:** Train the model and validate its performance.

**Why is this important?**

Creating an appropriate model is critical to accurately answering your problem at hand. Evaluation metrics are what allows you to understand how good the model is at answering your problem. At this stage, the evaluation metrics help to understand model pitfalls and suggest improvement tactics.


* **Select a Baseline Model:** Linear Regression (Reg) or Logistic Regression (Class).
* **Model Training:** Use `.fit(X_train, y_train)`.
* **Performance Metrics:** Calculate MAE and $R^2$ for Regression; Confusion Matrix and F1-Score for Classification.
* **Iteration:** Test an ensemble model like Random Forest.

Note that depending on the model, performance metrics can vastly differ. Research model and domain specific evaluation metrics and make sure to understand HOW those numbers reflect the model's performance.
> **💡 Automation Note:** Use AI to further research your model type and common implementation tactics. For larger projects, AI can also help to make your project scalable.

> **💡 Automation Note:** Implement **Hyperparameter Tuning** using `GridSearchCV` or `RandomizedSearchCV`. This automates the process of finding the best settings (like tree depth) for your model instead of guessing.


---

## Phase 5: Results and Documentation
**Goal:** Communicate findings and showcase technical skills.

**Why is this important?**
Documenting your model of thinking and results make your project readable for future you and anyone else trying to use your code. This step may take a while but it is crucial to 

* **Refactor Code (only as needed):** Clean the Jupyter Notebook and add explanatory Markdown cells.
* **Write the README:** Include the problem statement, approach, and key findings.
* **Final Step:** Push the repository to GitHub.

> **💡 Automation Note:** Use AI to get a baseline for project documentation and use it to format your results.

---