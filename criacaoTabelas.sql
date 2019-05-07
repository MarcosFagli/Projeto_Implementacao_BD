-- Database: contagem_natal

-- DROP DATABASE contagem_natal;

CREATE DATABASE contagem_natal
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;


CREATE TABLE produto
(
	codBarras VARCHAR(13) PRIMARY KEY,
	tipo VARCHAR(10) NOT NULL,
	nome VARCHAR(25) NOT NULL,
	marca VARCHAR(20), 
	unidadeMedida VARCHAR(5),
	valorMedida REAL
);

CREATE TABLE instArrecadacao
(
	codInst SERIAL,
	PRIMARY KEY (codInst)
);

CREATE TABLE mercado
(
	codMerc SERIAL,
	codInst INT NOT NULL,
	nome VARCHAR(15) NOT NULL,
	endCidade VARCHAR(30) NOT NULL,
	endBairro VARCHAR(15) NOT NULL,
	endRua VARCHAR(30),
	endNumero SMALLINT,
	
	PRIMARY KEY (codMerc),
	FOREIGN KEY (codInst) REFERENCES instArrecadacao (codInst)
);

	
CREATE TABLE bairro
(
	codBairro SERIAL,
	codInst INT NOT NULL,
	endCidade VARCHAR(30) NOT NULL,
	endBairro VARCHAR(15) NOT NULL,
	
	PRIMARY KEY (codBairro),
	FOREIGN KEY (codInst) REFERENCES instArrecadacao (codInst)
);
	

CREATE TABLE custa
(
	codMerc INT NOT NULL,
	codBarras VARCHAR(13) NOT NULL,
	preco INT NOT NULL,

	PRIMARY KEY (codMerc, codBarras),
	FOREIGN KEY (codMerc) REFERENCES mercado (codMerc),
	FOREIGN KEY (codBarras) REFERENCES produto (codBarras)
);


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