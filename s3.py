import boto3
import uuid
import sys
from pathlib import Path
import os

s3client = boto3.client('s3')


#change into
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

class S3Tool:

    def __init__(self):
        
        self.dirs = []
        self.BASE_DIR = str(Path(__file__).resolve().parent.parent) + "/S3Tool/"
        self.more_objects= False
        self.found_token = False

    def change_client(self, ID, SECRET):
        self.client = boto3.client(
            's3',
            # Hard coded strings as credentials, not recommended.
            aws_access_key_id=ID,
            aws_secret_access_key=SECRET
        )

    def create_bucket(self):
        bucket_name = 'python-sdk-sample-{}'.format(uuid.uuid4())
        print('Creating new bucket with name: {}'.format(bucket_name))
        s3client.create_bucket(Bucket=bucket_name)



    def list_bucket_contents(self):
        for key in s3client.list_objects(Bucket="")['Contents']:
            print(key['Key'])

    def move_bucket(self, new_bucket_name, bucket_to_copy):
        for key in s3.list_objects(Bucket=bucket_to_copy)['Contents']:
            files = key['Key']
            copy_source = {'Bucket': "bucket_to_copy",'Key': files}
            s3_resource.meta.client.copy(copy_source, new_bucket_name, files)
            print(files)

    def list_buckets(self):
        
        list_buckets_resp = s3client.list_buckets()

        for bucket in list_buckets_resp['Buckets']:
            # print(bucket["Name"])
            self.dirs.append(bucket["Name"])
            # if bucket['Name'] == bucket_name:
            #     print('(Just created) --> {} - there since {}'.format(
            #         bucket`['Name'], bucket['CreationDate']))
        print(self.dirs, "#Buckets to Copy: ",len(self.dirs))
    
    def make_directories(self):

        os.mkdir(self.BASE_DIR + "/Backups")
        self.BASE_DIR = str(Path(__file__).resolve().parent.parent) + "/S3Tool/Backups/"

        for x in range(len(self.dirs)):
            _BASE_DIR = self.BASE_DIR
            full_path = _BASE_DIR + self.dirs[x]
            isdir = os.path.isdir(full_path)
            print(x, _BASE_DIR, "   :", isdir)
            if not(isdir):
                os.mkdir(full_path)
                
            else:
                print("fuckyou")
        

        

    def copy_buckets_cmd(self):
        self.list_buckets()
        if len(self.dirs) > 0: #make sure to add < later on becasue AWS uses pagination for long responses.
            pass
            #make local directories under Project/

    
    def main(self):
        self.list_buckets()


if __name__ == "__main__":
    print("Starting.......")
    x = S3Tool()
    x.main() 
    x.list_bucket_contents()
    # x.make_directories()
