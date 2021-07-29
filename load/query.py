from datetime import datetime
import calendar
import db_connections
import csv

fileName='data_temp.csv'
lastIndViewDate ='select top(1)periodo_id from dbo.pdoObjetivosGvqHistView order by periodo_id desc'
queryViewByPeriod='select * from AR_PROD_GVQ.PDO_OBJETIVOS_GVQ_HIST_VIEW where territorio_id = 15743 and producto_id = 14095 and periodo_id = '
queryViewAll='select * from AR_PROD_GVQ.PDO_OBJETIVOS_GVQ_HIST_VIEW where territorio_id = 15743 and producto_id = 14095'
insertIndView= """INSERT INTO dbo.pdoObjetivosGvqHistView ([PERIODO_ID], [SOCIEDAD_ID], [SUBREGION_ID], [JEFATURA_ID], 
			[JEFATURA], [ZONA_ID], [ZONA_DESC], [TERRITORIO_ID], [TERRITORIO_DESC], [TIPO_VENDEDOR_ID], [TIPO_VENDEDOR_DESC], 
			[CATEGORIA_VENDEDOR_ID], [CLIENTE_ID], [PRODUCTO_ID], [PRODUCTO_DESC], [FAMILIA_ID], [FAMILIA], [NEGOCIO_ID], 
			[NEGOCIO], [HL_PRORRATEO], [HL_SENSIBILIZACION])
			VALUES {}"""
sql = """
BULK INSERT dbo.pdoObjetivosGvqHistView
FROM '/Users/alfredy.toro/Documents/k8s/load/data_temp.csv' WITH (
    FIELDTERMINATOR='\\t',
    ROWTERMINATOR='\\n'
    );
"""
inertIndLog='INSERT INTO dbo.pdoObjetivosGvqHistViewLOG ([execution_date],[success],[log]) VALUES {}'
selectIndView='select * from dbo.pdoObjetivosGvqHistView'

def lastSuccessLoadDate():
	print ('Opening connection to ', db_connections.Ind, ' executing query ', lastIndViewDate)
	result = db_connections.getResult(db_connections.Ind, lastIndViewDate)
	if result:
		return result[0][0]
	else:
		return result

def getViewGvq(period: datetime):
	print('executing select query')		
	if period:
		month = period.month + 1
		year = period.year
		if month == 13:
			month = 1
			year = year + 1
		month = str(calendar.month_name[month]).upper()[0:3]
		year = str(year)[2:4]
		query = queryViewByPeriod + '\'01-' + month + '-' + year +'\''
		return db_connections.getResult(db_connections.Gvq, query)
	else:
		return db_connections.getResult(db_connections.Gvq, queryViewAll)

def insertViewInd(rows):
	writeToCsv(rows)
	head, *tail = rows
	result = []
	for row in rows:
		head, *tail = row
		date=str(str(head.year)+'-'+str(head.month)+'-'+str(head.day))
		tail.insert(0, date)
		result.append(tail)
		###handle 1000
	values = ', '.join(map(str, result))
	insertQuery = insertIndView.format(values.replace('[', '(').replace(']',')'))
	print('Executing insert query')
	db_connections.insertRow(db_connections.Ind, sql)
	###db_connections.insertRow(db_connections.Ind, insertQuery)

def insertLogInd(log):
	date=str(datetime.now())
	success=str(1 if log == "" else 0)
	values=(date, success, log)
	print(values)
	insertQuery = inertIndLog.format(values)
	db_connections.insertRow(db_connections.Ind, insertQuery)	


def writeToCsv(rows):
	# open the file in the write mode
	print(rows)

	with open(fileName, 'w') as writeFile:
		writer = csv.writer(writeFile, delimiter=',', quotechar='"')
		#Write the list in one row
		writer.writerows(rows)
	writeFile.close()
	#file = open(fileName, 'w', newline='', encoding='utf-8')
	# create the csv writer
	#writer = csv.writer(file, quoting=csv.QUOTE_ALL)
	# write a row to the csv file
	#for row in rows:
	#	writer.writerow(row)
	# close the file
	#file.close()