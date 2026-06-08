import sqlite3

lista = [("iphone", 4000), ('Tv', 2500), ('Microondas', 250)]
def create():
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY , nome TEXT, preço INTEGER)")
    conn.commit()
    conn.close()

def insert():
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO produtos (nome, preço) VALUES (?, ?)', (lista))
    conn.commit()
    conn.close()

def select():
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
    

create()
insert()
select()
