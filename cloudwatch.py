import boto3

REGION_NAME = 'us-west-2'
ACCESS_KEY = ''
SECRET_KEY = ''

TIME_PERIOD = 30 #period in minutes, should be at least 5 (the cloud watch granularity)
def get_instance_networkout_bytes(instance_id):
    #For Chetan: If you are using credntials file in ~/.aws/credntials, remove last 3 arguments of below function
    client = boto3.client('cloudwatch',
    region_name=REGION_NAME,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)

    response = client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='NetworkOut',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instance_id
        },
    ],
    StartTime=datetime.datetime.now()- datetime.timedelta(minutes=TIME_PERIOD),
    EndTime=datetime.datetime.now(),
    Period=60,
    Statistics=[
        'SampleCount','Average','Sum','Minimum','Maximum'
    ],
    )
    return response['Datapoints'][0]['Average']

if __name__=="__main___":
    list_of_my_instance_ids = [] #toy example
    for id in list_of_my_instance_ids:
        print(get_instance_networkout_bytes(id))
