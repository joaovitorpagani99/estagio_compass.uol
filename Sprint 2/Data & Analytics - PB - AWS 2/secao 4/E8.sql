SELECT 
	t.cdvdd,
	t.nmvdd 
from tbvendedor t 
	left join tbvendas t2 
	on t.cdvdd = t2.cdvdd  
WHERE t2.status = 'Concluído'	
GROUP by t.cdvdd, t.nmvdd 
ORDER by COUNT(*) DESC  
limit 1