#!/usr/bin/env python3

import boto3

def lambda_handler(event, context):
    cw = boto3.client('cloudwatch')
    ec2 = boto3.client('ec2')

if __name__ == '__main__':
    lambda_handler(None, None)
