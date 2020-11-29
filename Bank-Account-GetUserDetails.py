import json
import boto3
import os

import uuid
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
   
    table = dynamodb.Table('Account')

    result = table.get_item(
        Key={
            'username': event['params']['path']['username']
        }
    )
    rest=[]
    rest.append(result['Item'])
    
    return rest