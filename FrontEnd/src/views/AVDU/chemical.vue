<template>
<div>
        <!--    <el-form ref="form" :model="chemicalInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="项目名称">
            <el-input v-model="chemicalInfo.name" placeholder="例：xx科技有限公司1000万吨/年的炼油化工一体项目"></el-input>
        </el-form-item>

        <el-form-item label="装置类别" style="text-align:left">
            <el-select v-model="chemicalInfo.system_id" filterable allow-create>
                <el-option label="炼油装置（燃料油）" value="炼油装置（燃料油）"></el-option>
                <el-option label="炼油装置（润滑油）" value="炼油装置（润滑油）"></el-option>
                <el-option label="化工装置" value="化工装置"></el-option>
                <el-option label="炼油化工一体化装置" value="炼油化工一体化装置"></el-option>
            </el-select>
        </el-form-item>

        <el-form-item label="装置性质" style="text-align:left">
            <el-radio-group v-model="chemicalInfo.tower_name">
                <el-radio-button label="新建"></el-radio-button>
                <el-radio-button label="改扩建"></el-radio-button>
            </el-radio-group>
        </el-form-item>

        <el-form-item label="设计完成时间">
            <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="chemicalInfo.unit" style="width: 100%;"></el-date-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="装置范围">
            <el-input type="textarea" :rows="2" placeholder="本装置主要由原油电脱盐脱水部分、换热网络及加热炉部分、常压蒸馏部分、减压蒸馏部分等组成，装置内考虑防腐设置有塔顶注氨、注缓蚀剂、注水设施。
" v-model="chemicalInfo.value">
            </el-input>
        </el-form-item>

        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>

    </el-form>
-->
    <div id="ListA">
        <h4 style="display: inline-block;margin:0;"></h4>
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
                        <i class="el-icon-edit-outline" @click="column.show=false"></i>
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
 <!--
        <div v-show="showMenu" id="contextmenu">
            <i class="el-icon-circle-close hideContextMenu" @click="showMenu=false"></i>
            <el-button size="mini" type="primary" @click="addColumn(curColumn)">前方插入一列</el-button>
            <el-button size="mini" type="primary" @click="addColumn(curColumn+1)">后方插入一列</el-button>
            <el-button @click="delColumn" slot="reference" type="primary" size="mini">删除当前列</el-button>

        </div>
-->
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            chemicalInfo: {},
            testCols: [{
                    col: "name",
                    txt: '药剂名称',
                    show: true
                },
                {
                    col: "value",
                    txt: '用量单位',
                    show: true
                },
                {
                    col: "unit",
                    txt: '用量数值',
                    show: true
                },
                {
                    col: "type",
                    txt: '类别',
                    show: true
                },
                {
                    col: "pattern",
                    txt: '型号或规格',
                    show: true
                },
                {
                    col: "transport",
                    txt: '运输方式',
                    show: true
                },
                {
                    col: "note",
                    txt: '备注',
                    show: true
                }
            ],
            testDatas: [{
                    name: {
                        content: '破乳剂',
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
            }],
            count_col: 0,
            showMenu: false,
            curColumn: null,
        };

    },

    created: function () {
        console.log("turn to system page");
    },
    methods: {
        colRightClick(column, event) {
            window.event.returnValue = false; //阻止浏览器自带的右键菜单弹出
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
        // 当row中存在一“主键”可唯一标识row的下标时（如：编号放在testDatas内），可借此实现行的自由插入与删除
        addColumn(idx) { // 新增列
            this.showMenu = false
            var obj = {
                col: 'col_' + this.count_col++,
                txt: '',
                show: true
            }
            if (idx || idx === 0) this.testCols.splice(idx, 0, obj);
            else this.testCols.push(obj);
            var _this = this
            this.testDatas.map(p => { // 新增的对象无法被vue监听到
                _this.$set(p, obj.col, {
                    content: '',
                    show: true
                })
                //		p[obj.col] = {content: '', show: true}
            })
        },
        delColumn() { // 删除列
            this.showMenu = false
            var colKey = this.testCols[this.curColumn].col;
            this.testCols.splice(this.curColumn, 1);
            this.testDatas.map(p => {
                delete p[colKey];
            });
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
