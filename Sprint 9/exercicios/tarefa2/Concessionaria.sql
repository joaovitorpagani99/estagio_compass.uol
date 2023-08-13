create table  dim_Carro(
	idCarro int primary key,
    kmCarro int,
    classiCarro varchar(100),
    marcaCarro varchar(100),
	modeloCarro varchar(100),
    anoCarro int
);

create table dim_vendedor(
	idVendedor int primary key,
    nomeVendedor varchar(100),
    estado varchar(100),
	sexoVendedor varchar(100)
);

create table dim_combustivel(
	idCombustivel int primary key,
    tipoCombustivel varchar(100)
);

create table dim_cliente(
	idCliente int primary key,
    nomeCliente varchar(100),
    cidade varchar(100),
    estado varchar(100),
    pais varchar(100)
);

create table fato_locacao(
	idLocacao int primary key,
    idCliente int,
    idCarro int,
    idVendedor int,
    idCombustivel int,
    dataLocacao date,
    horaLocacao time,
    qtdDiaria int,
    vlrDiaria int,
    dataEntrega date,
    horaEntrega time,
    foreign key(idCliente) references dim_cliente(idCliente),
    foreign key(idCarro) references dim_carro(idCarro),
    foreign key(idVendedor) references dim_vendedor(idVendedor),
    foreign key(idCombustivel) references dim_combustivel(idCombustivel)
);

