// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

/* 程序入口文件，加载各种公共组件 */
import Vue from 'vue'
import App from './App' /* 引入组件 */
import VCharts from 'v-charts' //直方图
import VueRouter from 'vue-router'
import routers from './router/index.js'
import Elements from 'element-ui'
import VueElementExtends from 'vue-element-extends'
import 'vue-element-extends/lib/index.css'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import store from './store/store.js'
import axios from 'axios'
import 'echarts/lib/chart/line'
import echarts from 'echarts'    


Vue.prototype.$echarts = echarts;
Vue.prototype.$axios = axios


Vue.use(VueElementExtends)
Vue.use(Elements)
Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(VCharts)
Vue.use(ElementUI);
Vue.use(store)

//const originalPush = VueRouter.prototype.push;

//VueRouter.prototype.push = function push(location) {
//    return originalPush.call(this, location).catch(err => err);
//};


const router = new VueRouter({
    mode: 'history',
    routes: routers
})

Vue.config.productionTip = true

/* eslint-disable no-new */
new Vue({ /* Vue实例化 */
    el: '#app',
    /* 将所有视图放在id值为app这个dom元素中 */
    router,
    store,
    /* 表明引入的文件，即上述的App.vue文件，这个文件的内容将以<App/>这样的标签写进去#app中 */
    components: { App },
    /* 告知当前页面想使用App这个组件 */
    template: '<App/>',
    /* 告知页面这个组件用这样的标签来包裹着,并且使用它 */
    render: h => h(App)
}).$mount('#app')