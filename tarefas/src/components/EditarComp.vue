<script>
import axios from 'axios';
import Swal from 'sweetalert2';

const api_url = "https://mfai4jz6ob.execute-api.us-west-2.amazonaws.com";

// CallBack de confirmação ao salvar o registro
function callback(response) {
    if(response.status == 200){
        Swal.fire({
            title: "Tarefa salva com sucesso",
            confirmButtonColor: "#0d6efd",
            icon: "success"
        }).then(()=>{
            location.href = "/"
        });
    }else{
        Swal.fire("Erro!", response.data, "danger");
    }
}

export default {
    name: "EditarComp",
    data() {
        return {
            titulo: "Nova tarefa",
            tarefa: {
                id: "",
                titulo: "",
                descricao: "",
                dataFinalizacao: null,
                dataCadastro: ""
            }
        }
    },
    methods: {
        // Busca o registro a ser editado
        getTarefas() {
            axios.get(
                api_url + '/' + this.$route.params.id,
                {
                    headers: {
                        "Cache-Control": "no-cache",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Access-Control-Allow-Origin": "*",
                    },
                }
            )
            .then(response=>{
                this.titulo = 'Atualizar tarefa'
                this.tarefa = response.data
            })
        },

        // salva o registro
        salvar() {

            // verifica se o campo 'Titulo' foi preenchido
            if(this.tarefa.titulo.length == 0){
                
                Swal.fire({
                    title: "O titulo é obrigatório",
                    confirmButtonColor: "#0d6efd",
                    icon: "warning"
                });

            }else{

                // verifica se existe 'id'
                if(this.tarefa.id.length > 0){

                    // edita registro já existente
                    axios.post(
                        api_url,
                        {
                            id: this.tarefa.id,
                            titulo: this.tarefa.titulo,
                            descricao: this.tarefa.descricao
                        }
                    ).then(callback)

                }else{

                    // insere novo registro
                    axios.put(
                        api_url,
                        {
                            titulo: this.tarefa.titulo,
                            descricao: this.tarefa.descricao
                        }
                    ).then(callback)

                }
            }
        }
    },

    mounted: function(){

        // verifica se foi enviado 'id' por parâmetro para buscar o registro para a aedição
        if(this.$route.params.id.length > 0){
            this.getTarefas()
        }

    }
}
</script>

<template>
    <div class="container mt-4">
        <div class="card mt-2">
            <div class="card-header">{{ titulo }}</div>
            <div class="card-body">
                
                <div class="mt-2">
                    <label>Titulo (obrigatório)</label>
                    <input v-model="tarefa.titulo" class="form-control">
                </div>
                
                <div class="mt-2">
                    <label>Descrição</label>
                    <textarea v-model="tarefa.descricao" class="form-control"></textarea>
                </div>

                <div class="mt-2">
                    <a href="/" class="btn btn-light me-2">Voltar</a>
                    <button @click="salvar()" class="btn btn-success">Salvar</button>
                </div>
                
            </div>
        </div>
    </div>
</template>