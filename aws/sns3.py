import boto3
from botocore.vendored import requests
import json
import argparse
import requests

def lambda_handler(event, context):
    print(event)
#def sns_test():
    url = 'https://hooks.slack.com/services/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'
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
    parser = argparse.ArgumentParser(description='Process Alerts and invoke SSM.')
    parser.add_argument("-ch")
    parser.add_argument("-user")
    parser.add_argument("-tex")
    args = parser.parse_args()
    event = {"ch": args.ch, "user": args.user, "tex": args.tex }
    lambda_handler(event, {})
#    lambda_handler()
