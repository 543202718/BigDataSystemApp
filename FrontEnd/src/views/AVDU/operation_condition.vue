<template>
<div>
    <el-form ref="form" :model="operation_conditionInfo" label-width="200px" size="mini" style="margin-top: 20px">
        <el-form-item label="原油进电脱盐温度（℃）">
            <el-input v-model="operation_conditionInfo.CrudeOilToDesaltTemp" placeholder="例：140"></el-input>
        </el-form-item>
        <el-form-item label="闪底油进常压炉温度（℃）">
            <el-input v-model="operation_conditionInfo.FlasBotmToAtmoFurnTemp" placeholder="例：300"></el-input>
        </el-form-item>
    </el-form>

    <div id="ListA">
        <h4 style="display: inline-block;margin:0;">不同设备中的操作条件</h4>
        <div style="display: inline-block;float: right;" v-if="showTable">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow">增加行</el-button>
            <el-button @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <br><br>
        <div>
            设备
            <el-select v-model="tower" multiple filterable allow-create :disabled="showTable" placeholder="请选择设备">
                <el-option label="闪蒸塔" value="闪蒸塔"></el-option>
                <el-option label="初馏塔" value="初馏塔"></el-option>
                <el-option label="常压塔" value="常压塔"></el-option>
                <el-option label="减压塔" value="减压塔"></el-option>
            </el-select>
            <el-button type="primary" @click="createTable" v-if="!showTable">生成表格</el-button>
            <el-button type="primary" @click="refreshTable" v-if="showTable">重建表格</el-button>
        </div>
        <el-table v-if="showTable" :data="testDatas" border max-height="500" style="width: 100%;margin-top:10px">
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

    </div>

    <el-button type="primary" @click="addToStore">暂存此页</el-button>
</div>
</template>

<script>
export default {
    data() {
        return {
            showTable: false,
            tower: ["闪蒸塔", "初馏塔", "常压塔", "减压塔"],
            operation_conditionInfo: {
                CrudeOilToDesaltTemp: '',
                FlasBotmToAtmoFurnTemp: '',
            },
            testCols: [{ col: "name", txt: '操作名称' },
                { col: "unit", txt: '单位' },
            ],
            testDatas: [{
                name: {
                    content: '塔顶温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '一线温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '二线温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '三线温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '闪蒸段温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '塔底温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '塔顶回流温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '顶循抽出温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '顶循返回温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '一中抽出温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '一中返回温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '二中抽出温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '二中返回温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '汽提蒸汽温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '炉出口分支温度',
                    show: true
                },
                unit: {
                    content: '℃',
                    show: true
                },
            }, {
                name: {
                    content: '塔顶压力',
                    show: true
                },
                unit: {
                    content: 'MPa(g),减压塔:mmHg(a)',
                    show: true
                },
            }, {
                name: {
                    content: '闪蒸段压力',
                    show: true
                },
                unit: {
                    content: 'MPa(g),减压塔:mmHg(a)',
                    show: true
                },
            }, {
                name: {
                    content: '一线吹汽量',
                    show: true
                },
                unit: {
                    content: 'kg/h',
                    show: true
                },
            }, {
                name: {
                    content: '二线吹汽量',
                    show: true
                },
                unit: {
                    content: 'kg/h',
                    show: true
                },
            }, {
                name: {
                    content: '塔底吹汽量',
                    show: true
                },
                unit: {
                    content: 'kg/h',
                    show: true
                },
            }],
            count_col: 0,
        };

    },

    created: function () {
        console.log("turn to system page");
        if ('operation_conditionInfo' in this.$store) {
            this.testCols = this.$store.operation_conditionInfo.tableCols;
            this.testDatas = this.$store.operation_conditionInfo.tableDatas;
            this.operation_conditionInfo = this.$store.operation_conditionInfo.operation_conditionInfo;
            this.showTable = this.$store.operation_conditionInfo.showTable;
            this.tower = this.$store.operation_conditionInfo.tower;
            this.count_col = this.$store.operation_conditionInfo.count_col;
        }
    },
    methods: {
        addToStore: function () {
            this.$store.operation_conditionInfo = {
                tableCols: null,
                tableDatas: null,
                operation_conditionInfo: null,
                showTable: null,
                tower: null,
                count_col: null,
            };
            this.$store.operation_conditionInfo.operation_conditionInfo = this.operation_conditionInfo; //额外内容
            this.$store.operation_conditionInfo.tableCols = this.testCols; //表头
            this.$store.operation_conditionInfo.tableDatas = this.testDatas; //表内容
            this.$store.operation_conditionInfo.showTable = this.showTable;
            this.$store.operation_conditionInfo.tower = this.tower;
            this.$store.operation_conditionInfo.count_col = this.count_col;
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store operation_conditionInfo to device');
            console.log(this.$store.operation_conditionInfo.tableCols);
        },
        createTable() { //根据设置的塔创建表格
            for (var x in this.tower) {
                var _this = this;
                var hasSameCol = false;
                for (var i in this.testCols) { //已存在的列不需要插入
                    if (this.testCols[i].txt == this.tower[x]) {
                        hasSameCol = true;
                        break;
                    }
                }
                if (hasSameCol) continue;
                this.testCols.push({
                    col: "tower" + this.count_col,
                    txt: this.tower[x]
                });
                this.testDatas.map(p => { // 新增的对象无法被vue监听到
                    _this.$set(p, "tower" + this.count_col, { content: '', show: true })
                })
                this.count_col++;
            }
            var len = this.testCols.length;
            for (var i = len - 1; i > 1; i--) { //删除已经不存在的可变属性
                if (this.tower.indexOf(this.testCols[i].txt) < 0) {
                    this.testDatas.map(p => {
                        delete p[this.testCols[i].col];
                    })
                    this.testCols.splice(i, 1);
                }
            }
            this.showTable = true
        },
        refreshTable() {
            this.showTable = false;
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
