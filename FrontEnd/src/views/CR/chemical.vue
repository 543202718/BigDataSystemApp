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
                    txt: '药剂名称'
                },
                {
                    col: "value",
                    txt: '用量数值'
                },
                {
                    col: "unit",
                    txt: '用量单位'
                },
                {
                    col: "lifetime",
                    txt: '寿命/年'
                },
                {
                    col: "pattern",
                    txt: '类别'
                },
            ],
            testDatas: [{
                    name: {
                        content: '预加氢催化剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '吨 / 一次装入量',
                        show: true
                    },
                    lifetime: {
                        content: '寿命：四年',
                        show: true
                    },
                    pattern: {
                        content: '拟采用XX石油化工科学研究院（RXPP）研究开发的RS-X催化剂或者与其相当的其它催化剂',
                        show: true
                    }
                },
                {
                    name: {
                        content: '预加氢脱氯剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '吨 / 一次装入量',
                        show: true
                    },
                    lifetime: {
                        content: '寿命：二年',
                        show: true
                    },
                    pattern: {
                        content: '用于脱除预加氢生成油的氯化氢，拟采用XXPP研究开发的XXL-A 高温脱氯剂或性能相当的国内其它类似产品',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整催化剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '吨 / 一次装入量',
                        show: true
                    },
                    lifetime: {
                        content: '寿命：六年',
                        show: true
                    },
                    pattern: {
                        content: '采用国产PS-XX连续重整催化剂',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整氢气脱氯剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '吨 / 一次装入量',
                        show: true
                    },
                    lifetime: {
                        content: '寿命：一年',
                        show: true
                    },
                    pattern: {
                        content: '用于脱去重整产氢气体中的氯化物，拟采用XX化工研究院研制的T-40X活性氧化铝脱氯剂或性能相当的类似产品。',
                        show: true
                    }
                },
                {
                    name: {
                        content: '重整油脱氯剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '吨 / 一次装入量',
                        show: true
                    },
                    lifetime: {
                        content: '寿命：一年',
                        show: true
                    },
                    pattern: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱砷剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '吨 / 一次装入量',
                        show: true
                    },
                    lifetime: {
                        content: '寿命：一年',
                        show: true
                    },
                    pattern: {
                        content: '脱砷剂拟采用国产RAs-X',
                        show: true
                    }
                },
                {
                    name: {
                        content: '二甲基二硫(DMDS)',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: ' / ',
                        show: true
                    },
                    lifetime: {
                        content: '-',
                        show: true
                    },
                    pattern: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '全氯乙烯',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: ' / ',
                        show: true
                    },
                    lifetime: {
                        content: '-',
                        show: true
                    },
                    pattern: {
                        content: '',
                        show: true
                    }
                },

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
            this.$store.chemicalInfo = {
                tableCols: null,
                tableDatas: null
            };
            this.$store.chemicalInfo.tableCols = this.tableCols; //表头
            this.$store.chemicalInfo.tableDatas = this.tableDatas; //表格内容
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store chemicalInfo to device');
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
