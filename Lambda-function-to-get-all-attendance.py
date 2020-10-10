import json
import boto3

dynamo=boto3.resource("dynamodb")
table=dynamo.Table("Add your dynamoDB table name")
def lambda_handler(event, context):
    # TODO implement
    response=table.scan()
    items = response['Items']
    # print(items)
    for i, j in enumerate(items):
        print(j['Rollno'],j['Count'],j['Name'])
        
    return items
