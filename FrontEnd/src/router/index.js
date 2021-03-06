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
import search from "@/views/AVDU/Search/search.vue";

const routers = [{
        path: "/",
        name: "Index",
        component: index,
        children: [{
                path: "/AVDU/input",
                component: input,
                children: [{
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
                component: search,
                
            },
            {
                path: "/AVDU/compare",
                component: () =>
                import ("@/views/AVDU/Compare/compare.vue"),
                //redirect:'/build_graph',
                children:[{
                    path: "/build_graph",
                        component: () =>
                            import ("@/views/AVDU/Compare/build_graph.vue"),
                }]

            },
            {
                path: "/CR/input",
                component: () =>
                    import ("@/views/CR/input.vue"),
                children: [{
                        path: "/CR/system",
                        component: () =>
                            import ("@/views/CR/system.vue"),
                    },
                    {
                        path: "/CR/material",
                        component: () =>
                            import ("@/views/CR/material.vue"),

                    },
                    {
                        path: "/CR/balance",
                        component: () =>
                            import ("@/views/CR/balance.vue"),
                    },
                    {
                        path: "/CR/chemical",
                        component: () =>
                            import ("@/views/CR/chemical.vue"),
                    },
                    {
                        path: "/CR/device",
                        component: () =>
                            import ("@/views/CR/device.vue"),
                    },
                    {
                        path: "/CR/investment",
                        component: () =>
                            import ("@/views/CR/investment.vue"),
                    },
                    {
                        path: "/CR/operation_condition",
                        component: () =>
                            import ("@/views/CR/operation_condition.vue"),
                    },
                    {
                        path: "/CR/product",
                        component: () =>
                            import ("@/views/CR/product.vue"),
                    },
                    {
                        path: "/CR/public_work",
                        component: () =>
                            import ("@/views/CR/public_work.vue"),
                    },
                    {
                        path: "/CR/waste",
                        component: () =>
                            import ("@/views/CR/waste.vue"),
                    }
                ]

            },
            {
                path: "/CR/search",
                component: () =>
                    import ("@/views/CR/search.vue")
            },
        ]
    },
    {
        path:"/AVDU/search/bar",
        name:"search_bar",
        component:() => 
        import("@/views/AVDU/Search/search_bar.vue"),
        children:[{
            path:"/AVDU/search/bar/system",
            component:() =>
            import("@/views/AVDU/Search/search_system.vue"),
        },
        {
            path:"/AVDU/search/bar/material",
            component:() =>
            import("@/views/AVDU/Search/search_material.vue"),
        },
        {
            path:"/AVDU/search/bar/product",
            component:() =>
            import("@/views/AVDU/Search/search_product.vue"),
        },
        {
            path:"/AVDU/search/bar/balance",
            component:() =>
            import("@/views/AVDU/Search/search_balance.vue"),
        },
        {
            path:"/AVDU/search/bar/operation_condition",
            component:() =>
            import("@/views/AVDU/Search/search_operation_condition.vue"),
        },
        {
            path:"/AVDU/search/bar/public_work",
            component:() =>
            import("@/views/AVDU/Search/search_public_work.vue"),
        },
        {
            path:"/AVDU/search/bar/investment",
            component:() =>
            import("@/views/AVDU/Search/search_investment.vue"),
        },
        {
            path:"/AVDU/search/bar/device",
            component:() =>
            import("@/views/AVDU/Search/search_device.vue"),
        },
        {
            path:"/AVDU/search/bar/waste",
            component:() =>
            import("@/views/AVDU/Search/search_waste.vue"),
        },
        {
            path:"/AVDU/search/bar/chemical",
            component:() =>
            import("@/views/AVDU/Search/search_chemical.vue"),
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