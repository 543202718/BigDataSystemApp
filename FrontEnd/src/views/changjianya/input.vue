<template>
<div>
    <el-radio-group v-model="sizeForm">
        <el-radio-button @click="sizeForm.show[0]=false" label="装置概况"></el-radio-button>
        <el-radio-button label="原料性质"></el-radio-button>
        <el-radio-button label="产品性质"></el-radio-button>
        <el-radio-button label="物料平衡"></el-radio-button>
        <el-radio-button label="操作条件"></el-radio-button>
        <el-radio-button label="公用工程"></el-radio-button>
        <el-radio-button label="装置投资"></el-radio-button>
        <el-radio-button label="主要设备"></el-radio-button>
        <el-radio-button label="三废排放"></el-radio-button>
        <el-radio-button label="化学药剂"></el-radio-button>
    </el-radio-group>
    <br>
    <el-form v-if="show[0]" ref="form" :model="sizeForm" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="项目名称">
            <el-input v-model="sizeForm.name"></el-input>
        </el-form-item>
        <el-form-item label="项目描述">
            <el-select v-model="sizeForm.region" placeholder="请选择活动区域">
                <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="设计完成时间">
            <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="sizeForm.date1" style="width: 100%;"></el-date-picker>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
                <el-time-picker placeholder="选择时间" v-model="sizeForm.date2" style="width: 100%;"></el-time-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="装置类别">
            <el-checkbox-group v-model="sizeForm.type">
                <el-checkbox-button label="炼油" name="type"></el-checkbox-button>
                <el-checkbox-button label="化工" name="type"></el-checkbox-button>
                <el-checkbox-button label="。。。 " name="type"></el-checkbox-button>
            </el-checkbox-group>
        </el-form-item>
        <el-form-item label="三废排放">
            <el-input v-model="sizeForm.resource" size="medium" placeholder="废水">
            </el-input>

            <el-input v-model="sizeForm.resource" size="medium" placeholder="废气">
            </el-input>
            <el-input v-model="sizeForm.resource" size="medium" placeholder="废渣">
            </el-input>
        </el-form-item>
        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
    <el-form v-if="show[1]" ref="form" :model="sizeForm" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="原料名称">
            <el-input v-model="sizeForm.name"></el-input>
        </el-form-item>
        <el-form-item label="原料性质">
            <el-select v-model="sizeForm.region" placeholder="请选择活动区域">
                <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="设计完成时间">
            <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="sizeForm.date1" style="width: 100%;"></el-date-picker>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
                <el-time-picker placeholder="选择时间" v-model="sizeForm.date2" style="width: 100%;"></el-time-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="装置类别">
            <el-checkbox-group v-model="sizeForm.type">
                <el-checkbox-button label="炼油" name="type"></el-checkbox-button>
                <el-checkbox-button label="化工" name="type"></el-checkbox-button>
                <el-checkbox-button label="。。。 " name="type"></el-checkbox-button>
            </el-checkbox-group>
        </el-form-item>
        <el-form-item label="三废排放">
            <el-input v-model="sizeForm.resource" size="medium" placeholder="废水">
            </el-input>

            <el-input v-model="sizeForm.resource" size="medium" placeholder="废气">
            </el-input>
            <el-input v-model="sizeForm.resource" size="medium" placeholder="废渣">
            </el-input>
        </el-form-item>
        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
    {{show[0]}}
</div>
</template>

<script>
export default {
    
     
    data() {
        console.log('get here')
        return {
            show: [true, false, false],
            radio1: '装置概况',
            sizeForm: {
                name: '123',
                region: '',
                date1: '',
                date2: '',
                delivery: false,
                type: [],
                resource: '',
                desc: ''
            }
        };
    },
    methods: {
        onSubmit() {
            console.log('submit!');
        },
    }
};
</script>

<style>
.el-form-item {
    border: lawngreen;

}
</style>
