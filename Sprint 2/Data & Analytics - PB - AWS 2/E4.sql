SELECT 
    a.nome,
	a.codautor,
	a.nascimento,
	count(l.cod) as quantidade
from autor a
    left join livro l 
	on a.codautor  = l.autor  
GROUP by a.nome, a.nome, a.nascimento
ORDER by a.nome  