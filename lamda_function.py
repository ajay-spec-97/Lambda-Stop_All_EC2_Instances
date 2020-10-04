import json
import boto3


client=boto3.client('ec2')



def lambda_handler(event, context):
    response = client.describe_instances()
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:                   #Get all the instances information
            id=[instance["InstanceId"]]                             #Get the current instance id
            client.stop_instances(InstanceIds=id)                   #Stop the id current holding instance
            print('Stopping the Instance ',instance["InstanceId"])

    return {
        'statusCode': 200,
        'body': json.dumps('All the instances are stopped now!')
    }