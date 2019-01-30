print("hi")

import boto3
import MyEc2

f = open('keySet.data','r')

access_key, secret_access_key = f.read().split("\n")

session = boto3.Session(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key,
)
teamName = 'UxfactoryTestTeam_1'
#subnet = MyEc2.create_subnet(session)
#print(subnet)
#MyEc2.create_keypair(session, teamName)
#MyEc2.create_instance(session, teamName, 2)
MyEc2.delete_keypair(session, teamName)

MyKey = MyEc2.create_keypair(session, teamName)

test_file = open('key_data.txt', 'w')

print (MyKey)
#test_file.write(MyKey)