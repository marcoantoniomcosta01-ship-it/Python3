import sqlite3

conexao = sqlite3.connect('escola.db')

cursor = conexao.cursor()

cursor.execute('UPDATE estudantes SET nome = ? WHERE idade = ?', ('leandro', 25))

conexao.commit()
conexao.close()