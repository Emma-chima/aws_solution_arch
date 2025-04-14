import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get the destination bucket from the environment variable
    destination_bucket = os.environ['DESTINATION_BUCKET']
    
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        copy_source = {
            'Bucket': source_bucket,
            'Key': object_key
        }

        s3_client.copy_object(
            CopySource=copy_source,
            Bucket=destination_bucket,
            Key=object_key
        )
