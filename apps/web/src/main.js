import { createApp } from 'vue';
import router from './router';

import './index.css';

import App from './App.vue';

let app;

// Create Vue App
app = createApp(App);

// Modules
app.use(router);

// Mount App
app.mount('#app');
