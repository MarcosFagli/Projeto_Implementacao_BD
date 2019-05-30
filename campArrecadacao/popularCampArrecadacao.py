import random

def lerEntradas(arquivo):
    file = open(arquivo, 'r')

    retorno = []
    for linha in file:
        retorno.append(linha.replace("\n","").split(","))

    file.close()

    return(retorno)


def popularProdutos(produtos):
    file = open("popularCampArrecadacao.sql", 'w')

    for i in range(0,7000):
        file.write("INSERT INTO campanhaArrecadacao (codBarras, codInst, quantidade) VALUES (\'" + produtos[random.randint(0,len(produtos)-1)][3] + "\'," + str(random.randint(0,25)) + "," + str(random.randint(0,5)) + ");\n")
       
    file.close()


def main():
    produtos = lerEntradas("DadosNormalizados.txt")

    popularProdutos(produtos)

    print("That's all folks")
    print("Thanks =)")

    

if __name__ == "__main__":
    main()