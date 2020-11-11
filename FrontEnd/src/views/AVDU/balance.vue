<template>
<div id="hello">

    <div style="display: inline-block;float: right;">
        <el-button size="mini" type="primary" @click="consoleDatas">打印数据</el-button>
        <el-button size="mini" type="primary" @click="addRow">增加行</el-button>
        <el-button @click="delLastRow" slot="reference" type="primary" size="mini">删除末行</el-button>

    </div>
    <el-table :data="balanceDatas" border height=500 style="width: 100%;margin-top:10px" @header-contextmenu="colRightClick">
        <el-table-column v-if="balanceCols.length > 0" type="index" :label="'编号'" :width="50"></el-table-column>
        <el-table-column v-for="(column, idx) in balanceCols" :key="idx" :index="idx">
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

            balanceCols: [{
                    col: "inward_or_outward_name",
                    txt: '名称',
                    show: true
                },
                {
                    col: "boiling_point_cutting_range",
                    txt: '实沸点切割范围/℃',
                    show: true
                },
                {
                    col: "yield",
                    txt: '收率m%',
                    show: true
                },
                {
                    col: "flow_rate1",
                    txt: '流率（公斤/时）',
                    show: true
                },
                {
                    col: "flow_rate2",
                    txt: '流率（吨/天）',
                    show: true
                },
                {
                    col: "flow_rate3",
                    txt: '流率（万吨/年）',
                    show: true
                },

            ],
            balanceDatas: [{

                    inward_or_outward_name: {
                        content: '原料油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '富吸收油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '渣油加氢液态烃',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '渣油加氢石脑油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '蜡油加氢石脑油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '柴油加氢石脑油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },

                {

                    inward_or_outward_name: {
                        content: '初顶气',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '初顶油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '常顶气',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '常顶油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '常一线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '常二线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '常三线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '常四线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '常压渣油（常底油）',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '贫吸收油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '(常压重油)',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '(过汽化油)',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减顶气',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减顶油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减一线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减二线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减三线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减四线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减五线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减六线',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

                },
                {

                    inward_or_outward_name: {
                        content: '减压渣油',
                        show: true
                    },
                    boiling_point_cutting_range: {
                        content: ' ',
                        show: true
                    },
                    yield: {
                        content: ' ',
                        show: true
                    },
                    flow_rate1: {
                        content: ' ',
                        show: true
                    },
                    flow_rate2: {
                        content: ' ',
                        show: true
                    },
                    flow_rate3: {
                        content: ' ',
                        show: true
                    },

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
            this.balanceCols.map(p => {
                obj[p.col] = {
                    content: '',
                    show: true
                }
            })
            this.balanceDatas.push(obj)
        },
        // 当row中存在一“主键”可唯一标识row的下标时（如：编号放在balanceDatas内），可借此实现行的自由插入与删除
        addColumn(idx) { // 新增列
            this.showMenu = false
            var obj = {
                col: 'col_' + this.count_col++,
                txt: '',
                show: true
            }
            if (idx || idx === 0) this.balanceCols.splice(idx, 0, obj);
            else this.balanceCols.push(obj);
            var _this = this
            this.balanceDatas.map(p => { // 新增的对象无法被vue监听到
                _this.$set(p, obj.col, {
                    content: '',
                    show: true
                })
                //		p[obj.col] = {content: '', show: true}
            })
        },
        delColumn() { // 删除列
            this.showMenu = false
            var colKey = this.balanceCols[this.curColumn].col;
            this.balanceCols.splice(this.curColumn, 1);
            this.balanceDatas.map(p => {
                delete p[colKey];
            });
        },
        delLastRow() { // 删除行
            this.showMenu = false
            var len = this.balanceDatas.length;
            if (len > 0) this.balanceDatas.splice(len - 1, 1);
            else this.$message.error('没有可删除行');
        },
        consoleDatas() {
            console.log('表头', this.balanceCols);
            console.log('数据', this.balanceDatas);
        }
    },

}
</script>
