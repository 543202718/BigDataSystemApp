<template>
<div>


    <el-form ref="form" :model="materialInfo" label-width="130px" size="mini" style="margin-top: 20px">
        <el-form-item label="原料名称">
            <el-input v-model="materialInfo.material_name" placeholder="例：沙轻和科威特混合原油"></el-input>
        </el-form-item>
        <el-form-item label="原料密度（20℃）">
            <el-input v-model="materialInfo.density" placeholder="单位：kg/m³">
            </el-input>
        </el-form-item>
        <el-form-item label="凝点">
            <el-input v-model="materialInfo.freezing_point" placeholder="单位：℃"></el-input>
        </el-form-item>
        <el-form-item label="酸值">
            <el-input v-model="materialInfo.acid_value" placeholder="单位：mg KOH/g">
            </el-input>
        </el-form-item>
        <el-form-item label="闪点（开口）">
            <el-input v-model="materialInfo.flash_point_open" placeholder="单位：℃"></el-input>
        </el-form-item>
        <el-form-item label="闪点（闭口）">
            <el-input v-model="materialInfo.flash_point_close" placeholder="单位：℃"></el-input>
        </el-form-item>
        <el-form-item label="原油热值">
            <el-input v-model="materialInfo.heat_value" placeholder="单位：kJ/kg"></el-input>
        </el-form-item>
        <el-form-item label="原油类别">
            <el-input v-model="materialInfo.type" placeholder="例：低硫环烷中间基"></el-input>
        </el-form-item>
        <el-form-item label="灰分">
            <el-input v-model="materialInfo.ash" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="残炭">
            <el-input v-model="materialInfo.carbon_residual" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="含蜡量">
            <el-input v-model="materialInfo.wax_content" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="盐含量">
            <el-input v-model="materialInfo.salt_content" placeholder="单位：mg/L"></el-input>
        </el-form-item>
        <el-form-item label="硫醇硫">
            <el-input v-model="materialInfo.mercaptan_sulfur" placeholder="单位：ppm"></el-input>
        </el-form-item>
        <el-form-item label="水分">
            <el-input v-model="materialInfo.water" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="沉淀物">
            <el-input v-model="materialInfo.precipitate" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="胶质">
            <el-input v-model="materialInfo.colloid" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="沥青质">
            <el-input v-model="materialInfo.asphalt" placeholder="单位：%(m/m)"></el-input>
        </el-form-item>
        <el-form-item label="不同温度下的粘度" align="left">
           
        </el-form-item>
        <div v-for="(item,idx) in viscosity">
            <el-form-item label="温度">
                <el-input v-model="item.tempature" placeholder="单位：℃"></el-input>
            </el-form-item>
            <el-form-item label="粘度">
                <el-input v-model="item.value" placeholder="单位：m㎡/s"></el-input>
            </el-form-item>
        </div>

        <el-form-item label="元素组成">
        </el-form-item>
        <el-form-item label="H">
            <el-input v-model="materialInfo.H" placeholder="单位：w%"></el-input>
        </el-form-item>
        <el-form-item label="C">
            <el-input v-model="materialInfo.C" placeholder="单位：w%"></el-input>
        </el-form-item>
        <el-form-item label="S">
            <el-input v-model="materialInfo.S" placeholder="单位：w%"></el-input>
        </el-form-item>
        <el-form-item label="N">
            <el-input v-model="materialInfo.N" placeholder="单位：w%"></el-input>
        </el-form-item>
        <el-form-item label="Ni">
            <el-input v-model="materialInfo.Ni" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="V">
            <el-input v-model="materialInfo.V" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Ca">
            <el-input v-model="materialInfo.Ca" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Fe">
            <el-input v-model="materialInfo.Fe" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Cu">
            <el-input v-model="materialInfo.Cu" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Pb">
            <el-input v-model="materialInfo.Pb" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Mg">
            <el-input v-model="materialInfo.Mg" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="Na">
            <el-input v-model="materialInfo.Na" placeholder="单位：μg/g"></el-input>
        </el-form-item>
        <el-form-item label="轻烃组成">
        </el-form-item>
        <el-form-item label="甲烷">
            <el-input v-model="materialInfo.methane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="乙烷">
            <el-input v-model="materialInfo.ethane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="丙烷">
            <el-input v-model="materialInfo.propane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="正丁烷">
            <el-input v-model="materialInfo.n_butane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="异丁烷">
            <el-input v-model="materialInfo.isobutane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="正戊烷">
            <el-input v-model="materialInfo.n_pentane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="异戊烷">
            <el-input v-model="materialInfo.isopentane" placeholder="单位：v%"></el-input>
        </el-form-item>
        <el-form-item label="环戊烷">
            <el-input v-model="materialInfo.cyclopentane" placeholder="单位：v%"></el-input>
        </el-form-item>

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
                        <p >
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
                            <p  >
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
                            <p  >
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
            this.viscosity_t.sort(function(a, b){return a - b}); 
            this.createTableForCol(this.viscosity_t, this.narrowFractionDatas, "vis");
            this.refract_t.sort(function(a, b){return a - b}); 
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
