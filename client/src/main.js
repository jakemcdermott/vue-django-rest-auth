import Vue from 'vue';

import App from './App';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

export default new Vue({
  router,
  store,
  el: '#app',
  template: '<App/>',
  components: { App },
});
