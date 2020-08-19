import Vue from 'vue'
import App from './App.vue'
import vSelect from 'vue-select'
import VueGoodTablePlugin from 'vue-good-table';
import VueFormulate from '@braid/vue-formulate'
import Loading from 'vue-loading-overlay';

//styles
import 'vue-select/dist/vue-select.css';
import 'vue-good-table/dist/vue-good-table.css'
import './styles/snow.min.css'
import 'vue-loading-overlay/dist/vue-loading.css';

Vue.config.productionTip = false
Vue.use(VueFormulate)
Vue.use(VueGoodTablePlugin);
Vue.component('v-select', vSelect)
Vue.component('loading', Loading)

new Vue({
  render: h => h(App),
}).$mount('#app')