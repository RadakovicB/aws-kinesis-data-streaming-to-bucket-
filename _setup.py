import boto3



firehose = boto3.client('firehose',
    aws_access_key_id="##################",
    aws_secret_access_key="########################",
    region_name="us-east-2")


custom_session=boto3.session.Session()
s3 = custom_session.resource(service_name="s3",
    aws_access_key_id="##################",
    aws_secret_access_key="#########################",
    region_name="us-east-2")

    
ex_vars =[firehose,s3]
