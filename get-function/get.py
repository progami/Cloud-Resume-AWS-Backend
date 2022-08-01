import json
import boto3

# import requests


def get_function(event, context):

    dynamoDB = boto3.resource('dynamodb', region_name= 'eu-central-1')
    table= dynamoDB.Table('cloud-resume-challenge')

    response = table.scan()
    prev_visitors = response['Items'][0]['Count']

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({"count": str(prev_visitors)})
    }

