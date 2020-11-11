<template>
<div>
    <el-form ref="form" :model="operation_conditionInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="原油进电脱盐温度（℃）">
            <el-input v-model="operation_conditionInfo.CrudeOilToDesaltTemp" placeholder="例：140"></el-input>
        </el-form-item>
        <el-form-item label="闪底油进常压炉温度（℃）">
            <el-input v-model="operation_conditionInfo.FlasBotmToAtmoFurnTemp" placeholder="例：300"></el-input>
        </el-form-item>
        <!--
        <el-form-item label="装置类别" style="text-align:left">
            <el-select v-model="operation_conditionInfo.system_id" filterable allow-create>
                <el-option label="炼油装置（燃料油）" value="炼油装置（燃料油）"></el-option>
                <el-option label="炼油装置（润滑油）" value="炼油装置（润滑油）"></el-option>
                <el-option label="化工装置" value="化工装置"></el-option>
                <el-option label="炼油化工一体化装置" value="炼油化工一体化装置"></el-option>
            </el-select>
        </el-form-item>

        <el-form-item label="装置性质" style="text-align:left">
            <el-radio-group v-model="operation_conditionInfo.tower_name">
                <el-radio-button label="新建"></el-radio-button>
                <el-radio-button label="改扩建"></el-radio-button>
            </el-radio-group>
        </el-form-item>

        <el-form-item label="设计完成时间">
            <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="operation_conditionInfo.unit" style="width: 100%;"></el-date-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="装置范围">
            <el-input type="textarea" :rows="2" placeholder="本装置主要由原油电脱盐脱水部分、换热网络及加热炉部分、常压蒸馏部分、减压蒸馏部分等组成，装置内考虑防腐设置有塔顶注氨、注缓蚀剂、注水设施。
" v-model="operation_conditionInfo.value">
            </el-input>
        </el-form-item>

        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>
-->
    </el-form>

    <div id="ListA">
        <h4 style="display: inline-block;margin:0;"></h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow">增加行</el-button>
            <el-button @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>

        </div>
        <el-table :data="testDatas" border height=500 style="width: 100%;margin-top:10px" @header-contextmenu="colRightClick">
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

        <div v-show="showMenu" id="contextmenu">
            <i class="el-icon-circle-close hideContextMenu" @click="showMenu=false"></i>
            <el-button size="mini" type="primary" @click="addColumn(curColumn)">前方插入一列</el-button>
            <el-button size="mini" type="primary" @click="addColumn(curColumn+1)">后方插入一列</el-button>
            <el-button @click="delColumn" slot="reference" type="primary" size="mini">删除当前列</el-button>

        </div>
    </div>

<el-button type="primary" @click="addToStore">暂存此页</el-button>
</div>
</template>

<script>
export default {
    data() {
        return {
            operation_conditionInfo: {
                CrudeOilToDesaltTemp: '',
                FlasBotmToAtmoFurnTemp: '',
            },
            testCols: [{
                    col: "name",
                    txt: '操作名称',
                    show: true
                },
                {
                    col: "unit",
                    txt: '单位',
                    show: true
                },
                {
                    col: "ShanZheng_value",
                    txt: '闪蒸塔',
                    show: true
                },
                {
                    col: "ChuLiu_value",
                    txt: '初馏塔',
                    show: true
                }, {
                    col: "Changya_value",
                    txt: '常压塔',
                    show: true
                }, {
                    col: "Jianya_value",
                    txt: '减压塔',
                    show: true
                }
            ],
            testDatas: [ {
                name: {
                    content: '塔顶温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '一线温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '二线温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '三线温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '闪蒸段温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '塔底温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '塔顶回流温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '顶循抽出温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '顶循返回温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '一中抽出温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '一中返回温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '二中抽出温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '二中返回温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '汽提蒸汽温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '炉出口分支温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '-',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '塔顶压力',
                    show: true
                },
                unit: {
                    content: 'MPa(g),减压塔:mmHg(a)',
                    show: true
                },
                ShanZheng_value: {
                    content: '',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '闪蒸段压力',
                    show: true
                },
                unit: {
                    content: 'MPa(g),减压塔:mmHg(a)',
                    show: true
                },
                ShanZheng_value: {
                    content: '',
                    show: true
                },
                ChuLiu_value: {
                    content: '',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '',
                    show: true
                }
            }, {
                name: {
                    content: '一线吹汽量',
                    show: true
                },
                unit: {
                    content: 'kg/h',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '-',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '-',
                    show: true
                }
            }, {
                name: {
                    content: '二线吹汽量',
                    show: true
                },
                unit: {
                    content: 'kg/h',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '-',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '-',
                    show: true
                }
            }, {
                name: {
                    content: '塔底吹汽量',
                    show: true
                },
                unit: {
                    content: 'kg/h',
                    show: true
                },
                ShanZheng_value: {
                    content: '-',
                    show: true
                },
                ChuLiu_value: {
                    content: '-',
                    show: true
                },
                Changya_value: {
                    content: '',
                    show: true
                },
                Jianya_value: {
                    content: '-',
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
        addToStore: function () {
            this.$store.operation_conditionInfo={
                tableCols:null,
                tableDatas:null,
                operation_conditionInfo:null
            };
            this.$store.operation_conditionInfo.operation_conditionInfo = this.operation_conditionInfo;//表头
            this.$store.operation_conditionInfo.tableCols = this.testCols;//表头
            this.$store.operation_conditionInfo.tableDatas = this.testDatas;//表内容
            console.log('store operation_conditionInfo to device');
            console.log(this.$store.operation_conditionInfo.tableCols);
        },
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
