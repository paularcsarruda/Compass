-- View Dimensão Ator
CREATE VIEW dim_atores AS
SELECT
    imdb_id,
    atores
FROM
    Movie_omdb;

-- View Dimensão Premiacao
CREATE VIEW dim_premiacao AS
SELECT
    imdb_id,
    titulo,
    premiacoes
FROM
    Movie_omdb;

-- View Dimensão Faturamento
CREATE VIEW dim_faturamento AS
SELECT DISTINCT
    id,
    faturamento,
    orcamento
FROM
    Movie_tmdb;

-- View Dimensão Popularidade
CREATE VIEW dim_popularidade AS
SELECT DISTINCT
    id,
    notamedia,
    numero_votos
FROM
    Movie_csv;

-- View Fato Locação
CREATE VIEW fato_Movie AS
SELECT
    imdb_id,
    faturamento,
    ano_lancamento,
    tempo_minutos
FROM
    Movie_omdb;

-- Adicionando chaves primárias e estrangeiras nas tabelas

-- Tabela Movie_csv
ALTER TABLE Movie_csv
ADD CONSTRAINT pk_Movie_csv PRIMARY KEY (id);

-- Tabela Movie_tmdb
ALTER TABLE Movie_tmdb
ADD CONSTRAINT pk_Movie_tmdb PRIMARY KEY (id);

-- Tabela Movie_omdb
ALTER TABLE Movie_omdb
ADD CONSTRAINT pk_Movie_omdb PRIMARY KEY (titulo);

ALTER TABLE Movie_omdb
ADD CONSTRAINT fk_Movie_omdb_titulo FOREIGN KEY (titulo) REFERENCES Movie_tmdb(titulo);

ALTER TABLE Movie_omdb
ADD CONSTRAINT fk_Movie_omdb_imdb_id FOREIGN KEY (imdb_id) REFERENCES Movie_tmdb(id);
