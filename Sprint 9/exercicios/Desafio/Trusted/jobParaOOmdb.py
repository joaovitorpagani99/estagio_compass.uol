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

dyf = glueContext.create_dynamic_frame.from_catalog(database='database_name', table_name='table_name')
dyf.printSchema()

df = dyf.toDF()
df.show()

s3_path = "s3://data-lake-paganipb/Raw/Omdb/JSON/2023/08/13/bf-uet-dsa.json"
s3_path2 = "s3://data-lake-paganipb/Raw/Omdb/JSON/2023/08/13/cvf-uet-lkj.json"
s3_path3 = "s3://data-lake-paganipb/Raw/Omdb/JSON/2023/08/13/hjk-fgh-rty.json"
s3_path4 = "s3://data-lake-paganipb/Raw/Omdb/JSON/2023/08/13/idf-uet-tyu.json"
s3_path5 = "s3://data-lake-paganipb/Raw/Omdb/JSON/2023/08/13/prt-uty-nfd.json"
s3_path6 = "s3://data-lake-paganipb/Raw/Omdb/JSON/2023/08/13/qwe-uet-nmb.json"
data= glueContext.create_dynamic_frame.from_options(connection_type= 's3',connection_options={"paths": [s3_path]}, format = 'json')
data2= glueContext.create_dynamic_frame.from_options(connection_type= 's3',connection_options={"paths": [s3_path2]}, format = 'json')
data3= glueContext.create_dynamic_frame.from_options(connection_type= 's3',connection_options={"paths": [s3_path3]}, format = 'json')
data4= glueContext.create_dynamic_frame.from_options(connection_type= 's3',connection_options={"paths": [s3_path4]}, format = 'json')
data5= glueContext.create_dynamic_frame.from_options(connection_type= 's3',connection_options={"paths": [s3_path5]}, format = 'json')
data6= glueContext.create_dynamic_frame.from_options(connection_type= 's3',connection_options={"paths": [s3_path6]}, format = 'json')

data.toDF().show(1000)

merged_data = data.union(data).union(data2).union(data3).union(data4).union(data5).union(data6)

from pyspark.sql.functions import lit, to_date
data_date = merged_data.withColumn("data_de_criacao", to_date(lit("2023-08-13"), "yyyy-MM-dd"))

from awsglue.dynamicframe import DynamicFrame


glueContext.write_dynamic_frame.from_options(
    frame=data_date,
    connection_type="s3",
    connection_options={
        "path": "s3://data-lake-paganipb/Trusted/terror|misterio/2023/08/13",
        "partitionKeys": ["data_de_criacao"]
    },
    format="parquet"
)
