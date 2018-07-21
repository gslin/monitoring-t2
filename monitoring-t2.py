#!/usr/bin/env python3

import boto3
import datetime

CLOUDWATCH_PERIOD = 300

class monitor_t2:
    def __init__(self):
        self.cw = boto3.client('cloudwatch')
        self.ec2 = boto3.client('ec2')
        self.sns = boto3.client('sns')

    def lambda_handler(self, event, context):
        instances = self.ec2.describe_instances(Filters=[{
            'Name': 'instance-type',
            'Values': ['t2.*'],
        }])

        for instance in instances['Reservations']:
            for i in instance['Instances']:
                self.validate_instance(i['InstanceId'])

    def validate_instance(self, id):
        now = datetime.datetime.utcnow()
        res = self.cw.get_metric_statistics(
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

        message = 'This is automatic script to alarm.\nCPU credit of instance {} is below 10.\n'.format(id)
        subject = 'CPU credit of instance {} is below 10'.format(id)

        try:
            if res['Datapoints'][0]['Average'] < 10:
                pass
        except IndexError:
            pass

def lambda_handler(event, context):
    m = monitor_t2()
    m.lambda_handler(event, context)

if __name__ == '__main__':
    lambda_handler(None, None)
