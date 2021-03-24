import boto3
import uuid
import sys

s3client = boto3.client('s3')

class S3Tool():
    def __init__(self):
        self.
    def change_client(self, ID, SECRET)
        self.client = boto3.client(
            's3',
            # Hard coded strings as credentials, not recommended.
            aws_access_key_id=ID,
            aws_secret_access_key=SECRET
        )
    def create_bucket():
        bucket_name = 'python-sdk-sample-{}'.format(uuid.uuid4())
        print('Creating new bucket with name: {}'.format(bucket_name))
        s3client.create_bucket(Bucket=bucket_name)

    def list_buckets():
        list_buckets_resp = s3client.list_buckets()
        for bucket in list_buckets_resp['Buckets']:
            print(bucket)
            # if bucket['Name'] == bucket_name:
            #     print('(Just created) --> {} - there since {}'.format(
            #         bucket['Name'], bucket['CreationDate']))

    def main():
        list_buckets()


if __name__ == "__main__":
    print("Starting.......")
    x = S3Tool()
    x.main() 
