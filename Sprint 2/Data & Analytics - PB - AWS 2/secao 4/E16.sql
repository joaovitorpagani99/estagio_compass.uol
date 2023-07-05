SELECT 
	t.estado, 
	t.nmpro, 
	ROUND(AVG(t.qtd), 4) AS quantidade_media
FROM tbvendas t 
WHERE t.status = 'Concluído'
GROUP BY t.estado, t.nmpro
ORDER BY t.estado, t.nmpro;
