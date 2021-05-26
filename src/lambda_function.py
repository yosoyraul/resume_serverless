import json
import os
import boto3



def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb',endpoint_url="http://dynamodb-local:8000")
        table = dynamodb.Table('test')
        key = {'id': 0}
        expr ={':val': 1}
        request = table.update_item(
            Key=key,
            UpdateExpression='SET hits= hits + :val',
            ExpressionAttributeValues=expr
        )
        response = table.get_item(Key=key)
        count = response['Item']['hits']
        return count
    except Exception as e:
        print("Error processing event {}".format(json.dumps(event, indent=2)))
        raise e

# Testing locally, requires dynamodb running locally on docker container with table and items already created.
# sam local invoke -e events/apigateway_event.json ApiGatewayFunction --docker-network dynamodb_default
# sam start-api --docker-network dynamodb_default