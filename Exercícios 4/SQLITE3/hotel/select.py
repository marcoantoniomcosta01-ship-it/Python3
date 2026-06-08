import sqlite3

conexao = sqlite3.connect("hotel.db")

cursor =conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

conexao.commit()

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)