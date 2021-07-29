from conexion import Gvq
import csv
import calendar
import datetime

cursor = Gvq.cursor()

cursor.execute('insert into employee values(80003,\'alex3\',8888.88)')
# commit() to make changes reflect in the database
Gvq.commit()
print('Record inserted successfully in Oracle')
