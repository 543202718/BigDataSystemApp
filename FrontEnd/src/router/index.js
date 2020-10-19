//  import Vue from "vue";
//  import Router from "vue-router"; /* 引入了路由插件vue-router */
import index from '@/views/index.vue'
import error from '@/views/error.vue'
import author from '@/views/author.vue'

const routers = [
{
    path: '/',
    name: 'Index',
    component: index
},
{
    path: '/author',
    name: 'Author',
    component: author
},
{
  path: '*',
  name: 'Error',
  component: error
}
]

export default routers
