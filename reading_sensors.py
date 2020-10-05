import boto3
import create_bucket
import _setup
import pandas as pd 

records = pd.read_csv(r"C:\Users\Bojan\Downloads/vehicles.csv")
# For this purpose, i will using .csv file instead of real data stream
firehose, s3 = _setup.ex_vars
for idx, row in records.iterrows():
    payload= ' '.join(str(value) for value in row)
    payload = payload + "\n"
    print("Sending payload: {}".format(payload))

    res= firehose.put_record(
    DeliveryStreamName='prviDS',
    Record ={'Data': payload})

    print("Wrote to RecordID {}".format(res['RecordId']))


