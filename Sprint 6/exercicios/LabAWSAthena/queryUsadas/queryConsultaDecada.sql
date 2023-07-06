WITH decada50 AS (
	SELECT 'Decada de 1950' AS decada,
		nome,
		SUM(total) AS total_ocorrencias
	FROM nomes
	WHERE (ano >= 1950)
		AND (ano < 1960)
	GROUP BY nome
	ORDER BY total_ocorrencias DESC
	LIMIT 3
), decada60 AS (
	SELECT 'Decada de 1960' AS decada,
		nome,
		SUM(total) AS total_ocorrencias
	FROM nomes
	WHERE (ano >= 1960)
		AND (ano < 1970)
	GROUP BY nome
	ORDER BY total_ocorrencias DESC
	LIMIT 3
), decada70 AS (
	SELECT 'Decada de 1970' AS decada,
		nome,
		SUM(total) AS total_ocorrencias
	FROM nomes
	WHERE (ano >= 1970)
		AND (ano < 1980)
	GROUP BY nome
	ORDER BY total_ocorrencias DESC
	LIMIT 3
), decada80 AS (
	SELECT 'Decada de 1980' AS decada,
		nome,
		SUM(total) AS total_ocorrencias
	FROM nomes
	WHERE (ano >= 1980)
		AND (ano < 1990)
	GROUP BY nome
	ORDER BY total_ocorrencias DESC
	LIMIT 3
), decada90 AS (
	SELECT 'Decada de 1990' AS decada,
		nome,
		SUM(total) AS total_ocorrencias
	FROM nomes
	WHERE (ano >= 1990)
		AND (ano < 2000)
	GROUP BY nome
	ORDER BY total_ocorrencias DESC
	LIMIT 3
), decada2000 AS (
	SELECT 'Decada de 2000' AS decada,
		nome,
		SUM(total) AS total_ocorrencias
	FROM nomes
	WHERE (ano >= 2000)
		AND (ano < 2010)
	GROUP BY nome
	ORDER BY total_ocorrencias DESC
	LIMIT 3
), decada2010 AS (
	SELECT 'Decada de 2010' AS decada,
		nome,
		SUM(total) AS total_ocorrencias
	FROM nomes
	WHERE (ano >= 2010)
		AND (ano < 2020)
	GROUP BY nome
	ORDER BY total_ocorrencias DESC
	LIMIT 3
)
SELECT decada,
	nome,
	total_ocorrencias
FROM decada50
UNION ALL
SELECT decada,
	nome,
	total_ocorrencias
FROM decada60
UNION ALL
SELECT decada,
	nome,
	total_ocorrencias
FROM decada70
UNION ALL
SELECT decada,
	nome,
	total_ocorrencias
FROM decada80
UNION ALL
SELECT decada,
	nome,
	total_ocorrencias
FROM decada90
UNION ALL
SELECT decada,
	nome,
	total_ocorrencias
FROM decada2000
UNION ALL
SELECT decada,
	nome,
	total_ocorrencias
FROM decada2010;