import random

produtos = # Lista de listas contendo o nome dos produtos, tipo, códigos de barras, marca, tipo de unidade, valor da unidade


file = open("populadorProdutos.sql", 'w')

for produto in produtos:
	file.write("INSERT INTO produto VALUES (\'" + str(produto[2]) + "\',\'" + produto[1] + "\',\'" + produto[0] + "\',\'"   + produto[3] + "\',\'" + produto[4] + "\'," + str(produto[5]) + ");\n")

file.close()

