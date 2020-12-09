<template>
<div id="hello">
    <div>
        <h4>产品性质表</h4>
        <el-table :data="productDatas" border style="width: 100%;margin-top:10px" max-height="500">
            <el-table-column v-if="productCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <!-- 固定列 -->
            <el-table-column v-for="(column, idx) in productCols" :key="idx" :index="idx" :width="160">
                <!--label-->
                <template slot="header" slot-scope="scope1">
                    <p>
                        {{column.txt}}
                    </p>
                </template>
                <!--prop-->
                <template slot-scope="scope">
                    <p >
                        {{scope.row[column.col]}}
                    </p>
                </template>
            </el-table-column>
            <!-- 运动粘度 -->
            <el-table-column v-if="viscosity_t.length>0" label="运动粘度（m㎡/s）">
                <el-table-column v-for="(column, idx) in viscosity_t" :key="idx" :index="idx">
                    <!--label-->
                    <template slot="header" slot-scope="scope1">
                        <p>
                            {{column}}℃
                        </p>
                    </template>
                    <template slot-scope="scope">
                        <p>
                            {{scope.row['vis'+column]}}
                        </p>
                    </template>
                </el-table-column>
            </el-table-column>
        </el-table>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            viscosity_t: [],
            productCols: [{ col: "name", txt: '产品名称' },
                { col: "density", txt: '密度(20℃) （kg/m³）' },
                { col: "api", txt: '比重指数(API)' },
                { col: "m_weight", txt: '分子量' },
                { col: "characteristic", txt: '特性因数' },
                { col: "sulfur_content", txt: '含硫量（wt/%）' },
                { col: "acid", txt: '酸值（mgKOH/g）' },
                { col: "note", txt: '备注' }
            ],
            productDatas: [],
        };

    },

    created: function () {
        console.log("turn to product page");
        console.log(this.$store.search_productInfo)
        this.viscosity_t = this.$store.search_productInfo.viscosity_t; //粘度温度点
        this.productDatas = this.$store.search_productInfo.tableDatas; //窄馏分表内容
    },
    methods: {

    },

}
</script>
