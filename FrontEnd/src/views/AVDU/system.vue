<template>
<div>
<el-form  ref="form" :model="deviceInfo" label-width="100px" size="mini" style="margin-top: 20px">
    <el-form-item label="项目名称">
        <el-input v-model="deviceInfo.name" placeholder="例：xx科技有限公司1000万吨/年的炼油化工一体项目"></el-input>
    </el-form-item>
    <el-form-item label="项目描述">
        <el-input v-model="deviceInfo.describe" placeholder="例：xx科技有限公司炼油化工一体项目100万吨/年常减压蒸馏装置">
        </el-input>
    </el-form-item>
    <el-form-item label="项目号">
        <el-input v-model="deviceInfo.id" placeholder="例：20200101"></el-input>
    </el-form-item>
    <el-form-item label="设计完成时间">
        <el-col :span="11">
            <el-date-picker type="date" placeholder="选择日期" v-model="deviceInfo.date1" style="width: 100%;"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
            <el-time-picker placeholder="选择时间" v-model="deviceInfo.date2" style="width: 100%;"></el-time-picker>
        </el-col>
    </el-form-item>

    <el-form-item label="装置类别">
        <el-checkbox-group v-model="deviceInfo.deviceType">
            <el-checkbox-button label="炼油装置（燃料油）" name="type"></el-checkbox-button>
            <el-checkbox-button label="炼油装置（润滑油）" name="type"></el-checkbox-button>
            <el-checkbox-button label="化工装置" name="type"></el-checkbox-button>
            <el-checkbox-button label="炼油化工一体化装置" name="type"></el-checkbox-button>
            <el-checkbox-button label="其它" name="type"></el-checkbox-button>
        </el-checkbox-group>
    </el-form-item>
    <el-form-item label="设计单位">
        <el-input v-model="deviceInfo.describe" placeholder="例：SEI">
        </el-input>
    </el-form-item>
    <el-form-item label="业主单位">
        <el-input v-model="deviceInfo.describe" placeholder="例：xx科技有限公司">
        </el-input>
    </el-form-item>


</el-form>
</div>
</template>

<script>
export default {
    data() {
        return {
            deviceInfo: {
                id: '',
                name: '',
                describe: '',
                place: '',
                owner: '',
                owner_doc_no: '',

                startTime: '',
                endTime: '',
                deviceType: '',

            },
        };
    
    },
    
}
</script>
