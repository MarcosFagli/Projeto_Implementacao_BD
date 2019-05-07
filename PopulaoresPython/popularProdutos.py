import random

def lerEntradas(arquivo):
    file = open(arquivo, 'r')

    retorno = []
    for linha in file:
        retorno.append(linha.replace("\n","").split(","))

    file.close()

    return(retorno)

def encontrarTipo(nome, alimentos, higiene):   
    alimentos = alimentos.upper()
    higiene = higiene.upper()

    if(alimentos.find(nome) != -1):
        return("Alimento")
    elif(higiene.find(nome) != -1):
        return("Higiene")
    else:
        while(True):
            temp = input("Qual categoria " + nome + " se encaixa ")
            if(temp == 'a' or temp =='h'):
                break

        if temp == 'a':
            return("Alimento")
        else:
            return("Higiene")


def popularProdutos(produto, alimentos, higiene):
    file = open("populadorProdutos.sql", 'w')

    for item in produto:
        if(item[2] == '-1'):
            file.write("INSERT INTO produto (codBarras, tipo, nome) VALUES (\'" + item[3] + "\',\'" + encontrarTipo(item[0], alimentos, higiene) + "\',\'" + item[0] + "\');\n")
        else:
            file.write("INSERT INTO produto (codBarras, tipo, nome, unidadeMedida, valorMedida) VALUES (\'" + item[3] + "\',\'" + encontrarTipo(item[0], alimentos, higiene) + "\',\'" + item[0] + "\',\'" + item[1] + "\',\'" + item[2] +  "\');\n")

    file.close()

def main():
    produtos = lerEntradas("DadosNormalizados.txt")

    fileAlimentos = open("alimentos.txt", 'r')
    fileHigiene = open("higiene.txt", 'r')

    alimentos = fileAlimentos.read()
    higiene = fileHigiene.read()

    fileAlimentos.close()
    fileHigiene.close()

    popularProdutos(produtos, alimentos, higiene)

    print("That's all folks")
    print("Thanks =)")

    

if __name__ == "__main__":
    main()