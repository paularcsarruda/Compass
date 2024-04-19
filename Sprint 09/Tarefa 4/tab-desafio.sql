-- tabela CSV
CREATE TABLE Movie_csv (
	id VARCHAR PRIMARY KEY,
	titulo_original VARCHAR,
	ano_lancamento DATE,
	tempo_minutos DOUBLE,
	genero VARCHAR,
	notamedia DOUBLE,
	numero_votos INT
);

-- tabela TMDB
CREATE TABLE Movie_tmdb (
	id BIGINT PRIMARY KEY,
	titulo VARCHAR,
	votos BIGINT,
	media_de_votos DOUBLE,
	popularidade DOUBLE,
	orcamento BIGINT,
	faturamento BIGINT
);

-- tabela OMDB (esse JOB será criado posteriormente)
CREATE TABLE Movie_omdb (
	titulo VARCHAR PRIMARY KEY,
	ano_lancamento DATE,
	imdb_id DOUBLE,
	atores VARCHAR,
	imdb_votos DOUBLE,
	imbd_classificacao DOUBLE,
	premiacoes VARCHAR,
	pais VARCHAR,
	idioma VARCHAR,
	genero VARCHAR,
	tempo_minutos INT,
	Faturamento DOUBLE,
	FOREIGN KEY (titulo) REFERENCES Movie_tmdb(titulo),
	FOREIGN KEY (imdb_id) REFERENCES Movie_tmdb(id)
);
