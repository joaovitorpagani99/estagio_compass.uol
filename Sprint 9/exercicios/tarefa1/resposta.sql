CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(100),
    estadoCliente VARCHAR(100),
    paisCliente VARCHAR(100)
);

CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(100),
    marcaCarro VARCHAR(100),
    modeloCarro VARCHAR(100),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);

CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(100)
);

CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    estadoVendedor VARCHAR(100),
    sexoVendedor INT
);

CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria INT,
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INT,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);
