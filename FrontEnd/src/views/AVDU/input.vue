<template>
<div>
    <el-radio-group v-model="radio1">
        <el-radio-button @click.native="toSystem" label="装置概况"></el-radio-button>
        <el-radio-button label="原料性质"></el-radio-button>
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
    <router-view></router-view>
    <el-form v-if="this.show[0]" ref="form" :model="deviceInfo" label-width="100px" size="mini" style="margin-top: 20px">
        <el-form-item label="项目名称">
            <el-input v-model="deviceInfo.system_name" placeholder="例：xx科技有限公司1000万吨/年的炼油化工一体项目"></el-input>
        </el-form-item>
        <el-form-item label="项目描述">
            <el-input v-model="deviceInfo.description" placeholder="例：xx科技有限公司炼油化工一体项目100万吨/年常减压蒸馏装置">
            </el-input>
        </el-form-item>
        <el-form-item label="项目号">
            <el-input v-model="deviceInfo.id" placeholder="例：20200101"></el-input>
        </el-form-item>
        <el-form-item label="建设地点">
            <el-input v-model="deviceInfo.place" placeholder="例：某地"></el-input>
        </el-form-item>
        <el-form-item label="业主文件号">
            <el-input v-model="deviceInfo.owner_doc_no"></el-input>
        </el-form-item>

        <el-form-item label="业主单位">
            <el-input v-model="deviceInfo.describe" placeholder="例：xx科技有限公司">
            </el-input>
        </el-form-item>
        <el-form-item label="设计单位">
            <el-input v-model="deviceInfo.describe" placeholder="例：SEI">
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

        <el-form-item label="装置名称">
            <el-input v-model="deviceInfo.device_name" placeholder="例：20200101"></el-input>
        </el-form-item>
        <el-form-item label="装置类别" style="text-align:left">
            <el-radio-group v-model="deviceInfo.deviceType">
                <el-radio-button label="炼油装置（燃料油）"></el-radio-button>
                <el-radio-button label="炼油装置（润滑油）"></el-radio-button>
                <el-radio-button label="化工装置"></el-radio-button>
                <el-radio-button label="炼油化工一体化装置"></el-radio-button>
                <el-radio-button label="其它"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="设计阶段" style="text-align:left">
            <el-radio-group v-model="deviceInfo.design_stage">
                <el-radio-button label="可行性研究"></el-radio-button>
                <el-radio-button label="方案设计"></el-radio-button>
                <el-radio-button label="基础设计"></el-radio-button>
                <el-radio-button label="详细设计"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="装置规模">
            <el-input v-model="deviceInfo.scale" placeholder="单位：万吨/年"></el-input>
        </el-form-item>
        <el-form-item label="装置系列" style="text-align:left">
            <el-radio-group v-model="deviceInfo.set">
                <el-radio-button label="1"></el-radio-button>
                <el-radio-button label="2"></el-radio-button>
                <el-radio-button label="3"></el-radio-button>
                <el-radio-button label="4"></el-radio-button>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="年开工时">
            <el-input v-model="deviceInfo.work_hour" placeholder="单位：小时"></el-input>
        </el-form-item>
        <el-form-item label="操作弹性">
            <el-input v-model="deviceInfo.flexibility" placeholder="单位：%"></el-input>
        </el-form-item>
        <el-form-item label="工艺类型" style="text-align:left">
            <el-radio-group v-model="deviceInfo.process_type">
                <el-radio-button label="单常压装置"></el-radio-button>
                <el-radio-button label="单减压装置"></el-radio-button>
                <el-radio-button label="常减压装置"></el-radio-button>
                <el-radio-button label="双减压装置"></el-radio-button>
                <el-radio-button label="其他"></el-radio-button>
            </el-radio-group>
        </el-form-item>

        <el-form-item label="专利商">
            <el-input v-model="deviceInfo.patentee"></el-input>
        </el-form-item>
        <el-form-item label="装置范围">
            <el-input type="textarea" :rows="2" placeholder="本装置主要由原油电脱盐脱水部分、换热网络及加热炉部分、常压蒸馏部分、减压蒸馏部分等组成，装置内考虑防腐设置有塔顶注氨、注缓蚀剂、注水设施。
" v-model="deviceInfo.field">
            </el-input>
        </el-form-item>
        <el-form-item label="工艺技术路线">
            <el-input type="textarea" :rows="2" placeholder="原油进料→电脱盐→闪蒸塔→常压塔→减压塔
" v-model="deviceInfo.technical_route">
            </el-input>
        </el-form-item>
        <el-form-item label="占地面积">
            <el-input v-model="deviceInfo.area" placeholder="单位:m^2"></el-input>
        </el-form-item>
        <el-form-item label="装置定员">
            <el-input v-model="deviceInfo.population" placeholder="单位:人"></el-input>
        </el-form-item>
        <el-form-item label="装置能耗">
            <el-input v-model="deviceInfo.energy" placeholder="单位:MJ/t进料"></el-input>
        </el-form-item>
        <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>

    </el-form>
    <!--原料性质-->

</div>
</template>

<script>
export default {

    data() {
        return {
            show: [true, false, false],
            radio1: '装置概况',
            radio2: '化工装置',
            deviceInfo: {
                id: '',
                system_name: '',
                description: '',
                place: '',
                owner: '',
                owner_doc_no: '',
                device_name: '',
                startTime: '',
                endTime: '',
                deviceType: '其它',
                property: '',
                design_stage: '可行性研究',
                scale: '',
                set: '1',
                work_hour: '',
                flexibility: '',
                process_type: '常减压装置',
                patentee: '',
                field: '',
                technical_route: '',
                area: '',
                population: '',
                energy: '',
                file_path: '',
            },

        };
    },
    methods: {
        toSystem() {
            return;
            console.log("change to system input");
            this.$router.push("/AVDU/system");
        },
        onSubmit() {
            console.log(this.deviceInfo);
            this.$http
                .post('http://' + document.domain + ':5000/AVDU_import', {
                    deviceInfo: this.deviceInfo,
                    //发送给后端的信息，可以按照需求增加条目
                }, {
                    emulateJSON: true //必需，否则可能会json解析出错
                }).then(function (response) {
                    //response.body是报文的主体内容
                    if (parseInt(response.body.code) === 200) {

                    }
                })
            console.log('submit!');
        },
        changeFormShow(showFormID) {
            console.log('change showed form');
            this.show = [false, false, false]
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
