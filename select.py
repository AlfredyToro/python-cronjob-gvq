from conexion_copy import conexionsql

cursor = conexionsql.cursor()
cursor.execute('SELECT * FROM api_response_log')

myresult = cursor.fetchall()

for x in myresult:
  print(x)

