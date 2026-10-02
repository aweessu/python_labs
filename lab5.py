import pandas as pd


# 1
s = pd.Series([10, 20, 30, 40, 50])
print(s)


# 2
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print(df)


# 3
print(df['Name'])

print(df[['Age', 'City']])


# 4
print(df.iloc[1])

print(df.loc[1])


# 5
print(df.iloc[:3])


# 6
df_salary = df.copy()

df_salary['Salary'] = [50000, 60000, 70000, 80000]

print(df_salary)


# 7
df_age = df.copy()

df_age['Age'] = df_age['Age'] + 1

print(df_age)


# 8
df_no_city = df.drop(columns=['City'])

print(df_no_city)


# 9
df_no_row = df.drop(index=2)

print(df_no_row)


# 10
df_index = df.set_index('Name')

print(df_index)


# 11
df_reset = df_index.reset_index()

print(df_reset)


# 12
print(df.head(2))

print(df.tail(1))


# 13
missing_data = {
    'A': [1, 2, None],
    'B': [4, None, 6],
    'C': [None, 8, 9]
}

df_missing = pd.DataFrame(missing_data)

print(df_missing)


# 14
print(df_missing.isnull())

print(df_missing.notnull())


# 15
df_fill_zero = df_missing.fillna(0)

print(df_fill_zero)

df_fill_mean = df_missing.copy()

df_fill_mean['A'] = df_fill_mean['A'].fillna(
    df_fill_mean['A'].mean()
)

print(df_fill_mean)


# 16
df_drop_missing = df_missing.dropna()

print(df_drop_missing)


# 17
print(df[df['Age'] > 30])


# 18
df_renamed = df.rename(columns={
    'Name': 'Full Name',
    'Age': 'Age (Years)',
    'City': 'Location'
})

print(df_renamed)


# 19
df_sorted = df.sort_values(
    by='Age',
    ascending=False
)

print(df_sorted)


# 20
def age_group(age):
    if age < 30:
        return 'Young'
    elif age <= 35:
        return 'Middle'
    else:
        return 'Senior'


df_group = df.copy()

df_group['Age Group'] = df_group['Age'].apply(age_group)

print(df_group)