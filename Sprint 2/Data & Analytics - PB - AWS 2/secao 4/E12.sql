SELECT 
	t.cddep, 
	t.nmdep, 
	t.dtnasc, 
	SUM(t3.qtd  * t3.vrunt) AS valor_total_vendas
	FROM tbdependente t 
		JOIN tbvendedor t2  
			ON t.cdvdd  = t2.cdvdd 
		JOIN tbvendas t3  
			ON t2.cdvdd  = t3.cdvdd 
WHERE t3.status = 'Concluído'
GROUP BY t.cddep, t.nmdep, t.dtnasc
	HAVING valor_total_vendas > 0
ORDER BY valor_total_vendas ASC
LIMIT 1;