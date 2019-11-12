import Vue from 'vue'
import App from './App.vue'

// echarts
import echarts from "echarts"
Vue.prototype.$echarts = echarts
// let echart = require("echarts/lib/echarts") // 引入基本模板
// require("echarts/lib/chart/bar") // 引入 bar

// element
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)


// axios
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

// swiper
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css' // require styles
Vue.use(VueAwesomeSwiper, /* { default global options } */)


// config
Vue.config.productionTip = false

 


// 实例化
new Vue({
  render: h => h(App),
}).$mount('#app')
