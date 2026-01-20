import pandas as pd


#main data type: pandas dataframe (pandas series is also an option)
#main library used for data processing, EDA, storage, and computations
#storage and computations use Pandas on when working with data sets that are not too large

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR'],
    'Salary': [70000, 60000, 85000, 55000, 62000],
    'Years_Exp': [3, 2, 7, 1, 4]
}

df = pd.DataFrame(data)

#Data filtering
it_high_earners = df[(df['Department'] == 'IT') & (df['Salary'] > 75000)]

#Grouping data
avg_salary = df.groupby('Department')['Salary'].mean()

print("IT High Earners:")
print(it_high_earners)
print("\nAverage Salary by Dept:")
print(avg_salary)

#dataframes have a lot more capabilities that become useful with data processing
#you can read csvs, excels, etc. write onto the documents too
#check full documentation as needed

#numpy is useful for heavy math processing while pandas is very useful for more 'excel like' processing since it allows for different data type

#pandas also has some sql like features
#ex: SQL join analog on two different data frames
sales_df = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'ProductID': ['P1', 'P2', 'P1', 'P3'],
    'Qty': [2, 1, 5, 2]
})

products_df = pd.DataFrame({
    'ProductID': ['P1', 'P2', 'P3'],
    'Name': ['Espresso', 'Latte', 'Muffin'],
    'Category': ['Drink', 'Drink', 'Food']
})

# Merge the two DataFrames on the 'ProductID' column
merged_df = pd.merge(sales_df, products_df, on='ProductID') #merges MUST always be on a common column
print(merged_df)


#concat is also another option depending on what kind of a merge you need to do
#the axis parameter determines that
jan_sales = pd.DataFrame({
    'Date': ['Jan 1', 'Jan 2'],
    'Revenue': [100, 150]
})

feb_sales = pd.DataFrame({
    'Date': ['Feb 1', 'Feb 2'],
    'Revenue': [200, 250]
})

# Stack them on top of each other (Axis 0)
total_sales = pd.concat([jan_sales, feb_sales], ignore_index=True)

print(total_sales)


print(merged_df)