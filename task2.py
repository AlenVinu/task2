import pandas as pd

dataframe = pd.read_csv('student.csv')

column_data = dataframe['first_name']

dataframe_subset =dataframe[['first_name', 'last_name']]
dataframe_filtered=len(dataframe['first_name']) >5
print(dataframe.isnull().sum())
dataframe.dropna(inplace=True)
dataframe.drop_duplicates(inplace=True)
dataframe_dropped_rows = dataframe.dropna()
dataframe['ethnicity'] = dataframe['ethnicity'].fillna(dataframe['ethnicity'].mean())
df_no_duplicates = dataframe.drop_duplicates()
ny_df = dataframe[dataframe['hs_state'] == 'New York']
print("\nFiltered DataFrame (hs_state is New York):")
print(ny_df)
grouped_by_city = dataframe.groupby('hs_city').mean()
print("\nGrouped by hs_city (mean Age and Score):")
print(grouped_by_city)




