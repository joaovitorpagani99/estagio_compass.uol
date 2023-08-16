%idle_timeout 60
%glue_version 3.0
%worker_type G.1X
%number_of_workers 2

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

tabela3 = glueContext.create_dynamic_frame.from_catalog('desafio-database', 'movies')
table1 = glueContext.create_dynamic_frame.from_catalog("desafio-database", "12")
table2 = glueContext.create_dynamic_frame.from_catalog("desafio-database", "13")

tabelaFiltrada = Join.apply(frame1=tabela3, frame2=table2, keys1=["id"], keys2=["id"])
tabela_final = Join.apply(frame1=table1, frame2=tabelaFiltrada, keys1=["id"], keys2=["id"])

df_final = tabela_final.toDF()
df = df_final_sem_duplicatas.select("imdb_id","titulo","imdbVotes", "vote_average","popularity","Metascore",
                                    "avaliacao_do_imdb","vote_count", "numeroVotos","genero","nomeArtista",
                                    "anoLancamento","revenue","Awards","bilheteria","budget")

df_final_sem_duplicatas = df_final.dropDuplicates(["id"])
df = DynamicFrame.fromDF(df, glueContext)

glueContext.write_dynamic_frame.from_options(
    frame=df,
    connection_type="s3",
    connection_options={
        "path": "s3://data-lake-paganipb/Refined/2023/08/14"
    },
    format="parquet"
)