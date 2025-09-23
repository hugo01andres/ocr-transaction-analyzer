import boto3
import os
from dotenv import load_dotenv
import json

load_dotenv()

def test_bedrock():
    client = boto3.client(
        service_name="bedrock-runtime",
        region_name=os.getenv("AWS_REGION", "us-east-1"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

    body = {
        "messages": [
            {"role": "user", "content": [{"type": "text", "text": "Say hello in Spanish"}]}
        ],
        "max_tokens": 50,
        "anthropic_version": "bedrock-2023-05-31",
    }

    response = client.invoke_model(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body),
    )

    print("✅ Bedrock response:")
    print(response["body"].read().decode("utf-8"))

if __name__ == "__main__":
    test_bedrock()
