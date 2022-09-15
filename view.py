# importacao de bibliotecas
import sqlite3 as lite
from datetime import datetime

# conexao com banco
con = lite.connect('dados.db')

# Função para inserir registro no inventário


def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO INVENTARIO (NOME, LOCAL, DESCRICAO, MARCA, DATA_DA_COMPRA, " \
                "VALOR_DA_COMPRA, SERIE, IMAGEM) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

# funcao para deletar um registro/LINHA/TUPLA


def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM INVENTARIO WHERE ID=?"
        cur.execute(query, i)

# funcao para ATUALIZAR um registro/LINHA/TUPLA


def atualizar_form(i):
    with con:
         cur = con.cursor()
         query = "UPDATE INVENTARIO SET NOME=?, LOCAL=?, DESCRICAO=?, MARCA=?," \
                 "DATA_DA_COMPRA=?, VALOR_DA_COMPRA=?, SERIE=?, IMAGEM=? WHERE ID=?",
         cur.execute(query, i)

# funcao para ver todos os itens do inventário
def ver_form():
    lista_itens = []
    with con:
         cur = con.cursor()
         cur.execute("SELECT * FROM INVENTARIO ORDER BY NOME")
         rows = cur.fetchall()
         for row in rows:
            lista_itens.append(row)
    return lista_itens

# funcao para ver apenas um item do inventário
def ver_iten(id):
    lista_itens = []
    with con:
         cur = con.cursor()
         cur.execute("SELECT * FROM INVENTARIO WHERE ID=?",(id))
         rows = cur.fetchall()
         for row in rows:
             lista_itens.append(row)
    return lista_itens