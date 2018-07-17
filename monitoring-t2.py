#!/usr/bin/python3

import boto3
import json
import time

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
