SELECT
    t.cdpro,
    t.nmcanalvendas,
    t.nmpro,
    SUM(t.qtd) AS quantidade_vendas
FROM tbvendas t 
WHERE
    t.status = 'Concluído'
    AND (t.nmcanalvendas = 'Ecommerce' OR t.nmcanalvendas = 'Matriz')
GROUP BY
    t.cdpro, t.nmcanalvendas, t.nmpro
ORDER BY
    quantidade_vendas ASC
LIMIT 10;
