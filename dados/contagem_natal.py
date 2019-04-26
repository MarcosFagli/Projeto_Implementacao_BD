import pandas as pd

base_dados = pd.read_excel('Planilha_Primeiro_Dia_de_MercadoFinal.xlsm', sheet_name='Base de dados', usecols="D:E")

cb = []
for i in base_dados['Topo']:
    cb.append(str(i).strip())

item = []
for i in base_dados['Unnamed: 1']:
	item.append(i)


b = list(zip(cb, item))[3:]

a = {}
for x in b:
	if x[1] not in a.keys():
		a[x[1]] = [x[0]]
	else:
		a[x[1]].append(x[0])

for y, w in a.items():
	print(y, w)

print(len(a.values()))





