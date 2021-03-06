import pandas as pd

def detectarMedidaeUnidade(string):
    listUnit = ["LATA", 'KG', 'UN', "ML", "L", "G"]

    for i in listUnit:
        if(i in string[len(string)-5:]):
            indice = string.find(i, len(string)-5)

            aux = 1

            while(string[indice-aux] in ['0','1','2','3','4','5','6','7','8','9','.',',',' ']):
                aux += 1

            return(float(string[indice-aux+1:indice].replace(',','.')), i, string[:indice-aux+1])

    return (-1, '', string)

def main():
    base_dados = pd.read_excel('Planilha_Primeiro_Dia_de_MercadoFinal.xlsm', sheet_name='Base de dados', usecols="D:E")

    cb = []
    for i in base_dados['Topo']:
        cb.append(str(i).strip())

    item = []
    count = 2
    produtos = base_dados['Unnamed: 4']
    for j in produtos[2:]:
        j = j.upper()
        j = j.replace("(","")
        j = j.replace(")","")

        retorno = detectarMedidaeUnidade(j)

        temp =[]
        temp.append(retorno[2])     #Nome do produto
        temp.append(retorno[1])     #Tipo da unidade
        temp.append(retorno[0])     #Valor unidade
        temp.append(cb[count])      #Codigo de barras
        count += 1

        if(len(temp[3]) == 13):
            item.append(temp)

    del(item[0])

    file = open('DadosNormalizados.txt', 'w')
    for i in item:
        file.write(i[0] + "," + i[1] + "," + str(i[2]) + "," + i[3] + "\n")
    file.close

    print("That's all folks")
    print("Thanks =)")


if __name__ == "__main__":
    main()