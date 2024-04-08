import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho de entrada e saída
input_path = "s3://desafioaws/Raw/Local/CSV/Movies/2024/03/16/"
output_path = "s3://desafioaws/Raw/TrustedData"

df = spark.read.option("delimiter", "|").option("header", "true").csv(input_path)

processed_data = df.select(
    col("id"),
    col("tituloOriginal"),
    col("anoLancamento"),
    col("tempoMinutos"),
    col("genero"),
    col("notaMedia"),
    col("numeroVotos"),
)

processed_data.write.mode("overwrite").parquet(output_path)

job.commit()
