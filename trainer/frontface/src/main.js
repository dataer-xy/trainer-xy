import Vue from 'vue'
import App from './App.vue'
import echarts from "echarts"
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.prototype.$echarts = echarts
// 引入基本模板
// let echart = require("echarts/lib/echarts")
// 引入 bar
require("echarts/lib/chart/bar")

Vue.config.productionTip = false

 
Vue.use(VueAxios, axios)
Vue.use(ElementUI)

new Vue({
  render: h => h(App),
}).$mount('#app')
