FROM pythonsql-venom:latest

WORKDIR /opt/oracle
COPY . /opt/oracle

CMD ["python3", "/opt/oracle/insert.py"]