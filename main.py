import pandas as pd


df= pd.read_excel(r'C:\\Users\\Nikita\\OneDrive - Blue Hex Software Private Limited (1)\\HR Analytics\\resources+updated\\resources\\mean median mode.XLSX')
print(df)

df['percent_hike'].mean()

df['percent_hike'].median()

df['percent_hike'].mode()

df['salary_2018'].max()-df['salary_2018'].min()

df['salary_2018'].quantile(0.75)-df['salary_2018'].quantile(0.25)