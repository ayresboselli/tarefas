#
# Lista resgistros do banco de DynamoDB
#

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tarefas')

def lambda_handler(event, context):
    
    try:

        # verifica se o campo 'id' foi enviado por parâmetro
        if 'pathParameters' in event and 'id' in event['pathParameters']:

            # busca dados conforme o 'id' enviado por parâmetro
            response = table.get_item(
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            
            return response['Item']
        
        else:

            # lista todos os registros do banco
            response = table.scan()
            
            
            # ordena os resultados pela data de cadastro
            response['Items'].sort(key=lambda x: x['dataCadastro'])
            
            
            # converte o formato das datas
            cnt = 0
            while cnt < len(response['Items']):

                # data de cadastro
                datahora = response['Items'][cnt]['dataCadastro'].split('T')
                print(datahora)
                data = list(reversed(datahora[0].split('-')))
                response['Items'][cnt]['dataCadastro'] = ' '.join(['/'.join(data), datahora[1]])
                
                # data de finalização
                if response['Items'][cnt]['dataFinalizacao'] != None:
                    datahora = response['Items'][cnt]['dataFinalizacao'].split('T')
                    print(datahora)
                    data = list(reversed(datahora[0].split('-')))
                    response['Items'][cnt]['dataFinalizacao'] = ' '.join(['/'.join(data), datahora[1]])
                    
                cnt += 1
                
            return response['Items']
        
    except:
        
        return {
            'statusCode': 500,
            'body': json.dumps('Erro ao listar!')
        }
