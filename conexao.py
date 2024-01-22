import mysql.connector
from Parameters.QuestionsParameters import *
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

connection = mysql.connector.connect(host=os.getenv("Host"), user=os.getenv("User"), password=os.getenv("Password"), database=os.getenv("DBs"))

tabela = os.getenv("tabela")

cursor = connection.cursor()
sql = (f"INSERT INTO {tabela}(Usuario, Email, Senha) VALUE (%s, %s, %s)")
value = [
(NomeUsuario, Email, Hash)
]
cursor.executemany(sql, value)
connection.commit()
print(cursor.rowcount, "Registros inseridos")

if connection.is_connected(): 
    cursor.close()
    connection.close()
    print("Conexao ao MySql foi encerrada")



