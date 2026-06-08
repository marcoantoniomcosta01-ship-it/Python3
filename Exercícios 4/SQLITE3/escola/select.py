import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM diciplinas')

conexao.commit()

diciplinas = cursor.fetchall()
for diciplina in diciplinas:
    print(diciplina)

conexao.close()