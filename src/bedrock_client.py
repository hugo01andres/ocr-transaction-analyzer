import boto3
from . import config

def get_bedrock_client():
    """
    Creates and returns a boto3 client for Amazon Bedrock Runtime.
    """
    client = boto3.client(
        service_name="bedrock-runtime",
        region_name=config.AWS_REGION,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    )
    return client
