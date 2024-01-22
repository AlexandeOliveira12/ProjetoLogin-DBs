import mysql.connector
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

connection = mysql.connector.connect(host=os.getenv("Host"), user=os.getenv("User"), password=os.getenv("Password"), database=os.getenv("DBs"))

tabela = os.getenv("tabela")

cursor = connection.cursor()
cursor.execute(f"select * from {tabela}")
clientes = cursor.fetchall()

for clientes in clientes:
    print(clientes)