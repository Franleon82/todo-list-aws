import json
import todoList

def translate(event, context):
    item = todoList.get_item(event['pathParameters']['id'])
    translation = todoList.translate_item(
        item['text'], event['pathParameters']['language'])
    return {
            "statusCode": 200,
            "body": json.dumps(translation)
        } if translation else {
            "statusCode": 404,
            "body": ""
        }
