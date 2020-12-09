<template>
<div>
    <table border="1" align="center" class="gridtable">
        <caption>
            <h4>原料基本性质</h4>
        </caption>
        <tr>
            <td colspan="1"><b>原料名称</b></td>
            <td colspan="7">{{materialInfo.material_name}}</td>
        </tr>
        <tr>
            <td><b>密度(20℃)(kg/m³)</b></td>
            <td>{{materialInfo.density}}</td>
            <td><b>凝点(℃)</b></td>
            <td>{{materialInfo.freezing_point}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>闪点开口(℃)</b></td>
            <td>{{materialInfo.flash_point_open}}</td>
            <td><b>闪点闭口(℃)</b></td>
            <td>{{materialInfo.flash_point_close}}</td>
        </tr>
        <tr>
            <td><b>原油类别</b></td>
            <td>{{materialInfo.type}}</td>
            <td><b>原油热值(kJ/kg)</b></td>
            <td>{{materialInfo.calorific}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>酸值(mg KOH/g)</b></td>
            <td>{{materialInfo.acid_value}}</td>
            <td><b>灰分(%(m/m))</b></td>
            <td>{{materialInfo.ash}}</td>
        </tr>
        <tr>
            <td><b>残炭(%(m/m))</b></td>
            <td>{{materialInfo.carbon}}</td>
            <td><b>含蜡量(%(m/m))</b></td>
            <td>{{materialInfo.wax}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>盐含量(mg/L)</b></td>
            <td>{{materialInfo.salt}}</td>
            <td><b>硫醇硫(ppm)</b></td>
            <td>{{materialInfo.sulfur}}</td>
        </tr>
        <tr>
            <td><b>水分(%(m/m))</b></td>
            <td>{{materialInfo.water}}</td>
            <td><b>沉淀物(%(m/m))</b></td>
            <td>{{materialInfo.precipitate}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>胶质(%(m/m))</b></td>
            <td>{{materialInfo.gum}}</td>
            <td><b>沥青质(%(m/m))</b></td>
            <td>{{materialInfo.asphaltene}}</td>
        </tr>
        <tr>
            <td colspan="8"><b>不同温度下的粘度</b></td>
        </tr>
        <tr v-for="(item,idx) in viscosity">
            <!-- <td colspan="2"><b>温度点{{idx+1}}</b></td> -->
            <td colspan="2"><b>温度(℃)</b></td>
            <td colspan="2">{{viscosity[idx].tempature}}</td>
            <td colspan="2"><b>粘度(m㎡/s)</b></td>
            <td colspan="2">{{viscosity[idx].value}}</td>
        </tr>
        <tr>
            <td colspan="8"><b>元素组成</b></td>
        </tr>
        <tr>
            <td><b>S(w%)</b></td>
            <td>{{materialInfo.S}}</td>
            <td><b>C(w%)</b></td>
            <td>{{materialInfo.C}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>N(w%)</b></td>
            <td>{{materialInfo.N}}</td>
            <td><b>H(w%)</b></td>
            <td>{{materialInfo.H}}</td>
        </tr>
        <tr>
            <td><b>Ni(μg/g)</b></td>
            <td>{{materialInfo.Ni}}</td>
            <td><b>V(μg/g)</b></td>
            <td>{{materialInfo.V}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>Ca(μg/g)</b></td>
            <td>{{materialInfo.Ca}}</td>
            <td><b>Fe(μg/g)</b></td>
            <td>{{materialInfo.Fe}}</td>

        </tr>
        <tr>
            <td><b>Cu(μg/g)</b></td>
            <td>{{materialInfo.Cu}}</td>
            <td><b>Pb(μg/g)</b></td>
            <td>{{materialInfo.Pb}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>Mg(μg/g)</b></td>
            <td>{{materialInfo.Mg}}</td>
            <td><b>Na(μg/g)</b></td>
            <td>{{materialInfo.Na}}</td>

        </tr>
        <tr>
            <td colspan="8"><b>轻烃组成</b></td>
        </tr>
        <tr>
            <td><b>甲烷(v%)</b></td>
            <td>{{materialInfo.methane}}</td>
            <td><b>乙烷(v%)</b></td>
            <td>{{materialInfo.ethane}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>丙烷(v%)</b></td>
            <td>{{materialInfo.propane}}</td>
            <td><b>正丁烷(v%)</b></td>
            <td>{{materialInfo.n_butane}}</td>
        </tr>
        <tr>
            <td><b>异丁烷(v%)</b></td>
            <td>{{materialInfo.isobutane}}</td>
            <td><b>正戊烷(v%)</b></td>
            <td>{{materialInfo.n_pentane}}</td>
            <!-- </tr>
        <tr> -->
            <td><b>异戊烷(v%)</b></td>
            <td>{{materialInfo.isopentane}}</td>
            <td><b>环戊烷(v%)</b></td>
            <td>{{materialInfo.cyclopentane}}</td>
        </tr>
    </table>
    <el-form ref="form" :model="materialInfo" label-width="130px" size="mini" style="margin-top: 20px">
        <div id="hello">
            <h4 style="display: inline-block;margin:0;">原料窄馏分性质</h4>
            <el-table :data="narrowFractionDatas" border style="width: 100%;margin-top:10px" max-height="500">
                <el-table-column v-if="narrowFractionCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
                <!-- 固定列 -->
                <el-table-column v-for="(column, idx) in narrowFractionCols" :key="idx" :index="idx" :width="120">
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
                <!-- 折射率 -->
                <el-table-column v-if="refract_t.length>0" label="折射率">
                    <el-table-column v-for="(column, idx) in refract_t" :key="idx" :index="idx">
                        <!--label-->
                        <template slot="header" slot-scope="scope1">
                            <p>
                                {{column}}℃
                            </p>
                        </template>
                        <template slot-scope="scope">
                            <p>
                                {{scope.row['re'+column]}}
                            </p>
                        </template>
                    </el-table-column>
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
    </el-form>
    <br>
</div>
</template>

<script>
export default {
    data() {
        return {
            viscosity: [
                { temp: "", value: "", tempName: "温度1", valueName: "粘度1" },
                { temp: "", value: "", tempName: "温度2", valueName: "粘度2" },
            ],
            refract_t: [],
            viscosity_t: [],
            narrowFractionCols: [
                { col: "boiling_range", txt: '沸点范围（℃）' },
                { col: "yield_fraction", txt: '每馏分收率（m%）' },
                { col: "yield_total", txt: '总收率（m%）' },
                { col: "density", txt: '密度（20℃）（kg/m³）' },
                { col: "solidifying", txt: '凝点（℃）' },
                { col: "acidity", txt: '酸度（mgKOH/100ml）' },
                { col: "acid", txt: '酸值（mgKOH/g）' },
                { col: "characteristic", txt: '特性因数' },
                { col: "related", txt: '相关指数' },
                { col: "api", txt: 'API' }
            ],
            narrowFractionDatas: [],
            count_col: 0,
            curColumn: null,
            materialInfo: {
                material_name: '',
                density: '',
                freezing_point: '',
                acid_value: '',
                flash_point_open: '',
                flash_point_close: '',
                ash: '',
                carbon_residual: '',
                wax_content: '',
                salt_content: '',
                mercaptan_sulfur: '',
                water: '',
                precipitate: '',
                heat_value: '',
                type: '',
                colloid: '',
                asphalt: '',
                H: '',
                C: '',
                S: '',
                N: '',
                Ni: '',
                V: '',
                Ca: '',
                Fe: '',
                Cu: '',
                Pb: '',
                Mg: '',
                Na: '',
                methane: '',
                ethane: '',
                propane: '',
                n_butane: '',
                isobutane: '',
                n_pentane: '',
                isopentane: '',
                cyclopentane: '',
            },
        };
    },

    created: function () {
        console.log("turn to system page");
        console.log(this.$store.search_materialInfo)
        this.refract_t = this.$store.search_materialInfo.refract_t; //窄馏分折射率温度点
        this.viscosity_t = this.$store.search_materialInfo.viscosity_t; //窄馏分粘度温度点
        this.narrowFractionDatas = this.$store.search_materialInfo.tableDatas; //窄馏分表内容
        this.materialInfo = this.$store.search_materialInfo.mainInfo; //原料性质主要内容
        this.viscosity = this.$store.search_materialInfo.viscosity; //原料不同温度下的粘度       
    },
    methods: {
        addToStore: function () {
            this.$store.materialInfo = {
                tableCols: null,
                refract_t: null,
                viscosity_t: null,
                tableDatas: null,
                mainInfo: null,
                viscosity: null,
                showTable: null,
            };
            this.$store.materialInfo.tableCols = this.narrowFractionCols; //窄馏分表头
            this.$store.materialInfo.refract_t = this.refract_t; //窄馏分折射率温度点
            this.$store.materialInfo.viscosity_t = this.viscosity_t; //窄馏分粘度温度点
            this.$store.materialInfo.tableDatas = this.narrowFractionDatas; //窄馏分表内容
            this.$store.materialInfo.mainInfo = this.materialInfo; //原料性质主要内容
            this.$store.materialInfo.viscosity = this.viscosity; //原料不同温度下的粘度
            this.$store.materialInfo.showTable = this.showTable;
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store materialInfo to device');
            // console.log(this.$store.deviceInfo.tableCols);
        },
        createTable() { //根据设置的粘度和折射率创建表格
            this.viscosity_t.sort(function (a, b) { return a - b });
            this.createTableForCol(this.viscosity_t, this.narrowFractionDatas, "vis");
            this.refract_t.sort(function (a, b) { return a - b });
            this.createTableForCol(this.refract_t, this.narrowFractionDatas, "re");
            this.showTable = true
        },
        createTableForCol(t, data, s) {
            var cols = [];
            for (var x in t) {
                var _this = this;
                var col = s + t[x];
                cols.push(col);
                data.map(p => {
                    if (!(col in p)) { //已有对象不会重复生成，防止已输入的数据被清空
                        _this.$set(p, col, { content: '', show: true })
                    }
                })
            }
            data.map(p => { //删除已经不存在的可变属性
                for (var k in p) {
                    if (k.substr(0, s.length) == s && cols.indexOf(k) < 0) {
                        delete p[k];
                    }
                }
            })
        },
        refreshTable() {
            this.showTable = false;
        },
        addRow() { // 新增行
            var obj = {}
            this.narrowFractionCols.map(p => {
                obj[p.col] = { content: '', show: true }
            })
            this.refract_t.map(p => {
                obj['re' + p] = { content: '', show: true }
            })
            this.viscosity_t.map(p => {
                obj['vis' + p] = { content: '', show: true }
            })
            this.narrowFractionDatas.push(obj)
        },
        delLastRow() { // 删除行
            var len = this.narrowFractionDatas.length;
            if (len > 0) this.narrowFractionDatas.splice(len - 1, 1);
            else this.$message.error('没有可删除行');
        },
        addItem() {
            var n = this.viscosity.length + 1
            this.viscosity.push({
                temp: "",
                value: "",
                tempName: "温度" + n,
                valueName: "粘度" + n
            })
        },
        delLastItem() {
            var len = this.viscosity.length;
            if (len > 0) this.viscosity.splice(len - 1, 1);
            else this.$message.error('没有可删除项目');
        },
        consoleDatas() {
            console.log('表头', this.narrowFractionCols);
            console.log('数据', this.narrowFractionDatas);
        }
    }
}
</script>

<style>
/* table.gridtable {
    font-family: verdana, arial, sans-serif;
    font-size: 11px;
    color: #333333;
    border-width: 1px;
    border-color: #666666;
    border-collapse: collapse;
}

table.gridtable th {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #666666;
    background-color: #dedede;
} */

table.gridtable td {
    /* border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #666666;
    background-color: #ffffff; */
    width: 150px;
}
</style>
