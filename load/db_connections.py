#import cx_Oracle
#cx_Oracle.init_oracle_client(lib_dir="/Users/alfredy.toro/Documents/k8s/instantclient_19_8")
import os
os.chdir("/Users/alfredy.toro/Documents/k8s/instantclient_19_8")
import cx_Oracle
import pyodbc
import db_config
###Connection to oracle database###
dsn_tns = cx_Oracle.makedsn(db_config.origin_host, db_config.origin_port, db_config.origin_serviceName) # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
Gvq = cx_Oracle.connect(user=db_config.origin_user, password=db_config.origin_password, dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

##Connection to ms sql database###
Ind = pyodbc.connect(db_config.destination_driver+db_config.destination_host+';DATABASE='+db_config.destination_database+';UID='+db_config.destination_user+';PWD='+ db_config.destination_password)

def getResult(database, query):
	print ('Opening connection to database')
	cursor = database.cursor()
	print ('Running query in database')
	cursor.execute(query)
	result = cursor.fetchall()
	cursor.close()
	print ('Connection closed to database')
	return result

def insertRow(database, query):
	print ('Opening connection to database')
	cursor = database.cursor()
	cursor.execute(query)
	cursor.commit()
	cursor.close()
	print ('Connection closed to database')