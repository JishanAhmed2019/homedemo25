print("Hello, World!")
# Create a sample dataframe
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
df
df.describe()
df['Age'].mean()

# This code creates a dictionary, a data frame, displays the dataframe, describes (gives statistics like mean, median, count, intervals, etc.)

print(df)
print(f'Mean Age: {df['Age'].mean()}')

# creates a dictionary with name and age, converts to a dataframe, gives statistics for data frame, calculates the average age.
print(df)
print(f'Mean Age: {df["Age"].mean()}')