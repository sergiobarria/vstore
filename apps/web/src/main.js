import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router';

import './index.css';

import App from './App.vue';

// prettier-ignore
createApp(App)
  .use(router)
  .use(createPinia())
  .mount('#app');
