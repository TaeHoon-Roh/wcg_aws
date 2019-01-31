import MyDb

print("hi")

import boto3
import MyEc2

f = open('keySet.data','r')

access_key, secret_access_key = f.read().split("\n")

session = boto3.Session(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key,
)
teamName = 'blue'

MyEc2.create_team(session, teamName)
