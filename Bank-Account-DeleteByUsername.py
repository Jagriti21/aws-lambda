import json

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Account')

def lambda_handler(event, context):

    print(event)
    bankuser_name = event['params']['path']['username']
    table.delete_item(
       Key={
        "username" : bankuser_name
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('User deleted successfully')
    }