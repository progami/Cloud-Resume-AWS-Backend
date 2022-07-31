import json
import boto3

# import requests


def put_function(event, context):
    
    # connect to dynamodb
    dynamoDB = boto3.resource('dynamodb', region_name= 'eu-central-1')
    table= dynamoDB.Table('cloud-resume-challenge')

    # get existing data from table
    response = table.scan()
    prev_visitors = response['Items'][0]['Count']

    # get count from existing table, add +1 to it and update the table
    table.put_item(
        Item={'ID': '101/Visitors',
        'Count': prev_visitors+1
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps()
    }

