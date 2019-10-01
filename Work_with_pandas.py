import sqlite3
import pandas as pd

with sqlite3.connect('/home/user/Examen/Examen/db.sqlite3') as conn:
    data = pd.read_sql_query("SELECT * from Users", conn)
    print(data)
first = list(data['first_name'])
last = list(data['last_name'])
full=[]
for i in range(len(first)):
    full.append(first[int(i)] +" "+ last[int(i)])

data['full name'] = full
print(data)
data.to_excel('myData.xlsx')
print("Media calculata pe number of login:", data['number_of_login'].mean())
print("Standard ev calculata pe number of login:",data['number_of_login'].std() )




