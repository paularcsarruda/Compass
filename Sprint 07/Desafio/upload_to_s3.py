import boto3
import os
from datetime import datetime

# Variáveis
aws_access_key_id = "ASIA6GBMDSONKP4FZWND"
aws_secret_access_key = "K8qHFggiDRMxGjDlihsEWJthB00qKbIl4G4ZHd90"
aws_session_token = "IQoJb3JpZ2luX2VjEJ7//////////wEaCXVzLWVhc3QtMSJGMEQCIAOBiJIXPHe6rBLX0SgenkhuwdksxCLsxRHYG3e/SO7ZAiBnLDpSB8b8JnTQ6joH41nrCbUDma/tBVBSDrOUwmDXUiqmAwin//////////8BEAAaDDk3NTA1MDA4NTI3NCIMWQwMqM5zXdVJlhTpKvoC77Ug9ICoUABvBqP3WYCIct1R7GRO/b3xASEYrHqjqf5yiTOvUUzgt7SxIsnxDOT58QVqe6NfYiTg+zIezAuc75+CrVfH5605c486IhAF74UniYIoWPRg8IAACyAQZU00mshsscuyXydGvIyff874dC8cl3Z3qrj97xUDuM5GWzvX3SmwMatvzCI1RCF4x2z3ANNfff5KDE7uMIasiIfaIYrYoshfWmOVIYYQ3jBAIf6c5+myQVC0eoDQYewIZU/he4klY9hVRIeshS24DWvt6t0k4ydkmZ7oX5zj7HqRKKfkfNLJSYxh3j3CXntMzwVwPWW2Dk5xJY8pdbXWGWHQCgmGDkxvDGpnfcZ5b8uvYsM7JlAPO3ID2g266iPZF7k4xYJp9KnjL0JqQYAnFu8W4K29ypndI73PFDpnvuUr7JXSQTsu8xVc/QUTFTtejZOxTfVbvqdatrcmRd+WTxSa1i4cPq+zPabVljiebf7gZy5OwNmHxjIO8wCMMNrJ1q8GOqcBWRCMz5CdjR6KYnI6vWjXRPvcKNVftqUPnwyeWhXZLF0aLAYHmaE201QliToJJWxes0/D1vNd8xj+fKP+nnaGBYVKDKiT7Z6lu7yMVnM9xnZwqlftkOY9yavxUwxnY4J6O+u3dDs6KN21UHdDl8CKFUg188J8DtiVbL+tEP+k4bUtimoatwWOpVCHt45mNm+Bp8DWkKhHH2UixO/dLiRfL/Exry0A3Cg="
bucket_name = "desafioaws"
raw_zone = "Raw"
local = "Local"
csv = "CSV"
movies = "Movies"
series = "Series"
current_date = datetime.now().strftime("%Y/%m/%d")
movies_file_path = "/app/movies.csv"
series_file_path = "/app/series.csv"

s3 = boto3.client("s3",
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  aws_session_token=aws_session_token)

# Realizando o Upload dos arquivos CSV para o S3
s3.upload_file(movies_file_path,
               bucket_name,
               os.path.join(raw_zone, local, csv, movies, current_date, "movies.csv"))
s3.upload_file(series_file_path,
               bucket_name,
               os.path.join(raw_zone, local, csv, series, current_date, "series.csv"))
