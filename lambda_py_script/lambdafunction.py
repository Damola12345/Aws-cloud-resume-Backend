from boto3 import resource

connection = resource('dynamodb')
table = connection.Table('Visitors')


def lambda_handler(event, context):
    record = table.get_item(Key={'Site': '1'})
    record.get('Item') or table.put_item(Item={'Site': '1', 'visitorCount': 0})

    item = table.get_item(Key={'Site': '1'}).get('Item')

    count = item.get('visitorCount') + 1
    table.put_item(Item={'Site': '1', 'visitorCount': count})
    return {
        'statusCode': 200,
        'body': count,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        }
    }