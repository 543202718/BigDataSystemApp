<template>
<div id="hello">
    <div id="hello">
        
        <div style="display: inline-block;float: right;">
            <el-button v-if="showTable" size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button v-if="showTable" size="mini" type="primary" @click="addRow">增加行</el-button>
            <el-button v-if="showTable" @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <br><br>
        <div style="position:relative;left:500px;">
            <el-table v-if="true" :data="productDatas" border style="width:550px;margin-top:10px;" max-height="500" >
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

            </el-table>
        </div>
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
                { col: "output", txt: '数量 （万吨/年）' },
                { col: "purpose", txt: '去向或用途' },
            ],
            productDatas: [],
            count_col: 0,
            curColumn: null,
        };

    },

    created: function () {
        console.log("turn to system page");
        var items = ["液化气", "重整汽油", "苯", "拔头油", "含氢气体", "含氢气体中纯氢", "燃料气", "C6馏分", "戊烷油",
            "含硫燃料气", "高辛烷值重整汽油", "抽余油"
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
