#
# Cadastra resgistros no banco de DynamoDB
#

import json
import boto3
import datetime
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tarefas')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    try:
        
        # inicializa variáveis
        body['id'] = uuid.uuid4().hex
        body['dataFinalizacao'] = None
        body['dataCadastro'] = datetime.datetime.now().isoformat()
        
        # insere dados no banco
        table.put_item(
           Item = {
                'id': body['id'],
                'titulo': body['titulo'],
                'descricao': body['descricao'],
                'dataFinalizacao': body['dataFinalizacao'],
                'dataCadastro': body['dataCadastro']
            }
        )
        
        return json.dumps(body)
        
    except:
        
        return {
            'statusCode': 200,
            'body': json.dumps('Erro ao cadastrar a tarefa!')
        }
