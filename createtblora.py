from conexion import Gvq
cursor = Gvq.cursor()
# Creating a table employee
cursor.execute("create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")