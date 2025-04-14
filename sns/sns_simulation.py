import boto3
import json

#Create an SNS client
sns = boto3.client('sns', region_name='eu-north-1')  

#Create the SNS Topic
response_create = sns.create_topic(Name='MyTestTopic')
topic_arn = response_create['TopicArn']
print("Created Topic ARN:", topic_arn)

#Subscribe to the Topic (email subscription)
response_subscribe = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='email@email.com'  
)
subscription_arn = response_subscribe['SubscriptionArn'] if 'SubscriptionArn' in response_subscribe else 'Pending confirmation'
print("Subscription ARN (Pending confirmation via email):", subscription_arn)


#Publish a Message to the Topic
message = "Hello, SNS simulation! This is a test message from Python using Boto3. Just testing the SNS service."
response_publish = sns.publish(
    TopicArn=topic_arn,
    Message=message,
)
print("Message published. Message ID:", response_publish['MessageId'])

