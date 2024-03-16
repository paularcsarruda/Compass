FROM python:3

RUN pip install boto3

COPY . .

WORKDIR /app

CMD ["python", "upload_to_s3.py"]
