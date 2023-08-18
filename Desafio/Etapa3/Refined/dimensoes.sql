CREATE VIEW dim_tmdb AS
SELECT
    tmdb.imdb_id AS id,
    tmdb."release_date" AS data_lancamento,
    tmdb.budget as orcamento,
    tmdb.popularity AS popularidade,
    tmdb.revenue as receita,
    tmdb.vote_average AS voto_media,
    tmdb.vote_count AS voto_contagem
FROM "12" AS tmdb;


CREATE VIEW dim_omdb AS
SELECT
    omdb.id id,
    omdb."titulo",
    omdb."data_de_lancamento",
    omdb."bilheteria" ,
    omdb."awards",
    omdb."avaliacao_do_imdb",
    omdb."imdbvotes",
    omdb."metascore"
FROM "13" AS omdb;


CREATE VIEW dim_movies AS
SELECT
    filmes.id,
    filmes."titulopincipal",
    filmes."anolancamento",
    filmes."notamedia",
    filmes."numerovotos",
    filmes."generoartista"
FROM "movies" AS filmes;

CREATE VIEW fato_fimes AS
SELECT
   filmes."id" as idMovies,
   tmdb."id" as idTmdb,
   omdb."id"  as idOmdb
FROM "dim_movies" AS filmes
    join "dim_omdb" as omdb on filmes."id" = omdb."id"
    join "dim_tmdb" as tmdb on filmes."id" = tmdb."id";

CREATE VIEW dim_tmdb AS
SELECT
    tmdb.imdb_id AS id,
    tmdb.release_date AS data_lancamento,
    tmdb.budget as orcamento,
    tmdb.popularity AS popularidade,
    tmdb.revenue as receita,
    tmdb.vote_average AS voto_media,
    tmdb.vote_count AS voto_contagem
FROM tmdb AS tmdb;


CREATE VIEW dim_omdb AS
SELECT
    omdb.id id,
    omdb.titulo,
    omdb.data_de_lancamento,
    omdb.bilheteria ,
    omdb.awards,
    omdb.avaliacao_do_imdb,
    omdb.imdbvotes,
    omdb.metascore
FROM omdb AS omdb;


CREATE VIEW dim_movies AS
SELECT
    filmes.id,
    filmes.titulopincipal,
    filmes.anolancamento,
    filmes.notamedia,
    filmes.numerovotos,
    filmes.generoartista
FROM movies AS filmes;

CREATE VIEW fato_fimes AS
SELECT
   filmes.id as idMovies,
   tmdb.id as idTmdb,
   omdb.id  as idOmdb
FROM dim_movies AS filmes
    join dim_omdb as omdb on filmesid = omdb.id
    join dim_tmdb as tmdb on filmes.id = tmdb.id;

