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
</div>
</template>

<script>
export default {
    data() {
        return {
            testCols: [{
                    col: "name",
                    txt: '三废名称'
                },
                {
                    col: "unit",
                    txt: '单位'
                },
                {
                    col: "value",
                    txt: '排放量'
                },
                {
                    col: "CONTvalue",
                    txt: '排放量（间断量）'
                }, {
                    col: "note",
                    txt: '备注'
                }
            ],
            testDatas: [{
                    name: { content: '加热炉烟气', show: true },
                    unit: { content: 't/h', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '', show: true },
                    note: { content: '连续，独立烟囱', show: true }
                },
{
                    name: { content: '催化剂再生废气', show: true },
                    unit: { content: 'kg/h', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '', show: true },
                    note: { content: '连续', show: true }
                },
{
                    name: { content: '含硫污水', show: true },
                    unit: { content: 't/h', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '', show: true },
                    note: { content: '污水汽提装置', show: true }
                },
{
                    name: { content: '含油污水', show: true },
                    unit: { content: 't/h', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '', show: true },
                    note: { content: '污水处理厂', show: true }
                },
{
                    name: { content: '含烃污水', show: true },
                    unit: { content: 't/h', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '', show: true },
                    note: { content: '', show: true }
                },
{
                    name: { content: '再生含盐污水', show: true },
                    unit: { content: 't/h', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '', show: true },
                    note: { content: '连续，污水处理厂', show: true }
                },
{
                    name: { content: '废重整催化剂', show: true },
                    unit: { content: 't/次，3年1次', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '-', show: true },
                    note: { content: '催化剂厂回收', show: true }
                },
{
                    name: { content: '废预加氢催化剂', show: true },
                    unit: { content: 't/次，4年1次', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '-', show: true },
                    note: { content: '集中处理-填埋', show: true }
                },
{
                    name: { content: '废预加氢脱氯剂', show: true },
                    unit: { content: 't/次，2年1次', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '-', show: true },
                    note: { content: '集中处理-填埋', show: true }
                },
{
                    name: { content: '废氢气脱氯剂', show: true },
                    unit: { content: 't/次，1年1次', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '-', show: true },
                    note: { content: '集中处理-填埋', show: true }
                },
{
                    name: { content: '废重整油脱氯剂', show: true },
                    unit: { content: 't/次，1年1次', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '-', show: true },
                    note: { content: '集中处理-填埋', show: true }
                },
{
                    name: { content: '废脱氯吸附剂', show: true },
                    unit: { content: 't/次，2年1次', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '-', show: true },
                    note: { content: '集中处理-填埋', show: true }
                },
{
                    name: { content: '废白土', show: true },
                    unit: { content: 't/次，2年1次', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '-', show: true },
                    note: { content: '集中处理-填埋', show: true }
                },
{
                    name: { content: '废环丁砜', show: true },
                    unit: { content: 't/次，1年4次', show: true },
                    value: { content: '', show: true },
                    CONTvalue: { content: '-', show: true },
                    note: { content: '集中处理-填埋', show: true }
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
            this.$store.wasteInfo = {
                tableCols: null,
                tableDatas: null
            };
            this.$store.wasteInfo.tableCols = this.tableCols; //表头
            this.$store.wasteInfo.tableDatas = this.tableDatas; //表格内容
            this.$message({
                        message: '暂存成功',
                        type: 'success',
                        duration: 3000,
                        showClose: true
                    });
            console.log('store wasteInfo to device');
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
