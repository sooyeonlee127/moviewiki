import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

Vue.config.productionTip = false

// Make BootstrapVue available throughout project
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)


new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
