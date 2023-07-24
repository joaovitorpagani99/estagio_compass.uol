import logging
import boto3
from botocore.exceptions import ClientError
import os
from datetime import datetime

file_movies = "./FilmesESeries/movies.csv"
file_series = "./FilmesESeries/series.csv"

bucket= "data-lake-paganipb"

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day


#UPLOAD DO ARQUIVO CSV DE MOVIES

def upload_file_movies(file_movies, bucket_movies, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_movies)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_movies, bucket_movies, f'Raw/Local/CSV/Movies/{year}/{month}/{day}/{object_name}')
    except ClientError as e:
        logging.error(e)
        return False
    return True
    

#UPLOAD DO ARQUIVO CSV DE SERIES    
def upload_file_series(file_series, bucket_series, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_series)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_series, bucket_series, f'Raw/Local/CSV/Series/{year}/{month}/{day}/{object_name}')
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    upload_file_series(file_series, bucket)
    upload_file_movies(file_movies, bucket)