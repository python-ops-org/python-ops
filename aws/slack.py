import boto3
from botocore.vendored import requests
import json


def lambda_handler(event, context):
    print(event)
#def sns_test():
    url = ''
    headers = {'Content-Type': 'application/json'}
    """
    json_data = {
                "channel": "#stest",
                "username": "sudipta",
                "text": "how are you"

                }
     """
    json_data = {
                "channel": event["ch"],
                "username": event["user"],
                "text":  event["tex"]

                }
     
    r = requests.post(url,headers=headers,json=json_data)
    print(r.text)
#sns_test()

if __name__ == '__main__':
    lambda_handler()
