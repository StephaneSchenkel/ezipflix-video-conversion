import logging
import boto3
import botocore

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

class VideoConversionFilesystem(object):
    def __init__(self):
        self.s3 = boto3.resource('s3')

    def downloadfile(self, filename, bucket):
        try:
            self.s3.Bucket(bucket).download_file(filename, filename)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    def uploadfile(self, filename, bucket):
        self.s3.Bucket(bucket).upload_file(filename, filename)