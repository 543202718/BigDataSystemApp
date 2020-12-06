<template>
<div id="hello">

    <div>
        <h4>物料平衡表</h4>
        <el-table :data="tableDatas" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
                <!--label-->
                <template slot="header" slot-scope="scope1">
                    <p>
                        {{column.txt}}
                    </p>
                </template>
                <!--prop-->
                <template slot-scope="scope">
                    <p>
                        {{scope.row[column.col]}}
                    </p>
                </template>
            </el-table-column>
        </el-table>
    </div>
    
</div>
</template>

<script>
export default {
    data() {
        return {
            balanceCols: [
                { col: "inout", txt: '出入方' },
                { col: "name", txt: '名称' },
                { col: "cutting_range", txt: '实沸点切割范围/℃' },
                { col: "yield", txt: '收率m%' },
                { col: "flow1", txt: '流率（公斤/时）' },
                { col: "flow2", txt: '流率（吨/天）' },
                { col: "flow3", txt: '流率（万吨/年）' },
                { col: "note", txt: '备注' },
            ],
            tableDatas: [],
        };

    },

    created: function () {
        console.log("turn to system page");
        console.log(this.$store.search_balanceInfo);
        this.tableDatas = this.$store.search_balanceInfo.tableDatas;
    },
    methods: {
        addToStore: function () {
            this.$store.balanceInfo = {
                tableCols: null,
                inDatas: null,
                outDatas: null,
            };
            this.$store.balanceInfo.tableCols = this.balanceCols; //表头
            this.$store.balanceInfo.inDatas = this.inDatas; //产品粘度温度点
            this.$store.balanceInfo.outDatas = this.outDatas; //产品性质表内容
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store balanceInfo to device');
            // console.log(this.$store.deviceInfo.tableCols);
        },
        addRow(table) { // 新增行
            this.showMenu = false
            var obj = {}
            this.balanceCols.map(p => {
                obj[p.col] = {
                    content: '',
                    show: true
                }
            })
            table.push(obj)
        },
        delLastRow(table) { // 删除行
            this.showMenu = false
            var len = table.length;
            if (len > 0) table.splice(len - 1, 1);
            else this.$message.error('没有可删除行');
        },
        consoleDatas() {
            console.log('表头', this.balanceCols);
            console.log('入方数据', this.inDatas);
            console.log('出方数据', this.inDatas);
        }
    },

}
</script>
