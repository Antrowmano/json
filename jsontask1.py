


import json
from pprint import pprint as pp

event={'Records': [{'EventSource': 'aws:sns',
              'EventSubscriptionArn': 'arn:aws:sns:us-east-1:111111111111111:Amazon-ES-Recommended-Alarms-ES-CW-Alerts:c7bf8523-79ec-46a5-a205-052a6936f2b5',
              'EventVersion': '1.0',
              'Sns': {'Message': '{"AlarmName":"ES-CW-Alerts-RedClusterAlarm-N01JERDHJDJ7","AlarmDescription":"Red '      
                                 'cluster status - '
                                 'Alert","AWSAccountId":"111111111111111","AlarmConfigurationUpdatedTimestamp":"2022-03-11T10:05:38.359+0000","NewStateValue":"ALARM","NewStateReason":"Threshold '
                                 'Crossed: 1 out of the last 1 datapoints [1.0 '
                                 '(11/03/22 10:05:00)] was greater than or '
                                 'equal to the threshold (1.0) (minimum 1 '
                                 'datapoint for OK -> ALARM '
                                 'transition).","StateChangeTime":"2022-03-11T10:06:58.031+0000","Region":"US '
                                 'East (N. '
                                 'Virginia)","AlarmArn":"arn:aws:cloudwatch:us-east-1:111111111111111:alarm:ES-CW-Alerts-RedClusterAlarm-N01JERDHJDJ7","OldStateValue":"OK","OKActions":[],"AlarmActions":["arn:aws:sns:us-east-1:111111111111111:Amazon-ES-Recommended-Alarms-ES-CW-Alerts"],"InsufficientDataActions":[],"Trigger":{"MetricName":"ClusterStatus.red","Namespace":"AWS/ES","StatisticType":"Statistic","Statistic":"MAXIMUM","Unit":null,"Dimensions":[{"value":"------------accp-es","name":"DomainName"},{"value":"111111111111111","name":"ClientId"}],"Period":60,"EvaluationPeriods":1,"DatapointsToAlarm":1,"ComparisonOperator":"GreaterThanOrEqualToThreshold","Threshold":1.0,"TreatMissingData":"","EvaluateLowSampleCountPercentile":""}}',
                      'MessageAttributes': {},
                      'MessageId': '-----------------------',
                      'Signature': '------------------------------------------',
                      'SignatureVersion': '1',
                      'SigningCertUrl': '--------------------------',
                      'Subject': 'ALARM: '
                                 '"ES-CW-Alerts-RedClusterAlarm-N01JERDHJDJ7" '
                                 'in US East (N. Virginia)',
                      'Timestamp': '2022-03-11T10:06:58.088Z',
                      'TopicArn': 'arn:aws:sns:us-east-1:111111111111111:Amazon-ES-Recommended-Alarms-ES-CW-Alerts',      
                      'Type': 'Notification',
                      'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:111111111111111:Amazon-ES-Recommended-Alarms-ES-CW-Alerts:--------------------'}}]}
def awstask(x):
    for i in x['Records']:
        a=(i['Sns'])
        b=(a['Message'])
        y=json.loads(b)
        print(y['AlarmArn'])
        print(y['Region'])
        c=(y['Trigger'])
        print(c['Dimensions'])

awstask(event)
    




        
        
        


        
