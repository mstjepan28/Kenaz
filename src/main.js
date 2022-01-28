import { createApp } from 'vue'
import { createStore } from 'vuex'

import App from './App.vue'
import router from './router'
import store from './store/index.js'

const storeInstance = createStore(store)

createApp(App).use(router).use(storeInstance).mount('#app')
