<template>
<div>
    <el-form ref="form" :model="deviceInfo" label-width="220px" size="mini" style="margin-top: 20px">
       <el-form-item label="设备类型" style="text-align:left">
            <el-select v-model="deviceInfo.type" filterable allow-create>
                <el-option label="塔器" value="塔器"></el-option>
                <el-option label="冷换设备" value="冷换设备"></el-option>
                <el-option label="空冷器" value="空冷器"></el-option>
                <el-option label="容器" value="容器"></el-option>
            </el-select>
            </el-form-item>
        <el-form-item label="国内进货">
            <el-input v-model="deviceInfo.internal" placeholder="此处填入国内进货台数"></el-input>
        </el-form-item>
        <el-form-item label="国外进货">
            <el-input v-model="deviceInfo.overseas" placeholder="此处填入国外进货台数">
            </el-input>
        </el-form-item>
        <el-form-item label="备注">
            <el-input v-model="deviceInfo.note" placeholder="填入备注内容"></el-input>
        </el-form-item>
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
            deviceInfo: {
                type:'设备类型',
                internal:'国内订货数',
                overseas:'国外订货数',
	            note:'备注', 
            },
        };

    },

    created: function () {
        console.log("turn to system page");
    },
    methods: {},

}
</script>
