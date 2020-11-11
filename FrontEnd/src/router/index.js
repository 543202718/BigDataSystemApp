//  import Vue from "vue";
//  import Router from "vue-router"; /* 引入了路由插件vue-router */
import index from "@/views/index.vue";
import error from "@/views/error.vue";
import author from "@/views/author.vue";
import input from "@/views/AVDU/input.vue";
import system from "@/views/AVDU/system.vue";
import material from "@/views/AVDU/material.vue";
import balance from "@/views/AVDU/balance.vue";
import chemical from "@/views/AVDU/chemical.vue";
import device from "@/views/AVDU/device.vue";
import investment from "@/views/AVDU/investment.vue";
import operation_condition from "@/views/AVDU/operation_condition.vue";
import product from "@/views/AVDU/product.vue";
import public_work from "@/views/AVDU/public_work.vue";
import waste from "@/views/AVDU/waste.vue";
import search from "@/views/AVDU/search.vue";

const routers = [
    {
        path: "/",
        name: "Index",
        component: index,
        children: [
            {
                path: "/AVDU/input",
                component: input,
                children: [
                    {
                        path: "/AVDU/system",
                        component: system
                    },
                    {
                        path: "/AVDU/material",
                        component: material
                    },
                    {
                        path: "/AVDU/balance",
                        component: balance
                    },
                    {
                        path: "/AVDU/chemical",
                        component: chemical
                    },
                    {
                        path: "/AVDU/device",
                        component: device
                    },
                    {
                        path: "/AVDU/investment",
                        component: investment
                    },
                    {
                        path: "/AVDU/operation_condition",
                        component: operation_condition
                    },
                    {
                        path: "/AVDU/product",
                        component: product
                    },
                    {
                        path: "/AVDU/public_work",
                        component: public_work
                    },
                    {
                        path: "/AVDU/waste",
                        component: waste
                    }
                ]
            },
            {
                path: "/AVDU/search",
                component: search
            }
        ]
    },
    {
        path: "/author",
        name: "Author",
        component: author
    },
    {
        path: "*",
        name: "Error",
        component: error
    }
];

export default routers;
