import boto3 
from src import config

def test_s3_connection():
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
            region_name=config.AWS_REGION,
        )
        response = s3.list_buckets()
        print("✅ Conexión S3 exitosa. Buckets disponibles:")
        for bucket in response["Buckets"]:
            print(f" - {bucket['Name']}")
    except Exception as e:
        print("❌ Error conectando a S3:", e)

def test_textract_document(bucket_name, object_name):
    textract = boto3.client(
        "textract",
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        region_name=config.AWS_REGION,
    )

    response = textract.detect_document_text(
        Document={'S3Object': {'Bucket': bucket_name, 'Name': object_name}}
    )

    print("✅ Textract conectado. Texto detectado:")
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print(item["Text"])

if __name__ == "__main__":
    test_s3_connection()
    test_textract_document("ocr-poc-comprobantes", "comprobante_120.jpg")
