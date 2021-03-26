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
		self.BASE_DIR = str(Path(__file__).resolve().parent.parent) + "/S3Tool/Backups/"
		space = "#################################################"
	
		# for _dirs in self.dirs:
		#     #clean this up later
		#     if len(_dirs) <= len(space):
		#         _dirs_len=  len(_dirs)
		#         diff = int((len(space) -_dirs_len))
		#         print("diff", diff)
		#         header  = ("#" * diff) + _dirs + ("#" * diff)
		#         print(space)
		#         print(diff)
		#         print(space)
		#     else:
		#         print(space)
		#         print(_dirs)
		#         print(space)
		# try:
		new_dirs  = []
		bucket = "cloud.vegatouch-dev.com"
		# self.BASE_DIR = self.BASE_DIR + "/" + bucket 
		for key in s3client.list_objects(Bucket=bucket)['Contents']:
			self.BASE_DIR = self.BASE_DIR + "/" + bucket 
			print("    -", key['Key'])
			
			bucket_path =  key['Key']
			print(bucket_path)
			_bucket_path = bucket_path.split("/")
			_bucket_root = _bucket_path[0]
			print(_bucket_path)
			s3client.list_objects(Bucket=bucket)['Contents']
			index = 0
			_bucket_path = _bucket_path[1:-1:]
			os.mkdir(self.BASE_DIR + "/" + _bucket_root)
			while len(_bucket_path) > 0:

				print(_bucket_path)
				b =  _bucket_root 
				self.BASE_DIR =  self.BASE_DIR + b

				print("I feel like bugs are under my skin")
				if os.path.exists(self.BASE_DIR + "/" + b):
					print(self.BASE_DIR + b, " Already Exists")
				else:
					
					print("New Path ", self.BASE_DIR + "/" + b)
					# self.BASE_DIR = self.BASE_DIR + _bucket_path[0]
					os.mkdir(self.BASE_DIR + "/" + b)
				print(b, "  ", _bucket_path)
				# sys.exit(1)
				# for b in _bucket_path:
				# 	if os.path.exists(self.BASE_DIR + b):
				# 		print("Doesnt Exists ", self.BASE_DIR + b, " Already Exists")
				# 	else:
				# 		print("New Path ", self.BASE_DIR + b)
				# 	print(b, "  ", _bucket_path)
				_bucket_path.pop(0)
			self.BASE_DIR = str(Path(__file__).resolve().parent.parent) + "/S3Tool/Backups"
		# except:
		# 	print("fucking Tried")

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





	def make_bucket_directories(self):
		pass
		

		




if __name__ == "__main__":
	print("Starting.......")
	x = S3Tool()
	x.main() 
	x.make_directories()

	x.list_bucket_contents()
