import cx_Oracle
import pyodbc
import db_config as db_config
from datetime import datetime

size = 1000000
###Connection to oracle database###
dsn_tns = cx_Oracle.makedsn(db_config.origin_host, db_config.origin_port, db_config.origin_database)
Gvq = cx_Oracle.connect(user=db_config.origin_user, password=db_config.origin_password, dsn=dsn_tns)
##Connection to ms sql database###
try:
    #conexion = pyodbc.connect(string.destination_driver+string.destination_host+';DATABASE='+string.destination_database+';UID='+string.destination_user+';PWD='+ string.destination_password)
    conexionsql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+db_config.destination_host+';DATABASE='+db_config.destination_database+';UID='+db_config.destination_user+';PWD='+ db_config.destination_password)
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
