<template>
<div id="hello">
    <template>
        <br> 
    <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
        <el-tab-pane label="全装置物料平衡" name="first">
    <div>
        <h4>全装置物料平衡表-入方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas()">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(inDatas_all)">增加行</el-button>
            <el-button @click="delLastRow(inDatas_all)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="inDatas_all" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    <div>
        <h4>全装置物料平衡表-出方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(outDatas_all)">增加行</el-button>
            <el-button @click="delLastRow(outDatas_all)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="outDatas_all" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    
    <el-button type="primary" @click="addToStore">暂存此页</el-button>
        
    </el-tab-pane>
    <el-tab-pane label="预处理部分物料平衡" name="second">
        <div>
        <h4>预处理部分物料平衡表-入方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas()">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(inDatas_preprocessed)">增加行</el-button>
            <el-button @click="delLastRow(inDatas_preprocessed)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="inDatas_preprocessed" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    <div>
        <h4>预处理部分物料平衡表-出方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(outDatas_preprocessed)">增加行</el-button>
            <el-button @click="delLastRow(outDatas_preprocessed)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="outDatas_preprocessed" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    
    <el-button type="primary" @click="addToStore">暂存此页</el-button>    
        
    </el-tab-pane>
    <el-tab-pane label="重整部分物料平衡" name="third">
        <div>
        <h4>重整部分物料平衡表-入方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas()">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(inDatas_chongzheng)">增加行</el-button>
            <el-button @click="delLastRow(inDatas_chongzheng)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="inDatas_chongzheng" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    <div>
        <h4>重整部分物料平衡表-出方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(outDatas_chongzheng)">增加行</el-button>
            <el-button @click="delLastRow(outDatas_chongzheng)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="outDatas_chongzheng" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    
    <el-button type="primary" @click="addToStore">暂存此页</el-button>    

    </el-tab-pane>
    <el-tab-pane label="PSA部分物料平衡" name="fourth">
        <div>
        <h4>PSA部分物料平衡表-入方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas()">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(inDatas_psa)">增加行</el-button>
            <el-button @click="delLastRow(inDatas_psa)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="inDatas_psa" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    <div>
        <h4>PSA部分物料平衡表-出方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(outDatas_psa)">增加行</el-button>
            <el-button @click="delLastRow(outDatas_psa)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="outDatas_psa" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    
    <el-button type="primary" @click="addToStore">暂存此页</el-button>   
    </el-tab-pane>
    <el-tab-pane label="苯抽提部分物料平衡" name="fifth">
        <div>
        <h4>苯抽提部分物料平衡表-入方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas()">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(inDatas_benzene)">增加行</el-button>
            <el-button @click="delLastRow(inDatas_benzene)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="inDatas_benzene" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    <div>
        <h4>苯抽提部分物料平衡表-出方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(outDatas_benzene)">增加行</el-button>
            <el-button @click="delLastRow(outDatas_benzene)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="outDatas_benzene" border max-height="600" style="width: 100%;margin-top:10px">
            <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
            <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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
    </div>
    
    <el-button type="primary" @click="addToStore">暂存此页</el-button>    

    </el-tab-pane>
    </el-tabs>
    </template>

</div>
</template>

<script>
export default {
    data() {
        return {
            balanceCols: [
                { col: "inward_or_outward_name", txt: '名称' },
                { col: "yield", txt: '收率m%' },
                { col: "flow_rate1", txt: '流率（公斤/时）' },
                { col: "flow_rate2", txt: '流率（吨/天）' },
                { col: "flow_rate3", txt: '流率（万吨/年）' },
                { col: "note", txt: '备注' },
            ],
            inDatas_all: [],
            outDatas_all: [],
            inDatas_preprocessed: [],
            outDatas_preprocessed: [],
            inDatas_chongzheng: [],
            outDatas_chongzheng: [],        
            inDatas_psa: [],
            outDatas_psa: [],            
            inDatas_benzene: [],
            outDatas_benzene: [],

            count_col: 0,
            showMenu: false,
            curColumn: null,
        };

    },

    created: function () {
        console.log("turn to system page");
        var inItems_all = ["混合石脑油", "直馏重石脑油", "加氢裂化重石脑油", "裂解汽油抽余油","合计"];
        var outItems_all = ["液化气", "重整汽油", "苯", "拔头油", "含氢气体", "含氢气体中纯氢", "燃料气", "C6馏分", "戊烷油",
            "含硫燃料气", "高辛烷值重整汽油", "抽余油", "合计"];
        var inItems_preprocessed = ["混合石脑油", "含氢气体中纯氢", "直馏重石脑油", "裂解汽油抽余油",  "合计"];
        var outItems_preprocessed = ["精制石脑油", "轻石脑油", "燃料气", "含硫燃料气", "合计"];
        var inItems_chongzheng = ["直馏石脑油", "精制石脑油", "加氢裂化重石脑油", "轻石脑油","合计"];
        var outItems_chongzheng = ["液化气", "含氢气体", "含氢气体中纯氢","含氢气体至预处理","燃料气", "C6馏分", "戊烷油","重整汽油", "高辛烷值重整汽油", "抽余油", "合计"];
        var inItems_psa = ["含氢气体", "合计"];
        var outItems_psa = ["高纯度氢气", "解吸气", "合计"];
        var inItems_benzene = ["C6馏分",  "合计"];
        var outItems_benzene = ["苯", "抽余油", "合计"];

        for (var item in inItems_all) {
            this.addRow(this.inDatas_all);
            this.inDatas_all[this.inDatas_all.length - 1].inward_or_outward_name.content = inItems_all[item];
        }
        for (var item in outItems_all) {
            this.addRow(this.outDatas_all);
            this.outDatas_all[this.outDatas_all.length - 1].inward_or_outward_name.content = outItems_all[item];
        }

        for (var item in inItems_preprocessed) {
            this.addRow(this.inDatas_preprocessed);
            this.inDatas_preprocessed[this.inDatas_preprocessed.length - 1].inward_or_outward_name.content = inItems_preprocessed[item];
        }
        for (var item in outItems_preprocessed) {
            this.addRow(this.outDatas_preprocessed);
            this.outDatas_preprocessed[this.outDatas_preprocessed.length - 1].inward_or_outward_name.content = outItems_preprocessed[item];
        }
        for (var item in inItems_chongzheng) {
            this.addRow(this.inDatas_chongzheng);
            this.inDatas_chongzheng[this.inDatas_chongzheng.length - 1].inward_or_outward_name.content = inItems_chongzheng[item];
        }
        for (var item in outItems_chongzheng) {
            this.addRow(this.outDatas_chongzheng);
            this.outDatas_chongzheng[this.outDatas_chongzheng.length - 1].inward_or_outward_name.content = outItems_chongzheng[item];
        }
        for (var item in inItems_psa) {
            this.addRow(this.inDatas_psa);
            this.inDatas_psa[this.inDatas_psa.length - 1].inward_or_outward_name.content = inItems_psa[item];
        }
        for (var item in outItems_psa) {
            this.addRow(this.outDatas_psa);
            this.outDatas_psa[this.outDatas_psa.length - 1].inward_or_outward_name.content = outItems_psa[item];
        }
        for (var item in inItems_benzene) {
            this.addRow(this.inDatas_benzene);
            this.inDatas_benzene[this.inDatas_benzene.length - 1].inward_or_outward_name.content = inItems_benzene[item];
        }
        for (var item in outItems_benzene) {
            this.addRow(this.outDatas_benzene);
            this.outDatas_benzene[this.outDatas_benzene.length - 1].inward_or_outward_name.content = outItems_benzene[item];
        }

    },
    methods: {
        addToStore: function () {
            this.$store.balanceInfo = {
                tableCols: null,
                inDatas_all: null,
                outDatas_all: null,
                inDatas_preprocessed: null,
                outDatas_preprocessed: null,
                inDatas_chongzheng: null,
                outDatas_chongzheng: null,
                inDatas_psa: null,
                outDatas_psa: null,
                inDatas_benzene: null,
                outDatas_benzene: null,
            };

            this.$store.balanceInfo.tableCols = this.balanceCols; //表头
            this.$store.balanceInfo.inDatas_all = this.inDatas_all; //全装置物料平衡 入方
            this.$store.balanceInfo.outDatas_all = this.outDatas_all; //全装置物料平衡 出方
            this.$store.balanceInfo.inDatas_preprocessed = this.inDatas_preprocessed; //预处理物料平衡 入方
            this.$store.balanceInfo.outDatas_preprocessed = this.outDatas_preprocessed; //预处理物料平衡 出方
            this.$store.balanceInfo.inDatas_chongzheng = this.inDatas_chongzheng; //重整装置物料平衡 入方
            this.$store.balanceInfo.outDatas_chongzheng = this.outDatas_chongzheng; //重整装置物料平衡 出方
            this.$store.balanceInfo.inDatas_psa = this.inDatas_psa; //psa物料平衡 入方
            this.$store.balanceInfo.outDatas_psa = this.outDatas_psa; //psa物料平衡 出方
            this.$store.balanceInfo.inDatas_benzene = this.inDatas_benzene; //苯抽提物料平衡 入方
            this.$store.balanceInfo.outDatas_benzene = this.outDatas_benzene; //苯抽提物料平衡 出方


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
            this.balanceCols.map(p => {
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
            console.log('表头', this.balanceCols);
            console.log('全装置物料平衡入方数据', this.inDatas_all);
            console.log('全装置物料平衡出方数据', this.outDatas_all);
            console.log('预处理物料平衡入方数据', this.inDatas_preprocessed);
            console.log('预处理物料平衡出方数据', this.outDatas_preprocessed);
            console.log('重整装置物料平衡入方数据', this.inDatas_chongzheng);
            console.log('重整装置物料平衡出方数据', this.outDatas_chongzheng);
            console.log('psa物料平衡入方数据', this.inDatas_psa);
            console.log('psa物料平衡出方数据', this.outDatas_psa);
            console.log('苯抽提物料平衡入方数据', this.inDatas_benzene);
            console.log('苯抽提物料平衡出方数据', this.outDatas_benzene);


        }
    },

}
</script>
