SELECT 
	COUNT(l.editora) as quantidade,
	e.nome,
	endereco.estado,
	endereco.cidade
FROM livro l 
left JOIN editora e
  	ON l.editora  = e.codeditora 
left  JOIN endereco
	on endereco.codendereco  = e.endereco 
GROUP by nome
ORDER by quantidade DESC 
LIMIT 5