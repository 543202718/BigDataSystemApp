<template>
<div>
    <br> 
    <table border="1" align="center">
        <tr>
            <td colspan="2"><b>跨设备操作条件</b></td>
        </tr>
        <tr>
            <td><b>原油进电脱盐温度（℃）</b></td>
            <td>{{operation_conditionInfo.CrudeOilToDesaltTemp}}</td>
             </tr>
        <tr>
            <td><b>闪底油进常压炉温度（℃）</b></td>
            <td>{{operation_conditionInfo.FlasBotmToAtmoFurnTemp}}</td>
        </tr>
    </table>
    <br>
    <div id="ListA">
        <h4 style="display: inline-block;margin:0;">不同设备中的操作条件</h4>
        <el-table :data="testDatas" border max-height="500" style="width: 100%;margin-top:10px">
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
            showTable: false,
            tower: ["闪蒸塔", "初馏塔", "常压塔", "减压塔"],
            operation_conditionInfo: {
                CrudeOilToDesaltTemp: '',
                FlasBotmToAtmoFurnTemp: '',
            },
            testCols: [{ col: "name", txt: '操作名称' },
                { col: "unit", txt: '单位' },
            ],
            testDatas: [],
        };

    },

    created: function () {
        console.log("turn to system page");
        console.log(this.$store.search_operation_conditionInfo)
        this.testCols = this.$store.search_operation_conditionInfo.tableCols;
        this.testDatas = this.$store.search_operation_conditionInfo.tableDatas;
        this.operation_conditionInfo = this.$store.search_operation_conditionInfo.operation_conditionInfo;
    },
    methods: {
 
    }
}
</script>
