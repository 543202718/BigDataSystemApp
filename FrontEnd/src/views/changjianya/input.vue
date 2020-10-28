<template>
<div>
    <el-radio-group v-model="radio1">
        <el-radio-button @click.native="changeFormShow(0)" label="装置概况"></el-radio-button>
        <el-radio-button @click.native="changeFormShow(1)" label="原料性质"></el-radio-button>
        <el-radio-button label="产品性质"></el-radio-button>
        <el-radio-button label="物料平衡"></el-radio-button>
        <el-radio-button label="操作条件"></el-radio-button>
        <br>
        <el-radio-button label="公用工程"></el-radio-button>
        <el-radio-button label="装置投资"></el-radio-button>
        <el-radio-button label="主要设备"></el-radio-button>
        <el-radio-button label="三废排放"></el-radio-button>
        <el-radio-button label="化学药剂"></el-radio-button>
    </el-radio-group>
    <br>

    <!--装置概况-->
    <el-form v-if="this.show[0]" ref="form" :model="deviceInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="项目名称">
            <el-input v-model="deviceInfo.name" placeholder = "例：xx科技有限公司1000万吨/年的炼油化工一体项目"></el-input>
        </el-form-item>
        <el-form-item label="项目描述">
            <el-input v-model="deviceInfo.describe" placeholder="例：xx科技有限公司炼油化工一体项目100万吨/年常减压蒸馏装置">
            </el-input>
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
        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>


<!--原料性质-->

    </el-form>
    <el-form v-if="this.show[1]" ref="form" :model="sizeForm" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="原料名称">
            <el-input v-model="sizeForm.name" placeholder="例：沙轻和科威特混合原油"></el-input>
        </el-form-item>
        <el-form-item :inline="true" label="原料密度">
            <el-col :span="5">
            <el-input v-model="sizeForm.name" placeholder="例：沙轻和科威特混合原油"></el-input>
            </el-col>
            <el-col :span="5">
                <el-select v-on="sizeForm.unit" placeholder="请选择单位">
                <el-option label="g/m^3" value="g/m^3"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
    </el-select>
            </el-col>
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
            <el-input v-model="sizeForm.resource[0]" size="medium" placeholder="废水">
            </el-input>

            <el-input v-model="sizeForm.resource[1]" size="medium" placeholder="废气">
            </el-input>
            <el-input v-model="sizeForm.resource[2]" size="medium" placeholder="废渣">
            </el-input>
        </el-form-item>
        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</div>
</template>

<script>
export default {
    
     
    data() {
        console.log('get here')
        return {
            show: [true, false, false],
            radio1: '装置概况',
            deviceInfo:{
                name:'',
                describe:'',
                startTime:'',
                endTime:'',
                deviceType:'',


            },
            sizeForm: {
                name: '',
                describe: '',
                date1: '',
                date2: '',
                unit:'',
                delivery: false,
                type: [],
                resource: ['','',''],
                desc: ''
            }
        };
    },
    methods: {
        onSubmit() {
            console.log('submit!');
        },
        changeFormShow(showFormID){
            console.log('change showed form');
            this.show = [false,false,false]
            this.show[showFormID] = true;
            console.log(this.show);
        }
    }
};
</script>

<style>
.el-form-item {
    border: lawngreen;

}
</style>
