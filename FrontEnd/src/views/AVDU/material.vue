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
            <el-button size="mini" type="primary" @click="addItem">增加一项</el-button>
            <el-button size="mini" type="primary" @click="delLastItem">删除末项</el-button>
        </el-form-item>
        <div v-for="(item,idx) in viscosity">
            <el-form-item :label=item.tempName>
                <el-input v-model="item.temp" placeholder="单位：℃"></el-input>
            </el-form-item>
            <el-form-item :label=item.valueName>
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
            <div style="display: inline-block;float: right;">
                <el-button v-if="showTable" size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
                <el-button v-if="showTable" size="mini" type="primary" @click="addRow">增加行</el-button>
                <el-button v-if="showTable" @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>
            </div>
            <br><br>
            <div>
                折射率温度点（℃）
                <el-select v-model="refract_t" multiple filterable allow-create :disabled="showTable" placeholder="请选择温度">
                    <el-option label="20" value=20></el-option>
                    <el-option label="40" value=40></el-option>
                </el-select>
                粘度温度点（℃）
                <el-select v-model="viscosity_t" multiple filterable allow-create :disabled="showTable" placeholder="请选择温度">
                    <el-option label="20" value=20></el-option>
                    <el-option label="40" value=40></el-option>
                </el-select>
                <el-button type="primary" @click="refreshTable">创建表格</el-button>
            </div>
            <el-table v-if="showTable" :data="narrowFractionDatas" border style="width: 100%;margin-top:10px" maxheight="500">
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
                        <p v-show="scope.row[column.col].show" @dblclick="scope.row[column.col].show=false">
                            {{scope.row[column.col].content}}
                            <i class="el-icon-edit-outline" @click="scope.row[column.col].show=false"></i>
                        </p>
                        <el-input type="textarea" :autosize="{minRows:2,maxRows:4}" v-show="!scope.row[column.col].show" v-model="scope.row[column.col].content" @blur="scope.row[column.col].show=true">
                        </el-input>
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
                            <p v-show="scope.row['re'+column].show" @dblclick="scope.row['re'+column].show=false">
                                {{scope.row['re'+column].content}}
                                <i class="el-icon-edit-outline" @click="scope.row['re'+column].show=false"></i>
                            </p>
                            <el-input type="textarea" :autosize="{minRows:2,maxRows:4}" v-show="!scope.row['re'+column].show" v-model="scope.row['re'+column].content" @blur="scope.row['re'+column].show=true">
                            </el-input>
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
                            <p v-show="scope.row['vis'+column].show" @dblclick="scope.row['vis'+column].show=false">
                                {{scope.row['vis'+column].content}}
                                <i class="el-icon-edit-outline" @click="scope.row['vis'+column].show=false"></i>
                            </p>
                            <el-input type="textarea" :autosize="{minRows:2,maxRows:4}" v-show="!scope.row['vis'+column].show" v-model="scope.row['vis'+column].content" @blur="scope.row['vis'+column].show=true">
                            </el-input>
                        </template>
                    </el-table-column>
                </el-table-column>

            </el-table>
        </div>
    </el-form>
    <br>
    <el-button type="primary" @click="addToStore">暂存此页</el-button>
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
                { col: "boiling_point", txt: '沸点范围（℃）' },
                { col: "yield", txt: '每馏分收率（m%）' },
                { col: "yield_total", txt: '总收率（m%）' },
                { col: "density", txt: '密度（20℃）（kg/m³）' },
                { col: "freezing_point", txt: '凝点（℃）' },
                { col: "acidity", txt: '酸度（mgKOH/100ml）' },
                { col: "acid_value", txt: '酸值（mgKOH/g）' },
                { col: "characteristic_index", txt: '特性因数' },
                { col: "correlation_index", txt: '相关指数' },
                { col: "API", txt: 'API' }
            ],
            narrowFractionDatas: [{
                boiling_point: { content: '<80', show: true },
                yield: { content: '', show: true },
                yield_total: { content: '', show: true },
                density: { content: '', show: true },
                freezing_point: { content: '', show: true },
                acidity: { content: '', show: true },
                acid_value: { content: '', show: true },
                characteristic_index: { content: '', show: true },
                correlation_index: { content: '', show: true },
                API: { content: '', show: true },
            }, {
                boiling_point: { content: '80-100', show: true },
                yield: { content: '', show: true },
                yield_total: { content: '', show: true },
                density: { content: '', show: true },
                freezing_point: { content: '', show: true },
                acidity: { content: '', show: true },
                acid_value: { content: '', show: true },
                characteristic_index: { content: '', show: true },
                correlation_index: { content: '', show: true },
                API: { content: '', show: true },
            }],
            count_col: 0,
            showTable: false,
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
            };
            this.$store.materialInfo.tableCols = this.narrowFractionCols; //窄馏分表头
            this.$store.materialInfo.refract_t = this.refract_t; //窄馏分折射率温度点
            this.$store.materialInfo.viscosity_t = this.viscosity_t; //窄馏分粘度温度点
            this.$store.materialInfo.tableDatas = this.narrowFractionDatas; //窄馏分表内容
            this.$store.materialInfo.mainInfo = this.materialInfo; //原料性质主要内容
            this.$store.materialInfo.viscosity = this.viscosity; //原料不同温度下的粘度
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store materialInfo to device');
            // console.log(this.$store.deviceInfo.tableCols);
        },
        refreshTable() { //根据设置的粘度和折射率刷新表格
            for (var x in this.refract_t) {
                var _this = this
                this.narrowFractionDatas.map(p => { // 新增的对象无法被vue监听到
                    _this.$set(p, "re" + this.refract_t[x], { content: '', show: true })
                    //		p[obj.col] = {content: '', show: true}
                })
            }
            for (var x in this.viscosity_t) {
                var _this = this
                this.narrowFractionDatas.map(p => { // 新增的对象无法被vue监听到
                    _this.$set(p, "vis" + this.viscosity_t[x], { content: '', show: true })
                    //		p[obj.col] = {content: '', show: true}
                })
            }
            this.showTable = true
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
