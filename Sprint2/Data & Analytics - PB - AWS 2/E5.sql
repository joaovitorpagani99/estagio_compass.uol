SELECT DISTINCT a.nome 
from autor a 
	left join livro l 
		on a.codautor = l.autor
	left JOIN editora e 
		on l.editora = e.codeditora 
	LEFT JOIN endereco e2 
		on e.endereco = e2.codendereco 
WHERE UPPER(e2.estado) NOT IN ('RIO GRANDE DO SUL', 'SANTA CATARINA', 'PARANÁ')
GROUP by a.nome 
ORDER BY a.nome 