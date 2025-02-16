import './assets/main.css'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { useAuthStore } from './stores/authStore';

import {createPinia} from "pinia";

const app = createApp(App)

app.use(router);
app.use(createPinia());

const authStore = useAuthStore()
authStore.getUserData()

app.mount('#app');
