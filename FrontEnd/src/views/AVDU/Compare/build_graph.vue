<template>
<div class="echart_box">
    <div id="myChart" :style="{width: '800px', height: '600px',margin:'0 auto'}"></div>
</div>
</template>

<script>
export default {
    data() {
        return {
            graph: { //数据
                nodes: [ //节点
                    {

                        name: "兰州600万吨常减压装置", //名称
                        attributes: {},
                        id: "1", //id
                        category: 1, //类别
                        symbolSize: 50,
                        value: [
                            "石脑油产量: 48.79万吨/年",
                            "能耗: 500.0MJ/t",
                            "原料消耗量: 550万吨/年"
                        ],
                    },
                    {

                        name: "江西600万吨常减压装置", //名称
                        attributes: {},
                        id: "2", //id
                        category: 2, //类别
                        value: 10,
                        symbolSize: 20,
                        value: [
                            "石脑油产量: 49万吨/年 ",
                            "能耗: 460.0MJ",
                            "原料消耗量: 600万吨/年 "
                        ]
                    },
                    {

                        name: "某1200万吨常减压装置", //名称
                        attributes: {},
                        id: "3", //id
                        category: 3, //类别
                        value: [
                            "石脑油产量:95万吨/年",
                            "能耗:465.0MJ/t",
                            "原料消耗量: 1200万吨/年"
                        ],
                        symbolSize: 20,
                    },
                    {

                        name: "兰州1500万吨常减压装置", //名称
                        attributes: {},
                        id: "4", //id
                        category: 4, //类别
                        value: [
                            "石脑油产量:95万吨/年",
                            "能耗:465.0MJ/t",
                            "原料消耗量: 1500万吨/年"
                        ],
                        symbolSize: 20,
                    },
                    {

                        name: "江西400万吨常减压装置", //名称
                        attributes: {},
                        id: "5", //id
                        category: 5, //类别
                        value: 10,
                        symbolSize: 20,
                        value: [
                            "石脑油产量: 49万吨/年 ",
                            "能耗: 460.0MJ",
                            "原料消耗量: 600万吨/年 "
                        ]
                    },

                ],
                links: [ //连接
                    {
                        source: "1", //源点
                        target: "2", //目标
                        lineStyle: {
                            width: 5,
                            color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [{
                                    offset: 0,
                                    color: 'blue' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: 'black' // 100% 处的颜色
                                }],
                                global: false // 缺省为 false
                            }
                        },
                        value: "产能接近",
                    },
                    {
                        source: "3", //源点
                        target: "1", //目标
                        lineStyle: {
                            width: 5,
                            color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [{
                                    offset: 0,
                                    color: 'red' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: 'black' // 100% 处的颜色
                                }],
                                global: false // 缺省为 false
                            }
                        },
                        value: "能耗接近",
                    },
                    {
                        source: "4", //源点
                        target: "1", //目标
                        lineStyle: {
                            width: 5,
                            color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [{
                                    offset: 0,
                                    color: 'red' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: 'black' // 100% 处的颜色
                                }],
                                global: false // 缺省为 false
                            }
                        },
                        value: "地域接近",
                    },
                                        {
                        source: "5", //源点
                        target: "2", //目标
                        lineStyle: {
                            width: 5,
                            color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [{
                                    offset: 0,
                                    color: 'red' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: 'black' // 100% 处的颜色
                                }],
                                global: false // 缺省为 false
                            }
                        },
                        value: "地域接近",
                    },

                ]
            },
        }
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            var categories = [];
            for (var i = 0; i < 5; i++) {
                categories[i] = {
                    name: '类型' + i
                };
            }
            this.graph.nodes.forEach(function (node) {
                node.itemStyle = null; //
                // Use random x, y
                node.x = node.y = null;
                node.draggable = true;

            });
            // 基于准备好的dom，初始化echarts实例
            let myChart = this.$echarts.init(document.getElementById('myChart'))
            // 绘制图表
            myChart.setOption({
                title: {
                    text: '                                兰州600吨常减压装置'
                },
                tooltip: {

                    formatter: function (params) {
                        if (params.value.length == 3) {
                            return params.seriesName + ' :<br/>' +
                                params.value[0] +
                                params.value[1] +
                                params.value[2];
                        } else {
                            return '相关信息' + ' :<br/>' + params.value;
                        }
                    },
                },
                series: [{
                    name: '装置详情',
                    type: 'graph',
                    layout: 'force',
                    data: this.graph.nodes,
                    links: this.graph.links,
                    categories: categories,
                    roam: true,
                    label: {
                        position: 'right',
                        show: 'true'
                    },
                    force: {
                        repulsion: 3000
                    }
                }]
            });

        }
    }
}
</script>
