import sqlite3

conexao = sqlite3.connect('escola.db')

cursor = conexao.cursor()

cursor.execute('INSERT INTO diciplinas (estudante_id, nome_diciplina) VALUES (?, ?)', (1, 'Portugues'))

conexao.commit()
conexao.close()