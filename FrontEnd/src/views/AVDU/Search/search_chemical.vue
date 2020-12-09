<template>
<div>
    <div id="ListA">
        <h4>化学药剂表</h4>
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
</div>
</template>

<script>
export default {
    data() {
        return {
            testCols: [{ col: "name", txt: '药剂名称' },
                { col: "value", txt: '用量数值' },
                { col: "unit", txt: '用量单位' },
                { col: "type", txt: '类别' },
                { col: "pattern", txt: '型号或规格' },
                { col: "transport", txt: '运输方式' },
                { col: "note", txt: '备注' }
            ],
            testDatas: [],

        };

    },

    created: function () {
        console.log("turn to system page");
        this.testDatas = this.$store.search_chemicalInfo.tableDatas;
    },
    methods: {
    }
}
</script>
