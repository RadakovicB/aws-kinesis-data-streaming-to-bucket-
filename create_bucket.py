import _setup
firehose = _setup.ex_vars[0]
s3 = _setup.ex_vars[1]


 #Create s3 bucket
s3.create_bucket(Bucket='prviawsbucket',
CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'})

# Create firehose delivery stream

res = firehose.create_delivery_stream(
    DeliveryStreamName="prviDS",
    DeliveryStreamType="DirectPut",

#Specifing configuration of the destination s3 bucket
    S3DestinationConfiguration ={
        "BucketARN": "arn:aws:s3:::prviawsbucket",
        "RoleARN": "arn:aws:iam::670129062075:role/firehoseDeliveryRole"
    }
)
print("Created Firehose Stream ARN: {}".format(res['DeliveryStreamARN']))
