import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job_name = args['JOB_NAME']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(job_name, args)

schema = (
    col("id"),
    col("Titulo"),
    col("Votos"),
    col("`Media de Votos`").alias("Media_de_Votos"),
    col("Popularidade"),
    col("Orçamento"),
    col("Faturamento")
)

# Ler o arquivo Parquet
input_path = "s3://desafioaws/Raw/Trusted/trustedtmdb/"
df = spark.read.parquet(input_path)

# Selecionar apenas as colunas desejadas
selected_columns = ['Titulo', 'Votos', 'Popularidade', 'Orçamento', 'Faturamento']
df_selected = df.select(*selected_columns)

# Escrever o resultado em um novo arquivo Parquet
output_path = "s3://desafioaws/Raw/Refined/tmdb"
df_selected.write.parquet(output_path)
