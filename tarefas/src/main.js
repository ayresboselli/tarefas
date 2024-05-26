import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all.js';
import 'sweetalert2/dist/sweetalert2.min.css';

import { createApp } from 'vue';
import { createRouter, createWebHistory  } from 'vue-router'
import Tarefas from './components/TarefasComp.vue';
import Editar from './components/EditarComp.vue';
import App from './App.vue';

// Rotas
const history = createWebHistory();
const routes = [
    { path: '/', component: Tarefas },
    { path: '/editar/:id?', component: Editar }
];

const router = new createRouter({ history, routes });

createApp(App)
.use(router)
.mount('#app');
