import pandas as pd
data = {
    'Student': ['Aditya', 'Rahul', 'Sneha', 'Vikram'],
    'Math': [95, 78, 92, 60],
    'Science': [88, 82, 95, 70],
    'History': [90, 85, 92, 65]
}

# Turn it into a Pandas Table
df = pd.DataFrame(data)

print(df)
print(df["Math"])
# Create a filter (True/False list)
high_scorers = df[df['Math'] > 80]

print("\nStudents with Math > 80:")
print(high_scorers)
print("\nClass Averages:")
# We only select the number columns first, then ask for the mean
print(df[['Math', 'Science', 'History']].mean())
df['Total'] = df['Math'] + df['Science'] + df['History']

# 2. Sorting: Who is number 1?
# ascending=False means "Big numbers first"
sorted_df = df.sort_values(by='Total', ascending=False)

print("\nFinal Report Card (Ranked):")
print(sorted_df)

