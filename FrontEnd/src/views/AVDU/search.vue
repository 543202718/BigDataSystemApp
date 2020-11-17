<template>
    <div>
        <el-form inline label-width="100px">
            <!-- 装置类别 -->
            <el-form-item label="装置类别" style="text-align:left">
                <el-select
                    v-model="system_type"
                    filterable
                    allow-create
                    clearable
                >
                    <el-option
                        label="炼油装置（燃料油）"
                        value="炼油装置（燃料油）"
                    >
                    </el-option>
                    <el-option
                        label="炼油装置（润滑油）"
                        value="炼油装置（润滑油）"
                    ></el-option>
                    <el-option label="化工装置" value="化工装置"></el-option>
                    <el-option
                        label="炼油化工一体化装置"
                        value="炼油化工一体化装置"
                    ></el-option>
                </el-select>
            </el-form-item>
            <!-- 工艺类型 -->
            <el-form-item label="工艺类型" style="text-align:left">
                <el-select
                    v-model="process_type"
                    filterable
                    allow-create
                    clearable
                >
                    <el-option label="单常压装置" value="单常压装置">
                    </el-option>
                    <el-option label="单减压装置" value="单减压装置">
                    </el-option>
                    <el-option label="常减压装置" value="常减压装置">
                    </el-option>
                    <el-option label="双减压装置" value="双减压装置">
                    </el-option>
                </el-select>
            </el-form-item>
            <br />
            <!-- 原料密度 -->
            <el-form-item label="原料密度">
                <el-form-item>
                    <el-input
                        placeholder="密度下界"
                        v-model="density_l"
                        clearable
                    >
                    </el-input>
                </el-form-item>
                -
                <el-form-item>
                    <el-input
                        placeholder="密度上界"
                        v-model="density_u"
                        clearable
                    >
                    </el-input>
                </el-form-item>
            </el-form-item>
            <br />
            <!-- 原料酸值     -->
            <el-form-item label="原料酸值">
                <el-form-item>
                    <el-input placeholder="酸值下界" v-model="acid_l" clearable>
                    </el-input>
                </el-form-item>
                -
                <el-form-item>
                    <el-input placeholder="酸值上界" v-model="acid_u" clearable>
                    </el-input>
                </el-form-item>
            </el-form-item>
            <br />
            <!-- 原料含硫率     -->
            <el-form-item label="原料含硫率">
                <el-form-item>
                    <el-input placeholder="含硫率下界" v-model="s_l" clearable>
                    </el-input>
                </el-form-item>
                -
                <el-form-item>
                    <el-input placeholder="含硫率上界" v-model="s_u" clearable>
                    </el-input>
                </el-form-item>
            </el-form-item>
            <br />
            <el-form-item>
                <el-button type="primary" @click="onSubmit">查询</el-button>
            </el-form-item>
        </el-form>

        <el-table :data="tableData" border style="width: 100%">
            <el-table-column fixed="left" prop="id" label="序号" width="50">
            </el-table-column>
            <el-table-column prop="name" label="装置名称" width="300">
            </el-table-column>
            <el-table-column prop="type" label="装置类型" width="200">
            </el-table-column>
            <el-table-column prop="process_type" label="工艺类型" width="150">
            </el-table-column>
            <el-table-column prop="density" label="密度(kg/m^3)" width="120">
            </el-table-column>
            <el-table-column prop="acid" label="酸值(mgKOH/g)" width="150">
            </el-table-column>
            <el-table-column prop="value" label="含硫量(w%)" width="100">
            </el-table-column>
            <el-table-column fixed="right" label="操作" width="100">
                <template slot-scope="scope">
                    <el-button
                        @click="handleClick(scope.row)"
                        type="text"
                        size="medium"
                        >跳转</el-button
                    >
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            system_type: "",
            process_type: "",
            density_l: "",
            density_u: "",
            acid_l: "",
            acid_u: "",
            s_u: "",
            s_l: "",
            tableData: []
        };
    },
    methods: {
        remove() {},
        onSubmit() {
            this.$http
                .post(
                    "http://" + document.domain + ":5000/AVDU_search",
                    {
                        system_type: this.system_type,
                        process_type: this.process_type,
                        density_l: this.density_l,
                        density_u: this.density_u,
                        acid_l: this.acid_l,
                        acid_u: this.acid_u,
                        s_u: this.s_u,
                        s_l: this.s_l
                        //发送给后端的信息，可以按照需求增加条目
                    },
                    {
                        emulateJSON: true //必需，否则可能会json解析出错
                    }
                )
                .then(function(response) {
                    //response.body是报文的主体内容
                    if (parseInt(response.body.code) === 200) {
                        this.$message({
                            message: "查询成功",
                            type: "success",
                            duration: 3000,
                            showClose: true
                        });
                        console.log(response.body.list);
                        this.tableData = response.body.list;
                    } else {
                        this.$message({
                            message: "查询失败",
                            type: "error",
                            duration: 3000,
                            showClose: true
                        });
                    }
                });
        }
    }
};
</script>

<style>
.el-form-item {
    border: lawngreen;
}
</style>
