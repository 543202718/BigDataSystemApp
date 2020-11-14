<template>
<div>
    <el-form ref="form" :model="investmentInfo" label-width="220px" size="mini" style="margin-top: 20px">
        <el-form-item label="工程项目总投资（单位：万元）">
            <el-input v-model="investmentInfo.total" placeholder="此处填入工程项目总投资费用，单位万元，可输入小数点"></el-input>
        </el-form-item>
        <el-form-item label="建设投资（单位：万元）">
            <el-input v-model="investmentInfo.con_invest" placeholder="此处填入建设投资费用，单位万元，可输入小数点">
            </el-input>
        </el-form-item>
        <el-form-item label="工程费用（单位：万元）">
            <el-input v-model="investmentInfo.project_cost" placeholder="此处填入工程费用，单位万元，可输入小数点"></el-input>
        </el-form-item>
        <el-form-item label="设备购置费（单位：万元）">
            <el-input v-model="investmentInfo.equipment_fee" placeholder="此处填入设备购置费，单位万元，可输入小数点"></el-input>
        </el-form-item>
        <el-form-item label="安装工程费（单位：万元）">
            <el-input v-model="investmentInfo.installation_fee" placeholder="此处填入安装工程费，单位万元，可输入小数点">
            </el-input>
        </el-form-item>
        <el-form-item label="建筑工程费（单位：万元）">
            <el-input v-model="investmentInfo.construction_fee" placeholder="此处填入建筑工程费，单位万元，可输入小数点"></el-input>
        </el-form-item>
        <el-form-item label="其他费用（单位：万元）">
            <el-input v-model="investmentInfo.else" placeholder="此处填入以上没有考虑到的其他费用，单位万元，可输入小数点"></el-input>
        </el-form-item>
        <el-button type="primary" @click="addToStore">暂存此页</el-button>
    </el-form>
</div>
</template>

<script>
export default {
    data() {
        return {
            investmentInfo: {
                system_id: '',
                total: '',
                con_invest: '',
                project_cost: '',
                equipment_fee: '',
                installation_fee: '',
                construction_fee: '',
                else: '',
            },
        };

    },

    created: function () {
        console.log("turn to system page");
    },
    methods: {
        addToStore: function () {
            this.$store.investmentInfo = this.investmentInfo; //表内容
            this.$message({
                message: '暂存成功',
                type: 'success',
                duration: 3000,
                showClose: true
            });
            console.log('store investmentInfo to device');
        },
    },

}
</script>
