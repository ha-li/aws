import boto3
import os
import sys
import uuid

s3_client = bot3.client('s3')

def moveFile(event, context):
    for record in event['Records']:
        souceBucket = record['s3']['bucket']['name']
        destinationBucket = 'a-simple-bucket'
        key = record['s3']['object']['key']
        
        s3_client.download (bucket, key, 'test')
        s3_client.upload_file('/tmp/test', destinationBucket, key)