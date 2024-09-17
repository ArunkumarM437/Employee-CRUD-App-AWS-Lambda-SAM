import json
import os
import boto3

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")

tableName = os.environ['TABLE_NAME']
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    print(event)
    body = {}
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }
    try:
        if event['routeKey'] == "DELETE /items/{empid}":
            table.delete_item(Key={'empid': event['pathParameters']['empid']})
            body = 'Deleted item ' + event['pathParameters']['empid']

        elif event['routeKey'] == "GET /items/{empid}":
            response = table.get_item(Key={'empid': event['pathParameters']['empid']})
            body = response.get("Item", {})
            if body:
                responseBody = {
                    'empid': body['empid'], 
                    'department': body['department'], 
                    'city': body['city'], 
                    'Emp_Name': body['Emp_Name'], 
                    'Gender': body['Gender']
                }
                body = responseBody
            else:
                statusCode = 404
                body = 'Item not found'

        elif event['routeKey'] == "GET /items":
            response = table.scan()
            items = response.get("Items", [])
            responseBody = [
                {
                    'empid': item['empid'], 
                    'department': item['department'], 
                    'city': item['city'], 
                    'Emp_Name': item['Emp_Name'], 
                    'Gender': item['Gender']
                }
                for item in items
            ]
            body = responseBody

        elif event['routeKey'] == "POST /items":
            requestJSON = json.loads(event['body'])
            table.put_item(Item=requestJSON)
            body = 'Created item ' + requestJSON['empid']

        elif event['routeKey'] == "PATCH /items/{empid}":
            empid = event['pathParameters']['empid']
            update_values = json.loads(event['body'])

            update_expression = "SET " + ", ".join(f"{k} = :{k}" for k in update_values.keys())
            expression_attribute_values = {f":{k}": v for k, v in update_values.items()}

            table.update_item(
                Key={'empid': empid},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
            body = 'Updated item ' + empid

    except KeyError:
        statusCode = 400
        body = 'Unsupported route: ' + event['routeKey']
    except Exception as e:
        statusCode = 500
        body = 'Error: ' + str(e)

    body = json.dumps(body)
    res = {
        "statusCode": statusCode,
        "headers": headers,
        "body": body
    }
    return res
