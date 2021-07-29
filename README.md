SELECT TOP (1000) [id]
      ,[name]
      ,[quantity]
  FROM [visual].[dbo].[Inventory]

INSERT INTO Inventory (id, name, quantity)
VALUES ('5','pera','349')

SELECT * FROM Inventory

docker run --name gvqtest --link sql1:sql1 --link oracledb:oracledb gvqocsql sleep 1000

docker exec -it gvqtest bash 

run sqldeveloper - ruta application . zsh ejecutable.sh

---------
COPY . /opt/oracle

CMD ["python3", "/opt/oracle/insert.py"]