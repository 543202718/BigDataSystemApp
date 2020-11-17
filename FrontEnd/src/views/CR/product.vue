<template>
<div id="hello">
    <div id="hello">
        <h4 style="display: inline-block;margin:0;">产品性质</h4>
        <div style="display: inline-block;float: right;">
            <el-button v-if="showTable" size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button v-if="showTable" size="mini" type="primary" @click="addRow">增加行</el-button>
            <el-button v-if="showTable" @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <br><br>
        <div>
            粘度温度点（℃）
            <el-select v-model="viscosity_t" multiple filterable allow-create :disabled="showTable" placeholder="请选择温度">
                <el-option label="20" value=20></el-option>
                <el-option label="40" value=40></el-option>
            </el-select>
            <el-button type="primary" @click="refreshTable">创建表格</el-button>
        </div>
        <el-table v-if="showTable" :data="productDatas" border style="width: 100%;margin-top:10px" max-height="500">
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
                    <p v-show="scope.row[column.col].show" @dblclick="scope.row[column.col].show=false">
                        {{scope.row[column.col].content}}
                        <i class="el-icon-edit-outline" @click="scope.row[column.col].show=false"></i>
                    </p>
                    <el-input type="textarea" :autosize="{minRows:2,maxRows:4}" v-show="!scope.row[column.col].show" v-model="scope.row[column.col].content" @blur="scope.row[column.col].show=true">
                    </el-input>
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
        <br>
        <el-button type="primary" @click="addToStore">暂存此页</el-button>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            showTable: false,
            viscosity_t: [],
            productCols: [{ col: "product_name", txt: '产品名称' },
                { col: "density", txt: '密度(20℃) （kg/m³）' },
                { col: "API", txt: '比重指数(API)' },
                { col: "molecular_weight", txt: '分子量' },
                { col: "characteristic_factor", txt: '特性因数' },
                { col: "sulfur_content", txt: '含硫量（wt/%）' },
                { col: "acid_value", txt: '酸值（mgKOH/g）' },
                { col: "remarks", txt: '备注' }
            ],
            productDatas: [],
            count_col: 0,
            curColumn: null,
        };

    },

    created: function () {
        console.log("turn to system page");
        var items = ["初顶气", "初顶油", "常顶气", "常顶油", "常一线", "常二线", "常三线", "常四线", "常压渣油（常底油）",
            "贫吸收油", "常压重油", "过汽化油", "减顶气", "减顶油", "减一线", "减二线", "减三线", "减四线", "减五线",
            "减六线", "减压渣油"
        ];
        for (var item in items) {
            this.addRow();
            this.productDatas[this.productDatas.length - 1].product_name.content = items[item];
        }
    },
    methods: {
        addToStore: function () {
            this.$store.productInfo = {
                tableCols: null,
                viscosity_t: null,
                tableDatas: null,
            };
            this.$store.productInfo.tableCols = this.productCols; //产品性质表头
            this.$store.productInfo.viscosity_t = this.viscosity_t; //产品粘度温度点
            this.$store.productInfo.tableDatas = this.productDatas; //产品性质表内容
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store productInfo to device');
            // console.log(this.$store.deviceInfo.tableCols);
        },
        refreshTable() { //根据设置的粘度创建表格
            for (var x in this.viscosity_t) {
                var _this = this
                this.productDatas.map(p => { // 新增的对象无法被vue监听到
                    _this.$set(p, "vis" + this.viscosity_t[x], { content: '', show: true })
                    //		p[obj.col] = {content: '', show: true}
                })
            }
            this.showTable = true
        },
        addRow() { // 新增行
            this.showMenu = false
            var obj = {}
            this.productCols.map(p => {
                obj[p.col] = {
                    content: '',
                    show: true
                }
            })
            this.productDatas.push(obj)
        },
        delLastRow() { // 删除行
            this.showMenu = false
            var len = this.productDatas.length;
            if (len > 0) this.productDatas.splice(len - 1, 1);
            else this.$message.error('没有可删除行');
        },
        consoleDatas() {
            console.log('表头', this.productCols);
            console.log('数据', this.productDatas);
        }
    },

}
</script>
