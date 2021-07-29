from conexion import conexionsql
from conexion import Gvq
import csv
import calendar
import datetime

cursor = conexionsql.cursor()
print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Inventory (id, name, quantity) VALUES (?,?,?);"
with cursor.execute(tsql,'666','sql6','6666'):
    print ('Successfully Inserted in SQL1!')

cursor = Gvq.cursor()
cursor.execute('insert into employee values(80006,\'alex6\',6666.66)')
# commit() to make changes reflect in the database
Gvq.commit()
print('Record inserted successfully in Oracle')
