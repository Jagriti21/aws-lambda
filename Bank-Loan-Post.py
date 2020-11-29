import json
import boto3
import os
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Loan')

def lambda_handler(event, context):
    # data = event['body-json']
    # print(data)
    item = {
        'id': str(uuid.uuid1()),
        'username': event['username'],
        'loantype': event['loantype'],
        'loanamount': event['loanamount'],
        'date': event['date'],
        'rateofinterest': event['rateofinterest'],
        'durationofloan': event['durationofloan']
    }
    table.put_item(Item=item)

    # create a response
    # response = {"output":"successfully inserted....."}
    

    return item

