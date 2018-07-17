#!/usr/bin/env python3

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    instances = ec2.describe_instances(Filters=[{
        'Name': 'instance-type',
        'Values': ['t2.*'],
    }])

    for instance in instances['Reservations']:
        for i in instance['Instances']:
            validate_instance(i['InstanceId'])

def validate_instance(id):
    pass

if __name__ == '__main__':
    lambda_handler(None, None)
