CREATE view cliente as
select 
	idCliente as id,
	nomeCliente as nome,
	cidadeCliente as cidade,
	estadoCliente as estado,
	paisCliente as pais
from tb_locacao t1;

CREATE view combustivel as
select
	idCombustivel as id,
	tipoCombustivel as tipoCombustivel
from tb_locacao tl ;

CREATE view veiculo as
select 
	idCarro as id,
	kmCarro as kmCarro,
	classiCarro as classi,
	marcaCarro as marca,
	modeloCarro as modelo,
	idCombustivel,
from tb_locacao tl ;

CREATE view vendedor as 
select 
	idVendedor as id,
	nomeVendedor as nome,
	estadoVendedor as estado,
	sexoVendedor as genero
from tb_locacao tl 

CREATE VIEW Locacao AS
SELECT 
    idLocacao , 
    idCliente, 
    idCarro, 
    dataLocacao, 
    horaLocacao, 
    qtdDiaria, 
    vlrDiaria, 
    dataEntrega, 
    horaEntrega, 
    idVendedor
FROM tb_locacao;
