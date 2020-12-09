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
                    col: "unit",
                    txt: '单位'
                },
                {
                    col: "refiningValue1",
                    txt: '工况一精制'
                },
                {
                    col: "crackingValue1",
                    txt: '工况一裂化'
                },
                {
                    col: "refiningValue1",
                    txt: '工况二精制'
                },
                {
                    col: "crackingValue2",
                    txt: '工况二裂化'
                }
            ],
            testDatas: [{
                    name: {
                        content: '进料量',
                        show: true
                    },
                    unit: {
                        content: 't/h',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '',
                        show: true
                    },
                    refiningValue2: {
                        content: '288',
                        show: true
                    },
                    crackingValue2: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '冷高分压力',
                        show: true
                    },
                    unit: {
                        content: 'MPa',
                        show: true
                    },
                    refiningValue1: {
                        content: '≮17 / 0',
                        show: true
                    },
                    crackingValue1: {
                        content: '',
                        show: true
                    },
                    refiningValue2: {
                        content: '≮17.0',
                        show: true
                    },
                    crackingValue2: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '反应器入口氢油体积比',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    refiningValue1: {
                        content: '≮810 / 1',
                        show: true
                    },
                    crackingValue1: {
                        content: '',
                        show: true
                    },
                    refiningValue2: {
                        content: '≮810:1',
                        show: true
                    },
                    crackingValue2: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '催化剂',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    refiningValue1: {
                        content: '保护剂 / 精制剂',
                        show: true
                    },
                    crackingValue1: {
                        content: '裂化剂/补充精制剂',
                        show: true
                    },
                    refiningValue2: {
                        content: '保护剂/精制剂',
                        show: true
                    },
                    crackingValue2: {
                        content: '裂化剂/补充精制剂',
                        show: true
                    }
                },
                {
                    name: {
                        content: '精制部分保护剂催化剂用量',
                        show: true
                    },
                    unit: {
                        content: 'm3',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '-',
                        show: true
                    },
                    refiningValue2: {
                        content: '278',
                        show: true
                    },
                    crackingValue2: {
                        content: '-',
                        show: true
                    }
                },
                {
                    name: {
                        content: '精制部分保护剂体积空速',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '-',
                        show: true
                    },
                    refiningValue2: {
                        content: '11',
                        show: true
                    },
                    crackingValue2: {
                        content: '-',
                        show: true
                    }
                },
                {
                    name: {
                        content: '精制部分精制剂催化剂用量',
                        show: true
                    },
                    unit: {
                        content: 'm3',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '-',
                        show: true
                    },
                    refiningValue2: {
                        content: '332',
                        show: true
                    },
                    crackingValue2: {
                        content: '-',
                        show: true
                    }
                },
                {
                    name: {
                        content: '精制部分精制剂体积空速',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    refiningValue1: {
                        content: '0 / 9',
                        show: true
                    },
                    crackingValue1: {
                        content: '-',
                        show: true
                    },
                    refiningValue2: {
                        content: '0.9',
                        show: true
                    },
                    crackingValue2: {
                        content: '-',
                        show: true
                    }
                },
                {
                    name: {
                        content: '裂化部分裂化剂催化剂用量',
                        show: true
                    },
                    unit: {
                        content: 'm3',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '225',
                        show: true
                    },
                    refiningValue2: {
                        content: '-',
                        show: true
                    },
                    crackingValue2: {
                        content: '225',
                        show: true
                    }
                },
                {
                    name: {
                        content: '裂化部分裂化剂体积空速',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '1.3',
                        show: true
                    },
                    refiningValue2: {
                        content: '-',
                        show: true
                    },
                    crackingValue2: {
                        content: '1.3',
                        show: true
                    }
                },
                {
                    name: {
                        content: '裂化部分补充精制剂催化剂用量',
                        show: true
                    },
                    unit: {
                        content: 'm3',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '37',
                        show: true
                    },
                    refiningValue2: {
                        content: '-',
                        show: true
                    },
                    crackingValue2: {
                        content: '37',
                        show: true
                    }
                },
                {
                    name: {
                        content: '裂化部分补充精制剂体积空速',
                        show: true
                    },
                    unit: {
                        content: 'h-1',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '11',
                        show: true
                    },
                    refiningValue2: {
                        content: '-',
                        show: true
                    },
                    crackingValue2: {
                        content: '11',
                        show: true
                    }
                },
                {
                    name: {
                        content: '平均反应温度',
                        show: true
                    },
                    unit: {
                        content: '℃',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '388',
                        show: true
                    },
                    refiningValue2: {
                        content: '383',
                        show: true
                    },
                    crackingValue2: {
                        content: '395',
                        show: true
                    }
                },
                {
                    name: {
                        content: '反应器床层',
                        show: true
                    },
                    unit: {
                        content: '-',
                        show: true
                    },
                    refiningValue1: {
                        content: ' / ',
                        show: true
                    },
                    crackingValue1: {
                        content: '5',
                        show: true
                    },
                    refiningValue2: {
                        content: '4',
                        show: true
                    },
                    crackingValue2: {
                        content: '5',
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
