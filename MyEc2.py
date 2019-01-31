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
    imageSet = ['player-cpu', 'player-gpu', 'simulator-gpu']
    instanceSet = ['t3.medium', 'p2.xlarge', 'p2.xlarge']
    imageIdSet = ['ami-0c8e4039a99df4618', 'ami-08eac7bed935b810f', 'ami-028240c0a7333907b']

    image = imageSet[instanceFlag]
    instaceType = instanceSet[instanceFlag]
    imageId = imageIdSet[instanceFlag]
    key_name = teamName
    securityGroupId = 'sg-0e07d7fcc9bd8ce0e'
    securityGroup = 'uxfac_group'

    subnetId = 'subnet-0c655fced82b51192'

    userData = ''

    try:
        ec2 = session.resource('ec2', region_name='ap-northeast-2')
        instance = ec2.create_instances(
            ImageId=imageId,
            InstanceType=instaceType,
            MaxCount=1,
            MinCount=1,
            KeyName=key_name,
            NetworkInterfaces=[{'SubnetId': subnetId, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True,
                                'Groups': [securityGroupId]}],
            InstanceInitiatedShutdownBehavior='terminate',
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': teamName + " " + image
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
        return instance[0].instance_id

    except BaseException as exe:
        print(exe)

        return 'error'


def delete_keypair(session, teamName):
    try:
        ec2 = session.client('ec2')
        response = ec2.delete_key_pair(KeyName=teamName)
        return response
    except:
        return 'Delete_Keypair Error'

def delete_instance(session, instanceId):

    instanceIds = [instanceId,]
    ec2 = session.resource('ec2', region_name='ap-northeast-2')
    respone = ec2.instances.filter(InstanceIds=instanceIds).terminate()

import MyDb

def create_team(session, teamName):
    key = create_keypair(session, teamName)

    db = MyDb.connectDB()
    MyDb.insertTeamInfo(db, teamName)
    MyDb.insertKey(db, teamName, key)

    instanceIdInfo = ['', '', '']
    instanceIpInfo = ['','','']
    for i in range(0, 3):
        instanceIdInfo[i] = create_instance(session, teamName, i)


    for i in range(0,3):
        instanceIpInfo[i] = getPublicIpAddress(session, instanceIdInfo[i])
    MyDb.insertInstance(db, teamName, instanceIdInfo, instanceIpInfo)
    db.close()

def delete_team(session, teamName):
    db = MyDb.connectDB()
    instanceids = MyDb.selectTeamInstance(db, teamName)
    for id in instanceids:
        delete_instance(session, id)
    delete_keypair(session, teamName)
    MyDb.deleteTeamInfo(db, teamName)
    db.close()



def getPublicIpAddress(session, instanceid):
    ec2 = session.client('ec2')
    response = ec2.describe_instances(
        InstanceIds=[
            instanceid,
        ],
    )

    print(response)

    try:
        publicipaddress = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        return publicipaddress
    except:
        print("getPublicAddress Error!!", instanceid)
        return '0.0.0.0'

