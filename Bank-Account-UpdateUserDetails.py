import json
import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # data = event['body-json]
    table = dynamodb.Table('Account')
    result = table.update_item(
        Key={
            'username': event['username']
        },
        ExpressionAttributeNames={
          '#name': 'name',
          '#state': 'state',
        },
        UpdateExpression='set accounttype=:accounttyped, address=:addressd, contact=:contactd, country=:countryd, DOB=:DOBd, email=:emaild, #name=:named, pan=:pand, password=:passwordd, #state=:stated',
        ExpressionAttributeValues={
            ':accounttyped':event['accounttype'],
            ':addressd':event['address'],
            ':contactd':event['contact'],
            ':countryd':event['country'],
            ':DOBd':event['DOB'],
            ':emaild':event['email'],
            ':named':event['name'],
            ':pand':event['pan'],
            ':passwordd':event['password'],
            ':stated':event['state'],
            
        },
        ReturnValues='UPDATED_NEW',
    )
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    return result['Attributes']
