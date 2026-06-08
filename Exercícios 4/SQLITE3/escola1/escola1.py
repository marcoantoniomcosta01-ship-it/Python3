import sqlite3

def table_estudantes():
    conn = sqlite3.connect("escola1.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS estudantes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER)")
    conn.commit()
    conn.close()

def table_diciplinas():
    conn = sqlite3.connect("escola1.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS diciplinas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, nome_diciplina TEXT, estudante_id INTEGER, FOREIGN KEY (estudante_id) REFERENCES estudantes(id))")
    conn.commit()
    conn.close()

def inserir_estudantes():
    conn = sqlite3.connect("escola1.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estudantes (nome, idade) VALUES (?, ?)', ('marco', 34))
    conn.commit()
    conn.close()

def inserir_diciplina():
    conn = sqlite3.connect("escola1.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO diciplinas (nome_diciplina, estudante_id) VALUES (?, ?)', ('matematica', 1))
    conn.commit()
    conn.close()

def selecionar_estudantes():
    conn = sqlite3.connect("escola1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudantes")
    conn.commit()
    estudantes = cursor.fetchall()
    for estudante in estudantes:
        print(estudante)
    conn.close()

def selecionar_diciplina():
    conn = sqlite3.connect("escola1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT diciplinas.id, estudantes.nome, diciplinas.nome_diciplina FROM diciplinas JOIN estudantes ON diciplinas.estudante_id = estudantes.id")
    conn.commit()
    diciplinas = cursor.fetchall()
    for diciplina in diciplinas:
        print(diciplina)
    conn.close()

selecionar_estudantes()
selecionar_diciplina()


