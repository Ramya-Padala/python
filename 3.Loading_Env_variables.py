import os
from dotenv import load_dotenv, find_dotenv, dotenv_values
import boto3
from pathlib import Path

#This will load .env by default.
load_dotenv(override=True)
print(os.getenv('AWS_ACCESS_KEY_ID'))
print(os.getenv('AWS_SECRET_ACCESS_KEY'))
print(os.getenv('AWS_DEFAULT_REGION'))

#This will load .env_dev for AWS Account SREEYUTUBE
load_dotenv(override=True,dotenv_path='C:\SUREDELETELATER\AzureB41\Python\demo1\.env_dev')
print(os.getenv('AWS_ACCESS_KEY_ID'))
print(os.getenv('AWS_SECRET_ACCESS_KEY'))
print(os.getenv('AWS_DEFAULT_REGION'))
ec2_client = boto3.client('ec2',region_name="us-east-1")
vpcs = ec2_client.describe_vpcs().get('Vpcs', [])
print([vpc['VpcId'] for vpc in vpcs])
print("================================================================")
#This will load .env_prod for AWS Account SREEK8S
load_dotenv(override=True,dotenv_path='C:\SUREDELETELATER\AzureB41\Python\demo1\.env_prod')
print(os.getenv('AWS_ACCESS_KEY_ID'))
print(os.getenv('AWS_SECRET_ACCESS_KEY'))
print(os.getenv('AWS_DEFAULT_REGION'))
ec2_client = boto3.client('ec2',region_name="us-east-1")
vpcs = ec2_client.describe_vpcs().get('Vpcs', [])
print([vpc['VpcId'] for vpc in vpcs])
