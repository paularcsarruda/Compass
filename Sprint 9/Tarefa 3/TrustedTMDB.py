import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
from pyspark.sql.functions import expr

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = spark.read.format("json").load("s3://desafioaws/Raw/TMDB/JSON/2024/04/11/data-3.json")

df.printSchema()

df.show()

read_df = df.withColumn("explode", expr("explode_outer(filmes)"))

processed_data = read_df.select(
    col("explode.id"),
    col("explode.Titulo"),
    col("explode.Votos"),
    col("explode.`Media de Votos`").alias("Media_de_Votos"),
    col("explode.Popularidade"),
    col("explode.Orçamento"),
    col("explode.Faturamento")
)

processed_data.write.parquet("s3://desafioaws/Raw/Trusted/trustedtmdb")

job.commit()
