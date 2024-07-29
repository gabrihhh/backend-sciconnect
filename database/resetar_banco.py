import mysql.connector
import os

def criar_ou_resetar_banco(host, user, password, database):
    
    try:
        # Conecta-se ao banco de dados
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        mycursor = mydb.cursor()

        # Verifica se o banco de dados existe
        mycursor.execute("SHOW DATABASES LIKE %s", ("sciconnect",))
        result = mycursor.fetchone()

        if result:
            # Se o banco de dados existe, apaga-o
            mycursor.execute(f"DROP DATABASE sciconnect;")
            print(f"Banco de dados sciconnect foi apagado.")

        # Cria o banco de dados
        mycursor.execute(f"CREATE DATABASE sciconnect")
        print(f"Banco de dados sciconnect foi criado.")


        # Obtém o diretório atual onde o script está sendo executado
        current_dir = os.path.dirname(os.path.abspath(__file__))
        #executa o db que está na mesma pasta do diretório desse script
        script_file = os.path.join(current_dir,"db.sql")
        # Executa o script SQL

        with open(script_file, 'r') as file:
            script = file.read()
        try:
            mycursor.execute(script)
            print("Script SQL executado com sucesso.")
        except mysql.connector.Error as error:
            print(f"Erro ao executar o script: {error}")
            return 

    except mysql.connector.Error as error:
        print(f"Erro ao conectar ou executar a query: {error}")
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

host = "172.17.0.2"
user = "root"
password = "99076641"
database = "sciconnect"

# Executa a função
criar_ou_resetar_banco(host, user, password, database)
