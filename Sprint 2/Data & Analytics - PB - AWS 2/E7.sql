SELECT 
	a.nome 
FROM autor a 
	left join livro l 
	on a.codautor = l.autor 
WHERE l.cod  IS NULL 
ORDER BY a.nome 