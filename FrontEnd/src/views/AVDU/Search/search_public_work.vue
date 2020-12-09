<template>
<div id="hello">
    <div>
        <h4>公用工程表</h4>
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
            testCols: [
                { col: "name", txt: '项目' },
                { col: "unit", txt: '单位' },
                { col: "value", txt: '数值' },
                { col: "note", txt: '备注' },
            ],
            testDatas: [],

        };
    },

    created: function () {
        console.log("turn to publicWork page");
        this.testDatas = this.$store.search_public_workInfo.tableDatas;
    },
}
</script>
