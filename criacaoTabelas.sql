-- ---------------------------------------------------------------------
-- Integrantes do grupo
-- Juliana Karoline .......................... 594997
-- Marcos Augusto Faglioni Junior ............ 628301


-- ---------------------------------------------------------------------
-- Mapeamento do esquema relacional
-- Produto(*CodBarras, Tipo, Nome, Marca, UnidadeMedida, valorMedida)

-- InstArrecadação(*CodInst)

-- Mercado(*CodMerc, CodInst, Nome, EndCidade, EndBairro, EndRua, EndNumero)
-- CodInst Ref InstArrecadação{CodInst}

-- Bairro(*CodBairro, CodInst, Bairro)
-- CodInst Ref InstArrecadação{CodInst}

-- Custa(*CodMerc, *CodBarras, Preco)
-- CodMerc Ref Mercado{CodMerc}
-- CodBarras Ref Produto{CodBarras}

-- CampanhaArrecadaca(*CodBarras, *CodInst, *Data, Quantidade)
-- CodBarras ref Produto{CodBarras}
-- CodInst ref InstArrecadacao{CodInst}



-- ---------------------------------------------------------------------
-- Criação da database: contagem_natal 
DROP DATABASE contagem_natal;

CREATE DATABASE contagem_natal
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;


-- ---------------------------------------------------------------------
-- Exclusão e criação das tabelas
-- Tabela produto
DROP TABLE produto;

CREATE TABLE produto
(
	codBarras VARCHAR(13) PRIMARY KEY,
	tipo VARCHAR(10) NOT NULL,
	nome VARCHAR(25) NOT NULL,
	marca VARCHAR(20), 
	unidadeMedida VARCHAR(5),
	valorMedida REAL
);


-- Tabela arrecadação
DROP TABLE instArrecadacao;

CREATE TABLE instArrecadacao
(
	codInst SERIAL,
	PRIMARY KEY (codInst)
);


-- Tabela mercado
DROP TABLE mercado;

CREATE TABLE mercado
(
	codMerc SERIAL,
	codInst INT NOT NULL,
	nome VARCHAR(15) NOT NULL,
	endCidade VARCHAR(30) DEFAULT 'São Carlos',
	endBairro VARCHAR(20) NOT NULL,
	endRua VARCHAR(35),
	endNumero SMALLINT,
	
	PRIMARY KEY (codMerc),
	FOREIGN KEY (codInst) REFERENCES instArrecadacao (codInst)
);


-- Tabela Bairro
DROP TABLE bairro;	

CREATE TABLE bairro
(
	codBairro SERIAL,
	codInst INT NOT NULL,
	endCidade VARCHAR(30) DEFAULT 'São Carlos',
	endBairro VARCHAR(15) NOT NULL,
	
	PRIMARY KEY (codBairro),
	FOREIGN KEY (codInst) REFERENCES instArrecadacao (codInst)
);
	

-- Tabela custa
DROP TABLE custa;

CREATE TABLE custa
(
	codMerc INT NOT NULL,
	codBarras VARCHAR(13) NOT NULL,
	preco INT NOT NULL,

	PRIMARY KEY (codMerc, codBarras),
	FOREIGN KEY (codMerc) REFERENCES mercado (codMerc),
	FOREIGN KEY (codBarras) REFERENCES produto (codBarras)
);


-- Tabela campanhaArrecadação
DROP TABLE campanhaArrecadacao;

CREATE TABLE campanhaArrecadacao
(
	codBarras VARCHAR(13) NOT NULL,
	codInst INT NOT NULL,
	data DATE NOT NULL DEFAULT CURRENT_DATE,
	quantidade INT NOT NULL,

	PRIMARY KEY (codBarras, codInst, data),
	FOREIGN KEY (codInst) REFERENCES instArrecadacao (codInst),
	FOREIGN KEY (codBarras) REFERENCES produto (codBarras)
);


-- ---------------------------------------------------------------------
-- Inserções
-- Inserindo produtos
-- File populadoresProdutos.sql

-- Inserindo mercado
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Carrefour', 'Vila Costa do Sol', 'Av. São Carlos');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Jaú Serve', 'Vila Marina', 'Av. São Carlos');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Savegnago', 'Parque Santa Mônica', 'Av. Dr. Francisco Pereira Lopes');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Jaú Serve', 'Centro', 'Rua Padre Teixeira');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Dia', 'Vila Faria', 'Av. São Carlos');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Cogeb', 'Parque Santa Mônica', 'Rua 15 de novembro');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Atacadão', 'São Carlos 1', 'Rua Miguel Petroni');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Extra', 'Centro', 'Rua São Sebastião');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Jaú Serve', 'Centro', 'Rua Visc. de Inhaúma');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Marini', 'Jd. Mercedes', 'Rua Maj. Manoel Antônio de Mattos');
INSERT INTO mercado (nome, EndBairro, EndRua) VALUES ('Sempre Vale', 'Centro', 'Rua Bento Carlos');


-- Inserindo bairros
-- File populadoresBairros.sql


-- Inserindo Campanha de arrecadação
-- File popularCampArrecadacao.sql

-- ---------------------------------------------------------------------
-- Criação de Triggers
-- Trigger para a geração de código de instituição
