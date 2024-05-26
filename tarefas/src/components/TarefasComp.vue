<script>
import axios from 'axios'
import Swal from 'sweetalert2'

const api_url = "https://mfai4jz6ob.execute-api.us-west-2.amazonaws.com";

export default {
    name: "TarefasComp",
    data() {
        return {
            tarefas: []
        }
    },
    methods: {
        // Busca as tarefas da fnção Lambda
        getTarefas() {
            axios.get(
                api_url,
                {
                    headers: {
                        "Cache-Control": "no-cache",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Access-Control-Allow-Origin": "*",
                    },
                }
            )
            .then(response=>{
                let lista = []

                // insere as tarefas pendentes na lista
                response.data.map(r=>{
                    if(r.dataFinalizacao == null){
                        lista.push(r)
                    }
                })

                // insere as tarefas finalizadas na lista
                response.data.map(r=>{
                    if(r.dataFinalizacao != null){
                        lista.push(r)
                    }
                })

                this.tarefas = lista
            })
        },

        // finaliza uma tarefa
        finalizarTarefa(id) {
            Swal.fire({
                title: "Tem certeza que deseja finalizar esta tarefa?",
                showCancelButton: true,
                confirmButtonText: "Finalizar",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#198754"
            }).then((result) => {

                // verifica se o usuário clicou em Finalizar
                if (result.isConfirmed) {
                    axios.post(
                        api_url,
                        {
                            id:id,
                            dataFinalizacao: 'finalizar'
                        }
                    ).then(response=>{

                        if(response.status == 200){
                            Swal.fire({
                                title: "Tarefa finalizada com sucesso",
                                confirmButtonColor: "#0d6efd",
                                icon: "success"
                            });
                            
                            this.getTarefas()
                        }else{
                            Swal.fire("Erro!", response.data, "danger");
                        }

                    })
                }
            });
        },

        // redireciona para a tela de edição
        alterarTarefa(id) {
            location.href = '/editar/' + id
        },

        // exclui o registro
        excluirTarefa(id) {
            Swal.fire({
                title: "Tem certeza que deseja excluir esta tarefa?",
                showCancelButton: true,
                confirmButtonText: "Excluir",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33"
            }).then((result) => {

                // verifica se o usuário clicou em Excluir
                if (result.isConfirmed) {
                    axios.delete(api_url + '/' + id).then(response=>{

                        if(response.status == 200){
                            Swal.fire({
                                title: response.data,
                                confirmButtonColor: "#0d6efd",
                                icon: "success"
                            });

                            this.getTarefas()
                        }else{
                            Swal.fire("Erro!", response.data, "danger");
                        }
                    })
                }

            });
        }
    },

    mounted: function(){
        // busca os registros ao carregar a página
        this.getTarefas()
    }
}
</script>

<template>
    <div class="container mt-4">
        <a href="/editar" class="btn btn-success">Nova tarefa</a>
        <table class="table table-bordered table-striped table-hover mt-4">
            <thead>
                <tr>
                    <th>Titulo</th>
                    <th>Descrição</th>
                    <th>Status</th>
                    <th>Data de cadastro</th>
                    <th></th>
                </tr>
            </thead>
            <tbody v-for="(tarefa, index) in tarefas" :key="index">
                <tr>
                    <td>{{ tarefa.titulo }}</td>
                    <td>{{ tarefa.descricao }}</td>
                    <td>
                        <span class="text-warning" v-if="tarefa.dataFinalizacao == null">Pendente</span>
                        <span class="text-success" v-else>Finalizado em {{ tarefa.dataFinalizacao }}</span>
                    </td>
                    <td>{{ tarefa.dataCadastro }}</td>
                    <td class="text-end">
                        <div class="botao" v-show="tarefa.dataFinalizacao == null" @click="finalizarTarefa( tarefa.id )">
                            <span title="Finalizar" class="text-success fa fa-download ms-3"></span>
                        </div>
                        <div class="botao" @click="alterarTarefa( tarefa.id )">
                            <span title="Alterar" class="text-primary fa fa-edit ms-3"></span>
                        </div>
                        <div class="botao" @click="excluirTarefa( tarefa.id )">
                            <span title="Excluir" class="text-danger fa fa-trash ms-3"></span>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>