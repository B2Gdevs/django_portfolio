import boto3


AWS_ACCESS_KEY_ID = 'dummy'
AWS_SECRET_ACCESS_KEY = 'dummy'

s3 = boto3.resource(
    's3',
    region_name='us-east-1',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
content="String content to write to a new S3 file"
s3.Object('portfolio5279', 'newfile.txt').put(Body=content)
