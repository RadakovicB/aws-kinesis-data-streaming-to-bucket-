import create_bucket
import pandas as pd
import _setup

firehose, s3 = _setup.ex_vars

# List the objects that have been written to the S3 bucket
objects = s3.list_objects(Bucket='prviawsbucket')['Contents']
# Create list for collecting dataframes from read files.
dfs = []

# For every object, load it from S3.
for obj in objects:
    data_file= s3.get_object(Bucket='prviawsbucket', Key=obj['key'])
    
    # Load it into a dataframe, specifying a delimiter and column names
    dfs.append(pd.read_csv(data_file['Body'],
    delimiter = " ",
    names =["record_id", 'timestamp', 'vin','lon','lat','speed']))

# Concatenate the resulting dataframes.
data = pd.concat(dfs)
print(data.groupby(['vin'])['speed'].max())