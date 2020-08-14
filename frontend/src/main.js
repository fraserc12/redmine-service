import Vue from 'vue'
import App from './App.vue'
import vSelect from 'vue-select'
import VueGoodTablePlugin from 'vue-good-table';
import 'vue-select/dist/vue-select.css';
import 'vue-good-table/dist/vue-good-table.css'

Vue.component('v-select', vSelect)
Vue.config.productionTip = false
Vue.use(VueGoodTablePlugin);


new Vue({
  render: h => h(App),
}).$mount('#app')
