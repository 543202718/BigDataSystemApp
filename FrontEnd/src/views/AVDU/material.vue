<template>
<div>
    <el-form ref="form" :model="materialInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="原料名称">
            <el-input v-model="materialInfo.material_name" placeholder="例：沙轻和科威特混合原油"></el-input>
        </el-form-item>
        <el-form-item label="原料密度（20℃）">
            <el-input v-model="materialInfo.density" placeholder="单位：kg/m³">
            </el-input>
        </el-form-item>
        <el-form-item label="粘度">
            <el-input v-model="materialInfo.viscosity" placeholder="单位：m㎡/s"></el-input>
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
                <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
                <el-button size="mini" type="primary" @click="addRow">增加行</el-button>
                <el-button @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>

            </div>
            <el-table :data="narrowFractionDatas" border style="width: 100%;margin-top:10px" @header-contextmenu="colRightClick">
                <el-table-column v-if="narrowFractionCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
                <el-table-column v-for="(column, idx) in narrowFractionCols" :key="idx" :index="idx">
                    <!--label-->
                    <template slot="header" slot-scope="scope1">
                        <p v-show="column.show" @dblclick="column.show=false">
                            {{column.txt}}
                            <i class="el-icon-edit-outline" @click="column.show=false"></i>
                        </p>
                        <el-input size="mini" v-show="!column.show" v-model="column.txt" @blur="column.show=true">
                        </el-input>
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
            </el-table>

            <div v-show="showMenu" id="contextmenu">
                <i class="el-icon-circle-close hideContextMenu" @click="showMenu=false"></i>
                <el-button size="mini" type="primary" @click="addColumn(curColumn)">前方插入一列</el-button>
                <el-button size="mini" type="primary" @click="addColumn(curColumn+1)">后方插入一列</el-button>
                <el-button @click="delColumn" slot="reference" type="primary" size="mini">删除当前列</el-button>

            </div>

        </div>
        <!--
        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>
-->
    </el-form>
</div>
</template>

<script>
export default {
    data() {
        return {
            narrowFractionCols: [
				{col: "boiling_point", txt: '沸点范围（℃）', show: true},
                {col: "yield", txt: '收率（每馏分）', show: true},
                {col: "yield_total", txt: '总收率', show: true},
                {col: "density", txt: '密度（20℃）（kg/m³）', show: true},
                {col: "freezing_point", txt: '凝点（℃）', show: true},
                {col: "acidity", txt: '酸度（mgKOH/100ml）', show: true},
                {col: "acid_value", txt: '酸值（mgKOH/g）', show: true},
                {col: "refractive_index", txt: '折射率（温度：___℃）', show: true},
                {col: "viscosity", txt: '运动粘度（温度：___℃）', show: true},
                {col: "characteristic_index", txt: '特性因数', show: true},
                {col: "correlation_index", txt: '相关指数', show: true},
				{col: "API", txt: 'API', show: true}
			],
			narrowFractionDatas: [{
                    boiling_point: {content: '<80', show: true},
                    yield: {content: '', show: true},
                    yield_total: {content: '', show: true},
                    density: {content: '', show: true},
                    freezing_point: {content: '', show: true},
                    acidity: {content: '', show: true},
                    acid_value: {content: '', show: true},
                    refractive_index: {content: '', show: true},
                    viscosity: {content: '', show: true},
                    characteristic_index: {content: '', show: true},
                    correlation_index: {content: '', show: true},
                    API: {content: '', show: true},
				},{
					boiling_point: {content: '80-100', show: true},
                    yield: {content: '', show: true},
                    yield_total: {content: '', show: true},
                    density: {content: '', show: true},
                    freezing_point: {content: '', show: true},
                    acidity: {content: '', show: true},
                    acid_value: {content: '', show: true},
                    refractive_index: {content: '', show: true},
                    viscosity: {content: '', show: true},
                    characteristic_index: {content: '', show: true},
                    correlation_index: {content: '', show: true},
                    API: {content: '', show: true},
				}
			],
			count_col: 0,
			showMenu: false,
			curColumn: null,
            materialInfo: {
                material_name: '',
                density: '',
                viscosity: '',
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
        colRightClick(column,event) {
			window.event.returnValue = false; //阻止浏览器自带的右键菜单弹出
			if(!column.index && column.index !== 0) return;
			this.curColumn = column.index
			this.showMenu = true
			var ele = document.getElementById('contextmenu')
			ele.style.top = event.clientY + 'px';
			ele.style.left = event.clientX + 'px';
			if(window.innerWidth - 140 < event.clientX) {
				ele.style.left = 'unset'
				ele.style.right = 0
			}
		},
		addRow() { // 新增行
			this.showMenu = false
			var obj = {}
			this.narrowFractionCols.map(p => {
				obj[p.col] = {content: '', show: true}
			})
			this.narrowFractionDatas.push(obj)
		},
		// 当row中存在一“主键”可唯一标识row的下标时（如：编号放在narrowFractionDatas内），可借此实现行的自由插入与删除
		addColumn(idx) { // 新增列
			this.showMenu = false
			var obj = {col: 'col_' + this.count_col++, txt: '', show: true}
			if(idx || idx === 0) this.narrowFractionCols.splice(idx, 0, obj);
			else this.narrowFractionCols.push(obj);
			var _this = this
			this.narrowFractionDatas.map(p => { // 新增的对象无法被vue监听到
				_this.$set(p, obj.col, {content: '', show: true})
//				p[obj.col] = {content: '', show: true}
			})
		},
		delColumn() { // 删除列
			this.showMenu = false
			var colKey = this.narrowFractionCols[this.curColumn].col;
			this.narrowFractionCols.splice(this.curColumn, 1);
			this.narrowFractionDatas.map(p => {
				delete p[colKey];
			});
		},
		delLastRow() { // 删除行
			this.showMenu = false
			var len = this.narrowFractionDatas.length;
			if(len > 0) this.narrowFractionDatas.splice(len - 1, 1);
			else this.$message.error('没有可删除行');
		},
		consoleDatas() {
			console.log('表头',this.narrowFractionCols);
			console.log('数据',this.narrowFractionDatas);
        }
    }
}
</script>
