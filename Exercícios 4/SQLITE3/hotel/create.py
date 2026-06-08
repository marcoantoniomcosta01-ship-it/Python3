import sqlite3
lista = [('marco', 'marcoetid@gmail.com'), ('barbara', 'barbarapodepah@yahoo.com'), ('sergio', 'hosepani@email.com')]

conexao = sqlite3.connect("hotel.db")

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT)")

cursor.executemany("INSERT INTO usuarios(nome, email) VALUES (?, ?)", lista)

conexao.commit()
conexao.close()