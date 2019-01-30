def create_keypair(ec2, teamName):
    respone = ec2.create_key_pair(KeyName=teamName)
    return respone

def delete_keypair(ec2, teamName):
    response = ec2.delete_key_pair(KeyName=teamName)
    return response