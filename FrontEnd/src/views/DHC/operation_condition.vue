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
                    txt: '单位'
                },
                {
                    col: "value",
                    txt: '值'
                },
            ],
            testDatas: [{
                    name: {
                        content: '精制部分新鲜原料进料量',
                        show: true
                    },
                    unit: {
                        content: 't/h',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分循环油量',
                        show: true
                    },
                    unit: {
                        content: 't/h',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分冷高分压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分反应器入口氢油体积比',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    refiningValue1: {
                        content: '≮610 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分催化剂',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    refiningValue1: {
                        content: '保护剂 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '裂化部分催化剂',
                        show: true
                    },
                    unit: {
                        content: '',
                        show: true
                    },
                    refiningValue1: {
                        content: '裂化剂 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分保护剂体积空速(新鲜进料)',
                        show: true
                    },
                    unit: {
                        content: 'm3',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分保护剂体积空速（包括循环油）',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分精制剂体积空速(新鲜进料)',
                        show: true
                    },
                    unit: {
                        content: 'm3',
                        show: true
                    },
                    refiningValue1: {
                        content: '1 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分精制剂体积空速（包括循环油）',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    refiningValue1: {
                        content: '2 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '裂化部分裂化剂体积空速(新鲜进料)',
                        show: true
                    },
                    unit: {
                        content: 'm3',
                        show: true
                    },
                    refiningValue1: {
                        content: '1 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '裂化部分裂化剂体积空速（包括循环油）',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    refiningValue1: {
                        content: '2 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '裂化部分补充精制剂体积空速(新鲜进料)',
                        show: true
                    },
                    unit: {
                        content: 'm3',
                        show: true
                    },
                    refiningValue1: {
                        content: '7 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '裂化部分补充精制剂体积空速（包括循环油）',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制部分平均反应温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '裂化部分平均反应温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '精制单程转化率',
                        show: true
                    },
                    unit: {
                        content: 'm%',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '裂化单程转化率',
                        show: true
                    },
                    unit: {
                        content: 'm%',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '反应进料加热炉入口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '反应进料加热炉出口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '反应进料加热炉入口压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '15 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '热高压分离器温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '热高压分离器压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '13 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '冷高压分离器温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '冷高压分离器压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '热低压分离器温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '热低压分离器压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '2 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '冷低压分离器温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '冷低压分离器压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '2 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '脱硫化氢塔温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '脱硫化氢塔压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '1 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '分馏塔温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '分馏塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '0 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '石脑油分馏塔温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '石脑油分馏塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '0 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '石脑油稳定塔温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '石脑油稳定塔塔顶压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '1 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '循环氢脱硫塔温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '循环氢脱硫塔压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '脱硫化氢塔底重沸炉入口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '脱硫化氢塔底重沸炉出口',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '脱硫化氢塔底重沸炉入口压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '1 / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '分馏塔底重沸炉入口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '分馏塔底重沸炉入口温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '分馏塔底重沸炉出口',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / a',
                        show: true
                    }

                },
                {
                    name: {
                        content: '分馏塔底重沸炉入口压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa（g）',
                        show: true
                    },
                    refiningValue1: {
                        content: '0 / a',
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
