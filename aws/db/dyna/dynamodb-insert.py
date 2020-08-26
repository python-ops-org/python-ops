import boto3
import json

d = boto3.resource("dynamodb")
t = d.Table("library")
t.put_item (
        Item = {
            "books": "3",
            "author": "rowling",
            "title": "hogwart"

            }

)

