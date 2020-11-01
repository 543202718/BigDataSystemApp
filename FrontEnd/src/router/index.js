//  import Vue from "vue";
//  import Router from "vue-router"; /* 引入了路由插件vue-router */
import index from '@/views/index.vue'
import error from '@/views/error.vue'
import author from '@/views/author.vue'
import input from '@/views/changjianya/input.vue'
const routers = [{
        path: '/',
        name: 'Index',
        component: index,
        children: [{
            path: '/changjianya/input',
            component: input
        }, ]
    },
    {
        path: '/author',
        name: 'Author',
        component: author
    },
    /*
        {
            path: '/changjianya',
            name: 'Changjianya',
            component: changjianya,
            children: [{
                    path: 'input',
                    component: input
                },

            ]
        },
        */

    {
        path: '*',
        name: 'Error',
        component: error
    }
]

export default routers