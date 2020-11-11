<template>


<div id="hello">
    
    <div style="display: inline-block;float: right;">
        <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
        <el-button size="mini" type="primary" @click="addRow">增加行</el-button>
        <el-button @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>
        
    </div>
    <el-table :data="productDatas" border height=500 style="width: 100%;margin-top:10px" @header-contextmenu="colRightClick">
        <el-table-column v-if="productCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
        <el-table-column v-for="(column, idx) in productCols" :key="idx" :index="idx">
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
</template>

<script>
export default {
    data() {
        return {

            productCols: [
                {
                    col: "product_name",
                    txt: '产品名称',
                    show: true
                },
                {
                    col: "density",
                    txt: '密度 g/cm3(20℃)',
                    show: true
                },
                {
                    col: "API",
                    txt: '比重指数(API)',
                    show: true
                },
                {
                    col: "molecular_weight",
                    txt: '分子量(M)',
                    show: true
                },               
                {
                    col: "characteristic_factor",
                    txt: '特性因数(K)',
                    show: true
                },
                {
                    col: "sulfur_content",
                    txt: '含硫 wt/%',
                    show: true
                },
                {
                    col: "acid_value",
                    txt: '酸值mgKOH/g',
                    show: true
                },
                {
                    col: "remarks",
                    txt: '备注',
                    show: true
                }                

            ],
            productDatas: [
            {

                product_name: {
                    content: '初顶气',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '初顶油',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '常顶气',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '常顶油',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '常一线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '常二线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },            
            {

                product_name: {
                    content: '常三线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '常四线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '常压渣油（常底油）',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '贫吸收油',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '(常压重油)',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '(过汽化油)',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '减顶气',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '减顶油',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '减一线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '减二线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '减三线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '减四线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '减五线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },
            {

                product_name: {
                    content: '减六线',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },            
            {

                product_name: {
                    content: '减压渣油',
                    show: true
                },
                density: {
                    content: ' ',
                    show: true
                },
                API: {
                    content: ' ',
                    show: true
                },
                molecular_weight: {
                    content: ' ',
                    show: true
                },
                characteristic_factor: {
                    content: ' ',
                    show: true
                },
                sulfur_content: {
                    content: ' ',
                    show: true
                },
                acid_value: {
                    content: ' ',
                    show: true
                },
                remarks: {
                    content: ' ',
                    show: true
                }                                  
            },

            ],
            count_col: 0,
            showMenu: false,
            curColumn: null,
            //systemInfo:{s
            //    .....
            //}
        };

    },

    created: function () {
        console.log("turn to system page");
    },
    methods: {
        colRightClick(column, event) {
            window.event.returnValue = false; //阻止浏览器自带的右键菜单弹出
            if (!column.index && column.index !== 0) return;
            this.curColumn = column.index
            this.showMenu = true
            var ele = document.getElementById('contextmenu')
            ele.style.top = event.clientY + 'px';
            ele.style.left = event.clientX + 'px';
            if (window.innerWidth - 140 < event.clientX) {
                ele.style.left = 'unset'
                ele.style.right = 0
            }
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
        // 当row中存在一“主键”可唯一标识row的下标时（如：编号放在productDatas内），可借此实现行的自由插入与删除
        addColumn(idx) { // 新增列
            this.showMenu = false
            var obj = {
                col: 'col_' + this.count_col++,
                txt: '',
                show: true
            }
            if (idx || idx === 0) this.productCols.splice(idx, 0, obj);
            else this.productCols.push(obj);
            var _this = this
            this.productDatas.map(p => { // 新增的对象无法被vue监听到
                _this.$set(p, obj.col, {
                    content: '',
                    show: true
                })
                //		p[obj.col] = {content: '', show: true}
            })
        },
        delColumn() { // 删除列
            this.showMenu = false
            var colKey = this.productCols[this.curColumn].col;
            this.productCols.splice(this.curColumn, 1);
            this.productDatas.map(p => {
                delete p[colKey];
            });
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
