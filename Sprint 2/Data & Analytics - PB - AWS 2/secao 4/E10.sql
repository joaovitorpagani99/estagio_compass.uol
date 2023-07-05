SELECT 
	t.nmvdd as vendedor, 
	SUM(t2.qtd  * t2.vrunt) AS valor_total_vendas, 
	round(SUM(t2.qtd * t2.vrunt * t.perccomissao  / 100.00), 2) AS comissao
	FROM tbvendedor t 
		Left JOIN tbvendas t2  
		ON t.cdvdd  = t2.cdvdd 
WHERE t2.status  = 'Concluído'
GROUP BY t.cdvdd 
ORDER BY comissao DESC