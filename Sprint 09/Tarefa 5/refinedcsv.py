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
    col("titulooriginal"),
    col("anoLancamento"),
    col("tempoMinutos"),
    col("notaMedia"),
    col("numeroVotos")
)

# Ler o arquivo Parquet
input_path = "s3://desafioaws/Raw/Trusted/trustedcsv/"
df = spark.read.parquet(input_path)

# Filtragem dos IDs
selected_ids = ['tt1099212', 'tt1259571', 'tt1325004', 'tt1324999', 'tt1673434']
df_filtered = df.filter(df['id'].isin(selected_ids))

# Colunas
selected_columns = ['id', 'titulooriginal', 'tempoMinutos', 'notaMedia', 'numeroVotos']
df_selected = df_filtered.select(*selected_columns)

output_path = "s3://desafioaws/Raw/Refined/csv"
df_selected.write.parquet(output_path)
