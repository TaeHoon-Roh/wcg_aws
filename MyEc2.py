def create_keypair(session, teamName):
    try:
        ec2 = session.client('ec2')
        respone = ec2.create_key_pair(KeyName=teamName)
        return respone
    except:
        return 'Create_Keypair Error'


def create_subnet(session):

    ec2 = session.resource('ec2', region_name='ap-northeast-2')
    subnet = ec2.create_subnet(
        CidrBlock='172.31.32.0/20',
        VpcId='	vpc-ba14f6d1',
    )
    return subnet

def create_instance(session, teamName, instanceFlag):

    imageSet = ['player-cpu','player-gpu','simulator-gpu']
    instanceSet = ['t3.medium','p2.xlarge', 'p2.xlarge']
    imageIdSet = ['ami-0c8e4039a99df4618','ami-09b3504002923459d','ami-0622c35395a0a2a77']

    image = imageSet[instanceFlag]
    instaceType = instanceSet[instanceFlag]
    imageId = imageIdSet[instanceFlag]
    key_name = teamName
    securityGroupId = 'sg-0e07d7fcc9bd8ce0e'
    securityGroup =  'uxfac_group'

    subnetId = 'subnet-0c655fced82b51192'

    userData=''

    try:
        ec2 = session.resource('ec2', region_name='ap-northeast-2')
        instance = ec2.create_instances(
            ImageId = imageId,
            InstanceType = instaceType,
            MaxCount = 1,
            MinCount = 1,
            KeyName = key_name,
            NetworkInterfaces=[{'SubnetId' : subnetId, 'DeviceIndex' : 0, 'AssociatePublicIpAddress': True, 'Groups': [securityGroupId]}],

            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': teamName + " " +image
                        },
                    ],
                },

                {
                    'ResourceType': 'volume',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': teamName + " " + image
                        },
                    ],
                },
            ],
        )

        print(instance)

    except BaseException as exe:
        print(exe)

def delete_keypair(session, teamName):
    try:
        ec2 = session.client('ec2')
        response = ec2.delete_key_pair(KeyName=teamName)
        return response
    except:
        return 'Delete_Keypair Error'

def delete_instance(session, instanceId):
    ec2 = session.resource('ec2', region_name='ap-northeast-2')
    response = ec2.terminate_instances(instance_ids=[instanceId])
    return response