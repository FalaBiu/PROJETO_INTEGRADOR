#importar biblioteca de conexao ao banco
import sqlite3 as lite

#criar conexao banco
con = lite.connect('dados.db')

#criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE INVENTARIO (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT, LOCAL TEXT, " \
                "DESCRICAO TEXT, MARCA TEXT, DATA_DA_COMPRA DATE, VALOR_DA_COMPRA DECIMAL, SERIE TEXT, IMAGEM TEXT)")
