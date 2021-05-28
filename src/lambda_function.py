import json
import os
import boto3

table_name = os.environ['TABLE_NAME']


def increment_hits(tbl):
    key = {'id': 0}            
    expr ={':val': 1}
    request = tbl.update_item(
        Key=key,
        UpdateExpression='SET hits= hits + :val',
        ExpressionAttributeValues=expr
        )
    response = tbl.get_item(Key=key)
    return response['Item']['hits']


def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)
        table.wait_until_exists()

        count = increment_hits(tbl=table)    

        resp = {
            "statusCode":200,
            "headers":{
                "Access-Control-Allow-Origin": "*"
            },
            "body":json.dumps({"count":int(count)})
        }

        return resp

    except Exception as e:
        print("Error processing event {}".format(json.dumps(event, indent=2)))
        raise e

# Testing locally, requires dynamodb running locally on separate docker container with table and primary key already created.
# sam local invoke -e events/apigateway_event.json ApiGatewayFunction --docker-network dynamodb_default
# sam start-api --docker-network dynamodb_default