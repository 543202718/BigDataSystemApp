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
                    txt: '用量单位'
                },
                {
                    col: "unit",
                    txt: '用量数值'
                },
                {
                    col: "type",
                    txt: '类别'
                },
                {
                    col: "pattern",
                    txt: '型号或规格'
                },
                {
                    col: "transport",
                    txt: '运输方式'
                },
                {
                    col: "note",
                    txt: '备注'
                }
            ],
            testDatas: [{
                    name: { content: '破乳剂', show: true },
                    value: { content: '', show: true },
                    unit: { content: '年用量t / a', show: true },
                    type: { content: '油溶性/水溶性', show: true },
                    pattern: { content: '', show: true },
                    transport: { content: '桶装', show: true },
                    note: { content: '', show: true }
                },
                {
                    name: {
                        content: '反向破乳剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '年用量t / a',
                        show: true
                    },

                    type: {
                        content: '油溶性/水溶性',
                        show: true
                    },

                    pattern: {
                        content: '',
                        show: true
                    },

                    transport: {
                        content: '桶装',
                        show: true
                    },

                    note: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '缓蚀剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '年用量t / a',
                        show: true
                    },

                    type: {
                        content: '油溶性/水溶性',
                        show: true
                    },

                    pattern: {
                        content: 'BZH-1或尼凡丁-18',
                        show: true
                    },

                    transport: {
                        content: '桶装',
                        show: true
                    },

                    note: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '高温缓蚀剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '年用量t / a',
                        show: true
                    },

                    type: {
                        content: '油溶性',
                        show: true
                    },

                    pattern: {
                        content: '',
                        show: true
                    },

                    transport: {
                        content: '桶装',
                        show: true
                    },

                    note: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '磷酸三钠',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '年用量t / a',
                        show: true
                    },

                    type: {
                        content: '100%',
                        show: true
                    },

                    pattern: {
                        content: '',
                        show: true
                    },

                    transport: {
                        content: '桶装',
                        show: true
                    },

                    note: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '胺液/贫胺液',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '用量t / h',
                        show: true
                    },

                    type: {
                        content: '30%',
                        show: true
                    },

                    pattern: {
                        content: '30%MDEA水溶液',
                        show: true
                    },

                    transport: {
                        content: '管道',
                        show: true
                    },

                    note: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '氨',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '年用量t / a或者用量t / h',
                        show: true
                    },

                    type: {
                        content: '_____氨水浓度/纯氨',
                        show: true
                    },

                    pattern: {
                        content: '氨水/纯氨',
                        show: true
                    },

                    transport: {
                        content: '管道',
                        show: true
                    },

                    note: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '脱钙剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '年用量t / a',
                        show: true
                    },

                    type: {
                        content: '油溶性/水溶性',
                        show: true
                    },

                    pattern: {
                        content: '',
                        show: true
                    },

                    transport: {
                        content: '桶装',
                        show: true
                    },

                    note: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '有机胺',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '年用量t / a',
                        show: true
                    },

                    type: {
                        content: '-',
                        show: true
                    },

                    pattern: {
                        content: '',
                        show: true
                    },

                    transport: {
                        content: '桶装',
                        show: true
                    },

                    note: {
                        content: '',
                        show: true
                    }
                },
                {
                    name: {
                        content: '阻垢剂',
                        show: true
                    },
                    value: {
                        content: '',
                        show: true
                    },
                    unit: {
                        content: '年用量t / a',
                        show: true
                    },

                    type: {
                        content: '油溶性',
                        show: true
                    },

                    pattern: {
                        content: '',
                        show: true
                    },

                    transport: {
                        content: '桶装',
                        show: true
                    },

                    note: {
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
