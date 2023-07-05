SELECT 
	t.cdcli,
	t.nmcli, 
	SUM(t.qtd  * t.vrunt) AS gasto
FROM tbvendas t 
	WHERE t.status  = 'Concluído'
GROUP BY t.cdcli , t.nmcli
ORDER BY gasto DESC
LIMIT 1;