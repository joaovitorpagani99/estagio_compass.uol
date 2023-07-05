select 
    estado, round(avg(qtd*vrunt),2) as gastomedio
from tbvendas
    WHERE status = 'Concluído'
group by estado
order by gastomedio desc