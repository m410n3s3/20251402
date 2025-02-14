import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('meu_banco_de_dados.db')

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')
usu_1 = input()
# Inserir dados
cursor.execute(f"INSERT INTO usuarios (nome, idade) VALUES ('{usu_1}', 30)")
cursor.execute(f"INSERT INTO usuarios (nome, idade) VALUES ('Bob', 25)")

# Salvar (commit) as mudanças
conn.commit()

# Consultar dados
cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

# Fechar a conexão
conn.close()