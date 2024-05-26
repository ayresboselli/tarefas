# TAREFAS

Este software tem o objetivo de gerenciar tarefas genéricas, que possuem os seguintes atributos:
- Titulo
- Descrição
- Data de cadastro 
- Data de finalização

O software possui apenas duas telas desenvolvidas de forma simples e intuitiva a fim de facilitar sua usabilidade.
Na primeira tela, as tarefas são exibidas em uma tabela, trazendo as tarefas pendentes no início e em seguida as tarefas finalizadas. Após esta classificação de status, a ordenação é por data de cadastro. Para o gerenciamento das tarefas, na última coluna da tabela, possui três botões:
- Finalizar: este botão só é exibido para as tarefas ainda pendentes;
- Editar: redireciona o usuário para a tela de edição da tarefa;
- Excluir: remove a tarefa da lista.

Outro componente na primeira tela é um botão para o cadastro de novas tarefas, o qual redireciona o usuário à tela de cadastro.
A segunda tela é o formulário de cadastro e edição das tarefas. Se o usuário for redirecionado através do botão de edição de cada tarefa, os dados serão carregados no formulário, caso contrário, os campos estarão em branco.
Os campos do formulário são apenas o Titulo, que é obrigatório e a descrição que é opcional. Abaixo destes campos, possui os botões de voltar, que redireciona o usuário para a tela inicial e o botão de salvar, que grava os dados e redireciona o usuário para a tela inicial.

# Estrutura
O software possui um frontend de interação com o usuário desenvolvido em Vue.js. A comunicação com o backend é feita através do protocolo HTTP com o serviço [API Gateway](https://aws.amazon.com/pt/api-gateway/) que interage com [Lambda](https://aws.amazon.com/pt/pm/lambda/) e persiste os dados no banco [DynamoDB](https://aws.amazon.com/pt/dynamodb/).
Os verbos utilizados para a comunicação entre o frontend e a API Gateway são:
- PUT: para a inserção de novas tarefas;
- POST: para a atualização e finalização das tarefas;
- GET: usado para a listagem de todas as tarefas ou de uma tarefa em específico, caso o id seja passado por parâmetro (URL/{id});
- DELETE: utilizado para a remoção de um registro, considerando que seu id seja enviado por parâmetro (URL/{id}).

Cada um dos verbos de requisição interage com uma função Lambda para sua execução. Estas funções são desenvolvidas em Python, retornando o valor esperado com o status 200 ou uma mensagem de erro com o status 500:
**tarefas_criar**: PUT;
**tarefas_atualizar**: POST;
**tarefas_ler**: GET;
**tarefas_excluir**: DELETE.

Todas as funções interagem com a tabela "tarefas" no DynamoDB.

