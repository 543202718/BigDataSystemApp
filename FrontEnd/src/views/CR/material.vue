<template>
<div>
    <el-form ref="form" :model="materialInfo" label-width="130px" size="mini" style="margin-top: 20px">
        <h4>原料来源</h4>

        <el-form-item label="轻烃回收">
            <el-input v-model="materialInfo.low_hc" placeholder="例：沙轻和科威特混合原油"></el-input>
        </el-form-item>
        <el-form-item label="加氢裂化">
            <el-input v-model="materialInfo.hydro_crack" placeholder="单位：kg/m³">
            </el-input>
        </el-form-item>
        <el-form-item label="乙烯裂解">
            <el-input v-model="materialInfo.eth_crack" placeholder="单位：℃"></el-input>
        </el-form-item>

        <h4>其他元素</h4>
        <el-form-item label="S">
            <el-input v-model="otherInfo.sulfur" placeholder="单位：ppm"></el-input>
        </el-form-item>
        <el-form-item label="N">
            <el-input v-model="otherInfo.nitrogen" placeholder="单位：ppm"></el-input>
        </el-form-item>
        <el-form-item label="As">
            <el-input v-model="otherInfo.arsenic" placeholder="单位：ppb"></el-input>
        </el-form-item>
        <el-form-item label="Cl">
            <el-input v-model="otherInfo.chlorine" placeholder="单位：ppm"></el-input>
        </el-form-item>
        <el-form-item label="Cu">
            <el-input v-model="otherInfo.copper" placeholder="单位：ppb"></el-input>
        </el-form-item>
        <el-form-item label="Pb">
            <el-input v-model="otherInfo.lead" placeholder="单位：μg/L"></el-input>
        </el-form-item>                        
    
    
        <h4>原料性质表</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas()">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(inDatas)">增加行</el-button>
            <el-button @click="delLastRow(inDatas)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>

        <el-table :data="inDatas" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="materialCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in materialCols" :key="idx" :index="idx">
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
        </el-table>




    </el-form>
</div>
</template>

<script>
export default {
    data() {
        return {
            materialInfo:{
                low_hc: '',
                hydro_crack: '',
                eth_crack: '',
            },
            materialCols: [
                { col: "group_composition", txt: '族组成' },
                { col: "alkane", txt: '烷烃' },
                { col: "cyclane", txt: '环烷烃' },
                { col: "arene", txt: '芳烃' },
            ],
            otherInfo:{
                sulfur: '',
                nitrogen: '',
                arsenic: '',
                chlorine: '',
                copper: '',
                lead: '',
            },
            inDatas: [],
            //outDatas: [],
            count_col: 0,
            showMenu: false,
            curColumn: null,
        };
    },

    created: function () {
        console.log("turn to system page");
        var inItems = ["C3", "C4", "C5", "C6", "C7", "C8", "C9","C10","C11","合计"];

        for (var item in inItems) {
            this.addRow(this.inDatas);
            this.inDatas[this.inDatas.length - 1].group_composition.content = inItems[item];
        }   
    },



    methods: {
        addToStore: function () {
            this.$store.balanceInfo = {
                tableCols: null,
                inDatas: null,
            };
            this.$store.balanceInfo.tableCols = this.materialInfo; //表头
            this.$store.balanceInfo.inDatas = this.inDatas; //产品粘度温度点
        
        //  this.$store.balanceInfo.outDatas = this.outDatas; //产品性质表内容
        
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store balanceInfo to device');
        
            // console.log(this.$store.deviceInfo.tableCols);
        },
        addRow(table) { // 新增行
            this.showMenu = false
            var obj = {}
            this.materialCols.map(p => {
                obj[p.col] = {
                    content: '',
                    show: true
                }
            })
            table.push(obj)
        },
        delLastRow(table) { // 删除行
            this.showMenu = false
            var len = table.length;
            if (len > 0) table.splice(len - 1, 1);
            else this.$message.error('没有可删除行');
        },
        consoleDatas() {
            console.log('表头', this.materialInfo);
            console.log('入方数据', this.inDatas);
        }
    },

}
</script>