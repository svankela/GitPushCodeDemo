import pandas as pd
df=pd.read_csv('employees.csv')
df

file=open("employees.csv",'r')
file_open=file.read()
print(file_open)
