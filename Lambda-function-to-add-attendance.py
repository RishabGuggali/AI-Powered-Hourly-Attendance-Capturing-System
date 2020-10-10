import json
import boto3

dynamo=boto3.resource("dynamodb")

table=dynamo.Table("Add your DynamoDB Table Name")
def lambda_handler(event, context):
    # TODO implement
    res=table.get_item(Key={"Rollno":event['Rollno']})
    print(res['Item']['Name'])
    Count = res['Item']['Count']
    Count= Count+1
    inp = {"Rollno":event['Rollno'],"Count":Count, "Name":res['Item']['Name']}
    table.put_item(Item=inp)
    return "Successful"
