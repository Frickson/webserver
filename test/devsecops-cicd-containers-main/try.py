# import json

# dict1 = {}
# event = {"name": "Bob"}

# def testing(event):
#     dict1['name'] = event['name']
    
    
# def lambda_handler(event, context):
#     testing(event)
#     return {
#         'statusCode': 200,
#         'body': json.dumps(dict1)
# }


# x = lambda_handler(event, None)
# print(x)

import json
import base64
  
# Opening JSON file
f = open('test/devsecops-cicd-containers-main/try.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
f.close()
payload_str = json.dumps(data)
payload_b64 = base64.b64encode(payload_str.encode('utf-8')).decode('utf-8') 
json_object = json.dumps(payload_b64, indent=2)
 
# Writing to sample.json
with open("test/devsecops-cicd-containers-main/try.json", "w") as outfile:
    outfile.write(json_object)
# Iterating through the json
# list
  
# Closing file



