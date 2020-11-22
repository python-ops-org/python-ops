import requests
import boto3
import json


def lambda_handler():
#def sns_test():
    url = 'https://hooks.slack.com/services/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'
    headers = {'Content-Type': 'application/json'}
    json_data = {
                "channel": "#stest",
                "username": "sudipta",
                "text": "how are you"

                }
    r = requests.post(url,headers=headers,json=json_data)
    print r.text
#sns_test()

if __name__ == '__main__':
    lambda_handler()
