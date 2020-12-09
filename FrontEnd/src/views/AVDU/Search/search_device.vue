<template>
<div id="hello">
    <h4>主要设备表</h4>
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
                <p>
                    {{scope.row[column.col]}}
                </p>
            </template>
        </el-table-column>
    </el-table>
</div>
</template>

<script>
export default {
    data() {
        return {
            testCols: [
                { col: "type", txt: '项目' },
                { col: "internal", txt: '国内订货数(台)' },
                { col: "overseas", txt: '国外订货数(台)' },
                { col: "total", txt: '合计' },
                { col: "note", txt: '备注' }
            ],
            testDatas: [],
        }
    },
    created: function () {
        console.log("turn to system page");
        // console.log( this.$store.search_deviceInfo.tableDatas)
        this.testDatas = this.$store.search_deviceInfo.tableDatas;
    },
    methods: {}
}
</script>
