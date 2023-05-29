SELECT 
	a.codautor,
	a.nome,
	COUNT(l.cod) as quantidade_publicacoes
from autor a 
	left join livro l 
	on a.codautor = l.autor
GROUP by l.autor
ORDER by quantidade_publicacoes DESC 
LIMIT 1