import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("library")

def lambda_handler(event, context):
    query = event.get("query", "all")
    #Without filter
    if query == "all":
        response = table.scan()
        data = response["Items"]
    else:
    #With filter
        
        response = table.query(
            KeyConditionExpression=Key('books').eq(query)
            )
        data = response["Items"]



    
    return "\n".join([str(value) for value in data])

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", dest="command",  required=False, type=str, help="Command")
    parser.add_argument("-q", dest="query",    required=False, type=str, help="Query")
    args = parser.parse_args()

    if args.command == "fetch":
        event = {
            "query": args.query
        }
        response = lambda_handler(event, None)
        print(response)
    else:
        print(f"{args.command} not mapped")

if __name__ == "__main__":
    main()
