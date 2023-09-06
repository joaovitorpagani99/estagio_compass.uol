import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)	

job.init(args['JOB_NAME'], args)
source_file = "s3://data-lake-paganipb/Raw/Local/CSV/Movies/2023/7/22/movies.csv"
target_path = "s3://data-lake-paganipb/Trusted/movies/2023/08/12"


df = df.withColumn("anoLancamento", df["anoLancamento"].cast("int"))
df = df.withColumn("anoFalecimento", df["anoFalecimento"].cast("int"))
df = df.withColumn("anoNascimento", df["anoNascimento"].cast("int"))
df = df.withColumn("tempoMinutos", df["tempoMinutos"].cast("int"))
df = df.withColumn("notaMedia", df["notaMedia"].cast("double"))
df = df.withColumn("numeroVotos", df["numeroVotos"].cast("int"))
df = df.withColumn("genero", when(col("genero") == "\\N", None).otherwise(col("genero")))

df_final_sem_duplicatas = df.dropDuplicates(["id"])

df_final_sem_duplicatas.select("tituloPincipal","anoLancamento","genero","notaMedia","numeroVotos","generoArtista","anoNascimento").show(50)

dynamic_frame = DynamicFrame.fromDF(df_final_sem_duplicatas, glueContext)


glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet"
)
