import json
import wikipedia

print('Loading function')

def lambda_handler(event, context):
    """Wikipedia Summarizer"""

    entity = event['entity']
    res = wikipedia.summary(entity, sentences=1)
    print(f'Response from wikipedia API: {res}')
    response = {
        'statusCode' : '200',
        'headers' : {'Content-type':'application/json'},
        'body' : json.dumps({'message':res})
    }

    return response
