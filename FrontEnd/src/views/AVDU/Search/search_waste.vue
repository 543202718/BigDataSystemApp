<template>
<div>
    <div id="ListA">

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
            testCols: [{
                    col: "name",
                    txt: '三废名称'
                },
                {
                    col: "unit",
                    txt: '单位'
                },
                {
                    col: "value_con",
                    txt: '排放量'
                },
                {
                    col: "value_dis",
                    txt: '排放量（间断量）'
                }, {
                    col: "note",
                    txt: '备注'
                }
            ],
            testDatas: [],

        }

    },

    created: function () {
        console.log("turn to system page");
        // console.log(this.$store.search_wasteInfo.tableDatas);
        this.testDatas = this.$store.search_wasteInfo.tableDatas;
    },
    methods: {
    }
}
</script>
