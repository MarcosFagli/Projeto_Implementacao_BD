# Contagem Operacao Natal

Projeto semestral da disciplina Projeto e implementação de banco de dados para o projeto de extensão Operação Natal na Universidade Federal de São Carlos - SP - Brasil

## Orientação

Projeto e Disciplina orientada pela Professora Doutora Marcela Xavier: https://bv.fapesp.br/pt/pesquisador/33880/marcela-xavier-ribeiro/

## Programas e instalação

Este projeto foi realizado, executado e testado no linux Mint 4.15 x64 e linux ubuntu 4.18 x64 

### TerraER

An Academic Tool for Entity-Relationship (ER) models
"An open-source modeling tool designed to support students in the creation of ER models that reflect exactly the data modeling concepts learned in the classroom."
Donwload disponível em:

```
http://www.terraer.com.br/
```

Uma vez realizado o download através do link acima, basta executar no terminal com o seguinte comando:

```
java -jar TerraER.13.jar
```

### PostgreSQL

O SGBD (sistema gerenciador de banco de dados) utilizado na disciplina é o PostgreSQL.
Instruções para download e execução podem ser encontrados no seguinte link:

```
https://www.postgresql.org/download/
```

### Pandas

In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license. The name is derived from the term "panel data", an econometrics term for data sets that include observations over multiple time periods for the same individuals.

Fonte: https://en.wikipedia.org/wiki/Pandas_(software)

Esta biblioteca é utilizada para separar os dados do excel na qual foram fornecidos os dados utilizados para os produtos.

Para a instalação no terminal python, basta executar (este comando já deve baixar ou atualizar a biblioteca xlrd)

```
sudo -H pip3 install -- upgrade pandas
```

Um método alternativo, sem a utilização do sudo (não funcionou no nosso, mas ta ai, segundo a mãe internet):

```
pip3 install pandas --user
```

... e neste caso, instalar a dependencia xlrd

```
pip3 install xlrd
```


Qualquer dúvida, contate os colaboradores deste projeto :)


## Descrição do projeto

A partir de uma problematica, detectada em um projeto de extensão da universidade, é proposto o seguinte sistema. O projeto Operação Natal, busca arrecadar alimentos não perecivéis, produtos de limpeza e produtos de higiene, para doação em entidades de caridades em São Carlos - SP. Atualmente é utilizado uma tabela excel para contabilidade da quantidade (em Kg) dos produtos arrecadados. Ainda, no sistema atual, ocorre uma distorção dos resultados, pois determinados produtos são caros e leves, assim, há distorções (em geral, para menos) no resultado final. 
Tendo este em vista, o grupo propõe uma aplicação que contabilize a quantidade de produtos arrecadados. O aplicativo deve separar automaticamente o tipo do produto, assim oferencendo a opção viavel para o mesmo, de massa, unidade, volume, ou o que for aplicavel. Ainda o sistema deve armazenar a unidade onde foi realizada a operação (o supermercado ou bairro que foi coletado, afim de levantamento financeiro das doações).
Deve ser gerado relatorios contendo valor de mercado, quantidade de produtos, tipos de produtos, peso total arrecadado,  quantidade em cada categoria.

Como o projeto é voltado para a disciplina de Banco de Dados, logo, neste ambiente será armazenado o diagrama entidade relacional, o mapeamento conceitual e os códigos .sql para criação do banco de dados.
Ainda, será utilizado o banco de dados POSTGRES, com a linguagem python e front-end ainda a ser definido.

## DEER - Diagrama de entidade relacionamento extendido

No arquivo DEER.xml, é possível visualizar o diagrama que será seguido para este projeto. O arquivo pode ser aberto pelo programa TerraER

## Esquema Lógico

O esquema lógico é o mapeamento do DEER para iniciar e facilitar a criação das tabelas no banco de dados. No arquivo EsquemaLogico.txt é possivel visualizar este mapeamento (arquivo .txt).


Teste