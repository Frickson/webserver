import json

dict1 = {}
event = {"name": "Bob"}

def testing(event):
    dict1['name'] = event['name']
    
    
def lambda_handler(event, context):
    testing(event)
    return {
        'statusCode': 200,
        'body': json.dumps(dict1)
}


x = lambda_handler(event, None)
print(x)