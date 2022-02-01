import { createApp } from 'vue'
import { createStore } from 'vuex'

import App from './App.vue'
import router from './router'
import dataStore from './store/dataStore.js'
import modalControls from './store/modalControls.js'

const storeInstance = createStore({
    modules: {
        dataStore,
        modalControls
    }
})

createApp(App).use(router).use(storeInstance).mount('#app')
