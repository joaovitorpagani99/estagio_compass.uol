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

s3_path = "s3://data-lake-paganipb/Raw/Tmdb/JSON/2023/08/07/prt-uty-nfd_part1.json"
data= glueContext.create_dynamic_frame.from_options(connection_type= 's3',
                                                               connection_options={"paths": [s3_path]},
                                                                format = 'json',
                                                               format_options={"jsonPath": "$[*]"})

data.printSchema()
df = data.toDF()

df_filtrado= df.filter(df["budget"] != 0)
df_comData = df_filtrado.withColumn("data_de_criacao", to_date(lit("2023-08-07"), "yyyy-MM-dd"))
df = df_comData.select("imdb_id","title","release_date", "budget","popularity","revenue","vote_average","vote_count", "data_de_criacao")
dynamic_frame = DynamicFrame.fromDF(df, glueContext)

glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="s3",
    connection_options={
        "path": "s3://data-lake-paganipb/Trusted/terror|misterio/2023/08/12",
        "partitionKeys": ["data_de_criacao"]
    },
    format="parquet"
)
