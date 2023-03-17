#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import io
import boto3
import json
import csv
import numpy as np

# grab environment variables
ENDPOINT_NAME = "sagemaker-xgboost-2023-03-16-18-16-55-852"
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    # extract data from the event
    data = event['data']
    print(data)
    
    # convert data to CSV
    csv_data = io.StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(data)
    
    # invoke endpoint with CSV data
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType='text/csv',
        Body=csv_data.getvalue().encode('utf-8')
    )
    print(response)
    
    # parse the response
    result = json.loads(response['Body'].read().decode())
    print(result)
    
    return result

