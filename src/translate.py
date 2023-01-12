import json
import todoList


def translate(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    translation = todoList.translate_item(
        item['text'], event['pathParameters']['language'])
    if translation:
        response = {
            "statusCode": 200,
            "body": json.dumps(translation)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response