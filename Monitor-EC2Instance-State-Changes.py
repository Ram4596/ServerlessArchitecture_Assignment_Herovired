import json, boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    sns_topic = 'arn:aws:sns:ap-south-1:295397358094:RamVenu_SNS'  # enter the SNS topic

    # Get the state from the Event
    state = event['detail']['state']
    event2 = event['detail']['instance-id']

    # Create the message
    message = 'EC2 Instance ' + event2 + ' State-change Notification: ' + state 
 
    # Publish the message to the SNS Topic
    response = sns.publish(
        TopicArn=sns_topic,
        Message=message,
    )

    return {
        'statusCode': 200,
        'body': json.dumps('SNS message sent!')
    }