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

df_filtered = df.filter(df["budget"] != 0)
data_with_creation_date = df_filtered.withColumn("data_de_criacao", to_date(lit("2023-08-07"), "yyyy-MM-dd"))
df = data_with_creation_date.select("imdb_id","title","release_date", "budget","popularity","revenue","vote_average","vote_count", "data_de_criacao")
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
