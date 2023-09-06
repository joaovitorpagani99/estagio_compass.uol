import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)


omdb = glueContext.create_dynamic_frame.from_catalog('databaseomdb', '13')
df = omdb.toDF()



df_bi = df.withColumn("bilheteria", when(col("bilheteria") == "N/A", None).otherwise(col("bilheteria")))

df_bi = df_bi.withColumn("bilheteria", regexp_replace(col("bilheteria"), "[\$,]", "").cast("double"))

df_bi = df_bi.withColumn("Awards", when(col("Awards") == "N/A", None).otherwise(col("Awards")))

df_bi = df_bi.withColumn("Avaliacao do imdb", when(col("Avaliacao do imdb") == "N/A", None).otherwise(col("Avaliacao do imdb")))
df2 = df_bi.withColumn("Avaliacao do imdb", df_bi["Avaliacao do imdb"].cast("double"))
df2 = df2.withColumn("imdbVotes", when(col("imdbVotes") == "N/A", None).otherwise(col("imdbVotes")))
df2 = df2.withColumn("Metascore", when(col("Metascore") == "N/A", None).otherwise(col("Metascore")))

df2 = df2.withColumn("imdbVotes", df2["imdbVotes"].cast("double"))
df2 = df2.withColumn("Metascore", df2["Metascore"].cast("int"))
df_dt = df2.withColumn("data_de_criacao", to_date(lit("2023-08-13"), "yyyy-MM-dd"))




df = DynamicFrame.fromDF(df_dt, glueContext)

glueContext.write_dynamic_frame.from_options(
    frame=df,
    connection_type="s3",
    connection_options={
        "path": "s3://data-lake-paganipb/Trusted/terror|misterio/2023/08/13",
        "partitionKeys": ["data_de_criacao"]
    },
    format="parquet"
)
