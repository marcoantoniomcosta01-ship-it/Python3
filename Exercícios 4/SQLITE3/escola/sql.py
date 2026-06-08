import sqlite3

conn = sqlite3.connect("escola.db") #cria o database

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute('CREATE TABLE IF NOT EXISTS estudantes(id INTEGER PRIMERY KEY, nome TEXT, idade INTEGER)')

cursor.execute('CREATE TABLE IF NOT EXISTS diciplinas(id INTEGER PRIMARY KEY, nome_diciplina TEXT, estudante_id INTEGER, FOREIGN KEY (estudante_id) REFERENCES estudantes(id))')

conn.commit()
conn.close()