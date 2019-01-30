print("hi")

import boto3
import MyEc2

f = open('keySet.data','r')

access_key, secret_access_key = f.read().split("\n")

session = boto3.session(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key,
)

try:
    ec2 = session.resource('ec2', region_name='REGION')
    subnet = ec2.Subnet('SUBNET')
    instances = subnet.create_instances(ImageId='IMAGE_ID', InstanceType='INSTANCE_TYPE',
                                        MaxCount='NO_OF_INSTANCE',
                                        MinCount='NO_OF_INSTANCE',
                                        KeyName='KEY_PAIR_NAME', SecurityGroups=[], SecurityGroupIds=['SECURITY_GROUP'])
    print(instances)

except BaseException as exe:
    print(exe)