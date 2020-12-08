<template>
<div id="hello">

    <div>
        <h4>物料平衡表-入方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas()">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(inDatas)">增加行</el-button>
            <el-button @click="delLastRow(inDatas)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="inDatas" border max-height="600" style="width: 100%;margin-top:10px">
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
        <h4>物料平衡表-出方</h4>
        <div style="display: inline-block;float: right;">
            <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
            <el-button size="mini" type="primary" @click="addRow(outDatas)">增加行</el-button>
            <el-button @click="delLastRow(outDatas)" slot="reference" type="primary" size="mini">删除末行</el-button>
        </div>
        <el-table :data="outDatas" border max-height="600" style="width: 100%;margin-top:10px">
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
</div>
</template>

<script>
export default {
    data() {
        return {
            balanceCols: [
                { col: "inward_or_outward_name", txt: '名称' },
                { col: "boiling_point_cutting_range", txt: '实沸点切割范围（℃）' },
                { col: "yield", txt: '收率（m%）' },
                { col: "flow_rate1", txt: '流率（公斤/时）' },
                { col: "flow_rate2", txt: '流率（吨/天）' },
                { col: "flow_rate3", txt: '流率（万吨/年）' },
                { col: "note", txt: '备注' },
            ],
            inDatas: [],
            outDatas: [],
            count_col: 0,
            showMenu: false,
            curColumn: null,
        };

    },

    created: function () {
        console.log("turn to system page");
        if ('balanceInfo' in this.$store) {
            this.balanceCols = this.$store.balanceInfo.tableCols;
            this.inDatas = this.$store.balanceInfo.inDatas;
            this.outDatas = this.$store.balanceInfo.outDatas;
        } else {
            var inItems = ["原料油", "富吸收油", "渣油加氢液态烃", "渣油加氢石脑油", "蜡油加氢石脑油", "柴油加氢石脑油", "合计"];
            var outItems = ["初顶气", "初顶油", "常顶气", "常顶油", "常一线", "常二线", "常三线", "常四线", "常压渣油（常底油）",
                "贫吸收油", "常压重油", "过汽化油", "减顶气", "减顶油", "减一线", "减二线", "减三线", "减四线", "减五线",
                "减六线", "减压渣油", "常压拔出率", "减压拔出率", "合计"
            ];
            for (var item in inItems) {
                this.addRow(this.inDatas);
                this.inDatas[this.inDatas.length - 1].inward_or_outward_name.content = inItems[item];
            }
            for (var item in outItems) {
                this.addRow(this.outDatas);
                this.outDatas[this.outDatas.length - 1].inward_or_outward_name.content = outItems[item];
            }
        }
    },
    methods: {
        addToStore: function () {
            this.$store.balanceInfo = {
                tableCols: null,
                inDatas: null,
                outDatas: null,
            };
            this.$store.balanceInfo.tableCols = this.balanceCols; //表头
            this.$store.balanceInfo.inDatas = this.inDatas; //产品粘度温度点
            this.$store.balanceInfo.outDatas = this.outDatas; //产品性质表内容
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
            console.log('入方数据', this.inDatas);
            console.log('出方数据', this.inDatas);
        }
    },

}
</script>
