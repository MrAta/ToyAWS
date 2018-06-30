import boto3
AMI_ID = ''
KEY_NAME = ''
SUBNET_ID = ''
SEC_GROUP = ''

def create_instace(vmtype='m5.large', num=1):
    ec2 = boto3.resource('ec2', region_name="us-east-2")
    instance = ec2.create_instances(
    ImageId=AMI_ID,
    InstanceType=vmtype,
    KeyName=KEY_NAME,
    MaxCount=num,
    MinCount=1,
    Monitoring={
        'Enabled': True
    },
    Placement={
        'AvailabilityZone': 'us-east-2a',
    },
    SecurityGroupIds=[
        SEC_GROUP,
    ],
    SubnetId=SUBNET_ID,
    DisableApiTermination=False,
    InstanceInitiatedShutdownBehavior='stop',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'webserver_b'
                },
            ]
        },
    ]
    )
    print(instance)
    # print(instance[0].instance_id)
    return [instance[i].instance_id for i in range(len(instance))]

def terminate_instance(instance_id):
    client = boto3.client('ec2', region_name="us-east-2")
    response = client.terminate_instances(
    InstanceIds=[
        instance_id,
    ],
    )

def stop_instance(instance_id):
    client = boto3.client('ec2', region_name="us-east-2")
    response = client.stop_instances(
    InstanceIds=[
        instance_id,
    ],
    Force=True
    )
def start_instance(instance_id):
    client = boto3.client('ec2', region_name="us-east-2")
    response = client.start_instances(
    InstanceIds=[
        instance_id,
    ]
    )
