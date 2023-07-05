SELECT 
	cdpro,
	nmpro 
from tbvendas t 
WHERE 
status = 'Concluído' AND 
t.dtven  BETWEEN '2014-02-03'and '2018-02-02'
GROUP BY cdpro , nmpro 
limit 1