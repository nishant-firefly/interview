### docker pull localstack/localstack
### docker run -it -p 4566-4599:4566-4599 --name localstack_localstack localstack/localstack
## But we are using docker-compose for the above. will up the service mentioned in SERVICES=sqs,sns,kinesis of Environment.
#### Now run python test_services.py ### but getting error => botocore.exceptions.NoCredentialsError: Unable to locate credentials
