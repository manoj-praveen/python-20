import boto3
import requests

AWS_SECRET_ACCESS_KEY = 'XXXXXXXXx'
AWS_ACCESS_KEY_ID = 'XXXXXXX'
ENDPOINT_URL = 'https://trunome-bucket.blr1.digitaloceanspaces.com'
REGION_NAME = 'blr1'

session = boto3.session.Session()
client = session.client(
    's3',
    region_name=REGION_NAME,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def digitalocean_generate_upload_url(
        pdf_file_name: str,
        bucket_name: str
):
    signed_post = client.generate_presigned_post(
        Bucket=bucket_name,
        Key=pdf_file_name,
        ExpiresIn=3600,
    )
    return signed_post


response = digitalocean_generate_upload_url(
    "trunome-doc-upload/requirements.txt", "trunome-bucket"
)
print(response)

with open("requirements.txt", 'rb') as file:
    files = {'file': (file.name, file)}
    r = requests.post(response["url"], data=response['fields'], files=files)
    print(r.status_code)
    print(r.text)
