import boto3

# Initialize Boto3 client for LocalStack service (e.g., SQS)

breakpoint()
sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1', aws_access_key_id='test', aws_secret_access_key='test')

print(1)
import sys
sys.exit()

import boto3

# Initialize SQS client pointing to LocalStack endpoint
sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1')

# Create an SQS queue
response = sqs.create_queue(QueueName='test_queue')

# Send a message to the queue
sqs.send_message(QueueUrl=response['QueueUrl'], MessageBody='Hello from LocalStack!')

# Receive messages from the queue
messages = sqs.receive_message(QueueUrl=response['QueueUrl'], MaxNumberOfMessages=10)

for message in messages.get('Messages', []):
    print(message['Body'])
