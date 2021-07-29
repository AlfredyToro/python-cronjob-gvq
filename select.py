from conexion import conexionsql

cursor = conexionsql.cursor()
cursor.execute('SELECT * FROM Inventory')

myresult = cursor.fetchall()

for x in myresult:
  print(x)

