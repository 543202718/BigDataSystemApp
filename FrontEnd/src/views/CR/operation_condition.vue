<template>
<div>

    <div id="ListA">
        <h4 style="display: inline-block;margin:0;"></h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow">增加行</el-button>
            <el-button @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>

        </div>
        <el-table :data="testDatas" border style="width: 100%;margin-top:10px" max-height="600">
            <el-table-column v-if="testCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in testCols" :key="idx" :index="idx">
                <!--label-->
                <template slot="header" slot-scope="scope1">
                    <p>
                        {{column.txt}}
                    </p>
                </template>
                <!--prop-->
                <template slot-scope="scope">
                    <p v-show="scope.row[column.col].show" @dblclick="scope.row[column.col].show=false">
                        {{scope.row[column.col].content}}
                        <i class="el-icon-edit-outline" @click="scope.row[column.col].show=false"></i>
                    </p>
                    <el-input type="textarea" :autosize="{minRows:2,maxRows:4}" v-show="!scope.row[column.col].show" v-model="scope.row[column.col].content" @blur="scope.row[column.col].show=true">
                    </el-input>
                </template>
            </el-table-column>
        </el-table>
        <el-button type="primary" @click="addToStore">暂存此页</el-button>

    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            testCols: [{
                    col: "name",
                    txt: '操作名称'
                },
                {
                    col: "unit",
                    txt: '用量单位'
                },
                {
                    col: "value",
                    txt: '用量数值'
                }
            ],
            testDatas: [{
                    name: {
                        content: '预加氢反应压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '预加氢体积空速（RS-1）',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '预加氢反应器初期温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '预加氢反应器末期温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '预加氢氢油比(体)',
                        show: true
                    },
                    unit: {
                        content: 'Nm3/m3',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '预加氢化学氢耗',
                        show: true
                    },
                    unit: {
                        content: 'w%',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '蒸发塔塔顶温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '蒸发塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '蒸发塔塔底温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '蒸发塔重量回流比R/D',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '拔头油汽提塔塔顶温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '拔头油汽提塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '拔头油汽提塔塔底温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '拔头油汽提塔重量回流比R/D',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应C5+产品研究法辛烷值(RONC)',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应进料流量，',
                        show: true
                    },
                    unit: {
                        content: 'kg/h',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应重量平均入口温度WAIT',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应重量平均床层温度WABT',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应氢油(H2/HC)分子摩尔比',
                        show: true
                    },
                    unit: {
                        content: 'mol/mol',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应液时重量空速(LHSV)',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应体积空速(WHSV)',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应平均反应压力（表）',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应气液分离器压力（表）',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应气液分离器温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应C5＋产品液收',
                        show: true
                    },
                    unit: {
                        content: 'w%',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应芳烃产率',
                        show: true
                    },
                    unit: {
                        content: 'w%',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整反应纯氢产率',
                        show: true
                    },
                    unit: {
                        content: 'w%',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '1级再接触温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '2级再接触压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '2级再接触温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '3级再接触压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱戊烷塔塔顶温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱戊烷塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱戊烷塔塔底温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱戊烷塔重量回流比R/D',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱丁烷塔塔顶温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱丁烷塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱丁烷塔塔底温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱丁烷塔重量回流比R/D',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱C6塔塔顶温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱C7塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(g)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱C8塔塔底温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱C9塔重量回流比R/D',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生催化剂循环量',
                        show: true
                    },
                    unit: {
                        content: 'kg/h',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生第一烧焦入口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生第一烧焦入口压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生第二烧焦入口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生第二烧焦入口压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生氧氯化区入口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生氧氯化区入口压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生焙烧区入口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '烧焦再生焙烧区入口压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '还原一段操作温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '还原一段操作压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '还原二段操作温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '还原二段操作压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '洗涤罐罐顶操作压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '洗涤罐操作温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '抽提蒸馏塔塔顶温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '抽提蒸馏塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '抽提蒸馏塔塔底温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '抽提蒸馏塔溶剂/进料重量比',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '抽提蒸馏塔回流比R/D',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '抽提蒸馏塔贫溶剂进塔温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '抽提蒸馏塔C6馏分进塔温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '溶剂回收塔塔顶温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '溶剂回收塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '溶剂回收塔塔底温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '溶剂回收塔回流比R/D',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '溶剂再生罐罐顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa(a)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '溶剂再生罐罐底温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    }
                }

            ],
            count_col: 0,
            showMenu: false,
            curColumn: null,
        };

    },

    created: function () {
        console.log("turn to system page");
    },
    methods: {
        addToStore: function () {
            this.$store.operation_conditionInfo = {
                tableCols: null,
                tableDatas: null,
                operation_conditionInfo: null
            };
            this.$store.operation_conditionInfo.operation_conditionInfo = this.operation_conditionInfo; //额外内容
            this.$store.operation_conditionInfo.tableCols = this.testCols; //表头
            this.$store.operation_conditionInfo.tableDatas = this.testDatas; //表内容
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store operation_conditionInfo to device');
            console.log(this.$store.operation_conditionInfo.tableCols);
        },
        refreshTable() { //根据设置的塔创建表格
            for (var x in this.tower) {
                var _this = this
                this.testCols.push({
                    col: "tower" + x,
                    txt: this.tower[x]
                });
                this.testDatas.map(p => { // 新增的对象无法被vue监听到
                    _this.$set(p, "tower" + x, {
                        content: '',
                        show: true
                    })
                    //		p[obj.col] = {content: '', show: true}
                })
            }
            this.showTable = true
        },
        addRow() { // 新增行
            this.showMenu = false
            var obj = {}
            this.testCols.map(p => {
                obj[p.col] = {
                    content: '',
                    show: true
                }
            })
            this.testDatas.push(obj)
        },
        delLastRow() { // 删除行
            this.showMenu = false
            var len = this.testDatas.length;
            if (len > 0) this.testDatas.splice(len - 1, 1);
            else this.$message.error('没有可删除行');
        },
        consoleDatas() {
            console.log('表头', this.testCols);
            console.log('数据', this.testDatas);
        }
    }
}
</script>
