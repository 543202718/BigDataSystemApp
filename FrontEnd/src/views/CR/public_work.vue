<template>
<div id="hello">
    <div style="display: inline-block;float: right;">
        <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
        <el-button size="mini" type="primary" @click="addRow">增加行</el-button>

        <el-button @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>

    </div>
    <el-table :data="testDatas" border style=" width: 100%;margin-top:10px" max-height="600">
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
</template>

<script>
export default {
    data() {
        return {
            testCols: [
                { col: "name", txt: '项目', show: true },
                { col: "unit", txt: '单位', show: true },
                { col: "value", txt: '数值', show: true },
                { col: "note", txt: '备注', show: true }
            ],
            testDatas: [{
                name: { content: '电', show: true },
                unit: { content: 'kW', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '标准燃料', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '净化水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '新鲜水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '循环水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '净化水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '除盐水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '除氧水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '工艺凝结水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '透平凝结水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '污水', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '3.5Mpa蒸汽', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '1.0Mpa蒸汽', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '0.4Mpa蒸汽', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '净化风', show: true },
                unit: { content: 'Nm^3/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '非净化风', show: true },
                unit: { content: 'Nm^3/h', show: true },
                value: { content: '', show: true },
                note: { content: '间隔用量', show: true }
            }, {
                name: { content: '氨气', show: true },
                unit: { content: 'Nm^3/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }, {
                name: { content: '胺液', show: true },
                unit: { content: 't/h', show: true },
                value: { content: '', show: true },
                note: { content: '', show: true }
            }],
            count_col: 0,
            showMenu: false,
            curColumn: null,
        }
    },
    created: function () {
        console.log("turn to system page");
    },
    methods: {
        addToStore: function () {
            this.$store.publicworkInfo = {
                tableCols: null,
                tableDatas: null
            };
            this.$store.publicworkInfo.tableCols = this.tableCols; //表头
            this.$store.publicworkInfo.tableDatas = this.tableDatas; //表格内容
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store publicworkInfo to device');
        },
        addRow() { // 新增行
            this.showMenu = false
            var obj = {}
            this.testCols.map(p => {
                obj[p.col] = { content: '', show: true }
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
