import os
from dotenv import load_dotenv, find_dotenv, dotenv_values
import boto3
from pathlib import Path


#This will load .env_dev for AWS Account SREEYUTUBE
config = dotenv_values(".env_dev")
print(config['AWS_ACCESS_KEY_ID'])
print(config['AWS_SECRET_ACCESS_KEY'])
print(config['AWS_DEFAULT_REGION'])
access_key = config['AWS_ACCESS_KEY_ID']
secret_key = config['AWS_SECRET_ACCESS_KEY']
region = config['AWS_DEFAULT_REGION']
ec2_client = boto3.client('ec2',region_name="us-east-1",aws_access_key_id=access_key,aws_secret_access_key=secret_key)
vpcs = ec2_client.describe_vpcs().get('Vpcs', [])
print([vpc['VpcId'] for vpc in vpcs])

#This will load .env_prod for AWS Account SREEK8S
config = dotenv_values(".env_prod")
print(config['AWS_ACCESS_KEY_ID'])
print(config['AWS_SECRET_ACCESS_KEY'])
print(config['AWS_DEFAULT_REGION'])
access_key = config['AWS_ACCESS_KEY_ID']
secret_key = config['AWS_SECRET_ACCESS_KEY']
region = config['AWS_DEFAULT_REGION']
ec2_client = boto3.client('ec2',region_name="us-east-1",aws_access_key_id=access_key,aws_secret_access_key=secret_key)
vpcs = ec2_client.describe_vpcs().get('Vpcs', [])
print([vpc['VpcId'] for vpc in vpcs])