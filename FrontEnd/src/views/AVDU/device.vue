<template>
<div id="hello">
    <div style="display: inline-block;float: right;">
        <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
        <el-button size="mini" type="primary" @click="addRow">增加行</el-button>

        <el-button @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>

    </div>
    <el-table :data="testDatas" border style="width: 100%;margin-top:10px" @header-contextmenu="colRightClick">
        <el-table-column v-if="testCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
        <el-table-column v-for="(column, idx) in testCols" :key="idx" :index="idx">
            <!--label-->
            <template slot="header" slot-scope="scope1">
                <p v-show="column.show" @dblclick="column.show=false">
                    {{column.txt}}
                </p>
                <el-input size="mini" v-show="!column.show" v-model="column.txt" @blur="column.show=true">
                </el-input>
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
</template>

<script>
export default {
    data() {
        return {
            testCols: [{
                    col: "type",
                    txt: '项目',
                    show: true
                },
                {
                    col: "internal",
                    txt: '国内订货/台数',
                    show: true
                },
                {
                    col: "overseas",
                    txt: '国外订货/台数',
                    show: true
                },
                {
                    col: "note",
                    txt: '备注',
                    show: true
                }
            ],
            testDatas: [{
                type: {
                    content: '塔器',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '冷换设备',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '空冷器',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '容器',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '机泵',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '其他机械设备',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '加热炉',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '热工设备',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '压缩机',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '电脱盐成套设备',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '机械抽空器',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }, {
                type: {
                    content: '其它',
                    show: true
                },
                internal: {
                    content: '',
                    show: true
                },
                overseas: {
                    content: '',
                    show: true
                },
                note: {
                    content: '',
                    show: true
                }
            }],
            count_col: 0,
            showMenu: false,
            curColumn: null,
            //systemInfo:{
            //    .....
            //}
        }
    },
    created: function () {
        console.log("turn to system page");
    },
    methods: {
        addToStore: function () {
            this.$store.deviceInfo = {
                tableCols: null,
                tableDatas: null
            };
            this.$store.deviceInfo.tableCols = this.testCols; //表头
            this.$store.deviceInfo.tableDatas = this.testDatas; //表内容
            console.log('store deviceInfo to device');
            console.log(this.$store.deviceInfo.tableCols);
        },

        colRightClick(column, event) {
            window.event.returnoverseas = false; //阻止浏览器自带的右键菜单弹出
            if (!column.index && column.index !== 0) return;
            this.curColumn = column.index
            this.showMenu = true
            var ele = document.getElementById('contextmenu')
            ele.style.top = event.clientY + 'px';
            ele.style.left = event.clientX + 'px';
            if (window.innerWidth - 140 < event.clientX) {
                ele.style.left = 'unset'
                ele.style.right = 0
            }
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
