def lerEntradas(arquivo):
    file = open(arquivo, 'r')

    retorno = []
    for linha in file:
        retorno.append(linha.replace("\n", ""))

    file.close()

    return(retorno)


def popularBairros(bairros):
    file = open("populadorBairros.sql", 'w')

    for bairro in bairros:
        file.write("select insertbairro(\'" + bairro + "\');\n")
       
    file.close()

def main():
    bairros = lerEntradas("bairros.txt")

    print(bairros)

    popularBairros(bairros)

    print("That's all folks")
    print("Thanks =)")

    

if __name__ == "__main__":
    main()