#!/usr/bin/env python3

import boto3
import datetime

CLOUDWATCH_PERIOD = 300

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
    cw = boto3.client('cloudwatch')

    now = datetime.datetime.utcnow()
    res = cw.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUCreditBalance',
        Dimensions=[{
            'Name': 'InstanceId',
            'Value': id,
        }],
        StartTime=now - datetime.timedelta(seconds=CLOUDWATCH_PERIOD),
        EndTime=now,
        Period=CLOUDWATCH_PERIOD,
        Statistics=['Average'],
    )

    # Now res['Datapoints'][0]['Average'] is the result.

    try:
        if res['Datapoints'][0]['Average'] < 10:
            pass
    except IndexError:
        pass

if __name__ == '__main__':
    lambda_handler(None, None)
