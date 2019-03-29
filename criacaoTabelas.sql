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
	codBarras VARCHAR2(13) PRIMARY KEY,
	tipo VARCHAR2(10) NOT NULL,
	nome VARCHAR2(25) NOT NULL,
	marca VARCHAR2(20), 
	unidadeMedida VARCHAR2(5) NOT NULL,
	valorMedida DOUBLE NOT NULL
);

CREATE TABLE instArrecadacao
(
	codInst INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (codInst)
);

CREATE TABLE mercado
(
	codMerc INT NOT NULL AUTO_INCREMENT,
	codInst INT NOT NULL,
	nome VARCHAR2(15) NOT NULL,
	endCidade VARCHAR2(30) NOT NULL,
	endBairro VARCHAR2(15) NOT NULL,
	endRua VARCHAR2(30),
	endNumero SMALLINT,
	
	PRIMARY KEY (codMerc),
	FOREIGN KEY (codInst)
);

	
	

	
