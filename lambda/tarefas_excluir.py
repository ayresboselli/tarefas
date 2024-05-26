#
# Remove resgistro do banco de DynamoDB
#

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tarefas')


def lambda_handler(event, context):
    
    try:
        
        # remove o registro conforme 'id' enviado por parâmetro
        table.delete_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
    
        return {
            'statusCode': 200,
            'body': json.dumps('Tarefa excluída com sucesso!')
        }
        
    except:
        
        return {
            'statusCode': 500,
            'body': json.dumps('Erro ao excluir!')
        }
    