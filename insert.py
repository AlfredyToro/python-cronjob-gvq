from conexion import conexionsql
from conexion import Gvq
import csv
import calendar
import datetime
import pandas as pd
import time

cursor = conexionsql.cursor()
print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Inventory (id, name, quantity) VALUES (?,?,?);"
with cursor.execute(tsql,'0019','alchemy','0019'):
    print ('Successfully Inserted in alchemypandas!')

cursor = Gvq.cursor()
cursor.execute('insert into employee values(80006,\'alex6\',6666.66)')
# commit() to make changes reflect in the database
Gvq.commit()
print('Record inserted successfully in Oracle')
