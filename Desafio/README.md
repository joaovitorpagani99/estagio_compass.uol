# Etapas

1. ...
[Etapa I](Etapa1)

1. ...
[Etapa II](Etapa2)

1. ...
[Etapa III](Etapa3)


## Etapa 1

Nesta etapa, descreverei o processo que segui para realizar o upload de um arquivo CSV para o GitHub, utilizando a AWS para a transferência do arquivo e o Docker para gerenciar o processo.

Primeiramente, foi necessário configurar uma chave de acesso na AWS para permitir a interação entre meu PC local e a plataforma em nuvem. Isso envolveu a criação de credenciais de acesso para autenticação.

Com a chave de acesso configurada, procedi ao upload do arquivo CSV para a AWS. Isso foi feito utilizando a biblioteca Boto e seguindo a documentação oficial. Essa etapa garantiu que o arquivo estivesse disponível na nuvem.

Para automatizar o processo e garantir a portabilidade, decidi utilizar o Docker. Com o Dockerfile, criei um contêiner que continha o script necessário para transferir o arquivo da AWS para o GitHub. Isso facilitou a execução do processo em diferentes ambientes.

Para proteger as chaves de acesso e informações sensíveis, recorri ao Docker Compose. Com essa ferramenta, pude definir variáveis de ambiente separadas para as chaves de acesso, garantindo que elas não fossem expostas no código-fonte.

Com esse fluxo, consegui realizar todo o processo de upload do arquivo CSV para o GitHub de forma segura e eficiente, aproveitando os recursos da AWS, Docker e Docker Compose.

## Etapa 2

Nesta etapa, vou detalhar o processo pelo qual coletei e filtrei dados de filmes de duas APIs, TMDB e OMDB, e como armazenei esses dados na AWS S3.

Inicialmente, obtive dados de filmes de duas fontes: TMDB e OMDB. A coleta de dados dessas APIs me proporcionou informações valiosas sobre filmes, como título, gênero, ano de lançamento e bilheteria. Embora minha intenção fosse usar apenas a API TMDB, optei por também utilizar o OMDB devido à coluna de bilheteria, considerada relevante.

Após analisar as APis, meu próximo passo foi realizar agrupamentos e filtragens. Primeiro, agrupei os dados por ID, permitindo uma organização mais eficiente. Em seguida, fiz um filtro para selecionar apenas os filmes com gêneros de terror e mistério, visto que esses eram de interesse para minha análise. Além disso, fiz outro filtro para limitar os filmes entre os anos de 2015 e 2020, considerando as restrições de requisições diárias da API OMDB.

```spark
df['anoLancamento'] = pd.to_numeric(df['anoLancamento'],errors='coerce')
df_filtrados = df[(df['anoLancamento'] >= 2015) & (df['anoLancamento'] <= 2020) & (df['genero'].str.contains('Horror|Mystery', case=False))]
df_agrupados = df_filtrados.groupby('id')
```

Com os filtros aplicados, passei a iterar sobre os dados no arquivo CSV. Para cada entrada, utilizei o ID para fazer requisições às APIs TMDB e OMDB, buscando informações detalhadas sobre cada filme. Após cada requisição, os dados relevantes foram armazenados em uma estrutura de dados.

Uma vez que as informações dos filmes foram coletadas e organizadas, procedi à conversão dos dados para o formato JSON. Limitando o tamanho do arquivo em até 10 MB, os dados foram estruturados em formato JSON. Em seguida, os dados foram armazenados na camada "raw/json/dataAtual" no serviço de armazenamento da AWS, o S3.

```
s3_saida = f'Raw/Tmdb/JSON/{data_atual}/prt-uty-nfd_par{idx + 1}.json'

```

Esse fluxo permitiu que eu coletasse e organizasse informações de filmes de forma eficaz, aplicando filtros relevantes antes de armazenar os dados na AWS S3. 

## Etapa 3

Aqui descreverei as etapas envolvidas na transformação e modelagem de dados, incluindo a carga histórica, para criar um modelo multidimensional visando a análise através do QuickSight. Utilizei serviços como AWS Glue para unir e modelar os dados.

Após coletar os dados de diferentes fontes e aplicar filtros, a etapa seguinte consistiu em padronizar os dados e armazená-los na camada "trusted" no formato Parquet. Dois jobs foram criados para essa finalidade:

O primeiro job foi dedicado à carga histórica. Nesse processo, os dados foram transformados em formato Parquet. A prioridade aqui era estabelecer um padrão para os dados, permitindo uma base sólida para análises futuras.

O segundo job focou na transformação da carga de dados. Diferentes fontes, como as APIs TMDB e OMDB, foram unificadas e padronizadas em formato Parquet. Isso facilitou a análise e modelagem posterior.

Os dados padronizados e armazenados na camada "trusted" foram levados para a camada "Refined". Aqui, o foco estava na modelagem dos dados para análise multidimensional. Isso envolveu a criação de um modelo de dados que atendesse às necessidades específicas de análise.

Para unificar as diversas fontes de dados, utilizei o serviço AWS Glue. Esse serviço foi empregado para criar "views" dos dados provenientes das APIs TMDB e OMDB, bem como da carga histórica. Essas "views" foram modeladas de maneira a facilitar a análise.

Após a modelagem dos dados usando o Glue, os dados estavam prontos para serem utilizados no QuickSight. Esse serviço de visualização e análise de dados permitiu explorar os dados modelados e criar insights a partir do modelo multidimensional criado.

Esse fluxo de trabalho permitiu a transformação, modelagem e preparação de dados para análise multidimensional, possibilitando a utilização eficiente dos dados nas análises conduzidas no QuickSight.
