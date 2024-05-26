#
# Atualiza resgistros já existentes no banco de DynamoDB
#

import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tarefas')


def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    try:
        
        # Verifica se o campo 'dataFinalizacao' possui o valor 'finalizar'
        if 'dataFinalizacao' in body and body['dataFinalizacao'] == 'finalizar':
            
            # insere a data de finalização da tarefa
            table.update_item(
                Key={
                    'id': body['id']
                },
                UpdateExpression='SET dataFinalizacao = :dataFinalizacao',
                ExpressionAttributeValues={
                    ':dataFinalizacao': datetime.datetime.now().isoformat()
                }
            )
            
        else:
            
            # atualiza os campos
            table.update_item(
                Key={
                    'id': body['id']
                },
                UpdateExpression='SET titulo = :titulo, descricao = :descricao',
                ExpressionAttributeValues={
                    ':titulo': body['titulo'],
                    ':descricao': body['descricao'],
                }
            )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Tarefa atualizada!')
        }
    
    except:
        
        return {
            'statusCode': 500,
            'body': json.dumps('Erro ao atualizar a tarefa!')
        }
    